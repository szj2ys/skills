---
name: data-review
description: Read a live site's exported or dashboard data and decide what to do next — 数据分析, 看数据, weekly metrics review, GSC / GA4 / PostHog / Clarity / Stripe exports, "why aren't people paying". Funnel strategy without real data is pm-1-funnel-diagnostic; broken tracking is analytics.
---

# Data Review

## The one rule

**One review, one decision, sized to the evidence.** The decision is a fix, an experiment, an instrumentation repair, or "no change yet" — with the metric it should move and when it will be read again.

## 1. Trust the data before reading it

- **Reconcile by business effect**: for the same window and time zone, match provider payments (by status: paid, refunded, renewal) to paid accounts and credits in the database and to purchase events in analytics. Unexplained mismatches go to `payment-integrity`; missing or inflated events go to `analytics`.
- **Noise is a suspicion until corroborated**: one-country or one-network spikes with near-zero engagement, internal and test traffic. Keep raw totals; report the exclusion rule, the excluded count, and conclusions with and without it.
- **Gaps**: events that never fire, broken date ranges, client-only events that can double count.

## 2. Counts with denominators

Always show numerator / denominator and the window. With small denominators, state the uncertainty in words; no significance claims without a test designed for it.

## 3. Read the journey the product actually has

acquisition (queries and pages: impressions, CTR, position; referrers) → landing → first value → signup → paywall → checkout → paid → return, in this product's real order and branches. Rank losses by the value of the users lost, the strength of evidence and the effort to fix. A broken product path is fixed before buying more traffic.

## 4. Separate defect, cause and impact

Recordings, feedback or a reproduction can prove a **defect**. That it **causes** the measured drop is a hypothesis unless cohorts or an experiment show it; the expected **impact** is an estimate. Label each.

## 5. Search data

High impressions with low CTR → title, description, or a page type that mismatches the query. Position 4–20 → strengthen that page. Wrong URL for a query or two URLs splitting one → `serp-seo`. New queries without a page → backlog.

## Output

1. Data trust: reconciliation table, exclusions (with and without), gaps.
2. Journey table: step | numerator / denominator | source (file and column, or dated dashboard view with filters).
3. The leak: defect evidence, cause (supported / hypothesis), impact estimate.
4. Decision: the change or experiment, metric, read-again date, keep-or-revert rule.
5. Backlog: at most 5 other observations.
