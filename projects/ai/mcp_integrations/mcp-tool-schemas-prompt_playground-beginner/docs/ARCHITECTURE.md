# Architecture (HLD) — MCP Tool Schema Designer: Prompt_Playground

## Problem & Users

MCP Tool Schema Designer built as a prompt_playground. Tool schemas are the contract between model and tool: JSON Schema types, required fields, enums, and descriptions guide the model to produce valid arguments. Overly loose schemas invite bad calls; overly strict ones reject valid ones. The designer validates seeded schemas against sample calls and scores schema quality. A prompt template playground that substitutes variables into templates, runs A/B variants over seeded test inputs, and scores them with a rubric heuristic.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Tool Schema Designer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
template + variables -> render_template -> prompt
prompt -> stub_generate (hash-keyed canned content) -> response
response + rubric -> score_response -> 0..1
variants x inputs -> run_variant -> print_table comparison
```

## Storage

No persistence: inputs, prompts, and scores are regenerated from the seed each run.

## Scaling & Limits

The loop is single-threaded and suits hundreds of inputs; thousands would want batched or async model calls.

## Trade-offs

The stub model makes the harness fully offline and deterministic, but real model behavior needs a live backend.

## Failure Handling

Missing variables are left as literal {placeholders} in the prompt so a typo shows up visibly instead of crashing.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
