---
name: x-growth
description: Analyze an X (Twitter) account and grow its followers from a cold start. This skill should be used when a user shares their X/Twitter profile URL and asks how to get more followers, requests accounts to interact with, wants copy-paste reply drafts for specific posts, or needs a posting calendar and content system for X. Optimized for indie hackers, solo founders, and builders doing build-in-public.
agent_created: true
---

# X Growth

## Overview
End-to-end workflow for growing a personal X (Twitter) account from a cold start, built for indie hackers, solo founders, and builders doing build-in-public. The workflow moves from diagnosis, to borrowing others' audiences via high-value comments, to building a sustainable content engine, and finally to measurement-driven iteration. The goal is to turn "I should post more" into a concrete, repeatable machine.

## When to use
- User shares an X/Twitter profile URL and asks "how do I grow", "analyze my X", or "why am I not getting followers".
- User asks for accounts to interact with, or for copy-paste reply drafts for specific posts.
- User wants a posting calendar, thread format, or content system for X.
- User mentions build-in-public, indie-hacker growth, or low-follower-count frustration.

## Core principle
At a low follower count (under ~500), your own tweets reach almost no one. The comment section under bigger accounts is the single highest-leverage free ad space: one comment that gets liked or replied to by the original poster can out-perform your own tweet by 10–100x in impressions. Therefore the workflow front-loads **engagement** (Stage 3) over **posting** (Stage 4). Posting matters, but it compounds only after a baseline of visibility exists.

## Workflow

### Stage 1 — Diagnose (one pass, output 5 lines, not a report)
1. WebFetch the profile URL (e.g. `https://x.com/<handle>`). Extract: follower count, following count, post count, bio, and language mix.
2. Compute red flags:
   - Following:follower ratio > ~3:1 → account looks low-quality / bot-like; visitors will not follow back.
   - Posts per year < ~20 → account looks abandoned; the algorithm will not push it.
   - Empty or vague bio → wastes the one slot to say "who I am + why follow me".
   - Mixed-language posting → the algorithm cannot tell who to surface it to.
3. Output a **5-line diagnosis** (not a long doc): the 3 worst red flags + the single most important first action. Save the longer rationale only if the user asks.

### Stage 2 — Find interaction targets (build a standing roster)
1. WebSearch for real, currently-active accounts in three tiers relevant to the user's niche:
   - **A — Global English top**: biggest reach (indie-hacker / solopreneur / build-in-public leaders).
   - **B — Niche circle**: the user's specific topic (AI agents, SaaS, design, etc.) — highest chance to show real expertise.
   - **C — Same-language peer circle**: accounts the user can engage with zero language friction and build genuine reciprocal ties.
2. Produce a roster of 10–20 handles grouped by tier. Recommend the user create an **X List** from this roster and turn on notifications, so fresh posts surface daily without scraping.

### Stage 3 — Grab specific posts + write replies (the highest-value stage)
This stage is the most valuable and the most fragile: X login walls block automated fetching, and post links go stale fast.
1. For each target in the roster, WebFetch their profile and extract the **2–3 most recent posts**, each with the **full status URL** (`https://x.com/<handle>/status/<id>`), date, and full text.
2. For each post, write a **copy-paste reply** that:
   - Maps to at least one of the 7 viral elements (see `references/viral-elements.md`).
   - Ties to one of the **user's own true stories** (not generic praise). Collect 2–3 real experiences from the user up front (e.g. a launch that got throttled, a product with zero users, a hard-won lesson) and reuse them as reply hooks.
   - Adds a genuine question or a counter-point — never "nice post" / "great".
3. **Critical reliability rule**: because links decay, re-fetch the targets' latest posts *immediately before the user acts*, or instruct the user to engage from their X List + notifications directly. Do not hand the user a stale list and walk away.
4. Use the scenario templates in `references/reply-templates.md` to keep replies fast and consistent.

### Stage 4 — Content engine (turn existing material into a posting system)
1. Inventory the user's existing writing / docs / methodology. Convert the strongest pieces into **reusable post templates** rather than one-off threads.
2. Format threads X-native: hook in the first post (+ image if available), each subsequent post ≤ 280 characters, separated by clear beats.
3. Set a cadence the user can actually sustain (e.g. 3 original posts + 2 reply-driven commentary per week). Frequency beats polish at this stage.
4. Each original post must hit at least one viral element. If it hits none, do not post it.

### Stage 5 — Track & review (close the loop)
1. Use `assets/weekly-tracker.md` as a minimal log: date, whether it was a post or a reply, impressions, profile visits, followers gained.
2. Weekly review: double down on the element/format that won; swap the hook on what flopped. No data → no iteration, so the tracker is mandatory, not optional.

## Hard rules
- **No automation of posting or following.** It risks throttling (a real failure mode for this user) and reads as spam. Manual, real, consistent.
- **Engagement first, posting second** until ~500 followers.
- **Tie every reply to a true story.** Generic compliments get ignored; specific, vulnerable, or contrarian replies get seen.
- **Re-fetch before acting.** Never treat scraped post links as durable.

## Resources
- `references/viral-elements.md` — the 7 viral elements framework and how to map content/replies to each.
- `references/reply-templates.md` — scenario-based copy-paste reply templates with story placeholders.
- `assets/weekly-tracker.md` — minimal weekly tracking sheet.
