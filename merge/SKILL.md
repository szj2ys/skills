---
name: merge
description: Merge branches into current branch
argument-hint: "branch to merge"
---

# Git Merge

Merge branches into current branch

## Important:
- **NEVER add co-author information or Claude attribution**
- **PROTECT local configuration files** from being overwritten
- If there are merge conflicts, must figure out how to resolve them intelligently based on file status and content, then ask the user how to proceed

## Usage

```bash
/git-merge
```

The command will ask which branch to merge.

## Workflow

### 1. Ask user for branch to merge

Ask the user (and wait for the answer before continuing):

- **Which branch should be merged into the current branch?**
  - show common options (`main`, `develop`) when they exist
  - include **Other** for custom input

If the user picks a protected branch or anything without `/`, ask a second confirmation before merging.

### 2. Fetch remote changes of the target branch

### 3. Try to merge the target branch into current branch

Attention: Do not modify the files ignored by .gitignore
