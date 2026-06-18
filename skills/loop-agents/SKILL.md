---
name: loop-agents
description: Design an agentic loop orchestration or multi-agent topology for a given task. Use when the user asks to "design a loop agent", "create an agent workflow", "orchestrate agents", or needs a structured plan for how agents should collaborate, loop, and handle feedback to achieve a complex goal.
---

# Loop Agent Designer

Design a structured, framework-agnostic orchestration plan for agent workflows. Do not generate code by default. Output a complete design document detailing the agent topology, responsibilities, and loop control mechanisms.

## 0. Requirement Extraction

Analyze the user's request to extract:
- **Task Goal**: What is the ultimate objective?
- **Inputs/Outputs**: What data goes in, and what artifact comes out?
- **Constraints**: Are there time, cost, or tool limitations?
- **Existing Infrastructure**: Are there any existing tools or systems to integrate with?

If the information is insufficient to determine the complexity, ask exactly ONE clarifying question. Do not guess.

## 1. Task Decomposition

Break down the main goal into atomic responsibilities.
- Identify which steps must be sequential, which can run in parallel, and which operate independently.
- Note any steps that require human-in-the-loop intervention or approval.

## 2. Topology Recommendation

Recommend the most appropriate orchestration pattern based on the task complexity:
- **Single-step task**: No loop needed. State clearly that a single prompt is sufficient.
- **Multi-step linear process**: Sequential Pipeline (A → B → C).
- **Independent subtasks**: Parallel Execution (Fan-Out/Fan-In).
- **Dynamic scheduling needed**: Hierarchical (Supervisor + Workers).
- **Expertise switching based on context**: Handoff (Routing between specialized agents).
- **Iterative refinement**: Single-Agent Reflection Loop (Reason → Act → Observe → Reflect → Repeat).

Provide a one-sentence justification for the chosen topology.

## 3. Agent Specifications

For each agent in the chosen topology, define:
- **Role & Responsibility**: A one-sentence description of what the agent does.
- **Input Contract**: What exact data or state the agent expects to receive.
- **Output Contract**: What exact data or artifact the agent promises to deliver.
- **Required Tools/Capabilities**: Tools needed (e.g., web search, code execution, database access).
- **Activation Condition**: When does this agent start working?

## 4. Loop Control Design (Core)

Design the mechanisms that govern the loops and prevent infinite execution. Define:
- **Convergence Condition**: How do we know the task is "done"? (e.g., quality threshold met, external system confirmation, max attempts reached, self-evaluation passing).
- **Feedback Collection**: What information is gathered in each iteration? (e.g., tool errors, user feedback, environmental state).
- **Iteration Strategy**: How does the feedback influence the next loop? (e.g., targeted refinement vs. complete restart).
- **Limits & Fallbacks**: Define the maximum iteration count. Specify what happens if a tool continuously fails, outputs remain subpar, or a loop limit is hit (e.g., escalate to human, degrade gracefully).

## 5. Data Flow Diagram

Provide a text-based (ASCII or Mermaid) diagram illustrating the flow of information between the user, agents, and feedback loops.

## 6. Output Delivery

Present the final design as a structured document encompassing Steps 0 through 5. Format cleanly. Do not output code unless explicitly requested by the user after the design is approved.
