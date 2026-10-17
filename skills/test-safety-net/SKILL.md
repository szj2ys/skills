---
name: test-safety-net
description: Add missing tests to an existing app in risk order — 补测试, 代码测试, "this project has no tests", a regression net before refactoring or launch. Test-first development of new behaviour is tdd; hunting one bug is diagnosing-bugs.
---

# Test Safety Net

## The one rule

**Test what costs money or trust first, through the real interface, with expectations taken from the product's promise — never from today's output.**

## 1. Rank targets by blast radius

money and entitlements → auth and data isolation → data the user relies on being saved → the core task's happy path → the rest. Write the top 5–10 as sentences that include the forbidden outcome, e.g. "a duplicate payment webhook grants credits once", "user B cannot read user A's invoice".

## 2. Test through the outside

Use the smallest public boundary that exposes the risk — HTTP for a web app, the CLI for a tool, the function for a library — against disposable storage with the same semantics as production. Fake external services that change state or cost money at their boundary; tests run with test configuration and no live keys. Reuse the project's runner and CI; for a project with none, prefer the platform's built-in runner.

## 3. Expectations come from the contract

Derive each expected result from the product's promise or a worked example. When the intended behaviour is unclear, record the question. For each high-risk test, break the behaviour on purpose once and confirm the test fails, then restore.

## 4. Known bugs stay red

A safety test that fails because the product is wrong stays failing until the bug is fixed. A green run means every safety case ran and passed. Report each failing case as a bug.

## 5. Isolation and routine

Each test owns its data and leaves dev and production data untouched; tests pass in any order and wait on conditions instead of sleeping. One command runs everything and its exit code tells the truth.

## Output

Ranked behaviour list · tests added (file → behaviour) · the command and its real output (pass / fail counts) · bugs exposed · what stays untested and why.
