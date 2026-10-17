---
name: i18n-seo
description: Build or audit a multilingual site — 多语言, hreflang, language switcher, 语言自动识别 — or decide what a new language market needs — 本地化, 小语种站, local keyword research. Two branches, engineering and market.
---

# i18n SEO

## The one rule

**New indexable acquisition pages exist because that market searches for them; every locale page is wired so engines and people land on the right one.** Product, checkout and support localization follow user needs without a search-demand test.

Pick the branch: **engineering** when the site has or needs locales, **market** when deciding which markets and pages. "Add language X" runs both.

## Engineering branch

Mark each invariant PASS, FAIL or UNVERIFIED with evidence.

1. **URLs**: keep an existing valid scheme (prefixes, subdomains, country domains); stable, crawlable, one explicit route-to-locale mapping; new designs default to path prefixes (`/en/`, `/zh-CN/`); `?lang=` is not the SEO URL. One locale code everywhere: URL, `<html lang>`, metadata, hreflang, translation files.
2. **Resolution order**: explicit user choice > locale in URL > saved preference > Accept-Language > geo hint > default. Only locale-less entries such as `/` are detected; an explicit locale URL is served as requested.
3. **Memory**: a manual switch saves the preference (and to the account if one exists) and survives refresh, return visits and a browser-language change.
4. **Switcher**: one navbar control showing the current language; a dropdown of the languages that actually exist, with text labels, keyboard and mobile support. Ten or more languages never widen the navbar.
5. **Same page**: switching keeps the page (`/zh-CN/pricing` → `/en/pricing`), falling back to that locale's home only when no equivalent exists.
6. **Canonical**: each locale page is self-canonical.
7. **hreflang**: groups contain only true equivalents; each member lists every member of its group, itself included, reciprocally; `x-default` chosen deliberately. Targets return 200 in the right language; if both HTML and sitemap carry alternates, they agree.
8. **Links, sitemap, rendering**: internal links stay in the current locale; the sitemap lists final indexable locale URLs; raw HTML of each locale URL contains that locale's content.

Test with real requests: clear cookies and request `/` with each Accept-Language; switch → refresh → revisit `/`; request explicit locale URLs with a mismatched Accept-Language; switch from a deep page.

## Market branch

1. **Market = language + country** where it matters (`es-MX` ≠ `es-ES`): compare wording, currency, payment methods and SERPs before deciding between one language page and regional pages.
2. **Start from the job, not the English keyword**: business need → local wording → local search behaviour → local SERP → local intent → local page.
3. **Collect how locals say it, with sources**: local SERP (set region and language; say so if you cannot), autocomplete, Search Console by country, local competitors' copy, local forums and video, app stores and marketplaces. Term map: literal translation | common term | search term | community wording | commercial term. Recommend a term only with evidence; product and UI terms need two sources or `needs native review`.
4. **Decide per market**: pages to create (local demand the English site lacks), pages to skip (no local demand), payment, trust and legal differences.
5. **Copy**: keep the brand name; keep direct translations the evidence supports and rewrite where local usage differs. Naturalness is `unverified` until a native speaker reviews it.

## Output

Engineering: invariants 1–8 with evidence → fixes (when requested) → retest. Market: per market the term map, keyword map, SERP notes, create/skip list and evidence strength (strong / medium / weak).
