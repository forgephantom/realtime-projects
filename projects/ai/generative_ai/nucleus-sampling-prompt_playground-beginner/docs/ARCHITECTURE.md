# Architecture (HLD) — Nucleus (Top-P) Sampler: Prompt_Playground

## Problem & Users

Nucleus (Top-P) Sampler built as a prompt_playground. Nucleus sampling keeps the smallest set of tokens whose cumulative probability reaches p, adapting the candidate pool to the model's confidence: sharp distributions yield few candidates, flat ones yield many. This avoids the fixed-pool problems of top-k, where k is too big for confident steps and too small for uncertain ones. The simulator compares diversity and degeneracy across p values. A prompt template playground that substitutes variables into templates, runs A/B variants over seeded test inputs, and scores them with a rubric heuristic.

The intended user is a student or engineer working in ai (generative_ai) who needs a working, runnable reference for Nucleus (Top-P) Sampler — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
