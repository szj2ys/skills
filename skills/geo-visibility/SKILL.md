---
name: geo-visibility
description: Measure and improve a site's presence in live AI answers — GEO, AI 搜索可见性, "让 ChatGPT / Perplexity 推荐我的网站", AI crawler access, brand mentions in AI answers. Writing one citable page is geo-page; content claims are checked with the site's real code and data.
---

# GEO Visibility

## The one rule

**Measure with the questions buyers really ask, then fix in order: can AI search crawlers read us → do we say plainly what we are → do the sources AI already cites mention us.**

## Mode

A "how do I" or "take a look" request produces findings and a plan. Code, robots and CDN changes happen when the user asked for changes; external profiles and posts follow `backlink-outreach` / `launch-distribution` authorization.

## 1. Prompt panel — the baseline

Collect 10–20 questions from real sources first (search queries, community threads, support messages); questions an assistant suggests are labelled synthetic. Keep unbranded discovery questions separate from branded ones, and never give our URL or page text in discovery runs. Run each in a fresh session (no memory, clean or logged-out profile), recording assistant, model and search mode if visible, locale, date, the full answer, cited URLs and recommended products. Count separately: **mentioned**, **cited** (a link to our content that supports the answer), **recommended**. No clean session reachable → baseline `UNVERIFIED`.

## 2. Crawler access — by purpose

Classify each provider's crawlers from its current docs into search/answer retrieval (OAI-SearchBot, PerplexityBot, Bingbot), user-triggered fetch (ChatGPT-User, Perplexity-User), and training (GPTBot, ClaudeBot, Google-Extended). Visibility needs the search and fetch classes; training access is the owner's separate policy decision and stays as set. Check the production robots.txt rules and CDN or firewall bot settings for each class. `curl -A` probes are synthetic; real access is shown by server or CDN logs of verified crawler hits. Core content must be in raw HTML; most AI crawlers do not run JavaScript.

## 3. Plain identity

The same facts about who we are everywhere: name, one-line description, what it costs, who it is for — in the home page, About, schema (Organization or SoftwareApplication with `sameAs`), directories and social profiles. Wording may differ by audience and locale; the facts do not. Unsupported claims (user counts, testimonials) are listed for removal.

## 4. Be where AI already looks

From the panel's cited sources, list the third-party pages that shape answers: comparison lists, Reddit threads, review sites, docs, videos. For each, note the honest way in and hand it to `backlink-outreach` or `launch-distribution`. Gaps on our own site go to `geo-page`.

## 5. Re-measure

Same pinned panel and setup every 2–4 weeks; report counts per assistant with unavailable runs listed, and treat changes as observations, not proof of cause. llms.txt and similar files are optional extras with no shown effect on citations.

## Output

Panel table (question | source | assistant | mentioned / cited / recommended | cited URLs) · crawler table (bot | purpose | robots rule | CDN rule | evidence type) · identity fixes · third-party target list · re-measure date and owner.
