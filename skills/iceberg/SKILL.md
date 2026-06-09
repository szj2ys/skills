---
name: iceberg
description: "Deep analysis of a project, situation, or body of work to surface three categories of blind spots: (1) missed actions — things that should be done but aren't, (2) unknown unknowns — things the user hasn't even considered, (3) false confidence — areas where the user assumes understanding but evidence says otherwise. Use when the user wants a gap audit, blind spot check, 'what am I missing', 'what should I be doing', 'iceberg' analysis, asks for a critical review of their situation or project, or provides context (code, docs, plans, briefs) and wants to know what they're not seeing. Works on software projects, product strategies, personal plans, business decisions, or any domain where the user provides or points at a body of context. Supports hybrid input: code repos, text briefs, or both."
---

# Iceberg — What You're Not Seeing

Audit a body of work across three axes that humans systematically fail to self-diagnose. The skill is judgment-heavy: it reads what exists, infers the domain and goals, then compares against what should exist, what's invisible, and what's assumed but wrong.

## Three Axes

### Axis 1: Missed Actions (should-do / didn't-do)

Things that are standard practice, necessary, or obviously valuable — but absent.

Detection method: for each domain inferred from context, walk the canonical checklist for that domain. Mark present items. The gaps are missed actions. Only flag gaps that matter given the stated or inferred goals; don't flag infrastructure best practices for a throwaway prototype.

Examples: no tests on critical path, no error handling on external calls, no user research before building features, no monitoring after launch, no backup strategy, no pricing validation.

### Axis 2: Unknown Unknowns (don't-know-that-you-don't-know)

Adjacent concerns, second-order effects, hidden dependencies, or entire problem spaces the user hasn't surfaced.

Detection method: ask "what would an experienced practitioner in this domain worry about that isn't mentioned anywhere in this context?" Look for:
- Entire categories of work absent (e.g., security, observability, legal, accessibility)
- Assumptions that work only under favorable conditions
- External dependencies left implicit (third-party services, team capacity, timelines)
- Risks that scale non-linearly (what works at 10 users breaks at 1000)
- Regulatory or compliance concerns relevant to the domain

Do not flag generic advice. Every unknown-unknown must be grounded in something specific to the user's context.

### Axis 3: False Confidence (think-you-know / actually-don't)

Claims, plans, or technical statements in the user's context that sound correct but contain hidden errors, oversimplifications, or contradictions.

Detection method: find assertions in the context (explicit or implied). Stress-test each one:
- Is the stated mechanism actually how it works?
- Does the evidence in the code/docs match the claim?
- Are there known failure modes the author seems unaware of?
- Does the confidence level match the evidence level?

Report only when there's a concrete discrepancy between what's stated/implied and what the evidence shows. Don't speculate on unstated beliefs.

## Workflow

### Step 1: Ingest Context

Gather all available information. Hybrid: read code if a repo/path is given, read text if a brief is pasted, combine both if available. Infer:
- The domain(s) (software, product, business, personal, etc.)
- The user's role and goals (from explicit statement, repo structure, or content)
- The stage (early exploration, mid-build, shipped, etc.)

If the user provides a role or lens explicitly, weight findings through that lens. If nothing is provided, analyze as a generalist senior practitioner.

### Step 2: Domain-Adaptive Checklist

Based on inferred domain, mentally load the relevant checklist domains. For software: architecture, testing, security, observability, CI/CD, dependency management, error handling, documentation. For product: validation, user research, pricing, distribution, metrics, competitive positioning. For business: unit economics, legal, compliance, team, operations, cash flow.

Only activate domains relevant to the context. Don't audit security for a slide deck.

### Step 3: Run Three Axes

Walk each axis against the ingested context. Collect findings with:
- **Category**: missed-action | unknown-unknown | false-confidence
- **Evidence**: specific reference to what's in (or absent from) the context
- **Impact**: why this matters given the user's goals
- **Suggested action**: what to do about it

### Step 4: Prioritize and Present

Output structure:

```
## Summary
[2-3 sentence overview of what the audit found]

## Missed Actions
For each finding:
- **[Title]**: [What's missing + why it matters] | Evidence: [what you looked at]

## Unknown Unknowns
For each finding:
- **[Title]**: [What's absent from awareness + why it matters] | Evidence: [contextual basis]

## False Confidence
For each finding:
- **[Claim vs Reality]**: [What the user assumes] -> [What the evidence actually shows]

## Suggested Next Steps
[Ordered by impact. 3-7 concrete actions.]
```

## Boundaries

- Limit to 5-10 findings per axis per pass. More than that means either the context is too thin to analyze meaningfully or the user needs a different kind of help.
- Do not fabricate findings to fill categories. If an axis is clean, say so.
- Do not give generic advice ("you should write tests"). Every finding must reference something specific in the user's context.
- If the context is too thin to analyze, say what additional information would unlock a useful audit.
