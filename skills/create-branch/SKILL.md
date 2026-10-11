---
name: create-branch
description: Create a correctly named Git branch from a task description in a copied working directory, then push it to the remote with upstream tracking.
argument-hint: "describe your task for the new branch use to create a branch rather than doing the task itself, e.g. 'fix login crash on mobile' or 'add dark mode toggle'"
---

Create a properly named Git branch from a user-provided description, then copy the entire repository (including untracked files) to a structured directory, create the branch in the copied location, and push it to the remote so it exists upstream as well as locally.

## Platform

The command blocks below are POSIX (`sh`) and are verified to run under `sh`, `dash`
and `bash`.

- **macOS / Linux** — run them as written.
- **Windows** — run them in **Git Bash** or **WSL**; that is what Claude Code's Bash tool
  uses on Windows. Do not paste them into `cmd.exe` or PowerShell as-is — if PowerShell
  is your only shell, use the PowerShell block at the end of this file instead.

On Windows `$HOME` is `C:\Users\<you>`, so `work_dir` resolves to
`C:\Users\<you>\Documents\worktrees\<repo>\<type>-<slug>`. Print that Windows
spelling in the step 7 summary, not Git Bash's `/c/Users/...` form.

Windows checks that do not apply on macOS/Linux:

- Run `git config --global core.longpaths true` once, or copying a deep `node_modules`
  fails with `File name too long` (MAX_PATH).
- If the copy fails with `Access is denied` or `Device or resource busy`, another
  process holds a file (editor, antivirus, running dev server) — close it and retry.
  Remove `.git/index.lock` only when you are sure no git process is running.
- The filesystem is case-insensitive, so `Fix/X` and `fix/x` are the same branch name.


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

Get required information. Run this from anywhere inside the repository:

```bash
# Repository root — resolves correctly from any subdirectory
repo_root=$(git rev-parse --show-toplevel) \
  || { echo "ERROR: not inside a git repository" >&2; exit 1; }

# A linked worktree (or submodule) has .git as a *file* pointing back at the
# original repo, so a copy would keep creating branches there instead of here.
if [ -f "$repo_root/.git" ]; then
  echo "ERROR: $repo_root is a linked worktree or submodule (.git is a file)" >&2
  echo "Run this skill from the main checkout so the copy is independent." >&2
  exit 1
fi

# Current repository name (directory name)
repo_name=$(basename "$repo_root")

# Current branch name
current_branch=$(git branch --show-current)

# Generated branch name (from step 2)
type="<type>"
short_slug="<short-slug>"
new_branch="${type}/${short_slug}"

# Destination for the copy
work_dir="$HOME/Documents/worktrees/${repo_name}/${type}-${short_slug}"
```

Construct target path:
```
~/Documents/worktrees/<repo_name>/<type>-<short_slug>
```

Run steps 3–6 in **one** shell invocation (a single Bash tool call). Shell state —
variables and the working directory — does not persist between separate tool calls,
so step 6 run on its own would see an empty `$work_dir` and never push.

Write the target as `"$HOME/..."`, never a quoted `"~/..."`: a quoted tilde is a
literal directory named `~`, so the copy silently lands inside the current directory.

### 4) Copy Repository

**DO NOT create the branch yet.** Only copy files.

```bash
# Ensure parent directories exist
mkdir -p "$(dirname "$work_dir")"

# Copy the working tree (including .git and untracked files)
if [ -e "$work_dir" ]; then
  echo "ERROR: $work_dir already exists" >&2
  echo "Pick a unique branch name (step 2) rather than merging into it." >&2
  exit 1
fi
mkdir -p "$work_dir"
cp -a "$repo_root/." "$work_dir"
```

Copying rather than `git clone` is deliberate: untracked files must survive.

### 5) Create Branch in Copied Repository

Now create and checkout the new branch in the copied location:

```bash
cd "$work_dir" || { echo "ERROR: copy missing at $work_dir"; exit 1; }

# Create and switch to new branch (detached from any remote tracking)
git checkout -b "${new_branch}" || exit 1

# Verify current branch
git branch --show-current
```

### 6) Push Branch to Remote

The branch now exists only in the local copy. Push it so the remote, CI and
teammates can see it. **Run this inside `$work_dir`, not in the original repo.**

```bash
: "${work_dir:?work_dir is empty - run steps 3-5 in the same shell invocation}"
cd "$work_dir" || exit 1

# Never push a branch this run did not actually check out (step 5 may have failed
# in a separate tool call, leaving HEAD on the copy's original branch).
current=$(git branch --show-current)
[ "$current" = "${new_branch}" ] || {
  echo "ERROR: HEAD is on '${current:-detached}', expected '${new_branch}'" >&2
  echo "Re-run step 5, or re-generate the branch name in step 2. Nothing was pushed." >&2
  exit 1
}

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "SKIP PUSH: no 'origin' remote configured"
else
  git push --set-upstream origin "${new_branch}" || exit 1
fi

# Verify: upstream is set locally and the ref exists on the remote
if git remote get-url origin >/dev/null 2>&1; then
  git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || echo "no upstream"
  git ls-remote --heads origin "${new_branch}"
fi
```

- `--set-upstream` makes later `git push` / `git pull` in this directory need no
  arguments. It also sets tracking when the ref is already up to date
  ("Everything up-to-date"), so re-running this step is safe.
- The copy branches from the local `HEAD`, not the latest remote. If your local base may
  be stale, run `git fetch origin` in the original repo first — this skill deliberately
  does not fetch or rebase, because it must preserve uncommitted and untracked files.
- The push sends only the new ref plus commits the remote does not already have,
  so on a copy of an existing repo it is normally near-instant.
- Everything that can go wrong exits non-zero here, so the summary never claims a push
  that did not happen: a branch that has diverged is rejected `non-fast-forward`,
  an unreachable or bad `origin` exits 128. This step never passes `--force` —
  integrate with `git pull`, or re-generate the branch name (step 2).
- **Exception:** if `origin` is an empty repo (first push ever), the full history
  transfers and git prints nothing until it finishes. A silent multi-minute push is
  not an auth hang — re-run with `git push --progress` and a long timeout rather
  than touching credential or proxy config.

### 7) Summary Output

Report what was done:

```
✅ Created branch: <new_branch>
📁 Location: <absolute work_dir>
🔀 Based on: <current_branch>
☁️  Pushed to: <origin url> (upstream origin/<new_branch>)
```

If the push was skipped, replace the last line with the skip reason instead.

## Windows: PowerShell equivalent

Not a step — a fallback for when Git Bash is unavailable. It mirrors steps 3–6 only;
steps 1, 2 and 7 are unchanged and the branch-name rules are identical.

```powershell
# step 3 — determine paths
$repo_root = git rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0 -or -not $repo_root) {
  Write-Host "ERROR: not inside a git repository"; exit 1
}
$repo_root = "$repo_root".Trim()
if (Test-Path (Join-Path $repo_root '.git') -PathType Leaf) {
  Write-Host "ERROR: linked worktree or submodule (.git is a file) - run from the main checkout"
  exit 1
}
$repo_name      = Split-Path $repo_root -Leaf
$current_branch = git branch --show-current
$type = "fix"; $short_slug = "empty-query-crash"    # generated in step 2
$new_branch = "$type/$short_slug"
$work_dir = Join-Path $HOME "Documents\worktrees\$repo_name\$type-$short_slug"

# step 4 — copy the repository; DO NOT create the branch yet
if (Test-Path $work_dir) {
  Write-Host "ERROR: $work_dir already exists - pick a unique branch name"
  exit 1
}
New-Item -ItemType Directory -Force -Path (Split-Path $work_dir) | Out-Null
Copy-Item -LiteralPath $repo_root -Destination $work_dir -Recurse -Force

# step 5 — create the branch in the copied repository
if (-not (Test-Path $work_dir)) { Write-Host "ERROR: copy missing at $work_dir"; exit 1 }
Set-Location $work_dir
git checkout -b $new_branch
if ($LASTEXITCODE -ne 0) { exit 1 }
git branch --show-current

# step 6 — push to the remote
$current = git branch --show-current
if ("$current" -ne $new_branch) {
  Write-Host "ERROR: HEAD is on '$current', expected '$new_branch' - nothing was pushed"
  exit 1
}
git remote get-url origin *> $null
if ($LASTEXITCODE -ne 0) {
  Write-Host "SKIP PUSH: no 'origin' remote configured"
} else {
  git push --set-upstream origin $new_branch
  if ($LASTEXITCODE -ne 0) { exit 1 }
  git rev-parse --abbrev-ref --symbolic-full-name '@{u}'
  git ls-remote --heads origin $new_branch
}
```

stop in there and do not proceed to any further steps.
