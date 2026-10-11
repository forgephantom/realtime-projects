# Token-Bucket Rate Limit Middleware: Monitoring Agent

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Token-Bucket Rate Limit Middleware built as a Monitoring agent. Rate limiting protects APIs from abuse: a token bucket refills at a fixed rate up to a capacity, and each request spends a token, so bursts are allowed but sustained rates are capped. The middleware keys buckets per API key or IP, returns 429 with Retry-After when empty, and exposes limit headers. Distributed deployments share bucket state so limits hold across instances. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

**Core concept — Token-Bucket Rate Limit Middleware:** Rate limiting protects APIs from abuse: a token bucket refills at a fixed rate up to a capacity, and each request spends a token, so bursts are allowed but sustained rates are capped. The middleware keys buckets per API key or IP, returns 429 with Retry-After when empty, and exposes limit headers. Distributed deployments share bucket state so limits hold across instances.

**Why this matters in the real world:** API gateways (Kong, AWS API Gateway), GitHub, and Twitter all rate-limit with token or leaky bucket variants.

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
cd projects/computer_science/web_development/token-bucket-rate-limiter-monitoring_agent-intermediate
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
