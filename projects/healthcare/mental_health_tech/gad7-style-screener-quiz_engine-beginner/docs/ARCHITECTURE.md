# Architecture (HLD) — GAD-7-Style Self-Assessment Scorer: Quiz Engine

## Problem & Users

GAD-7-Style Self-Assessment Scorer built as a quiz engine. Anxiety screening questionnaires follow the same structure as depression screens: frequency-rated items summed into a total with severity bands. The tool is strictly educational, showing how scoring works on synthetic data while making clear that results are not a diagnosis. Disclaimer text accompanies every result screen. Includes prominent disclaimer text that the tool is for wellness self-tracking and screening only, never a diagnosis, and encourages consulting a professional. A multiple-choice quiz engine that shuffles options deterministically, scores auto-answered or interactive sessions, and assigns letter grades.

The intended user is a student or engineer working in healthcare (mental_health_tech) who needs a working, runnable reference for GAD-7-Style Self-Assessment Scorer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Question | main | One multiple-choice question: prompt, options, and the correct index. |
| Quiz | main | Holds questions and runs auto-answered or interactive quiz sessions with scoring. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
question bank -> seeded option shuffle -> Quiz
Quiz.run_auto -> simulated answers -> per-question correct/wrong
results -> score/total -> grade -> printed breakdown
```

## Storage

In-memory only: questions, answers, and scores exist only for the run and are printed, not saved.

## Scaling & Limits

In-memory question bank; fine for hundreds of questions, no database or multi-user session support.

## Trade-offs

A fixed built-in bank keeps the demo self-contained; a real quiz product would load questions from files or a database.

## Failure Handling

An out-of-range answer index raises ValueError at construction; interactive mode re-prompts on invalid input instead of crashing.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
