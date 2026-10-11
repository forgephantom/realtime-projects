# Triage Escalation Monitor: Monitoring Agent

**Domain:** healthcare | **Subdomain:** telemedicine | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Triage Escalation Monitor built as a Monitoring agent. Escalation monitoring watches triage queues for patients whose severity, wait time, or deteriorating inputs cross escalation thresholds, re-prioritizing them automatically. Audit trails record every escalation decision for review. Synthetic triage streams with planted escalation events verify the monitor. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

**Core concept — Triage Escalation Monitor:** Escalation monitoring watches triage queues for patients whose severity, wait time, or deteriorating inputs cross escalation thresholds, re-prioritizing them automatically. Audit trails record every escalation decision for review. Synthetic triage streams with planted escalation events verify the monitor.

**Why this matters in the real world:** Escalation monitors keep remote triage queues safe under load.

---

## Features

- **Monitor**: Samples metrics, evaluates thresholds, and collects alerts.
- `read_metrics` (`read_metrics(rng, cycle)`): Sample one synthetic topic metric reading.
- `check_thresholds` (`check_thresholds(reading, thresholds)`): Return a list of alert strings for readings over threshold.
- `Monitor.run` (`Monitor.run(self, cycles, interval)`): Sample `cycles` readings, print them, return alert count.
- `main` (`main()`): Parse args and run the monitor.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Periodic sampling with static threshold evaluation. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(cycles) total; O(1) per sample. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/healthcare/telemedicine/triage-escalation-monitor-monitoring_agent-advanced
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

One line per cycle (cpu, memory, latency) with ALERT lines for threshold breaches, plus a cycle/alert summary.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
