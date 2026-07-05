---
name: find-unknowns
description: Surface hidden assumptions, blind spots, and unconsidered unknowns before, during, and after implementation. Use when starting work in unfamiliar territory or a new part of the codebase, planning or prototyping a feature, interviewing the user to clarify requirements, requesting a reference to mimic, reviewing an implementation plan, logging deviations during execution, packaging a pitch/explainer for stakeholders, or quizzing the user to verify they understand a change before merging.
---

# Find Unknowns

## Overview

The map (your prompt, plan, and skills) is not the territory (the real codebase and its constraints). The gap between them is the unknowns. This skill gives a repeatable loop for discovering and verbalizing unknowns before, during, and after implementation so that decisions are made deliberately, not by default.

Run the loop iteratively. Unknowns surface at every phase, and finding one late is more expensive than finding one early.

## Kinds of unknowns

When probing a task, classify findings into:

- Known knowns: what the user already stated they want.
- Known unknowns: things the user knows they have not decided.
- Unknown knowns: assumptions so obvious the user would never write them down, but would recognize if surfaced.
- Unknown unknowns: things neither user nor agent has considered yet.

The goal is not to eliminate every unknown up front. It is to surface the ones that would change the path, and to leave the agent room to improvise through the rest.

## How to use this skill

1. Identify the user's phase: pre-implementation, during implementation, or post-implementation.
2. Pick the matching technique below.
3. Anchor on the user's own context: codebase, prior artifacts, stated constraints, and how much of the domain they already know.
4. Produce the named artifact, or answer questions directly.
5. After each pass, restate what is now known, what is still unknown, and where the user should decide next.

## Techniques

### Blind spot pass (pre-implementation)

Use when the user is entering unfamiliar work, a new part of the codebase, or a new domain and may not know what questions to ask.

- Ask for context first: role, what they already know, what they have tried, where they are stuck.
- Read the relevant parts of the codebase if files are indicated or discoverable.
- Surface unknown unknowns and unknown knowns that could change the approach: hidden constraints, prior art, failure modes, what "good" looks like.
- Output a concise report (HTML or Markdown) of risks, open questions, and suggested next steps.

### Brainstorms and prototypes (pre-implementation)

Use when the criteria are "I'll know it when I see it," especially for UI/UX, API shape, or project scope.

- Generate 2-5 concrete options, or a throwaway prototype (single HTML file, fake data, no backend wiring).
- Keep it cheap and disposable; do not touch the real app yet.
- After the user reacts, narrow scope before committing to implementation.

### Interview (pre-implementation)

Use after brainstorming when the user still has unresolved unknowns.

- Ask one question at a time.
- Prioritize questions whose answers would change the architecture, data model, or scope.
- Stop when the path is clear enough to plan.

### Reference (pre-implementation)

Use when the user cannot describe what they want in words but can point at existing code, docs, or a public site or module.

- Read the reference (folder, file, library, or URL).
- Extract the pattern, semantics, or structure the user wants.
- Re-apply it to the user's context, noting where their constraints differ.

### Implementation plan (pre-implementation)

Use when the user thinks they are ready to implement.

- Write a plan that leads with decisions the user is most likely to tweak: data model changes, new type interfaces, user-facing flows.
- Put mechanical refactoring at the bottom.
- Ask the user to approve or adjust before coding.

### Implementation notes (during implementation)

Use when the user has handed off a spec or prototype and wants the agent to execute.

- Keep a temporary `implementation-notes.md` (or `.html`) in the workspace.
- When an edge case forces a deviation from the plan, pick the conservative option, log it under a "Deviations" section, and keep going.
- Never silently change the plan.

### Pitches and explainers (post-implementation)

Use when the user needs to communicate a result to stakeholders or reviewers.

- Package the prototype, spec, and implementation notes into one artifact.
- Lead with the demo or the thing that creates understanding fastest.
- Make the unknowns you surfaced visible, so reviewers can see you accounted for the failure points they would have anticipated.

### Quiz (post-implementation)

Use when the user wants to verify they understand a change before merging.

- Produce an HTML report on the change: context, intuition, what was done, and how it behaves.
- Append a short quiz the user must answer.
- Review answers, fill gaps, and only consider the work done when the user passes.

## Reference prompts

For copy-pasteable example prompts for each technique, see [references/prompts.md](references/prompts.md). Read it when the user asks for a starter prompt or when you are unsure how to phrase a request for a given technique.
