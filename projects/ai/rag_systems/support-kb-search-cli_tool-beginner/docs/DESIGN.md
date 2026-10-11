# Design (LLD) — Support Knowledge Base Search: Command-Line Tool

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| generate_rows | generate_rows(seed, count) | Generate deterministic synthetic topic rows. |
| cmd_summary | cmd_summary(rows, args) | Print per-category counts and value statistics. |
| cmd_top | cmd_top(rows, args) | Print the top-N rows by value. |
| cmd_filter | cmd_filter(rows, args) | Print rows whose value is at least --min-value. |
| main | main() | Parse args and dispatch to the chosen subcommand. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Support Knowledge Base Search:

| Parameter | Meaning |
|---|---|
| article_count | help articles indexed |
| filters | metadata filters applied |
| top_k | results shown per query |

## Algorithm & Complexity

The core of this project is Deterministic synthetic rows + subcommand dispatch.

- **Time complexity:** O(n) to generate rows; O(n log n) for top-N sort
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/rag_systems/support-kb-search-cli_tool-beginner
python3 src/main.py --help
python3 src/main.py
```
Try `python3 src/main.py top --top-n 3`, `python3 src/main.py filter --min-value 900`, or add --json to any command.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
