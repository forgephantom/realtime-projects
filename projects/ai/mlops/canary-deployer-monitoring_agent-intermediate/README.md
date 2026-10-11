# Canary Deployment Orchestrator: Monitoring Agent

**Domain:** ai | **Subdomain:** mlops | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Canary Deployment Orchestrator built as a Monitoring agent. Canary deployment shifts a slice of traffic to the new model and watches guardrail metrics before proceeding: error rate, latency, and key business metrics must stay within bounds. Automated analysis promotes or rolls back based on statistical comparison with the stable version. The orchestrator steps traffic percentages on seeded metric streams. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

**Core concept — Canary Deployment Orchestrator:** Canary deployment shifts a slice of traffic to the new model and watches guardrail metrics before proceeding: error rate, latency, and key business metrics must stay within bounds. Automated analysis promotes or rolls back based on statistical comparison with the stable version. The orchestrator steps traffic percentages on seeded metric streams.

**Why this matters in the real world:** Model platforms canary every production model update before full rollout.

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
cd projects/ai/mlops/canary-deployer-monitoring_agent-intermediate
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
