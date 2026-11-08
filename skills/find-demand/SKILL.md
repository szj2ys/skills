---
name: find-demand
description: Find and rank paid demand worth building, and research search competitors — 找需求, 找方向, 做什么网站赚钱, seed-word expansion (种子词), copying a validated product (抄产品), entering a market big sites hold (后来者), 竞品主打什么关键词, 竞品拿流量的页面, keyword gap, what competitors rank for, picking a site's next page from competitors' earning pages, paywall reverse lookup (支付墙反查, Similarweb read by the owner), or validating an existing site's imagined audience. Improvement ideas for a product are growth-ideas; scoping a chosen clone is website-mvp; a positioning dossier is competitor-profiling.
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
| validated-market | a mature category whose head terms big sites hold, or a live site choosing its next page | Competitors in search, then Late entrant |
| paywall-reverse | the owner has Similarweb Pro and reads it by hand (its terms forbid robots and scrapers) | checkout domains (checkout.stripe.com, paypal, paddle, dodopayments, creem, clinkbill, razorpay) → referring sites → small independent tool sites → their organic keywords → SERP |
| seed-expand | the user gives seed words | seed × function word (generator, converter, checker, extractor, tracker…) × a new capability × a concrete actor and action: "AI product photo generator for Shopify sellers", not "AI generator" |

## Late entrant

Big sites holding the head terms prove that people pay; the terms are context, not the target. A young domain will not win them soon, and a competitor's conversions cannot be seen from outside, so competitor data finds proven paid demand and open splits. It is not a keyword list to copy.

1. **One split.** Take one split of the job — a persona, a destination app or a constraint — found in autocomplete, user threads and competitors' earning pages, and name the route that found it.
2. **Open or taken.** Read the split's top 10 through a route from Data routes and name it. Mostly forums, videos and social posts mean the split is open; three or more dedicated tools mean it is taken. A results page no route observed is `unknown`, and an `unknown` split is not built.
3. **Differ in the output**: the result the destination needs, ready to use (for a multi-colour 3D print, a 3MF with one part per colour), not a general page under a new title. Users recognise the output; answer engines cite a fact others lack (geo-page); search engines want one intent per URL, in the page type the results page shows (serp-seo).
4. **Volume and repeat jobs** (shops, batches, APIs) beat small one-shot conversions. A bank-statement converter's new subscribers fell from 191 in January to 45 in August 2026 (bankstatementconverter.com/blog/posts/2026-08-28-business-is-dying, posted 2026-08-28, so August may be partial). Its owner does not know why and names three possibilities: no longer building in public, users converting a few pages with free-tier AI chatbots (hundreds of pages still need paid AI, which is slower and more expensive), and a much better competitor. The post mentions people using AI to build their own converters only as the reason the owner stopped sharing revenue; that such copies take one-shot jobs first is our inference, not the post's finding.
5. **First users** come from the threads that rank for the split, while a young domain waits months to rank. Plan them with launch-distribution, under its authorization: nothing is posted without the user's approval.
6. **New words** become a page on a site that already sells, or a new capability of an old paid job; a new word gets no site of its own while its demand is unproven.
7. **Kill numbers.** Every test — a split, a page, a thread, a price — gets a kill number and a date before it starts.

## Competitors in search

The order is fixed: who → what they target → which pages earn → which split.

1. **Who.** Competitors are the domains that rank for the paid job's queries, not the products that look alike. Take 10–20 queries (Search Console queries with impressions, the paid jobs, autocomplete splits), record each top 10 through a named search route and count domains: two or more queries make a competitor. Add the domains named by "X alternatives" and "X vs Y" pages and by AI answers. Lookalikes from similarity search or directories stay candidates until they rank. Sort them into giants (context), specialists and young winners (registered within about two years, ranking top 3); study the young winners first, because they show what wins at a young site's size now.
2. **What they target.** robots.txt → sitemaps, or the site's own links when it has no sitemap → URL families. Each family is a keyword template (`/convert/<a>-to-<b>`, `/<format>-for-<app>`, `/for/<persona>`, `/alternative/<brand>`, `/compare/<a>-vs-<b>`); a page's slug, title or H1 gives its main keyword, labelled `inferred`. Families that grew in the last 60 days (lastmod) are current bets; a removed family or sitemap is a bet that failed. Page counts show effort, not success.
3. **Which pages earn.** Per family: how often its pages recur across the sampled results (route, date), the query's volume (source, month), and the page's payment signal — where the paywall sits, plan prices, the checkout provider, and whether it sells a repeat job. Read each page as its user would: the job it finishes, the output and the app it is for, its limits, the free/paid line.
4. **Which split.** Late entrant points 1–3 decide. Then serp-seo maps the page to one intent and geo-page writes it.

What free data cannot show — state it in the report body:

- **Conversions and revenue**: not observable. Proxies only: paywall placement, prices, the checkout provider, ads in Google's Ads Transparency Center (owner-manual), revenue a founder publishes.
- **Real traffic per keyword or page**: only third-party estimates, often empty or wrong for small sites, or proxies (recurrence across sampled results, sitemap history).
- **Google rankings**: agents cannot observe them. www.google.com/robots.txt disallows /search, Google's terms forbid automated access that violates robots.txt, and Google served captchas to automated searches (seen 2026-11-07). Page-one checks are the owner's, by hand, or a paid SERP API's on the user's yes.
- **Authority**: a named route (Ahrefs' or Moz's free checker read by the owner, or paid), else `not available`.
- **A Bing keyword volume of 0** is below Bing's reporting threshold: `not found`, not zero demand.
- **The best data is first-party**: Search Console and Bing Webmaster queries for the user's own sites.

## Data routes

Every route carries one status; a route missing from the table is not agent-run until its terms are read and it is added:

- **agent-run**: terms read 2026-11-08; URLs and clauses are in the commit that added each row.
- **owner-manual**: the owner looks it up by hand; agents list the domains and ask for the numbers.
- **paid**: the user's decision; propose it with a sourced price and date.
- **not available**: state the exact error once, continue with the next route, mark the column.

| Need | Route | Status | Limit |
|---|---|---|---|
| Who ranks for a query | Tavily or Exa search, top 10 per query | agent-run | that tool's sample, not Google's results |
| Who ranks for a query | Codex web search, the agent's built-in hosted tool | agent-run | that tool's sample, not Google's results; its default cached mode reads an OpenAI index, not live pages |
| Lookalikes | Exa findSimilar | agent-run | mostly sites without traffic |
| What AI answers cite | Exa answer | agent-run | one engine's answer |
| What AI answers cite | ChatGPT, Perplexity, Google's AI answers | owner-manual | OpenAI's terms forbid programmatic extraction; Perplexity can be unreachable |
| Size and age | Tranco list API; RDAP through rdap.org | agent-run | absent from Tranco means small; rdap.org allows 10 requests per 10 s and returns 404 for some .io, .co and .sh domains that exist |
| Page list, page function, prices | the site's robots.txt, sitemaps, pages and pricing page | agent-run, on paths its robots.txt allows, a few pages at a human pace | JavaScript-rendered pages need a rendering fetch |
| Splits | Google autocomplete (suggestqueries.google.com) | agent-run | no volume |
| Volume | Bing Webmaster keyword API, one country and month | agent-run with the owner's key | 0 = below threshold |
| Own queries | Search Console API | agent-run with the owner's grant | own sites only |
| Trend | Google Trends | owner-manual | robots.txt disallows its explore page; relative numbers only |
| History | Common Crawl index | agent-run | often slow or failing; fall back to sitemap lastmod |
| History | Wayback Machine | owner-manual | its terms could not be read |
| Traffic, top pages and keywords, authority | Similarweb, Semrush and Ahrefs free views | owner-manual | their terms forbid robots and scrapers; small sites show no data |
| Google page one | the owner's browser; DataForSEO SERP API | owner-manual; paid | about $0.60 per 1,000 results pages, standard queue (third-party price comparisons, 2026-11-08) |
| Every keyword a domain ranks for, its top pages, keyword gaps | DataForSEO Labs; Semrush, Ahrefs or Similarweb API | paid | DataForSEO $50 minimum, $0.012 per task plus $0.00012 per row (dataforseo.com, 2026-11-08); the others from about $500–$1,500 a month or by quote |

## Evidence

- Every number (a price, a count of ranking tools, a registration year, a Search Console total) carries its source, its date or date range, and a label: observed, estimate or inferred. A number you did not observe is `not found`, and so is one an earlier agent run captured through a route that is not agent-run (saved Google, Trends or metasearch pages, a Similarweb export); list it for the owner to re-check.
- A claim about the current state (an API error, an outage, a page's status) carries its source and date like a number; one copied from an earlier report keeps that report's date and says it was not re-checked.
- User pain is a verbatim quote with a link.
- Name the route you actually used. A search tool's sample is not "Google top 10".
- A route that is not available is stated once; continue with the next route and mark the affected column.

## Demand test (each candidate)

1. Specific: who, in which situation, doing which action.
2. Frequency: how often one buyer needs it, and how many buyers need it. Occasional tasks qualify when willingness to pay is strong and buyers are reachable.
3. Searching: people search, ask, compare tools, or pay someone.
4. Pay reason: saves time, avoids errors, earns money, or avoids a loss.
5. Timing: dated trend evidence — rising, stable or eroding (for example, being absorbed by AI assistants or platforms).

## Worth-winning test

- Read the top 10 for the entry query through a named route: old strong domains or young sites? For a young site that ranks, check its size and how it earns (Competitors in search). A young ad-funded site with thin traffic means winning buys thin ad income.
- End state: separate observed inputs from assumptions; show low / base / high monthly contribution after delivery and acquisition cost, and the break-even paid conversion rate. If the case rests on an untested rate, the verdict is `investigate`.
- Volume is not a threshold: small volume with strong paid intent beats big volume of free-only users.
- Default out: ad sites, pure content sites, games, free tools without a paid path. Giants (Google, Adobe, Canva, Wikipedia) are context, not candidates.

## Output

1. Table: candidate | user + job | evidence (quotes, links) | entry query | can win? | worth winning? | verdict (`build` / `investigate` / `drop`) + one-line reason.
2. For each `build`: an MVP that ships in 7 days or less (homepage = the core tool, one keyword cluster), its first 3–5 URLs, and the paid path.
3. For the top candidate: where the first 100 users come from before SEO ranks, the one-week validation step, its cost, and the number that would kill it.
4. For competitor research: competitors (domain | queries ranked, n of N | route and date | age | size | type); keyword families per young winner (family | pages | newest lastmod | example URL | main keyword, `inferred`); earning pages (URL | function | main keyword, `inferred` | volume, source and month | payment signal); and the chosen split with its open/taken evidence and route, the output difference, and its kill number and date.

Done when every candidate has both questions answered or marked unknown with what would answer it, every competitor names the route that found it, every test has a kill number, and a last read of the reply finds every number and current-state claim with its source and date (a Search Console total with its start and end dates).
