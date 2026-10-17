---
name: programmatic-seo
description: Decide whether a templated page set deserves to exist and which values get pages — 程序化 SEO, pSEO, "X to Y converter" × N, tool × scenario or persona pages. Use before generating many similar pages; intent-to-URL mapping for existing pages is serp-seo.
---

# Programmatic SEO

## The one rule

**A value earns its own page only when it is a distinct user task with demand and a value-specific payload.** SERP overlap is the main evidence: values whose top results are mostly the same URLs usually share one task and get one page; values with different results are candidates. Where overlap and task disagree (synonyms, regional variants, one general tool serving many conversions), explain the call.

## Steps

1. **Variables.** Find them in real queries: input × output, format × format, tool × scenario, persona × task, industry × task, platform × task, region × task, software × action, size/number/unit, template/example, file type × use.
2. **Value set.** Define the allowed values and the exclusion rule. Approval never extends to the full Cartesian product.
3. **Sample.** Per variable, search high-demand, low-demand, likely-overlapping and doubtful values; record the top-5 URLs per value and the overlap. The sample is the evidence; keep it in the report.
4. **Payload.** Per page type, name what the page gives that a keyword swap would not: a working tool instance, a computed result, real data, examples specific to the value. No unique payload → not generated.
5. **Win chance.** Per sample query: is the SERP held only by giants, or do small and young pages rank?
6. **Structure.** URL template, hubs, internal links (hub → leaf, leaf ↔ siblings), sitemap groups, canonical rules, breadcrumbs. Every leaf is reachable from a hub.
7. **Upkeep.** Who refreshes the payload data, at what cost, the rule for removing a page, and the observed signal (indexing, impressions, task completion) required before expanding.

## Output

| page type | URL template | sample queries (observed) | SERP overlap | unique payload | win chance | page count (estimate from the value set) | generate? |
|---|---|---|---|---|---|---|---|

Then: a pilot of up to 20 qualified pages (zero is a valid answer), the expansion condition, and a "do not generate" list with reasons. Search volumes you did not observe are `unknown`.
