# Google SEO Guidelines: Crawling, Indexing & Structured Data

## High-Level Philosophy
**Optimize in the lab, validate in the field. Guide the crawler, don't trap it.**

Google's core objective is to discover, understand, and serve the most relevant, high-quality content to users. As an agent, your goal is to architect and maintain a site that makes this process frictionless.

**Core Directives:**
*   **What to do rather than how to do it:** Focus on architectural decisions and signal management.
*   **Never send mixed signals:** Your sitemap, canonical tags, internal links, and redirects must all point to the *same* URL.
*   **Visibility is mandatory:** Never mark up content with structured data that is hidden from the user.
*   **Crawl budget is finite:** Guide the bot away from infinite spaces (calendars, filters) and towards high-value content.

---

## Site Lifecycle Stages

### 1. Build Stage
*Objective: Architect the site to minimize inherent duplicate URLs and structural issues from day one.*

**Decision Frameworks:**
*   **Sitemap Strategy:** 
    *   *Need a sitemap:* Large sites (>500 pages), new sites with few backlinks, sites with rich media/news.
    *   *Don't need a sitemap:* Small sites (<500 pages) with comprehensive internal linking from the homepage.
*   **Crawl vs. Index Control:**
    *   *Goal: Keep out of index (e.g., staging, internal search).* -> Use `noindex` meta tag. **Do not** block in `robots.txt` (Google must crawl to see the tag).
    *   *Goal: Save crawl budget (e.g., faceted navigation).* -> Use `robots.txt` disallow.
*   **Structured Data Format:** Always default to **JSON-LD**. It is less prone to breaking layout than Microdata.

**Checklist:**
- [ ] Establish absolute consistency for URL patterns (trailing slash vs. no trailing slash, HTTP vs. HTTPS).
- [ ] Include a self-referencing `rel="canonical"` link tag in the base template of every indexable page.
- [ ] Define the Largest Contentful Paint (LCP) element early; ensure it renders server-side.
- [ ] Reserve space (aspect ratios/fixed dimensions) for all dynamic content to prevent Cumulative Layout Shift (CLS).

### 2. Launch Stage
*Objective: Signal exactly which URLs are canonical and validate lab data against reality.*

**Decision Frameworks:**
*   **Consolidation Method:**
    *   *When to use 301 Redirects:* The duplicate page is deprecated or you are forcing a global rule.
    *   *When to use `rel="canonical"`:* Multiple valid URLs serve the same content (e.g., product variants, tracking params), but only one should be indexed.
*   **Lab Data Thresholds:** Set stricter lab thresholds than field targets (e.g., target 1.5s LCP in the lab to ensure a 2.5s LCP in the field).

**Checklist:**
- [ ] Verify only preferred (canonical) URLs are included in the XML Sitemap.
- [ ] Remove staging `noindex` tags or HTTP header blocks.
- [ ] Run key templates through the Rich Results Test (do not launch without this).
- [ ] Establish performance baselines using Lighthouse CI or similar tools.

### 3. Maintain Stage
*Objective: Prevent duplicate URLs from proliferating and monitor field data.*

**Decision Frameworks:**
*   **Sitemap Hygiene (`<lastmod>`):** Only update the `<lastmod>` date when content has changed *substantively*. Google ignores `<priority>` and `<changefreq>`.
*   **Template vs. URL Triage:** Group failing URLs in Google Search Console (GSC) by template. A failure on 1,000 product pages is a single template issue, not 1,000 separate problems.
*   **Internal Linking:** Internal links are a massive canonicalization signal. Consistently link to the canonical URL, never to a redirect or parameterized version.

**Checklist:**
- [ ] Ensure newly generated dynamic parameters (like `?sort=`) have canonical tags pointing to the static base URL.
- [ ] Periodically audit the sitemap to replace redirects (301/302) with final destination URLs.
- [ ] Ensure structured data updates simultaneously when visible page content updates (e.g., stock status, price).

### 4. Diagnose Stage
*Objective: Identify and resolve indexing conflicts and ranking drops.*

**Decision Frameworks:**
*   **Triage via Search Console (Indexation):**
    *   *Discovered - currently not indexed:* Usually a crawl budget or quality issue. Improve internal linking.
    *   *Crawled - currently not indexed:* Usually a severe quality/intent issue or near-duplicate content.
    *   *Duplicate, Google chose different canonical:* Your signals are conflicting. Align sitemaps, internal links, and canonical tags.
*   **Rich Result Drop-Off:**
    *   Check Manual Actions for spammy/hidden markup penalties.
    *   Check Enhancements report for spike in errors (missing required fields).
*   **Core Web Vitals Triage Order:**
    *   1. CLS (easiest to fix: add aspect ratios).
    *   2. LCP (optimize hero asset or server response).
    *   3. INP (hardest: requires JS execution optimization).

---

## Decision Trees for Common Scenarios

### Scenario 1: Handling Duplicate Content
1. **Are the pages actually identical or nearly identical?**
   - *Yes, but both must exist for users (e.g., tracking URLs, color variants):* Use `rel="canonical"` on the duplicates pointing to the preferred version.
   - *Yes, and only one needs to exist (e.g., old URL structure):* Use a 301 Permanent Redirect to the new version.
   - *No, they serve different intents:* Differentiate the content significantly; they are not duplicates.

### Scenario 2: Blocking Content
1. **Should the page appear in Google Search?**
   - *Yes:* Ensure it is in the sitemap, has a self-referencing canonical, and is linked internally.
   - *No.* -> **Why not?**
     - *It's an infinite combination of filters/sorting wasting crawl budget:* Block crawling via `robots.txt` Disallow.
     - *It's thin, private, or administrative content that must never be indexed:* Add a `noindex` meta tag. **Do not** block in `robots.txt`.

### Scenario 3: Soft 404 Diagnosis
1. **Does the content still exist?**
   - *No:* Return a hard 404 or 410 HTTP status code.
   - *Yes, it moved:* Implement a 301 Redirect to the new location.
   - *Yes, it's right here:* Googlebot likely failed to render critical JS/CSS. Check if resources are blocked in `robots.txt` or timing out, resulting in a blank render.

---

## When to Escalate

While most SEO issues can be resolved architecturally, some require human escalation or cross-team collaboration:

*   **Conflicting Business vs. SEO Goals:** If marketing requires massive use of tracking parameters that are aggressively cannibalizing canonical signals, escalate to establish a URL parameter strategy.
*   **Persistent "Crawled - currently not indexed" on High-Value Content:** If technical signals are perfect but Google refuses to index core pages, this indicates a sitewide quality/authority issue requiring human content strategy intervention.
*   **Manual Actions:** Any notification of a Manual Action in GSC regarding Structured Data or spam requires immediate escalation and a formal reconsideration request.
*   **TTFB Failures (LCP):** If LCP fails due to Server Response Time (TTFB > 600ms), escalate immediately to Backend/DevOps. Frontend optimizations cannot fix a slow server.
*   **Traffic Drops with No Technical Errors:** If indexation is healthy, CWV is "Good," and structured data is valid, but organic traffic drops significantly, escalate to analyze algorithm updates or changing search intent.
