---
name: launch-readiness
description: Decide GO or NO-GO before a site or SaaS goes to production — 上线检查, 上线前审计, launch checklist, "can we ship". Audits by running the app and attacking it, not by reading code alone. Release decisions only; whole-repo quality review is ponytail-audit, UI critique is web-audit.
---

# Launch Readiness

## The one rule

**NO-GO while any P0 or release-critical journey is open or unverified.** A blocker closes only with evidence from this run that demonstrates the exact assertion: durability needs a storage read-back after restart, recovery needs restored data, a screenshot proves only what is on screen.

## Mode

A check request produces a report: reproduce and record, leave source and deployment untouched. Fix blockers only when the user asked for fixes. GO never authorizes deployment.

Attack an isolated copy: production build settings with test data, provider sandboxes and disposable accounts. Production writes, restarts, deletions or billable requests need explicit authorization for that target.

## 1. Critical journeys first

Write the 1–3 journeys the product exists for (e.g. sign up → create → pay → use → return). GO requires each to pass end to end. A broken step on one of them is a blocker.

## 2. P0 classes — attack each

- **Boots**: the production build starts with production config and its critical dependencies.
- **Success is real**: whatever the user sees as done (created, paid, deleted, saved) is read back from storage after a refresh and after a restart.
- **Authorization and injection**: user B requests user A's object by id; logged-out calls to protected APIs; normal user to admin actions; client-sent price, user id or status trusted; XSS, SQL injection, CSRF, abuse limits where applicable; session cookie flags.
- **Money and entitlement**: when payments exist, run `payment-integrity`; each illegal state it confirms is a P0.
- **Secrets**: none in frontend bundles, the repo or logs; test and live keys not mixed.
- **Data survives**: restart, deploy, a second instance (in-memory sessions, local files on ephemeral disk); a backup exists and a restore into a separate target was performed.
- **Indexable where intended**: the production robots, noindex and canonical settings keep public acquisition pages crawlable and private routes excluded. Read the production configuration branch.
- **Deletion matches the policy**: deleting an account revokes access and removes what the privacy policy promises.

## 3. P1 and P2

P1: logout and session expiry, mobile breakage of a critical journey, non-money consistency, missing privacy policy or terms, tracing a request user → order → payment → entitlement in logs. P2: performance, SEO polish, UX.

## Output

1. Verdict `GO` or `NO-GO` with the blocking items.
2. Table: item | class | P0/P1/P2 | attack | expected | observed | evidence | PASS/FAIL/UNVERIFIED.
3. Fixes made (only when requested), with rerun evidence.
4. Must fix before launch / can wait.

No real phone → mobile is `UNVERIFIED (no device)`. A self-verified PASS on money, auth or data paths needs one independent review — another session or agent — before GO.
