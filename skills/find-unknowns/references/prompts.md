# Reference Prompts

Copy-pasteable starting prompts for each technique in the find-unknowns skill. Adapt the bracketed parts to the task.

## Table of contents

1. Blind spot pass
2. Brainstorms and prototypes
3. Interview
4. Reference
5. Implementation plan
6. Implementation notes
7. Pitches and explainers
8. Quiz

## 1. Blind spot pass

I'm working on [task] but I know nothing about [module/domain]. Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better?

I don't know what [concept, e.g. color grading] is but I need to [goal]. Can you teach me to understand my unknown unknowns about [concept], so that I can prompt better?

## 2. Brainstorms and prototypes

I want [a dashboard for this data] but I have no visual taste and don't know what's possible. Make me an HTML page with 4 wildly different design directions so I can react to them.

Before wiring anything up, make a single HTML file mocking [the new editor toolbar] with fake data. I want to react to the layout before you touch the real app.

Here's my rough problem: [users churn after onboarding]. Search the codebase and brainstorm 10 places we could intervene, from cheapest to most ambitious. I'll tell you which ones resonate.

## 3. Interview

Interview me one question at a time about anything ambiguous in [task]. Prioritize questions where my answer would change the architecture.

## 4. Reference

This [Rust crate in vendor/rate-limiter] implements the exact [backoff] behavior I want. Read it and reimplement the same semantics in our [TypeScript API client].

Point at [module/URL/file] and extract the [pattern/semantics/structure] I want, then apply it to [our context]. Note where our constraints differ.

## 5. Implementation plan

Write an implementation plan in HTML, but lead with the decisions I'm most likely to tweak: data model changes, new type interfaces, and anything user-facing. Bury the mechanical refactoring at the bottom; I trust you on that part.

## 6. Implementation notes

Keep an `implementation-notes.md` file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under "Deviations", and keep going.

## 7. Pitches and explainers

Package the prototype, the spec, and the implementation notes into a single doc I can drop in Slack to get buy-in. Lead with the demo GIF.

## 8. Quiz

I want to make sure I understand everything that's happened in this change. Give me an HTML report on the changes with context, intuition, what was done, etc., and a quiz at the bottom on the changes that I must pass.
