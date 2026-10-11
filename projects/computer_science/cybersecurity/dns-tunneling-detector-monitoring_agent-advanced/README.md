# DNS Tunneling Detector: Monitoring Agent

**Domain:** computer_science | **Subdomain:** cybersecurity | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

DNS Tunneling Detector built as a Monitoring agent. DNS tunneling smuggles data out of a network by encoding it in subdomain labels of DNS queries, abusing a protocol that firewalls almost always allow. The detector scores queries on label entropy, query length, request frequency, and the rarity of the queried domain, because tunneled traffic looks random and chatty compared with human browsing. High-scoring domains get quarantined for analyst review. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

**Core concept — DNS Tunneling Detector:** DNS tunneling smuggles data out of a network by encoding it in subdomain labels of DNS queries, abusing a protocol that firewalls almost always allow. The detector scores queries on label entropy, query length, request frequency, and the rarity of the queried domain, because tunneled traffic looks random and chatty compared with human browsing. High-scoring domains get quarantined for analyst review.

**Why this matters in the real world:** Used by SOC analysts and DNS firewall vendors to catch data exfiltration over DNS.

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
cd projects/computer_science/cybersecurity/dns-tunneling-detector-monitoring_agent-advanced
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
