---
name: self-improve
description: Analyze AI coding tool usage logs (Claude Code, Codex, Hermes, OpenClaw) to identify user anti-patterns, inefficiencies, and missed capabilities. Reads local session files, scores usage across multiple dimensions, and provides actionable optimization recommendations. Use when user wants to improve their AI coding workflow, review past session quality, or get a usage audit report.
---

# Self-Improve — AI Coding Tool Usage Analyzer

## Quick Start

```
/self-improve                    # Analyze last 3 days, all tools
/self-improve 7                  # Analyze last 7 days
/self-improve --tool claude      # Only Claude Code sessions
/self-improve --tool codex       # Only Codex sessions
/self-improve --tool hermes      # Only Hermes sessions
```

## What It Analyzes

The skill reads local session logs from these tools:

| Tool | Log Location | Format |
|------|-------------|--------|
| Claude Code | `~/.claude/projects/**/` | JSONL per session |
| Codex | `~/.codex/sessions/{YYYY}/{MM}/{DD}/` | JSONL rollout files |
| Hermes | `~/.hermes/sessions/session_*.json` | JSON per session |
| OpenClaw | `~/.openclaw/` | Skills-only (limited data) |

## Analysis Dimensions

Each session is scored across 6 dimensions (1-10):

1. **Prompt Clarity** — Are instructions specific, contextual, and unambiguous?
2. **Task Decomposition** — Are complex tasks broken into atomic steps?
3. **Context Efficiency** — Is relevant context provided without noise?
4. **Tool Utilization** — Does the user leverage available tool capabilities?
5. **Iteration Quality** — Are follow-ups corrective or additive?
6. **Error Recovery** — When things go wrong, is the recovery path efficient?

## Workflow

### Step 1 — Collect Sessions

```
1. Parse args for time window (default: 3 days) and tool filter
2. Discover session files from all tool directories
3. Filter by modification time within window
4. Parse each file into normalized message list
```

### Step 2 — Analyze Each Session

For each session, extract:
- **User messages**: prompts, instructions, corrections
- **Tool calls**: which tools were invoked, success/failure
- **Turn count**: total back-and-forth exchanges
- **Topic shifts**: number of times the user changed direction
- **Completion signals**: did the task appear to finish?

### Step 3 — Score and Identify Patterns

Run scoring heuristics from [REFERENCE.md](REFERENCE.md). Flag:
- Anti-patterns (vague prompts, excessive backtracking, unused features)
- Positive patterns (clear specs, good task decomposition, effective reuse)

### Step 4 — Generate Report

Output a structured report:

```
## Usage Audit Report
Period: {start_date} → {end_date}
Sessions analyzed: {count} across {tools}

### Overall Score: {X}/10

### Dimension Breakdown
| Dimension | Score | Trend |
|-----------|-------|-------|
| Prompt Clarity | 7/10 | ↑ |
| ... | ... | ... |

### Top 3 Deficiencies
1. {pattern} — {evidence} — {recommendation}
2. ...
3. ...

### What You're Doing Well
- {positive pattern with evidence}

### Actionable Next Steps
1. {specific, concrete improvement}
2. ...
```

## Advanced Options

- `--session <id>` — Analyze a specific session in detail
- `--export md` — Save report to `~/.claude/self-improve-reports/`
- `--compare` — Compare current period with previous period
- `--verbose` — Include per-session breakdown

## Tips

- Run weekly for best results — patterns emerge over time
- Focus on the top 1-2 deficiencies, not all at once
- Compare scores across weeks to track improvement
