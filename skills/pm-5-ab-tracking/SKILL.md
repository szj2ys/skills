---
name: pm-5-ab-tracking
description: Experimentation design and data-tracking specifications. Use when planning user-behavior tracking, designing A/B test parameters, or planning post-launch data analysis and attribution.
---

# Experimentation Design & Event Tracking (Flywheel Step 5)

This skill ensures that every launch is scientific and measurable. If we cannot prove that our feature moved the target metric, the feature was not successfully completed.

## 🌀 The Flywheel Connection
- **Upstream Input (from `pm-4-edge-case-spec`)**: Unambiguous happy paths, error states, and state transitions.
- **Downstream Output (to `pm-1-funnel-diagnostic`)**: Event telemetry, conversion rate lifts, and updated statistical baselines to feed the next iteration cycle.

---

## 1. Tracking Specification (Event Schema)
Every interaction must have its tracking schema designed and agreed upon **prior** to writing code.
- **Naming format**: Use `snake_case` with `[object]_[action]` format (e.g., `checkout_button_click`, `profile_edit_save`).
- **Required parameters**: Always capture `user_id`, `session_id`, `timestamp`, and state-specific variables.
- **Track Exceptions**: Ensure we log error events from Step 4 (e.g., `error_type: "api_timeout"`).

---

## 2. A/B Experimentation Design
To isolate variables and guarantee that changes in metrics are due to our feature:
- **Enrollment Trigger**: User is enrolled strictly when they encounter the modified flow (not on app launch).
- **Allocation**: Divide traffic (e.g., 50% Control [Old experience], 50% Treatment [New experience]).
- **Statistical Significance Goal**: Run the experiment until $p < 0.05$ (95% confidence) before deciding to scale or roll back.
- **Statistical Power**: Target at least 80% power (1 - β) to ensure the experiment can detect a true effect of the expected size. Underpowered experiments risk false negatives—concluding a feature has no impact when it actually does.
- **Minimum Detectable Effect (MDE)**: Define the smallest metric lift that is both statistically detectable and business-meaningful. Calculate required sample size from baseline rate, MDE, significance level (α = 0.05), and power (1 - β = 0.80). Do not launch the experiment without confirming the sample size is achievable within the planned duration.

---

## 3. Post-Launch & Experimentation Questions
1. **What specific user action triggers A/B experiment enrollment?**
2. **What is the schema of events we will track, covering both happy and failed paths?**
3. **What is the target sample size and experiment duration?**
4. **Did the North Star metric move as expected? What does the data tell us?**
5. **Where did user behavior differ from our hypothesis?**

---

## Output Template (Feeds back to `pm-1-funnel-diagnostic`)

```markdown
### 📊 Experimentation & Tracking Plan

#### 1. A/B Experiment Settings
- **Experiment Name**: `exp_[feature_name]_[version]`
- **Enrollment Trigger**: User visits [Page/Route]
- **Traffic Split**: 50% Control (Old UI), 50% Treatment (New UI)

#### 2. Event Tracking Schema

| Event Name | Trigger Action | Key Parameters | Purpose |
| :--- | :--- | :--- | :--- |
| `[event_name_happy]` | Success screen renders | `user_id`, `session_id`, `order_value` | Measure North Star Metric lift. |
| `[event_name_click]` | Click on CTA | `user_id`, `session_id`, `button_id` | Measure interaction rate. |
| `[event_name_error]` | Exception encountered | `user_id`, `session_id`, `error_type` | Measure failure rates from Step 4. |

#### 3. Success Threshold & Closing the Flywheel
- **Primary Success Criteria**: North Star Metric lift is statistically significant ($p < 0.05$) with at least 80% power and a pre-defined MDE that is business-meaningful.
- **Closing the Flywheel**: Post-launch empirical data, error distribution, and updated baselines will be fed directly back into `pm-1-funnel-diagnostic` to construct the next iteration's funnel and expose the next leverage leak.
```
