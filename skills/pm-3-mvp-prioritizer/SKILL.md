---
name: pm-3-mvp-prioritizer
description: High-impact MVP scoping and ICE prioritization framework. Use when scope creep is slowing down development, you have too many ideas and limited resources, or you need to trim a feature set down to the absolute bare minimum to validate a hypothesis.
---

# MVP Scoping & ICE Prioritization (Flywheel Step 3)

This skill enforces ruthless minimalism. "Simplicity is the art of maximizing the amount of work not done." We trim down features to the absolute bare minimum needed to test our core hypothesis, preventing over-engineering and bloated software.

## 🌀 The Flywheel Connection
- **Upstream Input (from `pm-2-metric-guardrail`)**: The North Star Metric and Guardrails.
- **Downstream Output (to `pm-4-edge-case-spec`)**: A ruthlessly scoped, prioritized MVP feature set ready for zero-ambiguity functional specification.

---

## 1. The Core Hypothesis & Scoping Questions
Before prioritizing features, challenge the scope:
1. **What is the single core hypothesis we are validating?** (State as: "We believe that by providing [Minimum Value], users will [Perform North Star Action]").
2. **If we remove [Feature X], does it break the user's ability to validate that hypothesis?** (If no, it must be cut from the MVP and moved to the backlog).
3. **What is the smallest valuable version we can build in days, not weeks?** (If cold-starting with no data, can we run a cheap "Fake Door" or "Smoke Test" first to gauge interest?).

---

## 2. Rigorous ICE Scoring Framework
Score every candidate feature on a scale of 1 to 5:

- **Impact (1-5)**: How much will this feature move the **North Star Metric** defined in Step 2?
- **Confidence (1-5)**: How sure are we? (Backed by user data/competitor evidence = 5, intuitive guess = 1).
- **Ease (1-5)**: How simple is it to build **without degrading the defined Guardrails**? (1 day = 5, 1 month = 1).

$$\text{ICE Score} = \text{Impact} \times \text{Confidence} \times \text{Ease}$$

Only features with the highest ICE scores make it into the MVP. All others are ruthlessly deferred.

---

## Output Template (Seeds `pm-4-edge-case-spec`)

```markdown
### ✂️ MVP Scope & ICE Scoring

#### 1. Core Hypothesis & Validation Strategy
- **Core Hypothesis**: "We believe that by providing [Minimum Value], users will [Perform North Star Action]."
- **Data Capture Strategy**: [e.g., Fake door click capture, minimal static page]

#### 2. ICE Scoring Table (Tuned to NSM & Guardrails)

| Feature Name | Impact (1-5) | Confidence (1-5) | Ease (1-5) | Total Score (I*C*E) | Decision |
| :--- | :---: | :---: | :---: | :---: | :--- |
| [Feature A] | [5] | [4] | [4] | [80] | **MVP (In-Scope)** |
| [Feature B] | [4] | [2] | [4] | [32] | Backlog (Phase 2) |
| [Feature C] | [3] | [1] | [2] | [6] | Backlog (Phase 2) |

#### 3. Ruthlessly Deferred Out-of-Scope Items
- [Feature B]: Deferred to Phase 2 to ensure rapid delivery.
- [Feature C]: Removed from MVP.
- **Next Flywheel Step**: Pass the locked-in **MVP (In-Scope)** features to `pm-4-edge-case-spec` to detail acceptance criteria and map exception dimensions.
```
