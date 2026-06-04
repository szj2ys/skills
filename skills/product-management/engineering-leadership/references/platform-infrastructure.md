# Platform Infrastructure

# Platform Infrastructure

Help the user design and scale internal platforms and shared technical infrastructure using insights from 5 product and engineering leaders.

## How to Help

When the user asks for help with platform infrastructure:

1. **Understand the platform's purpose** - Ask whether they're building for internal developers, external partners, or both
2. **Assess organizational readiness** - Determine if they have the adoption and governance structures to support a platform
3. **Identify the leverage points** - Help them find where platform investment creates the most value multiplication
4. **Design for adoption** - Ensure the platform solves real developer problems, not theoretical ones

## Core Principles

### Abstract common capabilities into shared infrastructure
Daniel Lereya: "We actually stopped for the first time and say, 'What is the column like?' And we also organized all the product architecture around it... making the work of adding a new column just thinking about the specific." Scaling feature velocity requires abstracting repetitive components into a shared infrastructure so developers only focus on unique logic.

### Invisible infrastructure often matters most
Asha Sharma: "It wasn't the hundreds of features, it was all in the infrastructure and the platform... performance, reliability, privacy, safety, all of those things." The success of major platforms often depends on "invisible" qualities like reliability and speed rather than visible features.

### Plan for scale before you need it
Ivan Zhao: "During COVID, we just couldn't scale up our infrastructure. For the longest time, Simon's really good at don't do premature optimization... we're running off even the largest instance there is for Postgres." While avoiding premature optimization is good, infrastructure must be planned far enough ahead to avoid "doomsday" scenarios when usage spikes.

### Build discoverability into the architecture
Eli Schwartz: "If you create a categorized sitemap where you can say, 'These are all the questions on health and from the sitemap... then a search engine can navigate through the entire site, and all of the questions and answers are discoverable.'" For large-scale platforms, structural decisions like HTML sitemaps and internal linking are critical for search engine discoverability.

### Default to server-side tracking
Vijay: "The biggest mistake is setting up analytics using client side SDKs... start tracking events from your servers instead of from your clients." Server-side tracking is superior to client-side SDKs for data reliability, cross-platform consistency, and developer maintenance.

## Questions to Help Users

- "Who are the 'users' of this platform and what problems are they trying to solve today?"
- "What's the current developer experience pain point that's costing the most productivity?"
- "How will you measure whether this platform is actually being adopted?"
- "Is this a build vs buy decision, or should this remain a manual process for now?"
- "What's your 'doomsday clock' - when will current infrastructure hit its limits?"

## Common Mistakes to Flag

- **Building for the abstract future** - Creating capabilities based on anticipated needs rather than current developer pain
- **Platform without product ownership** - Treating infrastructure as a technical project without dedicated product management
- **Avoiding premature optimization until it's too late** - Not monitoring infrastructure limits to trigger scaling projects before failure
- **Client-side tracking by default** - Using browser SDKs instead of server-side event tracking
- **Ignoring the migration cost** - Building new platforms without accounting for the effort to move teams off existing solutions

## Deep Dive

For all 6 insights from 5 guests, see `references/guest-insights.md`

## Related Skills

- platform-strategy
- product-operations
- scoping-cutting

---

# Platform & Infrastructure - All Guest Insights

*5 guests, 6 mentions*

---

## Asha Sharma
*Asha Sharma*

> "it wasn't the hundreds of features, it was all in the infrastructure and the platform... performance, reliability, privacy, safety, all of those things."

**Insight:** The success of major platforms (like WhatsApp or Instacart) often depends on 'invisible' infrastructure qualities rather than visible features.

**Tactical advice:**
- Prioritize reliability, speed, and end-to-end encryption in communication platforms
- Focus on data residency and availability to build trust with enterprise customers

*Timestamp: 38:21*


## Daniel Lereya
*Daniel Lereya*

> "We actually stopped for the first time and say, 'What is the column like?' And we also organized all the product architecture around it... we defined what is it, and then create an infrastructure for all these shared things, making the work of adding a new column just thinking about the specific product that you want to provide."

**Insight:** Scaling feature velocity requires abstracting common capabilities into a shared infrastructure so developers only focus on unique logic.

**Tactical advice:**
- Identify repetitive feature components and build them into a core platform architecture
- Standardize capabilities like 'export to Excel' or 'filtering' at the infrastructure level

*Timestamp: 00:13:30*

---

> "We need few of our most talented people that are now not going to contribute features anymore. We are putting them on a separate place, and let's think and solve this problem while thinking about 100X."

**Insight:** Critical infrastructure projects (like MondayDB) require dedicated teams focused on 100X scale rather than incremental feature work.

**Tactical advice:**
- Isolate top talent to work on long-term architectural shifts that provide a competitive edge
- Anticipate infrastructure breaking points by planning for 100X current capacity

*Timestamp: 01:13:19*


## Eli Schwartz
*Eli Schwartz*

> "If you create a categorized sitemap where you can say, 'These are all the questions on health and from the sitemap... then a search engine can navigate through the entire site, and all of the questions and answers are discoverable.'"

**Insight:** For large-scale platforms, an HTML sitemap and clear internal linking are critical for search engine discoverability.

**Tactical advice:**
- Build a categorized HTML sitemap that allows bots to navigate the entire site depth
- Implement 'related content' links on every page to create a crawlable web for search engines

*Timestamp: 00:54:48*


## Ivan Zhao
*Ivan Zhao*

> "During COVID, we just couldn't scale up our infrastructure. For the longest time, Simon's really good at don't do premature optimization, so for the longest time, we Notion runs on one instance of Postgres database... we're running off even the largest instance there is for Postgres. So there's a doomsday clock... we just need to go as fast as you can to become sharding problem."

**Insight:** While avoiding premature optimization is good, infrastructure must be planned far enough ahead to avoid 'doomsday' scenarios when usage spikes.

**Tactical advice:**
- Monitor database limits and set a 'doomsday clock' to trigger scaling projects (like sharding) before failure.
- Be prepared to halt feature development to focus entirely on critical infrastructure scaling.

*Timestamp: 00:49:31*


## Vijay
*Vijay*

> "The biggest mistake is setting up analytics using client side SDKs... start tracking events from your servers instead of from your clients."

**Insight:** Server-side tracking is superior to client-side SDKs for data reliability, cross-platform consistency, and developer maintenance.

**Tactical advice:**
- Default to server-side event tracking to avoid data loss from ad-blockers
- Use server-side logs with user IDs as the primary source for behavioral events

*Timestamp: 35:12*



