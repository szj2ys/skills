---
name: create-branch
description: Create a branch
argument-hint: "describe your task for the new branch use to create a branch rather than doing the task itself, e.g. 'fix login crash on mobile' or 'add dark mode toggle'"
---

Create a properly named Git branch from a user-provided description, then copy the entire repository (including untracked files) to a structured directory and create the branch in the copied location.

## Workflow

### 1) Parse Task Information

Extract from user's input:
- **Task description**: What needs to be done (feature / bug fix / refactor / experiment) for the new branch use to create a branch rather than doing the task itself

Examples of user input formats:
- "Fix login crash on mobile"
- "Add dark mode toggle"
- "Refactor auth middleware"

!Important: Do not do user's task, just base this task description to create a properly named Git branch from a user-provided description for the new branch use to create a branch rather than doing the task itself.

### 2) Generate Branch Name

Format: `<type>/<short-slug>`

**Types:**
- `feat` - New features
- `fix` - Bug fixes
- `refactor` - Code restructuring without behavior change
- `chore` - Maintenance tasks, dependency updates
- `docs` - Documentation changes
- `style` - Formatting, linting fixes
- `test` - Adding or updating tests
- `perf` - Performance improvements
- `ci` - CI/CD configuration
- `build` - Build system changes
- `experiment` - Experimental work, spikes

**Slug rules:**
- Lowercase only
- Words separated by `-`
- 2–5 words maximum
- Drop stop words (the, a, an, in, on, for, to, etc.)
- Remove special characters

**Examples:**
| Description                            | Branch Name                |
| -------------------------------------- | -------------------------- |
| Fix empty query crash                  | `fix/empty-query-crash`    |
| Add dark mode toggle                   | `feat/dark-mode-toggle`    |
| Update README with API docs            | `docs/readme-api-docs`     |
| Refactor auth middleware               | `refactor/auth-middleware` |

If the description is too generic (e.g., "fix something"), make it unique:
- Append date suffix: `fix/misc-20260205`
- Or use `experiment/<date>-<brief-desc>` for experimental work

### 3) Determine Paths

Get required information:
```bash
# Current repository name (directory name)
repo_name=$(git remote get-url origin | xargs basename -s .git

# Current branch name
current_branch=$(git branch --show-current)

# Generated branch name (from step 2)
type="<type>"
short_slug="<short-slug>"
new_branch="<type>/<short-slug>"
```

Construct target path:
```
~/Documents/worktrees/${repo_name}/${type}-${short_slug}
```

```

### 4) Copy Repository

**DO NOT create the branch yet.** Only copy files.

```bash
# Ensure parent directories exist
mkdir -p "~/Documents/worktrees/${repo_name}/"

# Copy entire repository (including .git)
cp -r "$(git remote get-url origin | xargs basename -s .git)" "~/Documents/worktrees/${repo_name}/${type}-${short_slug}"
```

### 5) Create Branch in Copied Repository

Now create and checkout the new branch in the copied location:

```bash
cd "~/Documents/worktrees/${repo_name}/${type}-${short_slug}"

# Create and switch to new branch (detached from any remote tracking)
git checkout -b "${new_branch}"

# Verify current branch
git branch --show-current
```

### 6) Summary Output

Report what was done:

```
✅ Created branch: <new_branch>
📁 Location: <absolute_path>
🔀 Based on: <current_branch>

```

stop in there and do not proceed to any further steps.
