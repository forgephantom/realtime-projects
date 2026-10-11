# Architecture (HLD) — Code Fixing Agent: Agent_Loop_Sim

## Problem & Users

Code Fixing Agent built as a agent_loop_sim. A code-fixing agent reproduces a reported bug in a sandbox, proposes a patch, runs the test suite, and iterates until tests pass. Regression checks make sure the fix does not break unrelated tests. The simulation plants known bugs and measures fix rate within the attempt budget. A ReAct-style agent loop simulator that cycles Thought, Action, and Observation over a calculator and a lookup table until it reaches a final answer.

The intended user is a student or engineer working in ai (ai_agents) who needs a working, runnable reference for Code Fixing Agent — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Agent | main | ReAct agent: think picks a tool, act calls it, observe formats the result, run loops to a final answer. |
| LookupTable | main | Seeded key-value table exposed as a lookup tool. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
question -> Agent.think -> (thought, tool, arg)
(tool, arg) -> Agent.act -> tool result
result -> Agent.observe -> observation -> think again
observation with result -> final answer (or step limit)
```

## Storage

No persistence: the lookup table is rebuilt from the seed on every run and traces are printed only.

## Scaling & Limits

The rule-based thinker suits a handful of tools; real agents would replace it with a planner or model call.

## Trade-offs

Deterministic rules make the loop fully debuggable, but they cannot handle questions outside the two tool patterns.

## Failure Handling

Unknown questions get an honest 'I do not know' final answer, and the loop always stops at the step limit.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
