---
name: serp-seo
description: Decide which page should rank for which search intent from observed search results — SEO 优化 of an existing site, keyword-to-URL mapping, cannibalization (关键词蚕食), "why doesn't this page rank", a technical SEO pass. One new page is geo-page; templated page sets are programmatic-seo.
---

# SERP SEO

## The one rule

**No change without a row in the decision matrix.** An intent row is: query → observed SERP evidence → intent → what ranks → our URL → gap → action → expected user outcome. A technical row is: URL → observed HTTP, rendering or config evidence → defect → action (query `n/a`). An edit that traces to no row is out of scope.

## Mode

An analysis or "why" request produces the matrix and recommendations. Edit code when the user asked for changes. Removing pages, redirects, noindex and production indexing changes need that scope stated explicitly.

## 1. Product, then queries

Learn the product, users, money pages, framework, rendering and routes. Derive 5–15 core queries yourself: product, feature, scenario, problem, category, `best X`, `X alternatives`, `X vs Y`, `X free`, `how to …`.

## 2. Observe each SERP

Search for real. Per top result record rank, URL, page type (tool, product, category, comparison, list, guide, forum, video), title, H1, primary keyword (label it `inferred`) and what it gives the user. Note SERP features: People Also Ask, snippet, AI overview, video, forum results, related searches. Then answer: **what does the engine think this user wants?**

Name the engine or tool used; a search API is not Google. A query whose results you could not see stays `unknown` and gets no intent action.

## 3. First-party data first

State Available/Unavailable for Search Console, GA4, Bing Webmaster, analytics and server logs. With Search Console, work these first: position 4–20, high impressions with low CTR, a query landing on the wrong URL, two URLs splitting one query.

Label every claim Observed, Estimated or Inferred.

## 4. One intent, one URL

Per intent choose one action:

- **OPTIMIZE** — the existing page is the right one.
- **CREATE** — no fitting page, and real demand, a clear problem, product relevance and unique value all hold.
- **MERGE** — several pages split one intent.
- **REDIRECT** — no standalone value, but it has links or history worth keeping.
- **NOINDEX** — useful to users, not to search.
- **REMOVE** — low value or duplicate.

Cannibalization is the same intent judged by SERP and content topic, not shared words. Page type follows the SERP: a tool intent gets a tool page.

## 5. Crawler view

For each money page record raw HTML (no JS), rendered HTML, and content that needs a click or login. Core content missing from raw HTML is a risk for crawlers that do not render; flag what is actually absent rather than the component type. Check robots.txt in the **production** configuration, sitemap, canonical, noindex, status codes, redirects, and hreflang when multilingual. Private routes stay excluded.

## 6. Trust is evidence

User counts, testimonials, press, ratings and benchmarks without a source are flagged and removed, never added.

## 7. Verify what changed

After edits, run the changed revision in a production build or an identified preview and check every changed surface: status, title, H1, canonical, robots, raw-HTML content, schema, sitemap membership, links and redirects, locale alternates, mobile render. Check production again only after an authorized deploy, confirming its revision. Regression: no new 404, noindex, canonical error, lost content or cannibalization. A technical pass makes no ranking promise.

## Output

1. Data availability line.
2. Decision matrix (intent rows and technical rows).
3. Technical issues P0–P3: problem | evidence | file/URL | action.
4. Changes made: file | change | matrix row — or recommendations when in analysis mode.
5. Verification output.
6. Next queue, ordered by demand × intent fit × product relevance × ranking chance × business value.
