# szj2ys/skills

A focused library of 27 AI agent skills for product work, engineering delivery, frontend quality, growth, and documents.

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

- `Diagnose this failing test and find the root cause.` uses `diagnosing-bugs`.
- `Convert report.md into a styled PDF.` uses `any2pdf`.
- `Audit example.com for technical SEO issues.` uses `seo-audit`.

## Skills

### Analysis and Product

| Skill | Use it for | Install |
|---|---|---|
| [analysis](skills/analysis/SKILL.md) | Deep horizontal-vertical research on a company, product, technology, concept, or person. | `npx skills add szj2ys/skills -s analysis -y` |
| [iceberg](skills/iceberg/SKILL.md) | Surface missed actions, unknown unknowns, and false confidence in a plan or project. | `npx skills add szj2ys/skills -s iceberg -y` |
| [growth-ideas](skills/growth-ideas/SKILL.md) | Turn product context into concrete improvement, monetization, and acquisition ideas. | `npx skills add szj2ys/skills -s growth-ideas -y` |
| [pm-1-funnel-diagnostic](skills/pm-1-funnel-diagnostic/SKILL.md) | Diagnose funnels and identify high-leverage conversion improvements. | `npx skills add szj2ys/skills -s pm-1-funnel-diagnostic -y` |
| [pm-2-metric-guardrail](skills/pm-2-metric-guardrail/SKILL.md) | Define North Star metrics and guardrails before building a feature or experiment. | `npx skills add szj2ys/skills -s pm-2-metric-guardrail -y` |
| [pm-3-mvp-prioritizer](skills/pm-3-mvp-prioritizer/SKILL.md) | Scope an MVP and prioritize ideas with ICE when resources are limited. | `npx skills add szj2ys/skills -s pm-3-mvp-prioritizer -y` |
| [pm-4-edge-case-spec](skills/pm-4-edge-case-spec/SKILL.md) | Write unambiguous functional specs, states, errors, and edge cases. | `npx skills add szj2ys/skills -s pm-4-edge-case-spec -y` |
| [pm-5-ab-tracking](skills/pm-5-ab-tracking/SKILL.md) | Design A/B tests and the event-tracking specification needed to evaluate them. | `npx skills add szj2ys/skills -s pm-5-ab-tracking -y` |

### Engineering Delivery

| Skill | Use it for | Install |
|---|---|---|
| [commit](skills/commit/SKILL.md) | Review staged work and create one conventional commit. | `npx skills add szj2ys/skills -s commit -y` |
| [commits](skills/commits/SKILL.md) | Split related work into atomic, reversible conventional commits. | `npx skills add szj2ys/skills -s commits -y` |
| [create-branch](skills/create-branch/SKILL.md) | Create a correctly named working branch. | `npx skills add szj2ys/skills -s create-branch -y` |
| [pull-requests](skills/pull-requests/SKILL.md) | Prepare and create a clear pull request. | `npx skills add szj2ys/skills -s pull-requests -y` |
| [simplify](skills/simplify/SKILL.md) | Refine recently changed code for readability without changing behavior. | `npx skills add szj2ys/skills -s simplify -y` |

### Debugging and Review

| Skill | Use it for | Install |
|---|---|---|
| [diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) | Investigate hard bugs, failures, regressions, or performance drops to root cause. | `npx skills add szj2ys/skills -s diagnosing-bugs -y` |
| [doc-drift](skills/doc-drift/SKILL.md) | Find conflicts between documentation, prototypes, and implementation. | `npx skills add szj2ys/skills -s doc-drift -y` |
| [find-unknowns](skills/find-unknowns/SKILL.md) | Expose hidden assumptions and blind spots before implementation or merge. | `npx skills add szj2ys/skills -s find-unknowns -y` |

### Frontend and Performance

| Skill | Use it for | Install |
|---|---|---|
| [frontend-design](skills/frontend-design/SKILL.md) | Make deliberate interface, typography, and aesthetic decisions that avoid template sameness. | `npx skills add szj2ys/skills -s frontend-design -y` |
| [taste-skill](skills/taste-skill/SKILL.md) | Ship distinctive landing pages, portfolios, and redesigns with an audit-first process. | `npx skills add szj2ys/skills -s taste-skill -y` |
| [saas-landing](skills/saas-landing/SKILL.md) | Decide what belongs in a SaaS landing page and what should stay out of v1. | `npx skills add szj2ys/skills -s saas-landing -y` |
| [web-performance-optimization](skills/web-performance-optimization/SKILL.md) | Improve Core Web Vitals with current browser and framework techniques. | `npx skills add szj2ys/skills -s web-performance-optimization -y` |

### Growth and SEO

| Skill | Use it for | Install |
|---|---|---|
| [analytics](skills/analytics/SKILL.md) | Plan and implement measurement with GA4, GTM, Mixpanel, Segment, or another analytics stack. | `npx skills add szj2ys/skills -s analytics -y` |
| [seo-audit](skills/seo-audit/SKILL.md) | Diagnose technical, on-page, content, crawlability, and Core Web Vitals SEO issues. | `npx skills add szj2ys/skills -s seo-audit -y` |
| [site-niche-loop](skills/site-niche-loop/SKILL.md) | Choose, validate, and review the first niche website before investing further. | `npx skills add szj2ys/skills -s site-niche-loop -y` |
| [site-scale](skills/site-scale/SKILL.md) | Choose a scaling path after a site has validated traffic and revenue. | `npx skills add szj2ys/skills -s site-scale -y` |
| [x-growth](skills/x-growth/SKILL.md) | Build a cold-start X/Twitter engagement and posting system for builders. | `npx skills add szj2ys/skills -s x-growth -y` |

### Writing and Documents

| Skill | Use it for | Install |
|---|---|---|
| [writer](skills/writer/SKILL.md) | Draft or expand long-form WeChat articles from briefs and source material. | `npx skills add szj2ys/skills -s writer -y` |
| [any2pdf](skills/any2pdf/SKILL.md) | Convert Markdown with CJK text, code, tables, and formulas into a styled PDF. | `npx skills add szj2ys/skills -s any2pdf -y` |

## Validation

CI validates that every skill directory has parseable frontmatter with a unique, matching name and nonempty description:

```bash
python .github/scripts/validate_skills.py
```

## License

[MIT](LICENSE)
