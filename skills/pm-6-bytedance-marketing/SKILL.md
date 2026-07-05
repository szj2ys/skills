---
name: pm-6-bytedance-marketing
description: ByteDance-style algorithmic interest marketing playbook for designing product growth campaigns. Use when the user asks to optimize marketing for a product, design a growth campaign, build a content-driven go-to-market plan, or apply the FACT+ / A1-A5 / interest commerce methodology to improve acquisition, activation, or monetization. Triggers include interest marketing, 兴趣电商, FACT+, A1-A5, Douyin/TikTok campaign design, content matrix, KOL/influencer strategy, brand-effect synergy, and campaign performance optimization.
---

# ByteDance Algorithmic Interest Marketing Playbook (Flywheel Step 6)

This skill turns product/business context into an actionable growth campaign using the ByteDance marketing doctrine: **content-first, algorithmic distribution, and full-funnel user-asset operation**. It is decision-heavy; the goal is to choose the right marketing scene, not to produce decorative slides.

## 🌀 The Flywheel Connection
- **Upstream Input (from `pm-5-ab-tracking` or real telemetry)**: Validated user segments, winning messages/creative angles, baseline conversion rates, and guardrails.
- **Downstream Output (to execution + back to `pm-1-funnel-diagnostic`)**: A concrete campaign brief with a chosen FACT+ scene, A1-A5 target, content/creator mix, media plan, and success metrics. After launch, results feed the next diagnostic loop.

---

## 1. Define the Growth Task
State the business problem in one sentence. If the user only says "optimize marketing," ask for:
- Product / target segment
- Current funnel stage with biggest leak (acquisition, activation, retention, monetization)
- Existing creative/campaign assets and budget shape (fixed test budget vs. ongoing spend)
- Baseline numbers (impressions, CTR, conversion, CAC, LTV)

Do not proceed until the target segment and funnel stage are explicit.

---

## 2. Map A1-A5 User Assets and Pick the Gap
Use the A1-A5 model to describe the current distribution of the addressable audience. Identify which transition is the bottleneck.

| Stage | Definition | Typical Levers |
|---|---|---|
| A1 Aware | Know the brand/product | Mass reach ads, TopView, brand hashtags, viral content |
| A2 Appeal | Interested enough to engage | Emotional hooks, benefit demos, creator storytelling |
| A3 Ask | Actively considering / searching | Search ads, product education, FAQ, live Q&A |
| A4 Act | Purchase or key conversion | Live commerce, short-video storefront, coupon + countdown |
| A5 Advocate | Repeat purchase + referral | Loyalty content, seeding UGC, community challenges |

**Decision rule**: Do not try to move every stage at once. Choose **one primary A-stage gap** (e.g., A2→A3) and one secondary supporting stage.

For detailed A1-A5 definitions, content formats, and platform mechanics, see [references/bytedance-marketing-framework.md](references/bytedance-marketing-framework.md).

---

## 3. Select the FACT+ Marketing Scene
Pick the marketing scene(s) that best close the chosen A-stage gap. FACT+ is a portfolio, not a checklist; select based on product maturity, budget, and timeline.

| Scene | Best For | Core Tactic |
|---|---|---|
| F - Field 阵地自营 | Long-term asset, owned traffic, repeat conversion | Brand account, self-operated live streams, storefront, SEO within app |
| A - Alliance 达人矩阵 | Scale trust and persuasion at A2/A3 | Tiered KOL/KOC matrix: 1-2 head creators + mid-tier specialists + mass KOC |
| C - Campaign 主题活动 | Spike awareness or A4 conversion | Platform mega-sales, IP co-branding, hashtag challenges, time-boxed events |
| T - TopView 头部品效 | Brand lift + immediate traffic | Premium placement, splash/feed takeover, brand-effect combined buy |

**Decision rule**: Early-stage products with no brand awareness should bias toward **A + C** (creator proof + challenge/event). Established products with repeat purchase should bias toward **F + T** (owned operations + premium reach). Budget-constrained tests should start with **A** (micro-creator matrix) and only add C/T after proof.

---

## 4. Design the Content + Creator + Placement Mix
For the chosen scene(s), define the content formula, creator profile, and placement/distribution.

### 4.1 Content Formula
ByteDance content works when it stops the scroll and earns interactions. For the selected A-stage, pick one primary format:
- **Hook demo**: Problem → product in action → result (best for A2→A3)
- **Creator testimonial**: Real use by a trusted voice (best for A2→A3, A4 trust)
- **Live commerce**: Demonstration + limited offer + real-time social proof (best for A3→A4)
- **UGC challenge**: Low-friction participation with branded template (best for A1→A2, A5 advocacy)
- **Story/mini-drama**: Emotional payoff tied to product benefit (best for A1 awareness)

### 4.2 Creator Matrix
If Alliance is selected, specify tiers and roles. A standard matrix:
- **1-2 Head creators (>=1M fans)**: Borrow authority and generate mass awareness
- **5-20 Mid-tier creators (100K-1M fans)**: Deep persuasion, vertical expertise, explainers
- **Mass KOC / employees / users**: Social proof, UGC seeding, reviews, real scenarios

### 4.3 Placement Mix
Match placement to the scene:
- Feed ads / DOU+ / content加热 for scaling proven organic content
- Search ads / brand zone for capturing A3 intent
- Live-stream traffic / shopping ads for A4 conversion
- TopView / brand takeover for A1 brand events

---

## 5. Define Metrics and Guardrails
Borrow the discipline from `pm-2-metric-guardrail`. A campaign is only valid if success and safety are measurable.

| Layer | Example Metrics |
|---|---|
| North Star (business) | CAC, ROAS, GMV lift, paid-to-organic ratio, A4 conversion rate |
| Funnel stage metrics | A1→A2 transition rate, A2→A3 engagement rate, A3→A4 conversion rate |
| Content metrics | 3s/complete view rate, engagement rate, share rate, CTR |
| Guardrails | Brand safety score, negative comment rate, refund/return rate, frequency cap |

**Decision rule**: Every scene must map to at least one primary metric. If the user cannot measure it, remove that scene from the first phase.

---

## Output Template

Produce a concise campaign brief in this format. Do not include generic filler; every field must be specific to the product.

```markdown
### 🎯 ByteDance Interest-Marketing Campaign Brief

#### 1. Growth Task
- **Product**: [Name]
- **Target Segment**: [Who]
- **Funnel Stage to Move**: [A? → A?]
- **Current Baseline**: [Metric at start]
- **Primary Constraint**: [Budget / creative / time / measurement]

#### 2. A1-A5 Diagnosis
- Current distribution (estimate):
  - A1: [%]
  - A2: [%]
  - A3: [%]
  - A4: [%]
  - A5: [%]
- **Chosen Gap**: [A? → A?]
- **Why this gap**: [Quantified or hypothesis-backed reason]

#### 3. FACT+ Scene Selection
- **Primary Scene**: [F / A / C / T]
- **Supporting Scene(s)**: [if any]
- **Rationale**: [Why this scene matches the gap and constraint]

#### 4. Content + Creator + Placement Mix
- **Primary Content Formula**: [hook demo / testimonial / live commerce / UGC challenge / story]
- **Creator Matrix** (if A selected):
  - Head: [role / count / vertical]
  - Mid-tier: [role / count / vertical]
  - KOC/UGC: [role / mechanics]
- **Placement Mix**: [DOU+ / feed / search / live / TopView / challenge]

#### 5. Metrics & Guardrails
- **North Star**: [Metric + target]
- **Funnel Metrics**: [A-stage transitions to watch]
- **Content Metrics**: [engagement / view / share targets]
- **Guardrails**: [frequency, safety, returns, negative sentiment]
- **Decision Rule**: [When to scale, kill, or pivot after first [N] days / [X] spend]

#### 6. Next Step
- **Launch sequence**: [What runs first, second, third]
- **Feedback loop**: When results return, feed them into `pm-1-funnel-diagnostic` for the next cycle.
```
