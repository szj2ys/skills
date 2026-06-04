---
name: design-code-review
description: Audit and review web pages or UI designs across visual design, UX flow, code quality, accessibility, mobile responsiveness, and SEO. Use this skill whenever the user mentions reviewing a design, auditing a webpage, evaluating UI/UX, or wants feedback on any of these dimensions. Consider all six dimensions but allow the agent to freely assess each based on the context.
---

# Design & Code Review Skill

This skill helps you audit and review web pages or UI designs. When triggered, consider the following dimensions:

1. **Visual Design**: Look for professional use of emojis, advertisement prominence, and presence of micro-interactions.
2. **UX Flow**: Check for missing copy buttons, unclear time window explanations, and overall flow clarity.
3. **Code Quality**: Identify risks like unsafe DOM manipulation, inline event handlers, and global variable usage.
4. **Accessibility**: Note missing aria attributes, non-semantic HTML, and restrictive viewport settings (e.g., user-scalable=no).
5. **Mobile Responsiveness**: Check for hidden navigation links, lack of hamburger menu, and touch target sizes.
6. **SEO**: Verify presence of meta description, structured data, and Open Graph tags.

Provide a concise assessment for each dimension, including a score (out of 10) and the main issues found. Keep the review lightweight and focused—do not impose rigid constraints; instead, use these dimensions as a guide for your evaluation.

Review whatever the user provides: a URL, HTML snippet, code sample, design description, or project details. Base your assessment on the actual context given.
