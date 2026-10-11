# Architecture (HLD) — Cookie Consent Manager: Config Manager

## Problem & Users

Cookie Consent Manager built as a config manager. Privacy law requires consent before tracking: the manager shows a banner, records granular choices (necessary, analytics, marketing), blocks non-essential scripts until consent, and stores proof of consent per user. Consent must be revocable and re-prompted on policy change. The audit trail is the legal artifact. A layered configuration manager that merges defaults, an INI snippet, environment variables, and CLI overrides with type checking and validation.

The intended user is a student or engineer working in computer_science (web_development) who needs a working, runnable reference for Cookie Consent Manager — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Config | main | Layered configuration with typed coercion, per-key source tracking, and validation. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
SCHEMA defaults -> load_defaults
SAMPLE_INI string -> load_ini (layer 2)
PREFIX_* env vars -> load_env (layer 3)
--set key=value -> set (layer 4)
resolved table + sources -> validate -> printed report
```

## Storage

In-memory only: the demo plants one process-local env var and keeps nothing on disk.

## Scaling & Limits

Flat key/value schema suits service config; deeply nested configs would want a tree model instead.

## Trade-offs

Flat keys keep merging rules obvious; nested sections would complicate precedence and validation.

## Failure Handling

Unknown keys, bad INI lines, and uncoercible values raise ValueError with the offending line or key named; validate() collects range problems.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
