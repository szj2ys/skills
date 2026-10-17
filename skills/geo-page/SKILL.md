---
name: geo-page
description: Create or improve one website search page — a blog post or a tool page — that answer engines and AI assistants would cite. Use for 写一篇 SEO/GEO 博客, "get cited by ChatGPT or Perplexity", or one tool page for a query. Topic-only requests stop at ranked proposals; WeChat articles are writer; site-wide mapping is serp-seo.
---

# GEO Page

## The one rule

**One query, one page, with an information gap competitors lack — checked against them before it ships.** Other opportunities go to a backlog list. Site-level problems found on the way (robots, sitemap, rendering) are reported, not changed, unless the user asked for them.

## 1. Pick the query and the URL

Use Search Console if available, otherwise observed SERPs, People Also Ask and forums; name the tool used. The query needs demand evidence, a clear user problem and product relevance. Map the intent to existing URLs first: improve the page that already owns it; create a new page only when none should.

Then write the **information gap** in one sentence — your own data, your own test, a product capability, a worked example that the current top results lack. No gap → pick another query.

## 2. Blog or tool — the SERP decides

Answers, explanations and how-tos rank → a blog or guide. Pages that do the job (generate, convert, calculate, check) rank → a tool page with input → output and a short explanation.

## 3. Write for extraction

Open each section with the direct answer. Claim → evidence → source → context. Prefer facts, data, primary sources and your own tests over method, cases and opinion; label opinion and uncertainty. Include what only a real user of the product would know: limits, failure cases, real numbers.

## 4. Build within the existing stack

Reuse the site's route pattern, metadata, schema and canonical setup. Link to the page from 1–3 related pages and from it to the money page. Locale versions only through `i18n-seo` market evidence.

## 5. Blind comparison — content readiness

1. Take the real user question from step 1.
2. Collect the text of our page and the top 3 competing pages; hide site identity (brand, domain) while keeping each claim's cited sources.
3. Label them A–D in shuffled order and give question plus texts to a fresh judge session with no memory or context about us — one per assistant available (ChatGPT, Perplexity, another agent).
4. Ask: "Which source would you cite, for which exact claim? Which would you tell the user to open? Which adds nothing new? What is wrong or unsupported in each?"
5. **Ready** = our page is cited for a task-relevant, supported claim no competitor offers, and no judge finds a factual error in it. Report each judge separately, disagreements included.
6. Not ready → one focused revision and one retest in this run; still not ready → report the failing criterion.

Hinting which page is ours voids the round. No separate judge reachable → readiness is `UNVERIFIED`. Readiness predicts quality, not live citation, which stays a later measurement.

## 6. Verify the page

Run the site and fetch the page: status 200, title, H1, canonical, valid schema, content in raw HTML, links resolve, mobile render. A tool page also completes a representative input → correct output and handles one bad input.

## Output

URL · type · query · user problem · gap · judge results per round · page checks · site-level issues reported · backlog.
