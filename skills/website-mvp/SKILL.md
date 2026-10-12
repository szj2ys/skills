---
name: website-mvp
description: "Use when given a website URL to scope an MVP by replicating its core pages, or when asked which core pages a site has. Triggers: analyze this site for an MVP, which core pages does this site have, what should I clone, build an MVP from this site, 模仿这个网站做 MVP, 核心页面, 复刻, MVP 范围. Delivers a Core Page Map (paid job | core routes | result) and a P0/P1/Defer scope first; differentiation is a later, parked phase."
---

# Website MVP

## The one rule

**Emit the Core Page Map before any analysis.** If the user still cannot name the core pages after
your first screen, the report failed. Return exactly sections 1–8, in this order, nothing added.

## Stance — 僵化 → 固化 → 形成自己的东西

Faithfully replicate the target's core functional loop first (僵化), make that copy run end to end
second (固化), differentiate only later (§ Parked). You are extracting which pages and flows to copy
— not auditing the competitor and not hunting its problems.

## Inputs — start from a URL

The user hands you a site address. Missing input that would change the recommendation → state the
assumption and continue; do not block. Never guess a route from memory.

### Route discovery (verified — no single source is complete)

1. `curl -sL <origin>/robots.txt`: collect every `Sitemap:` line **and** every `Allow:`/`Disallow:`
   path token, then fetch each sitemap and parse `<loc>`. If a `<loc>` ends in `.xml` it is a
   sitemap **index**, not a route — fetch it and parse again (mocklive.ai: root index → 12 locale
   children, `en.xml` alone carries 337 routes). Sitemaps: notion.so 169, makeinterview.com
   16, `duolingo.com/sitemap.xml` → 200 with 0 `<loc>`. Robots paths are free route evidence — on
   makeinterview `/operator` and `/pass` are `Disallow`ed, absent from the sitemap and from every
   rendered href, and still return 200. A disallowed-but-alive path is often the real app route.
   If a `<loc>` ends in `.xml` it is a sitemap index, not a route — fetch it and parse *its* `<loc>`
   as routes (mocklive.ai: root index → 12 locale children, `en.xml` alone = 337 routes).
2. Take `href`s from the raw HTML **and** the rendered page (Playwright: `python3 -I` +
   `playwright.sync_api`, browsers installed), then from each hub page so nested routes reach the
   union. On makeinterview: raw HTML 9 page routes, rendered 8, sitemap 16 — none is complete alone.
   Strip asset hrefs first (`/_next/static/*`, `favicon.ico`, images, `cdn-cgi`).
3. Normalize: strip query and trailing slash, group by locale prefix, collapse `/en/*` and `/zh-CN/*`
   into one set — here 19 live routes → 12 distinct paths, 8 after long-tail folds into its area row.
   **Exception:** if hrefs carry `#/` or a page-defining query key, that is the router — keep it as
   the path, or a hash-routed SPA collapses to a single `/`.
4. Status-probe with redirects followed: `curl -sL -o /dev/null -w "%{http_code} %{url_effective}"`.
   Drop only 4xx/5xx, then normalize on the **effective** URL — without `-L`, `/pricing` reports 301
   and is a live route, and a `www.` paste 301s every candidate to the apex host. On a fallback SPA
   every path returns 200, so 200 alone does not prove the route renders: check for post-render
   content.
5. Open each hub and count what it actually renders — e.g. a practice hub exposing `Interviews 14,
   Exams 9, Roleplay 8, Speaking 3, Resume 4`. No visible count → `count not observed`; never
   estimate, and never import another site's counts into this site's map.

## 1. Core Page Map

**Paid to do: <the job the user is buying> → Gets: <what they walk away with>** — one line above the
table. If you cannot write it, you have not found the core yet.

| Area (the paid job) | Core routes | Role (what the user gets + the observed flow) |
|---|---|---|
| <paid job> | <route-1>, <route-2> | `observed` — setup flow; result: <artifact> |

One question classifies every discovered route:

- Does the user **perform the paid job, or receive its result**, here? → **core** — a row in this table.
- Does it only **authenticate or take money** to complete the job (arrival page, sign-in,
  pricing, checkout)? → **wrapper** (§4), never in this table.
- Neither — marketing, trust, SEO, legal, support content → **Defer** (§2).
- A hub that routes *into* the paid job is core; a page that only markets it is not.

Rules: one row per paid job, no route in two rows, long-tail folded into its job row, counts where
observed. Label each row `observed` / `inference` / `open question`. Never claim a feature without an
implementation path (route, API, or named build step) — no path → `open question`.

## 2. Recommended MVP Scope

Exactly three buckets, no preamble:

1. **P0 — <primary job>-focused MVP**: every core route on the path hub → core product route →
   result, plus the one state that proves value (`session state plus scored report/replay`), plus
   one wrapper line each for the arrival page, sign-in and pricing so it can ship. Every core P0
   route traces to a map row. One primary job, defaults over configuration, one working outcome over
   a menu of half-finished ones.
2. **P1 — one adjacent room**: best candidate, one alternative, one line of reason each
   (*best `/roleplay` with one scenario; alt `/speaking` with one presentation room; add `/exams` only
   if exam prep is the actual wedge*). A second area only if it is the wedge.
3. **Defer**: long-tail SEO pages; all content/variant/category routes; every catalog beyond the
   first working unit; multi-language; guides, comparisons, careers, legal beyond the minimum.
   Fragments, not paragraphs.

When the full catalog exceeds what can be cloned, P0 ships **one working path through it**, not a
thin version of all of them.

## 3. Core Loop Spec (僵化)

For the P0 core routes only:

- Flow line: `arrival → setup → core interaction → result → next action`.
- Per transition: source, trigger, destination, preserved data, primary CTA, failure fallback.
- States the copy must ship: empty, first-run, loading, partial, timeout/abort, resume.
- Observed gates on the core path (e.g. the target forces sign-in at session start) appear as one
  clause on the flow line — listed, never analyzed.
- Per P0 route: delivery path (API / server-rendered / named build step) and one acceptance
  criterion — no delivery path is an `open question`, not a plan.
- Copy the observed behavior; do not improve it. Deviations go to the Parked addendum.

**固化 gate** — only when a build was requested: the copy is done when every P0 route is reachable,
the core interaction completes, the result survives a refresh, and timeout / network-error /
duplicate-submit behave. A design-only report grows no build section.

## 4. Wrapper Surfaces — not core pages

`/`, `/pricing`, `/signin`, checkout, entitlement: **these are not core pages** and never appear in
§1. One table, one line each — `surface | minimum the P0 needs` — listed so they ship, deliberately
shallow: no funnel math, paywall essay, or conversion-trigger justification unless the user asks
after sections 1–5.

## 5. Evidence

One line each, no paragraphs: `route | observation | date | confidence` — `observed` rows only.
Counts and flows beat adjectives. No invented user evidence: no personas, testimonials, usage
numbers, or demand signals you did not observe. Sitemap size, nav labels, and marketing copy are not
demand.

## 6. Risks & Open Questions

Max 5 bullets, each an `open question` plus what would answer it. No generic risk boilerplate
("competitor may change pricing", "execution risk").

## 7. Next Step

The single next build or validation action.

## 8. Verification Status

```
Acceptance status: PASS | FAIL | UNVERIFIED | N/A — design-only
Evidence: <URL / route / command behind live claims, or why no runtime path exists>
assumed: <basis>   # every unsourced number
```

`N/A — design-only` only when no build was requested, and it must say why. Unsupported claims are
`UNVERIFIED`, never `PASS`.

## Report rules (anti-fluff)

- Max 3 visible sentences of prose per section; tables and bullets carry the rest.
- One table answers one question; never list the same route twice in one report.
- Never restate the user's brief or the target's marketing copy back to them.
- Forbidden: TAM, feature-parity lists, marketese, generic best-practice advice, section headers
  that exist only to be thorough.
- Delete test: if removing a section would not change what the user builds, delete it.
- Saved report: the harness HTML contract supplies page chrome (title, generated_at, charts,
  confidence, evidence matrix); the body stays exactly sections 1–8, with §1 first — it *is* the
  Key takeaway.

## Parked — later phase (silent unless asked)

Differentiation wedge · demand evidence · unit economics · ablation experiments · growth and
conversion loop · go/kill criteria. Run only after the P0 copy works (固化). If the user asks, add one
short addendum after section 8 — max 3 lines, including any deviation from the copied flow.
