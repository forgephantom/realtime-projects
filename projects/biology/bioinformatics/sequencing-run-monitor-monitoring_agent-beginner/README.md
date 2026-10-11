# Sequencing Run Monitor Agent: Monitoring Agent

**Domain:** biology | **Subdomain:** bioinformatics | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Sequencing Run Monitor Agent built as a Monitoring agent. Sequencing run monitors tail instrument log streams, tracking cluster density, quality-score trends, and error rates per cycle to catch failing runs early. The agent parses synthetic log lines, maintains rolling statistics, and raises alerts when metrics cross thresholds. It emits a run-health summary report. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

**Core concept — Sequencing Run Monitor Agent:** Sequencing run monitors tail instrument log streams, tracking cluster density, quality-score trends, and error rates per cycle to catch failing runs early. The agent parses synthetic log lines, maintains rolling statistics, and raises alerts when metrics cross thresholds. It emits a run-health summary report.

**Why this matters in the real world:** Run monitoring (Illumina SAV style) protects expensive sequencing runs in core facilities.

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
cd projects/biology/bioinformatics/sequencing-run-monitor-monitoring_agent-beginner
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
