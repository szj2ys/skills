---
name: backlink-outreach
description: Choose and submit backlinks one qualified site at a time — 外链, 发外链, backlink building, directory and launch-site submissions — keeping a ledger so nothing is submitted twice.
---

# Backlink Outreach

## The one rule

**Every submission passes the gate and lands in the ledger.** Link quality beats link count; a quota never overrides the gate.

## Mode

Research, screening and drafting need no permission. Submitting, posting, contacting people, creating accounts and paying happen only within the user's explicit authorization for this site list, identity and copy; reuse a grant already given for the same scope.

Sources or sites behind a login: use only a browser session the user has set up for agent use. Browser profile files, cookie stores and saved passwords stay unread. No usable session → mark the source `blocked — owner must log in` and continue with open sources.

## Before anything

1. Read the site: product, users, core keywords. Pick the 1–3 URLs that deserve links and say why someone would cite each (original data, a free tool, a resource). Nothing citable → recommend an asset to build rather than pitching the money page everywhere.
2. Load the ledger: `backlinks-ledger.csv` at the project root, or the path the user names; create it if missing. A site already `submitted` or `live` for the same target URL is not submitted again; `skipped` and `blocked` rows are revisited when their reason changes.

## Sources

Candidate lists the user names (for example the lxx.ai backlink database, columbus.tools AI backlink rank, the ai-tools-radar list), relevant AI and SaaS directories, launch sites (Product Hunt, Show HN, V2EX for Chinese developers), GitHub/Gitee/GitLab repositories with genuine content, niche resource pages, local media in target markets.

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

Captcha, phone verification, payment or identity checks → `blocked — owner must <action>`; move to the next site. An uncertain result (timeout after submit) is checked against the receipt or the site before retrying.

## Ledger columns

date, site, site_url, submit_page, target_url, link_type (dofollow/nofollow/unknown), domain_rating (with source), relevance (high/medium), status (candidate/submitted/live/skipped/blocked), live_link_url, note.

`live` only after the published page is opened and our link is seen on it.

## Output

Counts by status, the ledger rows added this run, and the next 5 candidates.
