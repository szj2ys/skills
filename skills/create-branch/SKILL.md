---
name: create-branch
description: Create a correctly named Git branch from a task description as a linked git worktree, switch the session into it, and push it to the remote with upstream tracking.
argument-hint: "describe your task for the new branch use to create a branch rather than doing the task itself, e.g. 'fix login crash on mobile' or 'add dark mode toggle'"
---

Create a properly named Git branch from a user-provided description. By default the branch lives in a new **linked git worktree** (`git worktree add -b`), the session switches into it, and the branch is pushed to the remote with upstream tracking. The repository is not copied.

## Platform

The command blocks below are POSIX (`sh`) and run under `sh`, `dash` and `bash`.

- **macOS / Linux** — run them as written.
- **Windows** — run them in **Git Bash** or **WSL**; that is what Claude Code's Bash tool uses on Windows. If PowerShell is the only shell, use the PowerShell block at the end.

On Windows `$HOME` is `C:\Users\<you>`, so `work_dir` resolves to `C:\Users\<you>\Documents\worktrees\<repo>\<type>-<slug>`. Print that Windows spelling in the step 6 summary, not Git Bash's `/c/Users/...` form.

The filesystem is case-insensitive on Windows and default macOS, so `Fix/X` and `fix/x` are the same branch name.

## Workflow

### 1) Parse Task Information

Extract from the user's input the **task description** (feature / bug fix / refactor / experiment) for the new branch.

Examples: "Fix login crash on mobile", "Add dark mode toggle", "Refactor auth middleware".

!Important: Do not do the user's task. Only create the branch and worktree for it.

### 2) Generate Branch Name

Format: `<type>/<short-slug>`

**Types:** `feat` new features, `fix` bug fixes, `refactor` restructuring without behavior change, `chore` maintenance and dependency updates, `docs` documentation, `style` formatting and lint fixes, `test` tests, `perf` performance, `ci` CI/CD configuration, `build` build system, `experiment` spikes.

**Slug rules:** lowercase only, words separated by `-`, 2–5 words, drop stop words (the, a, an, in, on, for, to), remove special characters.

| Description                 | Branch Name                |
| --------------------------- | -------------------------- |
| Fix empty query crash       | `fix/empty-query-crash`    |
| Add dark mode toggle        | `feat/dark-mode-toggle`    |
| Update README with API docs | `docs/readme-api-docs`     |
| Refactor auth middleware    | `refactor/auth-middleware` |

If the description is too generic ("fix something"), make it unique: append a date (`fix/misc-20260205`) or use `experiment/<date>-<brief-desc>`.

### 3) Create the Worktree

Run steps 3–4 in **one** shell invocation (a single Bash tool call): shell variables do not persist between calls.

```bash
type="<type>"
short_slug="<short-slug>"
new_branch="${type}/${short_slug}"

# Main repository name, correct even when run from inside another worktree
common_dir=$(git rev-parse --path-format=absolute --git-common-dir) \
  || { echo "ERROR: not inside a git repository" >&2; exit 1; }
repo_name=$(basename "$(dirname "$common_dir")")
current_branch=$(git branch --show-current)

work_dir="$HOME/Documents/worktrees/${repo_name}/${type}-${short_slug}"

if [ -e "$work_dir" ]; then
  echo "ERROR: $work_dir already exists - pick a unique branch name (step 2)" >&2
  exit 1
fi
mkdir -p "$(dirname "$work_dir")"

# Create the branch from the current HEAD and check it out in the new directory
git worktree add -b "$new_branch" "$work_dir" || exit 1
git worktree list
```

Write the target as `"$HOME/..."`, never a quoted `"~/..."`: a quoted tilde is a literal directory named `~`.

- The branch starts at the local `HEAD`, not the latest remote. If the local base may be stale, run `git fetch origin` first; this skill does not fetch or rebase.
- A worktree contains tracked files only. Uncommitted changes and untracked or ignored files (`.env`, `node_modules`, build output) stay in the original checkout. Tell the user when the original has uncommitted changes, and that dependencies must be reinstalled in the new directory. If the user wants those files carried over, use the copy fallback below.
- If the branch name already exists, `git worktree add -b` fails. Re-generate the name (step 2); never pass `-B` or `--force`.

### 4) Push Branch to Remote

Run inside `$work_dir`, not in the original checkout:

```bash
cd "$work_dir" || exit 1

current=$(git branch --show-current)
[ "$current" = "${new_branch}" ] || {
  echo "ERROR: HEAD is on '${current:-detached}', expected '${new_branch}'. Nothing was pushed." >&2
  exit 1
}

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "SKIP PUSH: no 'origin' remote configured"
else
  git push --set-upstream origin "${new_branch}" || exit 1
  git rev-parse --abbrev-ref --symbolic-full-name '@{u}'
  git ls-remote --heads origin "${new_branch}"
fi
```

- `--set-upstream` makes later `git push` / `git pull` in the worktree need no arguments, and is safe to re-run.
- This step never passes `--force`. A rejected `non-fast-forward` or an unreachable `origin` exits non-zero, so the summary never claims a push that did not happen.
- If `origin` is an empty repo (first push ever), the full history transfers and git prints nothing until it finishes. Re-run with `git push --progress` and a long timeout rather than touching credential or proxy config.

### 5) Switch Into the Worktree

Switching is part of the default behavior; do it after the push.

- **Claude Code:** call the `EnterWorktree` tool with `path` set to `work_dir` (the Windows spelling is fine). The path is already registered in `git worktree list`, so it is accepted, and the session's working directory moves there. Do not pass `name`, which would create a second worktree.
- **Other agents or a plain shell:** `cd "$work_dir"` in every later command, and print `work_dir` so the user can open it.

Then confirm with `git branch --show-current` and `pwd` from the new location.

### 6) Summary Output

```
✅ Created branch: <new_branch>
📁 Worktree: <absolute work_dir> (session switched here)
🔀 Based on: <current_branch>
☁️  Pushed to: <origin url> (upstream origin/<new_branch>)
```

If the push was skipped, replace the last line with the skip reason. Remind the user that the original checkout is untouched and `git worktree remove "<work_dir>"` cleans up when the branch is done.

## Fallback: full copy (only when the user asks)

Use this only when the user explicitly wants uncommitted and untracked files carried into the new directory. It is not the default.

```bash
repo_root=$(git rev-parse --show-toplevel) || exit 1
if [ -f "$repo_root/.git" ]; then
  echo "ERROR: $repo_root is a linked worktree or submodule; run from the main checkout" >&2
  exit 1
fi
[ -e "$work_dir" ] && { echo "ERROR: $work_dir already exists" >&2; exit 1; }
mkdir -p "$work_dir" && cp -a "$repo_root/." "$work_dir" || exit 1
cd "$work_dir" && git checkout -b "$new_branch" || exit 1
```

Then run step 4 unchanged and `cd` into the copy. On Windows, run `git config --global core.longpaths true` once first, or a deep `node_modules` fails with `File name too long`.

## Windows: PowerShell equivalent

Fallback for when Git Bash is unavailable. It mirrors steps 3–4 only; the branch-name rules and the step 5 switch are identical.

```powershell
$type = "fix"; $short_slug = "empty-query-crash"    # generated in step 2
$new_branch = "$type/$short_slug"

$common_dir = git rev-parse --path-format=absolute --git-common-dir
if ($LASTEXITCODE -ne 0 -or -not $common_dir) {
  Write-Host "ERROR: not inside a git repository"; exit 1
}
$repo_name      = Split-Path (Split-Path "$common_dir".Trim() -Parent) -Leaf
$current_branch = git branch --show-current
$work_dir = Join-Path $HOME "Documents\worktrees\$repo_name\$type-$short_slug"

if (Test-Path $work_dir) {
  Write-Host "ERROR: $work_dir already exists - pick a unique branch name"; exit 1
}
New-Item -ItemType Directory -Force -Path (Split-Path $work_dir) | Out-Null

git worktree add -b $new_branch $work_dir
if ($LASTEXITCODE -ne 0) { exit 1 }

Set-Location $work_dir
$current = git branch --show-current
if ("$current" -ne $new_branch) {
  Write-Host "ERROR: HEAD is on '$current', expected '$new_branch' - nothing was pushed"; exit 1
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
