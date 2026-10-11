# Architecture (HLD) — Storage Bucket Policy Auditor: Config Manager

## Problem & Users

Storage Bucket Policy Auditor built as a config manager. Public cloud storage buckets have caused some of the largest data breaches, usually from a policy that drifted open. The auditor evaluates bucket policies and ACLs, flagging public read or write, overly broad principals, and missing encryption defaults. It simulates policy changes before they are applied. A layered configuration manager that merges defaults, an INI snippet, environment variables, and CLI overrides with type checking and validation.

The intended user is a student or engineer working in computer_science (cybersecurity) who needs a working, runnable reference for Storage Bucket Policy Auditor — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
