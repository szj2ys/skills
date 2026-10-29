---
name: backlink-outreach
description: Find, choose and submit backlinks one qualified site at a time — 外链, 发外链, 挖外链, backlink building, directory and launch-site submissions, blog comments, guest posts (write for us), Google footprint searches (inurl:), automated backlink discovery with SERP and DR APIs — keeping a ledger so nothing is submitted twice.
---

# Backlink Outreach

## The one rule

**Every submission passes the gate and lands in the ledger.** Link quality beats link count; a quota never overrides the gate.

## Mode

Research, screening and drafting need no permission. Submitting, posting, contacting people, creating accounts and paying happen only within the user's explicit authorization for this site list, identity and copy; reuse a grant already given for the same scope.

Research sources behind a login (the user's own databases and tool subscriptions): use only a browser session the user has set up for agent use. Browser profile files, cookie stores and saved passwords stay unread. No usable session → mark the source `blocked — owner must log in` and continue with open sources.

A submission site that needs a free account gets one brand account, opened within the account authorization above and never through the user's sessions, cookies or browser profile: true brand facts, an address in an inbox agents already read (a plus-address, never disposable mail), a generated password kept only in the user's secret store, and a fresh headless browser that also opens the confirmation link. Later products reuse that account. Stop at payment, a phone number, an ID upload or a human check (statuses under Submit). Never open an account on a social or community launch site (Product Hunt, Hacker News, V2EX): draft the post for the owner. No account authorization → `blocked — owner must create account`.

Before accepting a site's terms at signup, read them: a ban on the automation you would use → `skipped — terms ban automation`; send risky clauses (auto-renewal, content licence, arbitration) to the owner's weekly digest.

## Before anything

1. Read the site: product, users, core keywords. Pick the 1–3 URLs that deserve links and say why someone would cite each (original data, a free tool, a resource). Nothing citable → recommend an asset to build rather than pitching the money page everywhere.
2. Load the ledger: `backlinks-ledger.csv` at the project root, or the path the user names; create it if missing. A site already `submitted` or `live` for the same target URL is not submitted again; `skipped` and `blocked` rows are revisited when their reason changes.

## Sources

Candidate lists the user names (for example the lxx.ai backlink database, columbus.tools AI backlink rank, the ai-tools-radar list), relevant AI and SaaS directories, launch sites (Product Hunt, Show HN, V2EX for Chinese developers), GitHub/Gitee/GitLab repositories with genuine content, niche resource pages, local media in target markets.

### Footprint search — find pages that already take links

When the named lists run dry, or to find openings competitors have not used, search Google with footprints: operators that match pages built to accept a link. Replace `<kw>` with the site's core keywords and close variants (`ai image generator`, `ai photo editor`, `ai tools`); run each family for 2–4 keywords.

| Opening | Queries | What it yields |
|---|---|---|
| Blog comments | `inurl:blog "leave a reply" <kw>` · `"leave a comment" <kw>` | Posts with an open comment form (WordPress). |
| Directories and resource pages | `<kw> inurl:resources` · `<kw> inurl:links "submit"` · `<kw> "submit a tool"` | Pages built to list tools; many have a submit form. |
| Guest posts | `<kw> "write for us"` · `<kw> "guest post guidelines"` · `<kw> "contribute" inurl:write-for-us` | Blogs that publish outside articles, with their rules. |

Run the queries in a real browser session (in the user's harness: the owner's Vivaldi through `scripts/chrome-session/cdp_client.py`, one background tab, a few seconds between queries) or a SERP API; plain HTTP requests to Google get a JavaScript wall. An "unusual traffic" page is a human check (see Submit); slow down, and switch to a SERP API if it repeats. Record the query in the ledger note, so later runs learn which footprints produce `live` links.

What the results are, measured 2026-10-29 on `inurl:blog "leave a reply" "ai image generator"`: 6 of 7 fetched posts still had an open comment form, and WordPress marks comment author links `rel="ugc nofollow"` by default. A comment link therefore passes little ranking value; its worth is the reader who clicks. Comment only on a post our product genuinely answers, with a comment that adds to it (a fact, a fix, a tested alternative), and link only where the comment needs it. Directory and guest-post results are leads, not approvals: each still goes through the gate, and guest posts follow the publisher's guidelines and disclose any affiliation.

### Automating the loop

An agent can run find → gate → draft → submit on its own when three inputs exist:

1. **Search**: a SERP API key (Serper, SerpApi, Brave Search, DataForSEO) in the secret store, or the browser route above.
2. **Authority and traffic**: an authority score (Open PageRank is free; Ahrefs, Moz, Semrush or DataForSEO are paid) and a traffic estimate (Similarweb, Semrush). Store keys only in the secret store; a missing key leaves the value `unknown` with the reason, never a guess.
3. **The rule**: this skill. The numbers rank candidates that passed the gate; they never pass a candidate that failed it, and a high score never excuses an irrelevant or spammy page.

Posting stays one site at a time, within the authorization below, with copy written for that page. Bulk or templated comments, links in unrelated posts and paid guest posts without disclosure are link spam under Google's spam policies: they earn nothing and can cost the site its rankings.

Paid listings: verify the current fee and terms, then ask for budget approval; a payment never replaces the gate, and the product must work when the site's reviewers try it.

## The gate — open every candidate

1. Relevant to our product, industry or users.
2. Alive: real content and recent activity. Traffic figures come from a named source or are `unknown`.
3. Accepts this kind of submission.
4. The link sits naturally: a listing, a resource entry or a genuine post.
5. Clean: no link farm, PBN, auto-generated pages, link-selling or reciprocal-badge scheme, or links dropped into unrelated threads and Q&A.
6. Worth the time: plausible clicks or brand exposure, not only domain rating.

A failed check → ledger row `skipped` with the reason.

## Submit (when authorized)

Write copy specific to each site whose claims, category and pricing match the current product.

Before submitting, name who approves the listing (directory editor, list maintainer, moderator) and what they check, from the site's submission rules and the entries it accepted or rejected. List the 3–5 objections that reviewer most likely raises (dead or thin product, no pricing, unclear data handling, duplicate of an existing entry, wrong category) and answer each in the submission with evidence: a demo GIF or a link that works logged out, real numbers, the price, a privacy or data-handling line.

A human check (captcha, Cloudflare challenge, phone code at signup): attempt it yourself only where the owner allows it (in the user's harness, docs/adr/0022: a headed browser with the tab in front, two attempts, and a signup phone code is asked from the user at that moment); never send it to a solving service. A check that still blocks → `blocked — human check (<kind>)`, batched for the owner's weekly digest instead of interrupting. Payment or identity checks → `blocked — owner must <action>`. Move to the next site. An uncertain result (timeout after submit) is checked against the receipt or the site before retrying.

## Ledger columns

date, site, site_url, submit_page, target_url, link_type (dofollow/nofollow/unknown), domain_rating (with source), relevance (high/medium), status (candidate/submitted/live/skipped/blocked), live_link_url, note.

`live` only after the published page is opened and our link is seen on it.

## Output

Counts by status, the ledger rows added this run, and the next 5 candidates.
