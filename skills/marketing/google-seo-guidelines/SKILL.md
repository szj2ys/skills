# Google SEO Guidelines

## 1. High-Level Philosophy

The goal of this skill is to operationalize Google Search Central documentation into actionable decision-making heuristics for agents. This is the definitive "what Google officially wants" guide.

**Core Principles:**
*   **Crawl Budget is Finite:** Prioritize what Googlebot sees. Don't waste crawl budget on low-value, duplicate, or infinite-space URLs (like complex faceted navigation).
*   **Indexation Requires Clarity:** Google needs unambiguous signals. Conflicting signals (e.g., a page is in the sitemap, has a self-referencing canonical, but is blocked by robots.txt) lead to unpredictable indexation.
*   **User Experience (Page Experience) is a Tie-Breaker:** Core Web Vitals (CWV) are a ranking factor. When content quality is equal, the faster, more stable page wins.
*   **Structured Data Needs Purpose:** Only implement schema if it makes the content eligible for a specific Google Search rich result.

---

## 2. Site Lifecycle Stages

### Phase 1: Build (Pre-Launch & Architecture)

**Prioritized Checklist:**
1.  **Determine Crawl Control:** 
    *   *Decision:* Do we need to block areas of the site from being crawled (e.g., admin panels, internal search results)?
    *   *Action:* Draft the `robots.txt` file.
2.  **Define Canonical Strategy:**
    *   *Decision:* Are there parameters that change the URL but not the core content (e.g., tracking tags, simple sorting)?
    *   *Action:* Implement self-referencing canonical tags on all core pages to establish the "master" version.
3.  **Plan the Sitemap:**
    *   *Decision:* Is the site large (>50,000 URLs)?
    *   *Action:* Plan a sitemap index file pointing to multiple child sitemaps. Ensure ONLY canonical, indexable (200 OK) URLs are included.
4.  **Establish CWV Baselines:**
    *   *Decision:* Are we using heavy JavaScript frameworks or large media?
    *   *Action:* Test templates using Lighthouse/PageSpeed Insights to ensure LCP (Largest Contentful Paint), CLS (Cumulative Layout Shift), and INP (Interaction to Next Paint) are within "Good" thresholds.

### Phase 2: Launch

**Prioritized Checklist:**
1.  **Remove Blockers:**
    *   *Action:* Ensure any global `noindex` tags or broad `Disallow: /` directives used during staging are removed.
2.  **Submit Sitemaps:**
    *   *Action:* Submit the sitemap index via Google Search Console (GSC).
3.  **Ping Google (Optional but Recommended):**
    *   *Action:* Use the Indexing API (if applicable for job postings/broadcast events) or manually inspect critical URLs in GSC to request indexing.

### Phase 3: Maintain (Ongoing Health)

**Prioritized Checklist:**
1.  **Monitor GSC Coverage:**
    *   *Decision:* Are there spikes in "Crawled - currently not indexed" or "Discovered - currently not indexed"?
    *   *Action:* If yes, evaluate content quality and internal linking.
2.  **Maintain CWV:**
    *   *Decision:* Check the CrUX (Chrome User Experience Report) data in GSC. Are URLs falling into "Needs Improvement" or "Poor"?
    *   *Action:* Prioritize fixing INP and CLS issues, as these often correlate strongly with poor user engagement.
3.  **Validate Structured Data:**
    *   *Action:* Monitor the Enhancements reports in GSC. Fix "Errors" immediately. "Warnings" can be deprioritized unless they block a desired rich result.

### Phase 4: Diagnose (Troubleshooting)

**Prioritized Checklist:**
1.  **The URL is not indexed:**
    *   *Action:* Run the URL Inspection tool in GSC. Check the specific error (e.g., blocked by robots.txt, noindex detected, duplicate without user-selected canonical).
2.  **Traffic dropped suddenly:**
    *   *Action:* Check GSC "Manual Actions" and "Security Issues". If clear, check if a specific section/template dropped, or if the whole site dropped (often algorithmic or a major technical failure).
3.  **Rich results disappeared:**
    *   *Action:* Test the URL with the Rich Results Test tool. Check if the schema broke due to a recent template change.

---

## 3. Decision Trees for Common Scenarios

### Scenario A: Duplicate Content Handling

**Context:** You have multiple URLs showing the same or highly similar content.

*   **Question 1:** Is one version clearly the "main" or preferred version?
    *   **Yes:** Add a `<link rel="canonical" href="[MAIN_URL]">` to all alternate versions pointing to the main version.
    *   **No (e.g., paginated series):** Use self-referencing canonicals on each page. Do *not* canonicalize page 2 to page 1.
*   **Question 2:** Do the alternate URLs serve a purpose for users but waste crawl budget (e.g., complex filter combinations)?
    *   **Yes:** Consider adding `Disallow` in `robots.txt` for those specific parameter patterns.
    *   **No:** Rely on the canonical tag.

### Scenario B: Blocking Crawling vs. Indexing

**Context:** You want to hide a page from Google.

*   **Question 1:** Do you need to ensure the page NEVER appears in search results, even if someone links to it?
    *   **Yes:** You must use a `noindex` meta tag or X-Robots-Tag HTTP header. **CRITICAL:** Do *not* block the URL in `robots.txt`. If Googlebot cannot crawl the page, it cannot see the `noindex` tag, and the page might still be indexed based on external links.
    *   **No, I just don't want Googlebot wasting time crawling it:** Use `Disallow` in `robots.txt`.

### Scenario C: Deleting Content

**Context:** A page is no longer needed.

*   **Question 1:** Is the content permanently gone with no relevant replacement?
    *   **Yes:** Serve a 404 (Not Found) or 410 (Gone) status code.
*   **Question 2:** Has the content moved or is there a highly relevant equivalent page?
    *   **Yes:** Implement a 301 (Permanent) redirect to the new/equivalent URL.

### Scenario D: Mobile Parity

**Context:** Auditing a separate mobile site (m.example.com) or responsive design.

*   **Rule:** Google uses mobile-first indexing.
*   **Decision:** Does the mobile version have the exact same primary content, structured data, and meta directives as the desktop version?
    *   **No:** *Action Required.* You must ensure parity. If content is hidden on mobile, Google assumes it doesn't exist.

---

## 4. When to Escalate

Agents should halt autonomous action and escalate to a human SEO or developer in the following situations:

1.  **Robots.txt Changes on Large Sites:** Modifying `robots.txt` on a site with millions of URLs can cause catastrophic de-indexation if a wildcard is misused. Escalate for review.
2.  **Sitewide Migration or Domain Change:** This requires complex 301 mapping mapping and staging environment validation.
3.  **Hacked Content / Security Warnings:** If GSC reports a security issue or if injected spam is detected, escalate immediately to security/devops.
4.  **JavaScript Rendering Failures:** If the URL Inspection tool's "View Tested Page" shows a blank screen or missing critical content, the JS framework is likely blocking Googlebot. This requires engineering intervention (e.g., implementing Dynamic Rendering or Server-Side Rendering).
5.  **Manual Actions:** Any manual penalty in GSC requires a human to review the violation, fix it, and write a reconsideration request.