# szj2ys/skills

A focused library of 39 AI agent skills for product work, engineering delivery, frontend quality, growth, and documents.

## Install

Install every skill:

```bash
npx skills add szj2ys/skills --all
```

Install one skill by replacing `<skill-name>`:

```bash
npx skills add szj2ys/skills -s <skill-name> -y
```

Skills are discovered from their `skills/<name>/SKILL.md` files. After installation, invoke them through your normal agent prompt; the descriptions below are also trigger hints.

Example prompts:

- `Which core pages does example.com have, and what should my MVP copy?` uses `website-mvp`.
- `Convert report.md into a styled PDF.` uses `any2pdf`.
- `Which URL on my site should rank for this search intent?` uses `serp-seo`.
- `Audit this landing page and tell me what to fix.` uses `web-audit`.
- `用罗胖体把这个素材写成稿.` or `把这段改成罗胖体` uses `luopang-writing`.

## Website lifecycle

Which skill to reach for at each stage of building a website, from idea to growth.

| Stage | Skills |
|---|---|
| Find demand | find-demand, analysis, website-mvp |
| Scope and spec | pm-1-funnel-diagnostic, pm-3-mvp-prioritizer, pm-4-edge-case-spec |
| Design | saas-landing, taste-skill, web-audit |
| Build features | pricing, payment-integrity, share-page, feedback-loop, i18n-seo |
| Tracking | analytics, pm-5-ab-tracking |
| Code testing | test-safety-net (existing code); tdd and diagnosing-bugs come from another library |
| User journey testing | journey-test |
| Pre-launch | launch-readiness, abuse-guard, seo-launch |
| Launch SEO and search | seo-launch, serp-seo, programmatic-seo, geo-page |
| Promotion | launch-distribution, backlink-outreach |
| GEO | geo-visibility (site-wide, measured), geo-page (one page) |
| Data analysis | data-review |
| Understand a codebase | systems-map |

## Skills

### Analysis and Product

| Skill | Use it for | Install |
|---|---|---|
| [analysis](skills/analysis/SKILL.md) | Deep horizontal-vertical research on a company, product, technology, concept, or person. | `npx skills add szj2ys/skills -s analysis -y` |
| [growth-ideas](skills/growth-ideas/SKILL.md) | Turn product context into concrete improvement, monetization, and acquisition ideas. | `npx skills add szj2ys/skills -s growth-ideas -y` |
| [pm-1-funnel-diagnostic](skills/pm-1-funnel-diagnostic/SKILL.md) | Diagnose funnels and identify high-leverage conversion improvements. | `npx skills add szj2ys/skills -s pm-1-funnel-diagnostic -y` |
| [pm-2-metric-guardrail](skills/pm-2-metric-guardrail/SKILL.md) | Define North Star metrics and guardrails before building a feature or experiment. | `npx skills add szj2ys/skills -s pm-2-metric-guardrail -y` |
| [pm-3-mvp-prioritizer](skills/pm-3-mvp-prioritizer/SKILL.md) | Scope an MVP and prioritize ideas with ICE when resources are limited. | `npx skills add szj2ys/skills -s pm-3-mvp-prioritizer -y` |
| [pm-4-edge-case-spec](skills/pm-4-edge-case-spec/SKILL.md) | Write unambiguous functional specs, states, errors, and edge cases. | `npx skills add szj2ys/skills -s pm-4-edge-case-spec -y` |
| [pm-5-ab-tracking](skills/pm-5-ab-tracking/SKILL.md) | Design A/B tests and the event-tracking specification needed to evaluate them. | `npx skills add szj2ys/skills -s pm-5-ab-tracking -y` |
| [find-demand](skills/find-demand/SKILL.md) | Find and rank paid demand worth building, keeping "can we win" separate from "is it worth winning". | `npx skills add szj2ys/skills -s find-demand -y` |
| [pricing](skills/pricing/SKILL.md) | Decide value metric, plans, annual framing and upgrade moments with honest, computed numbers. | `npx skills add szj2ys/skills -s pricing -y` |
| [systems-map](skills/systems-map/SKILL.md) | Explain a whole project as a system with evidence-labelled Excalidraw diagrams. | `npx skills add szj2ys/skills -s systems-map -y` |
| [data-review](skills/data-review/SKILL.md) | Read real exports (GSC, PostHog, Stripe, recordings), reconcile them, and decide one next change. | `npx skills add szj2ys/skills -s data-review -y` |
| [feedback-loop](skills/feedback-loop/SKILL.md) | Add in-product feedback capture with safe context and a triage path. | `npx skills add szj2ys/skills -s feedback-loop -y` |
| [website-mvp](skills/website-mvp/SKILL.md) | Scope an MVP from an existing site: map its core pages and sort them into P0 / P1 / Defer. | `npx skills add szj2ys/skills -s website-mvp -y` |

### Engineering Delivery

| Skill | Use it for | Install |
|---|---|---|
| [commit](skills/commit/SKILL.md) | Review staged work and create one conventional commit. | `npx skills add szj2ys/skills -s commit -y` |
| [commits](skills/commits/SKILL.md) | Split related work into atomic, reversible conventional commits. | `npx skills add szj2ys/skills -s commits -y` |
| [create-branch](skills/create-branch/SKILL.md) | Create a correctly named working branch and push it to the remote. | `npx skills add szj2ys/skills -s create-branch -y` |
| [pull-requests](skills/pull-requests/SKILL.md) | Prepare and create a clear pull request. | `npx skills add szj2ys/skills -s pull-requests -y` |
| [simplify](skills/simplify/SKILL.md) | Refine recently changed code for readability without changing behavior. | `npx skills add szj2ys/skills -s simplify -y` |

### Debugging and Review

| Skill | Use it for | Install |
|---|---|---|
| [launch-readiness](skills/launch-readiness/SKILL.md) | Decide GO / NO-GO by booting the app and attacking release blockers; reports unless fixes are requested. | `npx skills add szj2ys/skills -s launch-readiness -y` |
| [payment-integrity](skills/payment-integrity/SKILL.md) | Prove money, orders, subscriptions and entitlements agree; includes the test-to-live cutover. | `npx skills add szj2ys/skills -s payment-integrity -y` |
| [test-safety-net](skills/test-safety-net/SKILL.md) | Add missing tests in risk order, through the real interface, with known bugs kept red. | `npx skills add szj2ys/skills -s test-safety-net -y` |
| [journey-test](skills/journey-test/SKILL.md) | Walk a running site as its target user, break it on purpose, and cut steps safely. | `npx skills add szj2ys/skills -s journey-test -y` |
| [abuse-guard](skills/abuse-guard/SKILL.md) | Map bot and script abuse by cost and add server-side limits and challenges only where they bound the loss. | `npx skills add szj2ys/skills -s abuse-guard -y` |

### Frontend and Performance

| Skill | Use it for | Install |
|---|---|---|
| [web-audit](skills/web-audit/SKILL.md) | Measure a live page in a real browser (contrast, tap targets, LCP/CLS, payload, SSR-vs-hydrated parity, offline) and turn the numbers into a redesign proposal. | `npx skills add szj2ys/skills -s web-audit -y` |
| [taste-skill](skills/taste-skill/SKILL.md) | Ship distinctive landing pages, portfolios, and redesigns with an audit-first process. | `npx skills add szj2ys/skills -s taste-skill -y` |
| [saas-landing](skills/saas-landing/SKILL.md) | Decide what belongs in a SaaS landing page and what should stay out of v1. | `npx skills add szj2ys/skills -s saas-landing -y` |

### Growth and SEO

| Skill | Use it for | Install |
|---|---|---|
| [analytics](skills/analytics/SKILL.md) | Plan and implement measurement with GA4, GTM, Mixpanel, Segment, or another analytics stack. | `npx skills add szj2ys/skills -s analytics -y` |
| [serp-seo](skills/serp-seo/SKILL.md) | Map each search intent to one URL from observed SERPs; no change without a decision-matrix row. | `npx skills add szj2ys/skills -s serp-seo -y` |
| [programmatic-seo](skills/programmatic-seo/SKILL.md) | Decide whether a templated page set deserves to exist, using SERP-overlap samples and per-page payloads. | `npx skills add szj2ys/skills -s programmatic-seo -y` |
| [geo-page](skills/geo-page/SKILL.md) | Create or improve one page that answer engines would cite, checked by a blind comparison against competitors. | `npx skills add szj2ys/skills -s geo-page -y` |
| [i18n-seo](skills/i18n-seo/SKILL.md) | Wire locales correctly (resolution order, reciprocal hreflang) and decide what each language market needs. | `npx skills add szj2ys/skills -s i18n-seo -y` |
| [backlink-outreach](skills/backlink-outreach/SKILL.md) | Screen and submit backlinks one qualified site at a time, with a ledger. | `npx skills add szj2ys/skills -s backlink-outreach -y` |
| [share-page](skills/share-page/SKILL.md) | Make shared generated results open instantly for strangers without exposing private data. | `npx skills add szj2ys/skills -s share-page -y` |
| [seo-launch](skills/seo-launch/SKILL.md) | Make acquisition pages indexable at launch and track eligible / submitted / indexed separately for 30 days. | `npx skills add szj2ys/skills -s seo-launch -y` |
| [launch-distribution](skills/launch-distribution/SKILL.md) | Find where first users already ask, run up to three measured community experiments. | `npx skills add szj2ys/skills -s launch-distribution -y` |
| [geo-visibility](skills/geo-visibility/SKILL.md) | Measure presence in live AI answers with a pinned prompt panel; fix crawler access by bot purpose. | `npx skills add szj2ys/skills -s geo-visibility -y` |

### Writing and Documents

| Skill | Use it for | Install |
|---|---|---|
| [writer](skills/writer/SKILL.md) | Draft or expand long-form WeChat articles from briefs and source material. | `npx skills add szj2ys/skills -s writer -y` |
| [luopang-writing](skills/luopang-writing/SKILL.md) | All-in-one Luo Zhenyu (罗振宇) style writing: brainstorm topic/angle/audience/sources with the user, then a six-stage pipeline (material triage, golden lines mined from user material plus local quote/book corpora, outline gate, draft, review, final) to one finished draft; or use it standalone as a style spec to rewrite existing text. Includes a deterministic draft checker and quote searcher. Reverse-engineered from 2,544 real transcripts. | `npx skills add szj2ys/skills -s luopang-writing -y` |
| [any2pdf](skills/any2pdf/SKILL.md) | Convert Markdown with CJK text, code, tables, and formulas into a styled PDF. | `npx skills add szj2ys/skills -s any2pdf -y` |

## Validation

CI validates that every skill directory has parseable frontmatter with a unique, matching name and nonempty description:

```bash
python .github/scripts/validate_skills.py
```

## License

[MIT](LICENSE)
