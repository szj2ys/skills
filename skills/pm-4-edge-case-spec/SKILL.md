---
name: pm-4-edge-case-spec
description: Zero-ambiguity functional specification and edge-case mapping. Use when writing product requirements, aligning with engineering on acceptance criteria, or detailing state transitions, error-handling, and offline behaviors.
---

# Edge-Case Spec & Functional Zero-Ambiguity (Flywheel Step 4)

This skill ensures requirements are written with complete functional completeness. A high-end specification spends **30% on the happy path and 70% on edge cases, errors, and interaction extremes**.

## 🌀 The Flywheel Connection
- **Upstream Input (from `pm-3-mvp-prioritizer`)**: The ruthlessly trimmed MVP feature set.
- **Downstream Output (to `pm-5-ab-tracking`)**: Unambiguous state transitions and user flows (both happy paths and exception flows) that must be tracked as events.

---

## 1. Zero-Ambiguity Acceptance Criteria (Given/When/Then)
Write functional requirements in a strictly testable, non-ambiguous format:
- **Given**: [Current state of the application / user status]
- **When**: [The user performs a specific action]
- **Then**: [The expected system behavior occurs]

---

## 2. The 5-Dimension Exception Framework
For every MVP feature, you must explicitly specify the system behavior across these five dimensions:

### Dimension 1: Network & Performance Exceptions
- Offline behavior (e.g., network drops mid-action).
- API timeout thresholds (e.g., API takes > 5 seconds). Does it retry, show a non-blocking toast, and preserve user input?
- Loading states (e.g., skeleton screens, button spinners) to prevent double-submitting.

### Dimension 2: Data Extremes
- **Empty States**: Clear illustration and action when no records exist.
- **Overflow States**: Wrap or truncate with ellipsis for long text.
- **Limits**: Behavior when counts are zero, negative, or exceed maximum bounds.

### Dimension 3: User Interaction Extremes
- Frontend button disabling on click to block spam.
- Concurrent tabs or multi-session state conflicts.

### Dimension 4: Validation Failures
- Error indicators (inline red helper text vs blocking toasts).
- Input sanitization and format warnings.

### Dimension 5: System & Auth State
- Session expiration mid-flow.
- Permission denial.

---

## 3. Edge-Case Checklist
1. **Are all happy paths detailed as Given/When/Then criteria?**
2. **What are the top 3 exception scenarios that could fail?**
3. **How does the frontend handle slow networks, timeouts, and blank data?**

---

## Output Template (Seeds `pm-5-ab-tracking`)

```markdown
### 🛡️ Functional Spec & Edge Cases

#### 1. Given/When/Then Acceptance Criteria
- **Scenario 1: Happy Path [Name]**
  - **Given**: [State]
  - **When**: [Action]
  - **Then**: [Outcome]

#### 2. Exception Handling Specification

| Dimension | Triggering Event | Expected System Behavior |
| :--- | :--- | :--- |
| **Network** | API Timeout (>5s) or Offline | Show toast warning, keep form fields populated, enable retry button. |
| **Data** | Empty state (0 results) | Render placeholder screen with direct "Get Started" call-to-action. |
| **UX** | Button click | Instantly disable submit button, display loading spinner. |
| **Validation** | Format error | Outline input field in red, show inline error, keep submit disabled. |

- **Next Flywheel Step**: Pass these happy paths and exception states to `pm-5-ab-tracking` so we can track the rate of both successful and failed transitions.
```
