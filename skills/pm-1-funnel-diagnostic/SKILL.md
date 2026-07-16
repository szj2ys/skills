---
name: pm-1-funnel-diagnostic
description: Core ByteDance product diagnostic workflow for identifying business leverage points and defining conversion funnels. Use when you need to decide what to build, diagnose where users are dropping off, or estimate the value uplift of an optimization.
---

# Funnel Diagnostic & Leverage Mining (Flywheel Step 1)

This skill implements the canonical ByteDance diagnostic phase. In ByteDance, deciding **what to do** is far more critical than *how to do it*. We replace subjective intuition with math-backed customer journeys.

## 🌀 The Flywheel Connection
- **Upstream Input**: None (flywheel entry point). On subsequent cycles, `pm-5-ab-tracking` feeds back real post-launch user telemetry, empirical conversion rates, and updated behavioral baselines.
- **Downstream Output (to `pm-2-metric-guardrail`)**: An identified high-leverage drop-off bottleneck and a quantified target metric lift.

---

## 1. Context, Not Control: The ByteDance PM Paradigm
Instead of requesting specific features, this step uncovers the underlying business reality.
- **Identify the Core Value**: What is the ultimate terminal success action for the user? (e.g., successful purchase, first video published, report compiled).
- **Map the Ideal Journey**: Map the step-by-step conversion pipeline. If cold starting with **No Data**, construct a logical, idealized journey and use industry standard conversion rates as a hypothesis.

---

## 2. Business Value & Funnel Questions
When auditing an opportunity, the PM must answer these core questions:
1. **What problem are we solving, and for whom?** (Define the target segment and core pain point).
2. **What is the exact, step-by-step conversion funnel today?** (Quantify survival and drop-off rates at each transition).
3. **Where is the single biggest leak/drop-off hotspot?** (Must be backed by quantitative evidence or a strong, visible-friction hypothesis if cold starting).
4. **Why now? What happens if we do nothing?** (Assess urgency and opportunity cost).
5. **Is this a growth, retention, or monetization lever?** (Classify the business impact).
6. **What is the expected value uplift?** Multiply the projected conversion lift by total traffic to estimate the incremental value actions, then compare against implementation cost to assess priority.

---

## Output Template (Seeds `pm-2-metric-guardrail`)

```markdown
### 📊 Funnel Diagnosis: [Project Name]

#### 1. Current Funnel Performance & Baselines
- Step 1: [Name] -> [Count/Rate] (100%)
- Step 2: [Name] -> [Count/Rate] ([Survival]%) | ⚠️ [Leak Status / Friction Point]
- Step 3: [Name] -> [Count/Rate] ([Survival]%)

#### 2. The High-Leverage Drop-off Hotspot
- **Target Bottleneck**: [Describe the weakest transition step]
- **Qualitative Friction**: [Why do users fail here? e.g., overwhelming form inputs, slow load]
- **Target Improvement**: Lift transition rate from [A]% baseline to [B]%.

#### 3. Value Uplift & Business Leverage
- **Leverage Dimension**: [Growth / Retention / Monetization]
- **North Star Impact**: Projected end-to-end lift of [Z]%.
- **Daily Volume Increase**: +[N] [Value Actions] per day.
- **Urgency Assessment**: [What happens if we do nothing?]
- **Next Flywheel Step**: Pass this target bottleneck and improvement target to `pm-2-metric-guardrail` to formalize the North Star and Guardrail metrics.
```
