---
name: pull-requests
description: Pull Request Creation
argument-hint: "to <branch> or --into <branch>"
---

Create professional pull requests with an automated workflow. No mid-process branch confirmation prompts.


## When to Use

Use this skill when:
- User asks to "create PR", "submit PR", "open PR", "make a pull request"
- User wants to create a merge request on GitLab
- Any request that involves creating a pull/merge request

## Workflow

### 1) Parse Request Information

Extract from user's input:
- **Target branch** (optional): If user specifies with "--into <branch>" or "to <branch>", use that; otherwise defaults to repo’s main branch (usually `main`)

If target branch is not specified, use repo’s main branch as the default.

### 2) Repository Detection

- Examine remote URL to auto-detect GitHub or GitLab
- GitHub: uses `gh` CLI → creates Pull Requests
- GitLab: uses `glab` CLI → creates Merge Requests

### 3) Sync with Base Branch

Always sync before creating PR:

```bash
git fetch --all --prune
```

If the current branch has a tracked remote:

```bash
git merge origin/<base-branch> --no-edit
```

Resolve any merge conflicts before proceeding.

### 4) Generate PR Content

**Title**: Auto-generate from commit history:
- Use first line of most recent commit if it follows Conventional Commits format
- Otherwise, generate concise title describing the changes

**Body**: Generate description using the template below based on commits and changed files.

### 5) Create PR/MR

**GitHub:**
```bash
gh pr create --title "<title>" --body "<body>" --base <base-branch>
```

**GitLab:**
```bash
glab mr create --title "<title>" --description "<body>" --target-branch <base-branch>
```

## PR Guidelines

### Title

- Keep it **short and clear**: one sentence describing the core change/value
- Prefer **Conventional Commits-style** titles (aligned with allowed commit types):
  - `docs: ...`, `fix(api): ...`, `feat(web): ...`
- Don’t stuff implementation steps into the title

### Body Template

The PR description should clearly explain **what changed and why**.

```markdown
## Summary
- What & why (change + user/business impact)

## Changes
- Key changes (group by module/file/feature if helpful)

## Test Plan (Optional)
- [ ] Unit tests: ...
- [ ] Integration tests: ...
- [ ] Manual verification: ...

## Related Issues (Optional)
- Closes #123
- Related: #456
```

**Note**: Only include sections that are relevant. Keep it concise.

## Automated Behaviors

- Platform detection is automatic (GitHub vs GitLab)
- Default base branch is `main` if not specified
- Branch validation is automatic

## Important Guidelines

- Use **Conventional Commits** style for PR title (e.g., `feat(web):`, `fix(api):`, `docs:`)
- Allowed types: `fix|feat|build|chore|ci|docs|style|refactor|perf|test`
- Commits should be authored solely by the user
- Never add Claude attribution or co-author lines
- Do not ask the user to confirm the target branch - use `main` as default

## Error Recovery

If command fails:
1. Verify branch is pushed to remote: `git push --set-upstream origin <branch>`
2. Check `gh` or `glab` authentication: `gh auth status` / `glab auth status`
3. Verify base branch exists on remote
4. Retry PR creation after resolving issues
