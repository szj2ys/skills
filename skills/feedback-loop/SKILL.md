---
name: feedback-loop
description: Design or build in-product feedback capture with context and a triage path — 用户反馈, feedback widget, 反馈功能, user bug reports. A submitted defect is diagnosing-bugs; interpreting metrics is data-review.
---

# Feedback Loop

## The one rule

**Ask at the moment of experience, attach safe context automatically, and get every message to someone who acts on it.**

## Mode

Building the widget is in scope when asked. Replying to users, sending interview invitations and offering incentives (credits, discounts, gifts) need the owner's approval of the offer, budget and channel; until then they are drafts.

## 1. Where to ask

- **Always there**: a quiet feedback entry on the core task page, for logged-out visitors too.
- **One active prompt at most**: after the result is used, or after an error is recovered, with eligibility, cooldown and dismissal defined.
- Every prompt keeps the user's work in place.

## 2. What to attach without asking

An allowlist: route template (no query strings, fragments, tokens or ids), app version, browser and screen, recent client error type and message with values redacted, user id taken on the server for logged-in users. Form contents, documents, share links and payment data stay out unless the user chooses to attach them.

## 3. Store and protect

Store in the product's own database with size limits, a rate limit and a retention period. Anonymous users can submit but never read; only staff can list feedback; text is rendered as text.

## 4. Triage and reply

States: new → acknowledged → linked to a fix → fixed → verified → closed. Data loss, payment and security reports go to the owner the same day; the rest weekly. A "fixed" reply is sent only after the reporter's path is rechecked.

## Output

Placement plan · captured and excluded fields · storage and access rules · triage flow · implementation (when requested), verified logged out and logged in: confirmation shown, the user's work kept, the stored row read back, a rate-limited or failed submit handled without losing the draft.
