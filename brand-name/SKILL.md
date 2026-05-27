---
name: brand-name
description: "Data-driven brand and product naming. Use when the user wants to name a product, company, app, feature, or brand entity and wants the name grounded in search trends, linguistic patterns, and market data — not random brainstorming. Triggers include 'help me name,' 'naming a product,' 'brand name ideas,' 'what should I call this,' 'name suggestions,' '取名字,' '品牌命名,' '帮我起名,' 'product naming,' or any request where the user needs multiple name options backed by research. Outputs a curated shortlist with rationale for each candidate."
---

# Brand Name Generator

Generate brand/product names grounded in data, not gut feeling. Every name you propose must be justified by observable signals — search trends, linguistic patterns, category conventions, or competitive gaps.

## Core Principle

**Demand-first naming.** A good name encodes something people already search for, signals a clear category benefit, or occupies a white-space position in the competitive landscape. Never generate names from pure creativity alone.

For abstract/evocative names (where search demand doesn't apply), the "data" signal comes from phonetic analysis, emotional association, and category fit rather than search volume. The rationale must still be grounded — just in different evidence.

## Workflow

### Step 1 — Gather Context

Collect the following before naming. Ask if not provided:

1. **What is being named** — Product, company, app, feature, campaign?
2. **Category / industry** — What space does this live in?
3. **Target audience** — Who is this for? (demographics, psychographics)
4. **Core value proposition** — What does it do? What problem does it solve?
5. **Brand personality** — Premium? Playful? Technical? Minimal? (ask for 2-3 adjectives)
6. **Competitive landscape** — Any competitor names to differentiate from or align with?
7. **Constraints** — Preferred language (EN/CN/bilingual), length limits, domain availability needs, trademark concerns?
8. **What you've already considered** — Names the user likes or has rejected, and why.

### Step 2 — Research & Signal Gathering

Use `WebSearch` to gather real-world data. Run these searches in parallel:

1. **Category naming trends** — "top [category] brand names" or "[industry] naming trends" to understand conventions and emerging patterns.
2. **Search volume signals** — "[key benefit] + [category]" and "[audience] + [problem]" to find language your audience actually uses.
3. **Competitive naming analysis** — "[category] competitors" or "alternatives to [known brand]" to map the naming landscape and find white space.
4. **Linguistic & cultural signals** — "[word] meaning" or "[word] connotations" to vet names for unintended meanings.
5. **Trademark quick check** — "[name] trademark" for top candidates. This is a rough heuristic only — it can surface obvious conflicts but cannot replace a formal trademark search. Flag this limitation to the user when presenting results.

Document key findings:
- What naming patterns dominate the category? (descriptive, invented, metaphorical, compound…)
- What words/phrases appear repeatedly in how people talk about this space?
- Where are the gaps? (e.g., everyone uses Latin roots, no one uses verbs, all names are abstract…)

### Step 3 — Generate Candidates

Produce **8–12 name candidates** organized into **3–4 distinct naming strategies**. Each strategy should represent a different approach:

| Strategy | Description | Example |
|----------|-------------|---------|
| **Descriptive** | Directly communicates what it does | FastSend |
| **Metaphorical** | Evokes a feeling or analogy | Falcon (speed) |
| **Invented/Coined** | New word, often from morpheme blending | Spotify (spot + identify) |
| **Abstract/Evocative** | Sounds right, feels right, meaning is associative | Aura |
| **Compound** | Two relevant words merged | Snapchat |
| **Human/Name** | Personified, founder-style | Tesla |

For each name, provide:
- **The name** (bold)
- **Strategy** — Which approach it uses
- **Rationale** — Why this name, tied to research signals (search data, category gap, linguistic fit)
- **Pros** — 2-3 strengths
- **Cons** — 1-2 risks or weaknesses
- **Domain note** — Quick assessment of .com/.cn availability likelihood (don't actually check domains, just flag obvious conflicts)

### Step 4 — Present Results

Structure the output:

```
## Research Summary
[2-3 sentences on key findings: category conventions, audience language patterns, competitive white space]

## Name Candidates

### Strategy 1: [Strategy Name]
1. **[Name]** — [One-line pitch]
   - Rationale: [Data-backed reasoning]
   - Pros: […]
   - Cons: […]
   - Domain: [Likely available / Probably taken / Unclear]

### Strategy 2: [Strategy Name]
...

## Recommendation
[Pick 2-3 top candidates with a clear rationale for why they best fit the brief. Be direct about tradeoffs.]
```

### Step 5 — Iterate

After presenting, ask if the user wants to:
- Explore variations on a specific candidate
- Merge elements from multiple candidates
- Pivot to a different naming strategy
- Deep-dive on a shortlist (trademark, domain, linguistic vetting)

## Naming Heuristics

Keep these in mind throughout:

- **Phonetic clarity** — If you can't say it after hearing it once, it's a bad name.
- **Spellability** — If you can't spell it after hearing it once, it's a bad name.
- **Length bias** — Shorter is generally better (1-3 syllables ideal for EN, 2-4 characters for CN).
- **Category signaling** — The name should hint at the category or benefit without being generic.
- **Trademark risk** — Avoid names too close to known brands in the same category.
- **International check** — Flag if a name has negative connotations in major languages (especially EN/CN if either is relevant).
- **Social handle availability** — Note if the name is obviously taken on major platforms.

### Chinese Naming Considerations

When the brief involves Chinese (CN) or bilingual naming, apply these additional heuristics:

- **Pinyin availability** — Check if the pinyin romanization is intuitive and doesn't collide with existing brands. Avoid pinyin that looks like a common English word with a different meaning.
- **Tonal aesthetics** — Prefer name combinations where tonal patterns flow naturally (e.g., avoid consecutive 4th-tone characters, which sound harsh).
- **Character meaning depth** — Chinese characters carry layered meaning. Surface both the literal and associative meanings of proposed characters.
- **Four-character idiom variants** — Consider adapting or riffing on well-known chengyu (成语) for cultural resonance, but avoid forced or obscure references.
- **Stroke complexity** — For logos and UI, favor characters with balanced stroke counts (not too simple, not too dense).
- **Homophone traps** — Flag names that sound like negative words in Mandarin, Cantonese, or other major Chinese dialects.

## What NOT to Do

- Don't generate names without research. Every name needs a data-backed rationale.
- Don't output a flat list without strategy grouping. The user needs to see different approaches.
- Don't recommend only one name. Always present options.
- Don't ignore the competitive landscape. A name that fits the brief but collides with a major competitor is a bad name.
- Don't use placeholder reasoning like "sounds good" or "feels modern." Be specific about why.
