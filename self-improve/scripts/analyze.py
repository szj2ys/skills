#!/usr/bin/env python3
"""
Self-Improve — AI Coding Tool Usage Analyzer

Discovers and parses session logs from Claude Code, Codex, and Hermes.
Generates a structured usage audit report.

Usage:
    python3 analyze.py                     # Last 3 days, all tools
    python3 analyze.py --days 7            # Last 7 days
    python3 analyze.py --tool claude       # Only Claude Code
    python3 analyze.py --tool codex        # Only Codex
    python3 analyze.py --tool hermes       # Only Hermes
    python3 analyze.py --session <id>      # Specific session detail
    python3 analyze.py --export md         # Save report to file
"""

import argparse
import glob
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import Counter

HOME = Path.home()

# ─── Tool Log Paths ─────────────────────────────────────────────

TOOL_PATHS = {
    "claude": HOME / ".claude" / "projects",
    "codex": HOME / ".codex" / "sessions",
    "hermes": HOME / ".hermes" / "sessions",
}


# ─── Session Discovery ──────────────────────────────────────────

def discover_claude_sessions(since: datetime) -> list[dict]:
    """Find Claude Code session JSONL files within time window."""
    sessions = []
    projects_dir = TOOL_PATHS["claude"]
    if not projects_dir.exists():
        return sessions
    for jsonl in projects_dir.rglob("*.jsonl"):
        # Skip memory files
        if "memory" in jsonl.parts:
            continue
        mtime = datetime.fromtimestamp(jsonl.stat().st_mtime, tz=timezone.utc)
        if mtime >= since:
            sessions.append({
                "tool": "claude",
                "path": str(jsonl),
                "session_id": jsonl.stem,
                "modified": mtime.isoformat(),
                "project": jsonl.parent.name,
            })
    return sessions


def discover_codex_sessions(since: datetime) -> list[dict]:
    """Find Codex rollout JSONL files within time window."""
    sessions = []
    sessions_dir = TOOL_PATHS["codex"]
    if not sessions_dir.exists():
        return sessions
    for jsonl in sessions_dir.rglob("rollout-*.jsonl"):
        mtime = datetime.fromtimestamp(jsonl.stat().st_mtime, tz=timezone.utc)
        if mtime >= since:
            sessions.append({
                "tool": "codex",
                "path": str(jsonl),
                "session_id": jsonl.stem,
                "modified": mtime.isoformat(),
            })
    return sessions


def discover_hermes_sessions(since: datetime) -> list[dict]:
    """Find Hermes session JSON files within time window."""
    sessions = []
    sessions_dir = TOOL_PATHS["hermes"]
    if not sessions_dir.exists():
        return sessions
    for json_file in sessions_dir.glob("session_*.json"):
        mtime = datetime.fromtimestamp(json_file.stat().st_mtime, tz=timezone.utc)
        if mtime >= since:
            sessions.append({
                "tool": "hermes",
                "path": str(json_file),
                "session_id": json_file.stem,
                "modified": mtime.isoformat(),
            })
    return sessions


def discover_sessions(since: datetime, tool_filter: str | None = None) -> list[dict]:
    """Discover all sessions across tools."""
    all_sessions = []
    if tool_filter is None or tool_filter == "claude":
        all_sessions.extend(discover_claude_sessions(since))
    if tool_filter is None or tool_filter == "codex":
        all_sessions.extend(discover_codex_sessions(since))
    if tool_filter is None or tool_filter == "hermes":
        all_sessions.extend(discover_hermes_sessions(since))
    return sorted(all_sessions, key=lambda s: s["modified"], reverse=True)


# ─── Session Parsing ────────────────────────────────────────────

def parse_claude_session(path: str) -> dict:
    """Parse Claude Code JSONL session into normalized format."""
    messages = []
    tool_calls = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            entry_type = entry.get("type", "")

            if entry_type == "user":
                msg = entry.get("message", {})
                if isinstance(msg, dict):
                    content = msg.get("content", "")
                    if isinstance(content, list):
                        content = " ".join(
                            c.get("text", "") for c in content if isinstance(c, dict)
                        )
                    messages.append({"role": "user", "content": str(content)[:2000]})
                elif isinstance(msg, str):
                    messages.append({"role": "user", "content": msg[:2000]})

            elif entry_type == "assistant":
                msg = entry.get("message", {})
                if isinstance(msg, dict):
                    content = msg.get("content", "")
                    if isinstance(content, list):
                        parts = []
                        for c in content:
                            if isinstance(c, dict):
                                if c.get("type") == "text":
                                    parts.append(c.get("text", ""))
                                elif c.get("type") == "tool_use":
                                    tool_calls.append({
                                        "tool": c.get("name", "unknown"),
                                        "success": True,
                                    })
                        content = " ".join(parts)
                    messages.append({"role": "assistant", "content": str(content)[:2000]})

    return {
        "messages": messages,
        "tool_calls": tool_calls,
        "turn_count": len([m for m in messages if m["role"] == "user"]),
    }


def parse_codex_session(path: str) -> dict:
    """Parse Codex rollout JSONL into normalized format."""
    messages = []
    tool_calls = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            entry_type = entry.get("type", "")
            payload = entry.get("payload", {})

            if entry_type == "response_item":
                ptype = payload.get("type", "")
                role = payload.get("role", "")
                content_items = payload.get("content", [])

                if ptype == "message" and role in ("user", "assistant"):
                    text_parts = []
                    for item in content_items:
                        if isinstance(item, dict):
                            if item.get("type") in ("input_text", "output_text"):
                                text_parts.append(item.get("text", ""))
                            elif item.get("type") == "tool_call":
                                tool_calls.append({
                                    "tool": item.get("name", "unknown"),
                                    "success": True,
                                })
                    messages.append({
                        "role": role,
                        "content": " ".join(text_parts)[:2000],
                    })

    return {
        "messages": messages,
        "tool_calls": tool_calls,
        "turn_count": len([m for m in messages if m["role"] == "user"]),
    }


def parse_hermes_session(path: str) -> dict:
    """Parse Hermes session JSON into normalized format."""
    with open(path, "r") as f:
        data = json.load(f)

    messages = []
    tool_calls = []

    for msg in data.get("messages", []):
        role = msg.get("role", "")
        content = msg.get("content", "")

        if role in ("user", "assistant"):
            if isinstance(content, list):
                text_parts = []
                for item in content:
                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            text_parts.append(item.get("text", ""))
                        elif item.get("type") == "tool_use":
                            tool_calls.append({
                                "tool": item.get("name", "unknown"),
                                "success": True,
                            })
                content = " ".join(text_parts)
            messages.append({"role": role, "content": str(content)[:2000]})

    return {
        "messages": messages,
        "tool_calls": tool_calls,
        "turn_count": len([m for m in messages if m["role"] == "user"]),
    }


def parse_session(session: dict) -> dict:
    """Parse session based on tool type."""
    path = session["path"]
    tool = session["tool"]
    try:
        if tool == "claude":
            return parse_claude_session(path)
        elif tool == "codex":
            return parse_codex_session(path)
        elif tool == "hermes":
            return parse_hermes_session(path)
    except Exception as e:
        return {"messages": [], "tool_calls": [], "turn_count": 0, "error": str(e)}
    return {"messages": [], "tool_calls": [], "turn_count": 0}


# ─── Analysis ───────────────────────────────────────────────────

VAGUE_PATTERNS = [
    "fix this", "make it better", "update it", "change it",
    "do it", "fix", "help", "please", "idk", "whatever",
    "just do it", "figure it out", "handle it",
]

CLEAR_PATTERNS = [
    "in file", "function", "class", "method", "endpoint",
    "line ", "error:", "expected", "should return", "because",
    "specifically", "ensure that", "must", "requirement",
]


def analyze_prompt_clarity(messages: list[dict]) -> tuple[float, list[str]]:
    """Score prompt clarity 1-10."""
    user_msgs = [m for m in messages if m["role"] == "user"]
    if not user_msgs:
        return 5.0, []

    vague_count = 0
    clear_count = 0
    total_words = 0
    findings = []

    for msg in user_msgs:
        content = msg["content"].lower()
        words = content.split()
        total_words += len(words)

        for pattern in VAGUE_PATTERNS:
            if pattern in content and len(words) < 15:
                vague_count += 1
                break

        for pattern in CLEAR_PATTERNS:
            if pattern in content:
                clear_count += 1
                break

    avg_words = total_words / len(user_msgs) if user_msgs else 0

    score = 5.0
    if avg_words < 10:
        score -= 2
        findings.append(f"Average prompt length is {avg_words:.0f} words — too short for clarity")
    elif avg_words > 30:
        score += 1

    if vague_count > len(user_msgs) * 0.3:
        score -= 2
        findings.append(f"{vague_count}/{len(user_msgs)} prompts are vague")

    if clear_count > len(user_msgs) * 0.5:
        score += 2
        findings.append(f"{clear_count}/{len(user_msgs)} prompts include specific references")

    return max(1, min(10, score)), findings


def analyze_task_decomposition(messages: list[dict]) -> tuple[float, list[str]]:
    """Score task decomposition 1-10."""
    user_msgs = [m for m in messages if m["role"] == "user"]
    turn_count = len(user_msgs)
    findings = []

    if turn_count == 0:
        return 5.0, []

    # Check for monolithic requests (long first message)
    first_msg_words = len(user_msgs[0]["content"].split()) if user_msgs else 0
    score = 5.0

    if first_msg_words > 200:
        score -= 2
        findings.append(f"First prompt is {first_msg_words} words — likely too broad")

    if turn_count > 30:
        score -= 2
        findings.append(f"{turn_count} turns suggests task was not well decomposed")
    elif turn_count > 20:
        score -= 1
        findings.append(f"{turn_count} turns — moderate complexity")
    elif turn_count < 5:
        score += 1
        findings.append(f"Concise session with {turn_count} turns")

    # Check for "and" conjunctions in prompts (multiple tasks)
    multi_task_count = sum(
        1 for m in user_msgs
        if m["content"].lower().count(" and ") >= 2
    )
    if multi_task_count > 2:
        score -= 1
        findings.append(f"{multi_task_count} prompts bundle multiple tasks")

    return max(1, min(10, score)), findings


def analyze_context_efficiency(messages: list[dict]) -> tuple[float, list[str]]:
    """Score context efficiency 1-10."""
    user_msgs = [m for m in messages if m["role"] == "user"]
    findings = []
    score = 5.0

    long_pastes = sum(1 for m in user_msgs if len(m["content"]) > 2000)
    if long_pastes > 0:
        score -= 2
        findings.append(f"{long_pastes} messages contain large content dumps (>2000 chars)")

    file_refs = sum(
        1 for m in user_msgs
        if any(p in m["content"] for p in ["/", "\\", ".py", ".js", ".ts", ".md"])
    )
    if file_refs > len(user_msgs) * 0.3:
        score += 2
        findings.append("Good use of file path references")

    return max(1, min(10, score)), findings


def analyze_tool_utilization(tool_calls: list[dict], messages: list[dict]) -> tuple[float, list[str]]:
    """Score tool utilization 1-10."""
    findings = []
    score = 5.0

    if not tool_calls:
        score = 3
        findings.append("No tool calls detected — treating AI as plain chat")
        return score, findings

    tool_names = Counter(t["tool"] for t in tool_calls)
    unique_tools = len(tool_names)

    if unique_tools >= 5:
        score += 2
        findings.append(f"Uses {unique_tools} different tools — good variety")
    elif unique_tools >= 3:
        score += 1
        findings.append(f"Uses {unique_tools} tools")
    else:
        findings.append(f"Only {unique_tools} tools used — explore more capabilities")

    total_calls = len(tool_calls)
    user_turns = len([m for m in messages if m["role"] == "user"])
    if user_turns > 0:
        calls_per_turn = total_calls / user_turns
        if calls_per_turn > 2:
            score += 1
            findings.append(f"Good tool chaining ({calls_per_turn:.1f} calls/turn)")

    return max(1, min(10, score)), findings


def analyze_iteration_quality(messages: list[dict]) -> tuple[float, list[str]]:
    """Score iteration quality 1-10."""
    user_msgs = [m for m in messages if m["role"] == "user"]
    findings = []
    score = 5.0

    if len(user_msgs) < 2:
        return score, findings

    correction_patterns = [
        "no,", "not what i", "that's wrong", "incorrect", "try again",
        "not right", "redo", "revert", "undo", "that's not",
        "i didn't mean", "actually", "wait", "nevermind",
    ]

    correction_count = sum(
        1 for m in user_msgs
        if any(p in m["content"].lower() for p in correction_patterns)
    )

    correction_ratio = correction_count / len(user_msgs) if user_msgs else 0

    if correction_ratio > 0.3:
        score -= 3
        findings.append(f"{correction_count}/{len(user_msgs)} turns are corrections — high rework")
    elif correction_ratio > 0.15:
        score -= 1
        findings.append(f"Moderate correction rate ({correction_ratio:.0%})")
    elif correction_ratio < 0.05:
        score += 2
        findings.append("Very low correction rate — high quality iterations")

    return max(1, min(10, score)), findings


def analyze_error_recovery(messages: list[dict]) -> tuple[float, list[str]]:
    """Score error recovery 1-10."""
    findings = []
    score = 5.0

    error_msgs = [
        m for m in messages
        if m["role"] == "assistant" and any(
            w in m["content"].lower()
            for w in ["error", "failed", "exception", "traceback", "bug"]
        )
    ]

    if not error_msgs:
        score = 6
        findings.append("No errors detected in session")
        return score, findings

    user_after_error = 0
    adapted_after_error = 0

    for i, msg in enumerate(messages):
        if msg["role"] == "assistant" and any(
            w in msg["content"].lower() for w in ["error", "failed", "exception"]
        ):
            if i + 1 < len(messages) and messages[i + 1]["role"] == "user":
                user_after_error += 1
                followup = messages[i + 1]["content"].lower()
                if any(w in followup for w in ["try", "instead", "alternative", "different", "maybe"]):
                    adapted_after_error += 1

    if user_after_error > 0:
        adaptation_rate = adapted_after_error / user_after_error
        if adaptation_rate > 0.5:
            score += 2
            findings.append(f"Good adaptation after errors ({adaptation_rate:.0%})")
        elif adaptation_rate < 0.2:
            score -= 2
            findings.append(f"Low adaptation after errors ({adaptation_rate:.0%}) — try different approaches")

    return max(1, min(10, score)), findings


def analyze_session(session: dict) -> dict:
    """Run full analysis on a parsed session."""
    parsed = parse_session(session)
    messages = parsed["messages"]
    tool_calls = parsed["tool_calls"]

    clarity_score, clarity_findings = analyze_prompt_clarity(messages)
    decomp_score, decomp_findings = analyze_task_decomposition(messages)
    context_score, context_findings = analyze_context_efficiency(messages)
    tool_score, tool_findings = analyze_tool_utilization(tool_calls, messages)
    iter_score, iter_findings = analyze_iteration_quality(messages)
    recovery_score, recovery_findings = analyze_error_recovery(messages)

    return {
        "session_id": session["session_id"],
        "tool": session["tool"],
        "project": session.get("project", "N/A"),
        "modified": session["modified"],
        "turn_count": parsed["turn_count"],
        "message_count": len(messages),
        "tool_call_count": len(tool_calls),
        "scores": {
            "prompt_clarity": clarity_score,
            "task_decomposition": decomp_score,
            "context_efficiency": context_score,
            "tool_utilization": tool_score,
            "iteration_quality": iter_score,
            "error_recovery": recovery_score,
        },
        "findings": {
            "prompt_clarity": clarity_findings,
            "task_decomposition": decomp_findings,
            "context_efficiency": context_findings,
            "tool_utilization": tool_findings,
            "iteration_quality": iter_findings,
            "error_recovery": recovery_findings,
        },
    }


# ─── Report Generation ─────────────────────────────────────────

DIMENSION_LABELS = {
    "prompt_clarity": "Prompt Clarity",
    "task_decomposition": "Task Decomposition",
    "context_efficiency": "Context Efficiency",
    "tool_utilization": "Tool Utilization",
    "iteration_quality": "Iteration Quality",
    "error_recovery": "Error Recovery",
}


def generate_report(analyses: list[dict], days: int) -> str:
    """Generate markdown report from analysis results."""
    if not analyses:
        return f"## No sessions found in the last {days} days.\n"

    # Aggregate scores
    dim_scores = {dim: [] for dim in DIMENSION_LABELS}
    all_findings = {dim: [] for dim in DIMENSION_LABELS}
    tool_counts = Counter()

    for a in analyses:
        tool_counts[a["tool"]] += 1
        for dim, score in a["scores"].items():
            dim_scores[dim].append(score)
        for dim, findings in a["findings"].items():
            all_findings[dim].extend(findings)

    avg_scores = {
        dim: sum(scores) / len(scores) if scores else 0
        for dim, scores in dim_scores.items()
    }
    overall = sum(avg_scores.values()) / len(avg_scores)

    # Build report
    lines = []
    lines.append("## Usage Audit Report")
    lines.append("")
    lines.append(f"**Period:** Last {days} days")
    lines.append(f"**Sessions analyzed:** {len(analyses)}")
    tools_str = ", ".join(f"{v} {k}" for k, v in tool_counts.items())
    lines.append(f"**Tools:** {tools_str}")
    lines.append("")
    lines.append(f"### Overall Score: {overall:.1f}/10")
    lines.append("")

    # Dimension breakdown
    lines.append("### Dimension Breakdown")
    lines.append("")
    lines.append("| Dimension | Score | Rating |")
    lines.append("|-----------|-------|--------|")

    def rating(s):
        if s >= 8: return "Excellent"
        if s >= 6: return "Good"
        if s >= 4: return "Fair"
        return "Needs Work"

    for dim, label in DIMENSION_LABELS.items():
        s = avg_scores[dim]
        lines.append(f"| {label} | {s:.1f}/10 | {rating(s)} |")
    lines.append("")

    # Top deficiencies
    deficiency_counts = Counter()
    for dim, findings in all_findings.items():
        for f in findings:
            deficiency_counts[(dim, f)] += 1

    top_deficiencies = deficiency_counts.most_common(5)
    if top_deficiencies:
        lines.append("### Key Findings")
        lines.append("")
        for i, ((dim, finding), count) in enumerate(top_deficiencies, 1):
            label = DIMENSION_LABELS[dim]
            lines.append(f"{i}. **[{label}]** {finding} (seen in {count} session{'s' if count > 1 else ''})")
        lines.append("")

    # Per-tool summary
    if len(tool_counts) > 1:
        lines.append("### Per-Tool Scores")
        lines.append("")
        lines.append("| Tool | Sessions | Avg Score |")
        lines.append("|------|----------|-----------|")
        for tool in tool_counts:
            tool_analyses = [a for a in analyses if a["tool"] == tool]
            tool_avg = sum(
                sum(a["scores"].values()) / len(a["scores"])
                for a in tool_analyses
            ) / len(tool_analyses)
            lines.append(f"| {tool.title()} | {len(tool_analyses)} | {tool_avg:.1f}/10 |")
        lines.append("")

    # Recommendations
    lines.append("### Recommendations")
    lines.append("")

    recommendations = []
    if avg_scores["prompt_clarity"] < 5:
        recommendations.append("Write more specific prompts — include file paths, expected behavior, and constraints")
    if avg_scores["task_decomposition"] < 5:
        recommendations.append("Break complex tasks into smaller, verifiable steps before starting")
    if avg_scores["context_efficiency"] < 5:
        recommendations.append("Use file references instead of pasting large code blocks")
    if avg_scores["tool_utilization"] < 5:
        recommendations.append("Explore more tool capabilities — agents, skills, plan mode")
    if avg_scores["iteration_quality"] < 5:
        recommendations.append("Spend more time on the initial prompt to reduce correction cycles")
    if avg_scores["error_recovery"] < 5:
        recommendations.append("When errors occur, try a different approach rather than repeating the same request")

    if not recommendations:
        recommendations.append("Keep up the good work! Focus on maintaining consistency across sessions.")

    for i, rec in enumerate(recommendations, 1):
        lines.append(f"{i}. {rec}")
    lines.append("")

    return "\n".join(lines)


# ─── Main ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Self-Improve — AI Tool Usage Analyzer")
    parser.add_argument("--days", type=int, default=3, help="Analysis window in days (default: 3)")
    parser.add_argument("--tool", choices=["claude", "codex", "hermes"], help="Filter by tool")
    parser.add_argument("--session", type=str, help="Analyze specific session ID")
    parser.add_argument("--export", choices=["md"], help="Export report to file")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of report")
    args = parser.parse_args()

    since = datetime.now(timezone.utc) - timedelta(days=args.days)
    sessions = discover_sessions(since, args.tool)

    if args.session:
        sessions = [s for s in sessions if args.session in s["session_id"]]

    if not sessions:
        print(f"No sessions found in the last {args.days} days" +
              (f" for tool '{args.tool}'" if args.tool else ""))
        sys.exit(0)

    print(f"Found {len(sessions)} sessions. Analyzing...\n", file=sys.stderr)

    analyses = []
    for session in sessions:
        result = analyze_session(session)
        analyses.append(result)

    if args.json:
        print(json.dumps(analyses, indent=2))
    else:
        report = generate_report(analyses, args.days)
        print(report)

    if args.export == "md":
        report_dir = HOME / ".claude" / "self-improve-reports"
        report_dir.mkdir(parents=True, exist_ok=True)
        filename = f"report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
        report_path = report_dir / filename
        with open(report_path, "w") as f:
            f.write(report)
        print(f"\nReport saved to: {report_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
