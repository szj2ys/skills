---
name: find-demand
description: Find and rank paid demand worth building — 找需求, 找方向, 做什么网站赚钱, seed-word expansion (种子词), copying a validated product (抄产品), paywall reverse lookup (支付墙反查 via Similarweb), or validating an existing site's imagined audience. Improvement ideas for a product are growth-ideas; scoping a chosen clone is website-mvp.
---

# Find Demand

## The one rule

Answer two questions separately for every candidate, each with evidence:

- **Can we win?** at the entry query we would actually target: SERP strength, competitor age and authority.
- **Is it worth winning?** demand × payment intent × end-state revenue × build speed.

Low keyword difficulty answers only the first. A candidate earns `build` only when both are answered.

## Entries

| Entry | When | Start from |
|---|---|---|
| social-signal | demand before search volume exists | Reddit, X, YouTube comments, HN, GitHub issues, app and extension reviews: "is there a tool that", "I wish there was", "looking for an alternative", "how can I automate" |
| validated-market | mature category, looking for a late-entrant wedge | a proven product; treat its head term as context and test 3–5 long-tail task, scene or persona queries it under-serves |
| paywall-reverse | Similarweb Pro access | checkout domains (checkout.stripe.com, paypal, paddle, dodopayments, creem, clinkbill, razorpay) → referring sites → small independent tool sites → their organic keywords → SERP |
| seed-expand | the user gives seed words | seed × function word (generator, converter, checker, extractor, tracker…) × a new capability × a concrete actor and action: "AI product photo generator for Shopify sellers", not "AI generator" |

## Evidence

- Every number carries source and date. A number you did not observe is `not found`; third-party traffic and difficulty figures are labelled estimates.
- User pain is a verbatim quote with a link.
- Name the search tool you actually used. A web-search API result is not "Google top 10".
- A missing tool (no Similarweb login, Trends blocked) is stated once; continue with the next source and mark the affected column.

## Demand test (each candidate)

1. Specific: who, in which situation, doing which action.
2. Frequency: how often one buyer needs it, and how many buyers need it. Occasional tasks qualify when willingness to pay is strong and buyers are reachable.
3. Searching: people search, ask, compare tools, or pay someone.
4. Pay reason: saves time, avoids errors, earns money, or avoids a loss.
5. Timing: dated trend evidence — rising, stable or eroding (for example, being absorbed by AI assistants or platforms).

## Worth-winning test

- Read the top 10 for the entry query: old strong domains or young sites? For a young site that ranks, check its traffic and how it earns. A young ad-funded site with thin traffic means winning buys thin ad income.
- End state: separate observed inputs from assumptions; show low / base / high monthly contribution after delivery and acquisition cost, and the break-even paid conversion rate. If the case rests on an untested rate, the verdict is `investigate`.
- Volume is not a threshold: small volume with strong paid intent beats big volume of free-only users.
- Default out: ad sites, pure content sites, games, free tools without a paid path. Giants (Google, Adobe, Canva, Wikipedia) are context, not candidates.

## Output

1. Table: candidate | user + job | evidence (quotes, links) | entry query | can win? | worth winning? | verdict (`build` / `investigate` / `drop`) + one-line reason.
2. For each `build`: an MVP that ships in 7 days or less (homepage = the core tool, one keyword cluster), its first 3–5 URLs, and the paid path.
3. For the top candidate: where the first 100 users come from before SEO ranks, the one-week validation step, its cost, and the number that would kill it.

Done when every candidate has both questions answered or marked unknown with what would answer it, and no number lacks a source.
