---
name: seo-launch
description: Get a new site crawled and indexed at launch and set up the first 30 days of checks — 上线 SEO, 新站收录, Search Console setup, sitemap submission, "pages not indexed". Ranking and intent work is serp-seo.
---

# SEO Launch

## The one rule

**The pages meant for search are eligible to be indexed before launch; everything after is reported in three separate states:** technically eligible (verified now), submitted (receipt from the tool), indexed (observed in Search Console, with date).

## Mode

Diagnosis requests produce findings. Code changes when the user asked for launch preparation. DNS records, account setup, imports and URL submissions run only under the owner's authorization for that account; otherwise prepare exact steps and mark `blocked — owner must <action>`.

## 1. URL inventory

List the acquisition pages meant for search. Share links, account pages, staging and internal tools stay out of the index on purpose; launch work never exposes them.

## 2. Blockers — check the production build and host

- robots.txt allows the acquisition pages; staging sits behind authentication (noindex alone is not access control).
- No stray noindex on acquisition pages, in meta tags or the X-Robots-Tag header.
- One canonical host: http → https and www ↔ apex each end in a single 301 to it; canonicals, sitemap and internal links use it.
- Acquisition pages return 200 with core content in raw HTML; unknown paths return 404.
- sitemap.xml lists only those final, indexable, canonical URLs.
- Each acquisition page is linked from the home page or navigation, and one conversion event is visible in analytics.

## 3. Launch-day steps

Search Console domain property (DNS TXT), sitemap submitted, home page and 2–3 money pages inspected with indexing requested. Bing Webmaster Tools (import from Search Console) and IndexNow where the host supports it.

## 4. First 30 days

- **Week 1**: page indexing report — compare every exclusion with the URL inventory; fix the unintended ones only.
- **Week 2**: internal links from existing pages to new ones.
- **Week 3**: first brand profiles and directory listings (`backlink-outreach`).
- **Week 4**: high impressions with low CTR → titles and descriptions (`serp-seo`).

Each week compare indexed with submitted. A plan names the person or job that runs each check; it counts as active monitoring only after the first run is observed.

## Output

URL inventory · blocker table (check | command | observed | PASS / FAIL / UNVERIFIED) · launch steps done and owner-blocked · the 30-day plan with the number to read each week.
