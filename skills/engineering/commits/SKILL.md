---
name: commits
description: Create atomic git commits with proper messages
---

You are tasked with creating git commits for the changes.

**only** allows these commit `type`s:

- `fix`, `feat`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`

## Process

1. **Review changes + pick commit type**
   - Review conversation history to understand what was accomplished
   - `git status`
   - `git diff`
   - Choose a valid `type` from: `fix|feat|build|chore|ci|docs|style|refactor|perf|test`

2. **Create a commit message that passes the hook**

   **Format (Conventional Commits):**
   ```
   <type>(<scope>)?: <subject>

   <body>

   <footer>
   ```

   **Rules:**
   - `<type>` must be one of: `fix|feat|build|chore|ci|docs|style|refactor|perf|test`
   - `<scope>` is optional (e.g. `web`, `api`, `prompts`)
   - Keep the first line concise (aim for ≤ 72 chars)
   - Use imperative mood in `<subject>` (e.g. “add”, “fix”, “remove”, “refine”)
   - Do **not** add Claude attribution, `Co-Authored-By`, or “Generated with …” lines

   **Examples:**
   ```
   feat(web): add podcast generation form
   fix(api): handle empty query input
   refactor(prompts): simplify stock analysis prompt
   docs: update local dev commands
   ```

3. **Execute atomic commits**
   - Review changes and identify distinct logical changes (e.g., feature addition, bug fix, refactoring, formatting)
   - For **each logical change**, create a separate commit:
     - Stage only the files related to that change (`git add <files>`)
     - Write a focused commit message describing that specific change
     - Commit
   - Each commit should represent a single, complete, reversible unit of work
   - If the current branch already has a corresponding remote branch, push the commits to remote automatically. If the branch exists only locally and is not yet associated with any remote branch, ask the user whether they want to create a remote branch for it.


## Failure handling (commit-msg hook)

If the commit is rejected, it usually means the header doesn’t match the required pattern or the `type` is not in the allowed list. Adjust the commit message and retry.

## Important guidelines

- Commits should be authored solely by the user
- Never add any “Generated with Claude” messages or co-author lines
- Commit as-is based on the current state. Do not make any changes before committing—no edits, deletions, or additions. The fact that this command is being run means the state is already ready to commit, so you don’t need to modify anything.
- Never use `git restore` or undo commands, if there is secret, ask user how to proceed

