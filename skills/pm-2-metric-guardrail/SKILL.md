---
name: pm-2-metric-guardrail
description: Establishing target metrics and safety guardrails to evaluate product success. Use when starting a new feature or optimization to ensure clear measurement, define the single North Star metric, and set up guardrail metrics to prevent negative side effects.
---

# Metric Selection & Guardrail Setup (Flywheel Step 2)

This skill formalizes product goals into rigorous metrics. To avoid optimizing a single metric in a vacuum (e.g., increasing clicks while ruining user trust), we couple success metrics with strict safety look-after variables and system guardrails.

## 🌀 The Flywheel Connection
- **Upstream Input (from `pm-1-funnel-diagnostic`)**: The targeted drop-off hotspot and the quantified target improvement.
- **Downstream Output (to `pm-3-mvp-prioritizer`)**: A locked-in North Star Metric, its mathematical formula, and 2-3 look-after Guardrail Metrics.

---

## 1. Defining the Metric Architecture

### A. The Single North Star Metric (NSM)
The unambiguous rate or ratio that defines success.
- **Rate or Ratio**: Always avoid absolute numbers (like "total sign-ups"). Use ratios like "Checkout Completion Rate" or "Conversion Rate" to ensure scalability.
- **Direct Attribution**: It must directly reflect the user behavior we are changing.

### B. Core Business Guardrails
- **User Trust**: Unsubscribe rates, refund requests, user complaints.
- **Downstream Retention**: Ensure optimizing step A does not cannibalize step B (e.g., higher clicks but lower read duration).

### C. Hard Technical Guardrails
- **Performance**: LCP (Largest Contentful Paint) < 2.5s, TTI (Time to Interactive).
- **Reliability**: API error rate < 0.01%, database latency spikes, client crash rate.

---

## 2. Metric Commitment & Safety Questions
The PM and tech lead must align on these questions before continuing:
1. **What is the single North Star Metric for this project, and how is it mathematically calculated?**
2. **What is our current baseline versus the target successful lift?**
3. **What are the 2-3 specific Business and Technical Guardrail Metrics we will monitor to prevent regression?**
4. **What is the "Circuit Breaker" condition?** (The exact threshold of guardrail degradation that triggers an immediate, automatic rollback or feature halt).

---

## Output Template (Seeds `pm-3-mvp-prioritizer`)

```markdown
### 🎯 Metrics & Guardrails Commitment

#### 1. North Star Metric (Success)
- **Metric Name**: [e.g., Checkout Completion Rate]
- **Calculation Formula**: [e.g., Successful Purchases / Checkout Initiations]
- **Baseline**: [A]%
- **Target Lift**: +[X]% (Targeting [B]%)

#### 2. Guardrail Metrics (Safety Bounds)
- **Guardrail 1 (Tech)**: Page load time (LCP) must remain < [Y]s.
- **Guardrail 2 (Business)**: Downstream order return rate must not exceed [Z]%.
- **Guardrail 3 (UX)**: Interstitial close clicks must not spike.

#### 3. Circuit Breaker Conditions
- **Rollback Trigger**: If [Guardrail Metric] degrades by more than [W]% over [Timeframe], immediate rollback occurs.
- **Next Flywheel Step**: Feed these metrics into `pm-3-mvp-prioritizer` to score feature impact and evaluate implementation cost against our guardrails.
```
