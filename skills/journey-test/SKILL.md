---
name: journey-test
description: Test whether a target user can complete and recover the core task in a running site, then cut steps — 用户旅程测试, E2E 体验测试, 像真实用户一样测试, 业务流程梳理, weak network, refresh mid-task. Visual measurement is web-audit; one reproduced bug is diagnosing-bugs; automated coverage is test-safety-net; release decisions are launch-readiness.
---

# Journey Test

## The one rule

**Start where a real user starts, know only what they know, and finish their task — or record exactly where you could not.** During the walk use only what the user has: the visible page, their email, their device. Code reading, internal routes and direct API calls come afterwards, to explain what you saw.

## Mode

Walk an isolated copy with test data, disposable accounts and provider sandboxes. Real signups, sends, purchases or deletions on a live site need explicit authorization for that target. A test request produces findings; code changes only when asked.

## 1. Define the walk

Target user (who, what they want, which device), entry point (the URL they arrive on from search, an ad or a shared link), the core task, and the result they need next. Add the second journey: the person who receives what the user produces (shared link, export, email). States that need setup (expired plan, empty quota) are prepared as fixtures and recorded as prepared, not as user actions.

## 2. Walk it — real browser, mobile first

Mobile viewport with touch first, then desktop. For a harness PASS, record the desktop pass as the journey `desktop` list (website-experience.md §2.7: `viewport`, `action`, `observed`, own screenshot); a passing build is not a walkthrough. Check the software keyboard covering inputs, orientation, real gestures where used. Label emulation versus a physical device. After each step record action, expectation, observation and a screenshot; choose the next step from what the screen offers.

## 3. Break it on purpose

Refresh and back mid-task; close and reopen; two tabs; logout and re-entry; slow and offline network, then recovery; double submit; empty, oversized and invalid input; session expiry; out of quota. Paid flows hand success, failure, cancel and refund states to `payment-integrity`. Check that what the user sees equals what is stored equals the final result.

## 4. Cut steps without cutting safeguards

For each step ask, in order: delete, merge, automate, default — then guide. A cut keeps the task outcome, informed consent, price visibility, confirmation of destructive or paid actions, and recovery intact.

## Output

Friction log: # | step | expected | observed | evidence | impact (blocks task / slows / confuses) | cause if known | fix.
Then P0 (blocks the core task) / P1 / P2, untested cases, and the proposed shorter journey — labelled proposed until it is built and replayed from the same entry.

A journey that could not be finished is the first finding, with the exact point where it stopped.
