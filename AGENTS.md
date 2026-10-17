# Skills Project — Agent Guidelines

## Project Identity

This is **szj2ys/skills** — a personal skills library for AI agents. Each `skills/<name>/` directory is a self-contained skill with a `SKILL.md` whose frontmatter `name` matches the directory. Index every added or removed skill in README.md, and run `python .github/scripts/validate_skills.py` (CI runs it on push).

## Skill Home Rule

**All skill creation, updates, and management default to this project's skills directory, rather than .agents/skills.**

Unless the user explicitly specifies a different directory or project, any request to:
- Create a new skill
- Update an existing skill's content or metadata
- Delete or rename a skill


If the user's request is ambiguous about location, **ask before assuming** a different project.


with the skills, the most important thing is to deceide what to do rather than how to do it. This is the reason of this project.