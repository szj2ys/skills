# Self-Improve — Analysis Reference

## Detailed Scoring Heuristics

### 1. Prompt Clarity (1-10)

**Signals of low clarity:**
- User messages under 10 words with no file paths or specific targets
- Vague verbs: "fix this", "make it better", "update stuff"
- No success criteria stated
- Ambiguous pronouns ("it", "that", "this file") without context

**Signals of high clarity:**
- Specific file paths or function names mentioned
- Clear expected outcome described
- Constraints stated ("don't touch X", "keep it under Y")
- Examples provided for desired behavior

**Scoring:**
- 1-3: Most prompts are vague, require multiple clarification rounds
- 4-6: Mix of clear and vague, occasional rework needed
- 7-9: Mostly specific, minor clarifications occasionally
- 10: Every prompt is actionable with zero ambiguity

### 2. Task Decomposition (1-10)

**Signals of poor decomposition:**
- Single prompt requests 5+ file changes
- "Build entire feature X" with no phases
- User asks for end-to-end implementation in one shot
- Session has >20 turns on a single topic (likely thrashing)

**Signals of good decomposition:**
- Tasks scoped to 1-3 files per prompt
- Explicit phases: "first do X, then Y, then Z"
- Incremental building: scaffold → implement → test → refine
- Checkpoints: "now verify X works before moving to Y"

**Scoring:**
- 1-3: Monolithic requests, frequent mid-task pivots
- 4-6: Some decomposition but inconsistent
- 7-9: Clear phases, logical progression
- 10: Surgical task boundaries, each step verifiable

### 3. Context Efficiency (1-10)

**Signals of poor context usage:**
- User pastes entire files when only 5 lines are relevant
- Re-explaining context that was already provided
- Including irrelevant project history
- No file paths given when discussing specific code

**Signals of good context usage:**
- References specific files and line numbers
- Uses `@file` or paste snippets for targeted context
- Leverages project memory / CLAUDE.md for persistent context
- Asks tool to read files rather than pasting content

**Scoring:**
- 1-3: Context dumps, massive token waste
- 4-6: Reasonable but verbose
- 7-9: Targeted references, minimal noise
- 10: Surgical context, maximum signal per token

### 4. Tool Utilization (1-10)

**Signals of underutilization:**
- Never uses agents/subagents for parallel work
- Manually doing what a skill could automate
- Not using glob/grep for code search (using find/rg in bash instead)
- Ignoring available MCP tools
- Not leveraging plan mode for complex tasks

**Signals of good utilization:**
- Uses agents for research/exploration tasks
- Leverages skills for specialized workflows
- Uses appropriate tools (Edit over Write for modifications)
- Uses plan mode before complex implementations
- Chains tools effectively (Grep → Read → Edit)

**Scoring:**
- 1-3: Treats tool as plain chat, ignores 80%+ of capabilities
- 4-6: Uses basic tools, misses advanced features
- 7-9: Good tool selection, occasional missed optimization
- 10: Expert-level tool orchestration

### 5. Iteration Quality (1-10)

**Signals of poor iteration:**
- Corrective turns > additive turns (fixing vs building)
- Same error pattern repeated 3+ times
- Undo-redo cycles (change → revert → change again)
- "No that's not what I meant" appears frequently
- User changes direction mid-implementation

**Signals of good iteration:**
- Each turn builds on previous result
- Corrections are specific and final
- "Yes, now add X" pattern (progressive)
- Quick convergence on desired output

**Scoring:**
- 1-3: Circular patterns, high correction ratio
- 4-6: Some backtracking but generally forward
- 7-9: Mostly additive, quick convergence
- 10: Near-zero wasted turns

### 6. Error Recovery (1-10)

**Signals of poor recovery:**
- User repeats same failing request without modification
- No diagnosis attempted before requesting fix
- Abandons entire approach instead of adjusting
- "It doesn't work" without error details

**Signals of good recovery:**
- Provides error messages or symptoms
- Narrows scope when something fails
- Asks for diagnosis before requesting fix
- Tries alternative approach after first failure

**Scoring:**
- 1-3: Repeated failures, no adaptation
- 4-6: Eventually recovers but inefficiently
- 7-9: Good diagnostic instinct, quick recovery
- 10: Systematic debugging, first-try fixes

## Common Anti-Patterns Catalog

### The Wall of Text
User pastes 200+ lines of code with "fix this". No context about what's broken.
**Fix:** Paste only the relevant 10-20 lines + error message + expected behavior.

### The Kitchen Sink
Single prompt: "Add auth, database, API, and frontend for user management."
**Fix:** Break into 4 separate tasks, one per layer.

### The Mind Reader
"Make it better." Better how? Faster? Cleaner? More secure?
**Fix:** State the specific quality dimension and success criteria.

### The Copy-Paste Loop
User pastes same context in every message instead of using project files.
**Fix:** Put persistent context in CLAUDE.md or memory files.

### The Feature Creep
Session starts as a bug fix, grows into a rewrite. 50+ turns.
**Fix:** Set scope boundary at start. New ideas go to a backlog.

### The Tool Blindspot
Using bash `find` + `grep` instead of Glob/Grep tools.
Using Write for a 2-line change instead of Edit.
Not using agents for parallel research.
**Fix:** Review available tools periodically. Match tool to task.

### The Context Ping-Pong
User and AI exchange 10 messages clarifying requirements.
**Fix:** Use plan mode. Write spec first, then implement.

## Per-Tool Specific Guidance

### Claude Code
- Use CLAUDE.md for project-wide conventions
- Use memory for cross-session learnings
- Use plan mode for non-trivial features
- Leverage skills (slash commands) for repetitive workflows
- Use agents for parallel exploration

### Codex
- Leverage rollout files for session replay
- Use sandbox mode effectively for safe experimentation
- Configure model provider in config.toml for optimal routing

### Hermes
- Use system prompt customization for domain-specific behavior
- Leverage session metadata for debugging
- Use cron/session features for recurring tasks

### OpenClaw
- Leverage skills directory for workflow automation
- Monitor gateway logs for connectivity issues
