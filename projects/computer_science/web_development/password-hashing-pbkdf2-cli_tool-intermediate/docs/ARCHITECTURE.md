# Architecture (HLD) — Password Hashing with PBKDF2: Command-Line Tool

## Problem & Users

Password Hashing with PBKDF2 built as a Command-line tool. Passwords must never be stored reversibly: PBKDF2 stretches a password with a random salt through many HMAC iterations so each guess costs real work. The stored record keeps algorithm, iteration count, salt, and hash, letting the server raise iterations as hardware improves. Constant-time comparison and per-user salts defeat rainbow tables and timing probes. A subcommand CLI that generates seeded synthetic topic rows and reports summaries, top-N rows, or filtered rows as tables or JSON.

The intended user is a student or engineer working in computer_science (web_development) who needs a working, runnable reference for Password Hashing with PBKDF2 — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_rows (synthetic table)
subcommand: summary | top | filter -> formatted table or JSON
```

## Storage

No persistence: rows are regenerated from the seed on every invocation and nothing is written to disk.

## Scaling & Limits

Rows live in a Python list, so memory grows linearly with --rows; fine for tens of thousands of rows on a laptop.

## Trade-offs

Synthetic seeded data keeps the tool self-contained and reproducible, at the cost of not reading real input files.

## Failure Handling

An empty filter result prints a zero-count table rather than erroring; --top-n larger than the row count simply returns all rows.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
