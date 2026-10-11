# Design (LLD) — Attachment Risk Scorer: Log Analyzer

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
| generate_log | generate_log(seed, lines) | Generate synthetic topic log lines in memory. |
| parse_line | parse_line(line) | Parse one log line; return a dict or None if unparseable. |
| analyze | analyze(entries) | Aggregate level counts, service counts, and top error messages. |
| print_report | print_report(report, total) | Print the analysis report. |
| main | main() | Parse args, generate, parse, and report. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Attachment Risk Scorer:

| Parameter | Meaning |
|---|---|
| risky_types | extensions scored as dangerous |
| macro_weight | risk added by macro indicators |
| double_ext_weight | risk of invoice.pdf.exe tricks |
| size_anomaly | unexpected sizes for the claimed type |

## Algorithm & Complexity

The core of this project is Regex parsing with Counter aggregation.

- **Time complexity:** O(n) to generate, parse, and aggregate n lines
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/cybersecurity/attachment-risk-scorer-log_analyzer-beginner
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
