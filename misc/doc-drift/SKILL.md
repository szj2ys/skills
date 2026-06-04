---
name: doc-drift
description: Scan a repository for conflicts between documentation, prototypes, and code. Detects stale references, behavioral mismatches, missing coverage, contradictions, and prototype-vs-implementation drift. Reports actionable diffs so the user can decide how to reconcile.
---

# Doc Drift

Find where documentation, prototypes, and code have drifted apart. Report conflicts with suggested fixes — do not make any changes.

## Scope

Scan the repo. Include:

- **Docs**: `docs/`, `README.md`, `CONTRIBUTING.md`, wikis, guides, `CLAUDE.md`, `AGENTS.md`
- **Inline docs**: docstrings, JSDoc, code comments with verifiable claims
- **Config-driven docs**: OpenAPI/Swagger specs, config file comments
- **Prototypes**: wireframes, mockups, design specs (text-based or HTML), image files referenced in docs

**Skip**: `node_modules/`, `.git/`, `dist/`, `build/`, `vendor/`, lock files, generated files, test fixtures.

**Early exit**: If no documentation or prototype files are found, say so and stop.

## Step 1: Scan

### A — Doc-to-Code (verify documentation claims)

For each documentation file, extract verifiable claims: function/class names, parameter signatures, return types, file paths, config keys, env vars, CLI commands, API endpoints, setup steps, behavioral descriptions ("X does Y"). Search the codebase to verify each claim. Record mismatches.

### B — Code-to-Doc (find undocumented things)

For key code files, identify significant public-facing elements: exported functions/classes, public API endpoints, CLI commands, config options, env vars, breaking behaviors. Search documentation to see if mentioned. Record undocumented significant features.

### C — Prototype-vs-Implementation (compare designs to code)

For each prototype file (text wireframe, HTML mockup, or referenced image):

1. Extract what it describes: layout structure, UI components, labels/copy, interaction behavior
2. Find the corresponding frontend code (match by route, page name, component name, or file path hints)
3. Compare: are all elements present? Does layout match? Do labels match? Are interactions implemented? Are there extra elements in code not in the prototype?

Record mismatches.

## Step 2: Classify

| Category | Description |
|----------|-------------|
| `STALE_REFERENCE` | Docs mention a function/class/file/API that no longer exists or was renamed |
| `BEHAVIORAL_MISMATCH` | Docs describe behavior the code doesn't implement |
| `MISSING_COVERAGE` | Code has significant features not documented anywhere |
| `CONTRADICTION` | Docs say "do X" but code enforces "do Y" |
| `PROTOTYPE_MISMATCH` | Prototype differs from implementation (layout, components, copy, or interactions) |

## Step 3: Report

Group by source file. For each conflict show: category, current content, suggested fix, evidence from code (file path + line number).

```
# Doc Drift Report

## docs/api/authentication.md

### Line 23 — STALE_REFERENCE
Current:
  Call `authenticateUser(token)` to verify the token.

Suggested:
  Call `verifyToken(token)` to verify the token.

Evidence:
  Function was renamed in `src/auth.ts:45`. No `authenticateUser` exists in the codebase.

---

### MISSING_COVERAGE
`src/auth.ts:89` exports `refreshToken(token: string)` — not mentioned in any documentation.

---

## designs/checkout.html

### Line 15 — PROTOTYPE_MISMATCH (component)
Prototype has a CVV input field; `src/pages/checkout.tsx:42` does not implement it.
Suggested: Add CVV input after Card Number input.

### Line 23 — PROTOTYPE_MISMATCH (copy)
Prototype button: "Complete Purchase". Code button (`checkout.tsx:67`): "Submit Order".
Suggested: Change button text to "Complete Purchase".
```

### Rules

- Be precise: cite file paths and line numbers for both source and code
- For prototype conflicts, quote the prototype snippet and actual code snippet
- If no conflicts found, say so clearly — do not invent issues
- Order by source file, then line number
- Do not apply any changes — report only
