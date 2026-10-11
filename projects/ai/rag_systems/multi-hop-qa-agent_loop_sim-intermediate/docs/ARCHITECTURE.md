# Architecture (HLD) — Multi-Hop Question Answering: Agent_Loop_Sim

## Problem & Users

Multi-Hop Question Answering built as a agent_loop_sim. Multi-hop question answering chains multiple retrieval rounds, where each round's findings shape the next query. Bridge questions require combining facts from separate documents that share an entity. The simulation tracks hop accuracy and where chains break. A ReAct-style agent loop simulator that cycles Thought, Action, and Observation over a calculator and a lookup table until it reaches a final answer.

The intended user is a student or engineer working in ai (rag_systems) who needs a working, runnable reference for Multi-Hop Question Answering — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
