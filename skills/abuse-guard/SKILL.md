---
name: abuse-guard
description: Assess where bots and scripts can abuse a SaaS and propose the least friction that bounds the loss — 防刷, 人机检测, Cloudflare Turnstile, rate limiting, free-credit farming, scraping. Implements when asked. Payment correctness and suspicious-order review are payment-integrity.
---

# Abuse Guard

## The one rule

**Bound the loss where abuse costs money or harms users, enforce it on the server, and keep ordinary browsing free of challenges.**

## Mode

A check request produces the abuse map and a plan. Code changes when asked. Tests run against an isolated copy with sandboxed providers and capped request counts; production attacks, provider rule changes, refunds and bans need the owner's explicit decision.

## 1. Map abuse points by cost

Signups that grant free credits or trials · AI generation and other paid compute · login and password reset (credential stuffing, enumeration) · email and SMS sends · checkout (card testing) · invitations and rewards · enumerable endpoints exposing user data · forms that publish content · costly public reads.

For each: what an attacker gains, what each abuse costs us, current protection, and how an attacker would get around the obvious fix (rotating IPs, many emails, shared networks).

## 2. Choose controls per attack

Pick controls that bound the loss even when one is bypassed: limits per account, IP and device with defined windows and room for legitimate bursts; email verification before value is granted; Turnstile on the action that grants value; unguessable ids and ownership checks for user data; the payment provider's fraud rules for checkout.

A challenge token is checked on the server before the value is granted: action and hostname match, missing, invalid, expired and replayed tokens are refused, and an outage of the verifier has a defined behaviour. Search crawlers keep access through verified bot identity, not user-agent strings.

## 3. Prove it

From the policy, test below, at and above each limit, concurrent requests, and window reset; compare the work actually granted and stored, not only the HTTP status. Then run the normal journey and show it still works.

## Output

Abuse map (point | gain | cost to us | current | bypass | control) · changes (when requested) · replay results before and after · a review date with the numbers that decide rollback (legitimate completion rate, challenge failures).
