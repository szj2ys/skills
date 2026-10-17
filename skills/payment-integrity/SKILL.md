---
name: payment-integrity
description: Prove money, orders, subscriptions and entitlements agree — 支付审计, subscription/refund/webhook testing, double-granted credits — or switch payments from test to live (测试改真实支付). General launch checks are launch-readiness.
---

# Payment Integrity

## The one rule

**Each business effect happens exactly once, on the server, after the provider confirms it.** The client redirect, the success page and request fields grant nothing.

## Mode

Audit with sandbox money and isolated data; report findings and leave code unchanged unless fixes were requested. Live charges, refunds, cancellations, provider account changes and the live cutover need explicit authorization for that target and amount.

## 1. Write the policy, then hunt deviations

State the intended transitions the product supports: trial, grace period, full and partial refund, immediate versus period-end cancellation, renewal, failed renewal, dispute, upgrade and downgrade. Unknown policy → assume the provider's defaults and say so.

Deviations to hunt: paid but no entitlement · entitlement without confirmed payment · one effect granted twice (duplicate webhook, two events for one payment, refresh, retry, concurrency) · one checkout intent charged twice · refund or dispute leaving entitlement the policy says to revoke · cancelled yet charged again · an older event overwriting a newer state.

## 2. Audit the chain

checkout → order → payment → webhook → subscription → entitlement → account. For each link find the code and answer:

1. **Actor and offer**: is the buyer taken from the authenticated session, and the plan id validated server-side into product, price and currency? Identity, amount and payment success sent by the client are never trusted.
2. **State machine**: where are order states (pending, paid, failed, cancelled, refunded, expired, past_due) and are transitions guarded against out-of-order events?
3. **Webhook**: signature verified against the raw body; events claimed atomically; uniqueness enforced on the business effect (payment, invoice, billing period), not only the event id; a crash between claim and grant recoverable.
4. **Entitlement**: written with the order state change and keyed to it so it can be reversed.
5. **Recovery**: payment succeeded but the local write failed → a reconciliation job or provider re-query repairs it.
6. **Logs and keys**: no secrets, card data or full payloads in logs; key mode (test/live) matches price ids, product ids and the webhook secret.

## 3. Prove it

Run the worst cases against the sandbox: forged unsigned webhook, the same event twice, a direct hit on the success URL, a tampered amount, one checkout intent retried concurrently and after a timeout. Record each request and the stored state afterwards.

## Go-live branch

1. Identify provider and SDK/API version from the code; read the provider's **official** live-mode docs now and list their requirements.
2. The audit shows no open deviation. Test/live data are separated, displayed amounts equal live prices, and a rollback revision exists.
3. Configure live products, prices, webhook endpoint and secret, keys in the secret store. Owner-only steps (KYC, identity, bank, 2FA, legal attestations) → `UNVERIFIED: blocked — owner must <action>`; continue with the rest.
4. A real charge only with explicit approval in this conversation; use the provider's recommended live check, then refund.
5. Report sandbox coverage and live verification separately.

## Risk signals

Fast signup → pay → no usage → dispute looks like card testing. List suspicious orders for the owner; refunds and bans are the owner's call.

## Output

Case matrix: case | expected (per policy) | observed provider state | observed stored state | evidence | PASS/FAIL/UNVERIFIED. Findings: illegal state | repro | root cause file:line | type (payment / subscription / entitlement / consistency / webhook) | severity | fix. Overall rating and the top 3 fixes. An integrity pass needs every required case observed.
