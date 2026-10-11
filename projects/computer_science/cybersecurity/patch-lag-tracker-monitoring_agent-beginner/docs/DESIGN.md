# Design (LLD) — Patch Lag Tracker: Monitoring Agent

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Monitor | Samples metrics, evaluates thresholds, and collects alerts. |

## Functions

| Function | Signature | Description |
|---|---|---|
| read_metrics | read_metrics(rng, cycle) | Sample one synthetic topic metric reading. |
| check_thresholds | check_thresholds(reading, thresholds) | Return a list of alert strings for readings over threshold. |
| Monitor.run | Monitor.run(self, cycles, interval) | Sample `cycles` readings, print them, return alert count. |
| main | main() | Parse args and run the monitor. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Patch Lag Tracker:

| Parameter | Meaning |
|---|---|
| sla_days | allowed lag per severity tier |
| severity_weights | criticality multiplier per CVE rating |
| scan_interval_days | how often patch state is refreshed |
| exclude_hosts | decommissioned systems skipped |

## Algorithm & Complexity

The core of this project is Periodic sampling with static threshold evaluation.

- **Time complexity:** O(cycles) total; O(1) per sample
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/cybersecurity/patch-lag-tracker-monitoring_agent-beginner
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
