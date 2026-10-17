---
name: systems-map
description: Explain a whole project as a system — boundary, actors, end-to-end flows, feedback loops, constraints — with Excalidraw diagrams. Use for 系统思维分析项目 or a whole-system overview of a codebase. Concept walkthroughs are teach; module and interface design is codebase-design.
---

# Systems Map

## The one rule

**Each arrow carries its evidence.** Structural and data-flow edges cite the code that creates them. Causal and behavioural claims need a runtime observation; without one they are dashed hypotheses with the observation that could refute them.

Source files stay unchanged.

## Steps

1. **Trace one realistic case** through the code from trigger to outcome, including what happens when an important step fails.
2. **Boundary**: the problem, for whom, what success means (`unknown` if undocumented), what is inside versus external dependencies, where stakeholder goals conflict.
3. **Parts**: 5–8 main actors, activities or subsystems, and what each contributes.
4. **Relationships**: what flows between parts (data, money, decisions, feedback), separating structural dependency, data flow and causal influence. For key causal links: "when A changes, B may change because …".
5. **Behaviour over time**: feedback loops, delays, bottlenecks. A tradeoff where improving a part hurts the whole only when supported; label it hypothetical otherwise, or state none found.
6. **Leverage**: the likely constraint, candidate changes and their side effects, the unknown that would most change this picture, and one small observation that tests it.

## Diagrams

One Excalidraw scene with separate titled views: system overview (boundary and externals), end-to-end flow with the failure path, feedback loops when they explain behaviour. Labelled arrows, a small legend; solid = evidenced, dashed = hypothesis.

Save `systems-map.excalidraw` in the project root or the path the user names. Open it in Excalidraw (or render it) and check every view is readable with no overlapping text or dangling arrows. A share link only when the user asks for one: create it, reopen it, and report it; never upload internal architecture by default.

## Output

Short overview → the six sections with file references → diagram path and how it was checked → up to 3 questions that would most improve the model.
