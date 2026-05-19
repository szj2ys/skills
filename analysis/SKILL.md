---
name: analysis
description: |
  Horizontal-Vertical Analysis deep research skill. Created by Digital Lifeform Khazix, it draws on Saussure's diachronic-synchronic analysis, social science longitudinal and cross-sectional research designs, business school case study methods, and competitive strategy analysis.
  Use when the user wants to systematically research a product, company, concept, technology, or person. The core is dual-axis analysis: the vertical axis traces the subject's full life story from origin to present (presented as narrative), the horizontal axis performs a systematic cross-sectional comparison with competitors or peers at the current moment, and finally the two axes are crossed to produce original insights. The final output is a beautifully formatted PDF research report.
  Trigger phrases include but are not limited to: horizontal-vertical analysis, research this for me, help me analyze, deep research, do a research, investigate this, competitive analysis, help me figure out what this thing is, what's the deal with this product/company/concept, help me get to the bottom of this, help me understand this, help me do a deep research.
  Even if the user just says "help me learn about XX" or "what's XX's background," as long as the context suggests they need systematic deep research (rather than a simple concept explanation), it should trigger. It also applies when a user drops a product name, company name, or technical term and says "look into this for me."
  Do not use for simple definitions (user is just asking "what is XX"), do not use for WeChat article writing (use writer for that), do not use for pure title/summary generation (use wechat-title).
---

# Horizontal-Vertical Analysis Deep Research

> **Methodology Origins**
> Horizontal-Vertical Analysis was created by Digital Lifeform Khazix (Khazix). It synthesizes diachronic-synchronic analysis from linguistics (Saussure), longitudinal and cross-sectional research designs from social science, business school case study methods, and competitive strategy analysis into a universal research framework applicable to products, companies, concepts, and people. The core principle remains constant: trace time-depth vertically, pursue breadth across peers horizontally, and arrive at judgment where the two axes intersect.

You are conducting a Horizontal-Vertical Analysis deep research. The final deliverable is a **beautifully formatted PDF research report**.

## Prerequisites

### Environment Setup

1. **Confirm the PDF conversion script is available**: This skill includes `scripts/md_to_pdf.py` (built on WeasyPrint) for converting the final Markdown report into a polished PDF. Make sure dependencies are installed: `pip install weasyprint markdown --break-system-packages`.
2. **Writing style**: This skill includes a complete built-in writing style guide (see the "Writing Style" section below). No need to load additional skills.

### Define the Research Subject

After receiving user input, confirm the following information. If the user has already been specific enough (e.g., "use horizontal-vertical analysis to research Hermes Agent"), don't ask follow-up questions — just start:

1. **Research subject**: specific product name / company name / concept name / person's name
2. **Type**: product, company, concept, person, or something else?
3. **Research motivation** (optional): Why research this? What recently happened?
4. **Specific focus areas** (optional): Any particular angles you want to dig into?

---

## Step 1: Online Information Gathering

The quality of this methodology depends entirely on the richness and accuracy of the information collected. **You must search online** — don't rely solely on existing knowledge. The value of a research report lies in its depth and completeness, so during the information gathering phase, err on the side of searching more, not less. Shallow analysis from insufficient information is unacceptable.

### Parallel Search Strategy

Use sub-agents running in parallel for efficiency. Suggested division of labor:

- **Sub-agent 1 — Vertical information**: The subject's origins, founder backgrounds, development history, key events, version iterations, funding rounds, strategic pivots, crises
- **Sub-agent 2 — Horizontal information**: Competitor identification, each competitor's strengths and user reputation, industry comparison reviews, market share
- **Sub-agent 3** (only for complex subjects): Supplementary information such as deep founder backgrounds, shifts in industry landscape, community discussions (GitHub issues, Reddit, Twitter/X, Zhihu, etc.)

**Sub-agent online tool usage guide** (embed directly in each sub-agent's prompt):

Each sub-agent's prompt must include the following online access instructions:

> You need to gather information online. Use the following tools:
> - **WebSearch**: For discovering information sources and obtaining summaries and keyword-based results
> - **WebFetch**: When a specific URL is known, for extracting content from pages directly
> - If the user's environment has the web-access skill installed (check whether `/mnt/.claude/skills/web-access/SKILL.md` exists), load it first and follow its guidance — it provides stronger browser CDP capabilities
> - Search strategy: Use WebSearch first to discover sources and leads, then use WebFetch to dive deeper once you have specific URLs
> - Search multiple times with multiple keyword combinations. Don't give up after a single search
> - Primary sources over secondary sources: official blog > authoritative media original reporting > aggregations/reposts
> - **For academic research subjects, always check arXiv**: If the subject involves academic concepts, algorithms, AI models, technical paradigms, etc., you must use the arXiv API to find relevant papers. Call it like this: `curl -s "https://export.arxiv.org/api/query?search_query=all:keyword1+AND+all:keyword2&max_results=10"`, or use WebFetch on the same URL. Returns XML with title, authors, abstract, publication date, and PDF link. Adjust keyword combinations and result counts as needed. After finding key papers, use WebFetch to read the paper page (`https://arxiv.org/paperID`) for more details.

Prompts should describe goals ("obtain," "research," "learn about"), not imply specific methods ("search," "scrape"). Let each sub-agent determine the best approach on its own.

### Information Source Priority

Primary sources over secondary sources. Multiple outlets citing the same error creates a false impression of corroboration:

| Information Type | Primary Sources |
|-----------------|----------------|
| Product updates / technical decisions | Official blog, GitHub Release Notes, founder tweets |
| Funding / business data | Company official announcements, SEC / business registry filings |
| User reputation | GitHub Issues, Reddit discussions, Twitter/X, Zhihu posts |
| Industry analysis | Authoritative media original reporting (not reposts) |
| Academic / technical principles | arXiv papers (`export.arxiv.org/api/query`), Google Scholar, conference proceedings |

### Information Sufficiency Self-Check

After searching, verify:
- Vertical: Can you tell a complete story? Are there obvious gaps in the timeline?
- Horizontal: Is the competitor list complete? Are major players missing? Is there enough information on each competitor to make a meaningful comparison?
- Sources: Are key facts backed by reliable sources? Are any judgments resting on a single source?

If the information isn't enough, search again. Don't settle.

---

## Step 2: Vertical Analysis (Diachronic / Longitudinal)

Tracing along the time axis, fully reconstruct the research subject's development from birth to the present. This is the main body of the report and should carry the most weight.

### Content Requirements

**Origin trace**: What was the context of its birth? What technology, idea, or need did it grow out of? Who are the founders or key drivers? What had they done before, and why were they the ones to do this? What was the industry landscape at the time? Was there a specific event or inspiration that directly sparked its creation?

**Birth moment**: The definitive first release / founding / proposal date, its original form and positioning, and how it differed from what it is today.

**Evolution timeline**: From birth to now, chronologically lay out every key milestone. Including but not limited to: major version releases, funding events, team changes, strategic pivots, technical architecture shifts, user growth milestones, major partnerships or acquisitions, PR crises or controversies.

**Decision logic**: At each key juncture, reconstruct the reasoning behind the decisions as much as possible. Why A and not B? What constraints existed at the time? Which early decisions "locked in" later development paths that became hard to reverse? What mechanisms drove increasing commitment (network effects, ecosystem lock-in, technology stack choices, etc.)?

**Phase segmentation**: Naturally divide the whole timeline into distinct phases (incubation, rapid growth, transformation, etc.), each with its defining characteristics and core tensions.

### Length

6,000–15,000 words. Subjects with longer histories and more milestones push toward the upper bound; newer subjects toward the lower bound. The core principle is to tell the story completely and thoroughly. Every key milestone deserves expansion — don't skip important details for the sake of brevity. Err on the side of length and depth rather than skimming the surface.

---

## Step 3: Horizontal Analysis (Synchronic / Cross-sectional)

Using the current moment as a cross-section, perform a comprehensive comparison of the research subject against competitors or peers in the same space.

### First, Assess the Competitive Landscape

Handle three scenarios:

**Scenario A: No direct competitors.** If the subject is an entirely new category or operates in a highly exclusive domain, skip the one-by-one comparison. Instead analyze: Why does it have no competitors? Is the category too new, the barriers too high, or the market too small? From which direction are competitors most likely to emerge? Are there indirect alternatives or legacy solutions worth referencing?

**Scenario B: A few competitors (1–2).** Conduct a detailed head-to-head comparison with each.

**Scenario C: Plenty of competitors (3+).** Select the 3–5 most representative ones for comparison. Mention the rest briefly.

### Comparison Dimensions

Adapt flexibly based on the type of research subject, but cover at least the following:

**Core differentiators**: Technical approach / core methodology / underlying logic, product form / business model / organizational structure, target users / audience / use cases, core strengths and obvious weaknesses, pricing strategy / resource investment / scale.

**User perspective**: What is each competitor's real user reputation like? What are the most commonly praised strengths and complained-about weaknesses in community reviews and user experiences? Do users' actual usage patterns diverge from the official positioning? Don't write a spec-sheet comparison in paragraph form — convey what each competitor "actually looks like in practice" and what real reasons drive users to choose it.

**Ecological niche analysis**: In the overall landscape of this space, where does the subject sit? What gap does it fill, or whom is it directly competing against? Is the current landscape a flourishing ecosystem, a two-horse race, or a winner-take-all?

**Trend assessment**: Based on the cross-sectional comparison, where is the subject headed in the competitive landscape? What are the opportunities and risks?

### Length

3,000–10,000 words. Scenario A should stay around 3,000 words. In Scenario C, each major competitor deserves at least 1,500 words of dedicated analysis — don't gloss over any of them.

---

## Step 4: Intersection Insights

This is the highlight of the entire report. Synthesize the vertical development narrative with the horizontal competitive landscape to produce comprehensive, original judgments. Do not write an abridged recap of the preceding sections.

Core questions to answer:

1. **How history shaped the current competitive position**: Which decisions and events from the vertical timeline determined where it stands in today's horizontal comparison?
2. **Competitors on the timeline**: If you place the major competitors on a timeline too, how do their origins and evolution paths differ? How do those differences explain their current characteristics?
3. **Historical roots of strengths**: Each core strength today — which historical milestone or decision does it trace back to?
4. **Historical roots of weaknesses**: Each core weakness today — which historical decision does it trace back to? Have past "good decisions" become today's burdens?
5. **Future projection**: Based on vertical trends and horizontal competitive dynamics, lay out three scenarios — the most likely, the most dangerous, and the most optimistic. Each scenario must have logical support.

### Length

1,500–3,000 words.

---

## Writing Style

This is not a cold, corporate consulting report. It's a piece of deep research that people actually want to read from start to finish. The writing style needs to strike a balance between "research report rigor" and "Khazix's readability."

### Core Elements Borrowed from Khazix's Style

Apply the following style elements directly to report writing (for detailed definitions, refer to the writer skill):

**Rhythm**: Sentences alternate long and short, paragraphs flow with natural variation. Don't make every paragraph the same length — single-sentence paragraphs are fair game for emphasis. Good rhythm is like a wave: each beat drifts slightly off the main thread, then a "tie-back sentence" pulls it home.

**Narrative-driven, not list-driven**: The vertical section needs story arcs — setup, rising action, climax, resolution. Explain *why* a product suddenly exploded at a certain point, what laid the groundwork, and what the turning point was. Don't write a chronological ledger like "In January 2023 they released A, in March 2023 they released B."

**Knowledge dropped casually**: Weave background knowledge naturally into the narrative. No "let me take a moment to explain the basics."

**Have the courage to judge**: Opinions and insights are encouraged, but every opinion must be supported by facts. Lay out the facts first, then give the judgment. Label speculation clearly. When expressing judgments, use "I think" or "my read is" to acknowledge subjectivity rather than pronouncing decree from on high.

**Layered peeling**: Don't state the conclusion upfront. Unfold as "phenomenon → surface explanation → deeper question → core insight." Bring the reader along on the thinking process.

**Cultural elevation**: In the intersection insights section, connect to larger cultural, philosophical, or historical reference points. Not forced grandeur — the feeling of "this naturally came to mind as we were talking through it."

**Circular callbacks**: Details and hooks planted early in the intro or vertical section get called back in the intersection insights or conclusion. That sense of front-to-back closure is what turns a report from "information dump" into "a piece of work."

### Elements NOT Borrowed from Khazix's Style

The following elements suit WeChat articles but not research reports — use restraint:

- **Excessive informality**: The report can have a conversational feel, but don't litter it with slang. A light touch is fine, but at a much lower density than a WeChat article.
- **Heading-free writing**: WeChat articles aim for a seamless read without subheadings. Research reports are different — 10,000–30,000 words without clear structure and navigation will lose readers. Reports need a clear section structure.
- **Relaxed punctuation rules**: WeChat articles ban colons and dashes. Research reports can use them normally, since information delivery efficiency matters. The use of「」quotes can be retained.
- **No fixed footer**: Don't add the WeChat "like, follow, star" footer.

### Absolute Prohibitions (Still Apply)

The following AI-sounding tells must be avoided in any genre:
- Filler phrases: "First... second... finally," "In summary," "It's worth noting," "It's not hard to see"
- Empty buzzwords: "empower," "leverage," "close the loop"
- Textbook openings: "In today's rapidly evolving AI landscape," "As technology continues to advance"
- High-frequency red-flag phrases: "In plain terms," "What does this mean?" "This means," "Essentially," "In other words," "It's undeniable"
- Vague tool references: Don't say "an AI tool" or "some model" — use the specific name
- Fabricated scenarios: If something can't be found, honestly mark it as "[Information unavailable]" — never fabricate

### Write Like a Human

Avoid consulting-firm boilerplate and empty generalizations. Use specific details and examples instead of sweeping statements. Don't write "the company achieved rapid growth during this phase" — write "from $10M ARR in mid-2024 to $1B by end of 2025, the growth curve was nearly vertical."

---

## Step 5: Generate the PDF Report

Once the report is written, use the skill's built-in `scripts/md_to_pdf.py` script to convert the Markdown into a beautifully formatted PDF.

### Conversion Workflow

1. **Complete the Markdown draft first**: Write the full report in standard Markdown format, saved as `[Subject]_HV_Analysis_Report.md`
2. **Install dependencies** (if not already installed): `pip install weasyprint markdown --break-system-packages`
3. **Run the conversion script**:
   ```bash
   python [skill directory]/scripts/md_to_pdf.py input.md output.pdf --title "Research Subject Name" --author "Digital Lifeform Khazix"
   ```
4. The script automatically generates an intermediate HTML file (useful for debugging) and the final PDF

### Built-in Typography Standards

`md_to_pdf.py` has a complete CSS typesetting scheme built in — no manual adjustments needed:

- **Page**: A4, margins top 25mm / left-right 20mm / bottom 20mm
- **Cover page**: Auto-generated, includes title (28pt dark blue), subtitle "Horizontal-Vertical Analysis Deep Research Report," author info, decorative divider
- **Color scheme**: H1 = #1a5276 dark blue, H2 = #1e8449 green, H3 = #2e86c1 light blue, H4 = #5b2c6f purple, body text = #2c3e50 dark gray
- **Fonts**: CSS fallback chain `"Droid Sans Fallback", Helvetica, Arial, sans-serif`, handles Chinese-English mixed text automatically
- **Body text**: 10.5pt, line height 1.75, justified, orphan/widow control
- **Blockquotes**: Left 3pt dark blue vertical bar + light gray background
- **Tables**: Full width, dark blue header with white text, zebra-striped rows
- **Header**: "Report Title | Horizontal-Vertical Analysis Deep Research Report" (hidden on first page)
- **Footer**: "Page X" (hidden on first page)
- The first H1 in Markdown is automatically extracted as the cover title and won't appear again in the body

### Markdown Writing Notes

For the script to parse correctly and produce the best PDF output:

- Start with `# Title` as the report title (automatically used for the cover)
- Immediately after the title, use `> Research date: ... | Field: ... | Subject type: ...` format for metadata — it will be extracted onto the cover
- Use `##` for major section headings (Vertical Analysis, Horizontal Analysis, Intersection Insights, etc.)
- Use `###` and `####` for subsections
- Tables use standard Markdown table syntax
- Blockquotes use `>` syntax
- Bold uses `**text**`

### Closing Content

At the end of the Markdown draft, include:
- **Information sources**: A complete list of all cited sources with URLs and access dates
- **Methodology note**: A brief explanation of Horizontal-Vertical Analysis origins (1–2 sentences is sufficient)

### Report Structure Template

```
Cover Page

Table of Contents

1. One-Sentence Definition
[Concisely state what this thing is in one sentence]

2. Vertical Analysis: From Origin to Present
[Full vertical narrative, 6,000–15,000 words]

3. Horizontal Analysis: Competitive Landscape
[Cross-sectional comparison, 3,000–10,000 words]

4. Intersection Insights
[Cross-analysis and future projection, 1,500–3,000 words]

5. Information Sources
[List of all cited sources]
```

### File Naming and Delivery

Name the PDF file `[Subject Name]_HV_Analysis_Report.pdf` and save it to the user's working directory.

---

## Adapting to Different Subject Types

The core principle stays the same (trace time-depth vertically, pursue breadth horizontally), but the emphasis shifts:

**When researching a product**: The vertical axis focuses on version iterations, technical roadmap evolution, user growth curves, key product decisions; the horizontal axis focuses on feature comparison, performance comparison, user experience, and pricing.

**When researching a company**: The vertical axis focuses on founding team, funding history, strategic pivots, organizational changes, key personnel shifts; the horizontal axis focuses on business model differences, market share, revenue comparison, and organizational structure differences.

**When researching a concept** (technical paradigm, business model, cultural phenomenon): The vertical axis focuses on the concept's origin (who proposed it, what theory or need it grew from), how it gained traction, and what debates and evolutions it went through; the horizontal axis focuses on distinguishing it from related concepts, respective applicable contexts, and arguments from different camps.

**When researching a person**: The vertical axis focuses on personal history, career trajectory, key decisions, growth curve, evolution of public statements; the horizontal axis focuses on comparison with others in the same field (approach, style, achievements, influence, differences in path chosen).

---

## Length Overview

| Section | Word Range | Notes |
|---------|-----------|-------|
| Vertical Analysis | 6,000–15,000 words | Main body of the report. Don't skim. |
| Horizontal Analysis | 3,000–10,000 words | Adjust based on number of competitors |
| Intersection Insights | 1,500–3,000 words | The highlight — deliver new judgments |
| **Total** | **10,000–30,000 words** | Don't fear length. Depth and completeness are the value. |

---

## Quality Checklist

Self-check before delivery:

- [ ] Is the vertical axis a narrative with causal logic and a sense of the times — not a dry timeline ledger?
- [ ] Is the founder/initiator's background and motivation explored with sufficient depth?
- [ ] Is every key milestone expanded upon, with no important details skipped for brevity?
- [ ] Is decision logic reconstructed — not just "what happened" but "why this choice"?
- [ ] Is the competitive scenario for the horizontal axis correctly identified (A/B/C)? Is the competitor analysis deep enough?
- [ ] Does the user reputation section cite real user voices, not just official marketing?
- [ ] Does the intersection section produce original judgments rather than a condensed recap?
- [ ] Do all three future scenarios have logical support?
- [ ] Does the writing have rhythm and readability — not a cold consulting report?
- [ ] Does it avoid every item on the absolute prohibitions list?
- [ ] Are all key facts attributed to their sources?
- [ ] Is missing information honestly labeled as "unavailable" with no fabrication?
- [ ] Is the PDF well-formatted, clearly structured, and easy to read?
- [ ] Is the total word count within the 10,000–30,000 word range?
