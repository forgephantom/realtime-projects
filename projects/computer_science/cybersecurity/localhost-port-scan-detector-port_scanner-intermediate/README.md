# Localhost Port Scan Detector: Port Scanner

**Domain:** computer_science | **Subdomain:** cybersecurity | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Localhost Port Scan Detector built as a port scanner. Port scans probe many ports to map which services are listening, and the scan itself is visible as a burst of short connections across a port range. This localhost-only detector binds no remote targets: it watches connection attempts against the local machine, counts distinct ports touched per source within a window, and classifies the pattern as a horizontal scan, a vertical scan, or normal churn. It is strictly defensive and never scans anyone else. A loopback-only TCP port scanner that reports open/closed state and latency, and refuses any non-loopback target.

**Core concept — Localhost Port Scan Detector:** Port scans probe many ports to map which services are listening, and the scan itself is visible as a burst of short connections across a port range. This localhost-only detector binds no remote targets: it watches connection attempts against the local machine, counts distinct ports touched per source within a window, and classifies the pattern as a horizontal scan, a vertical scan, or normal churn. It is strictly defensive and never scans anyone else.

**Why this matters in the real world:** Used by host-based intrusion detection on workstations and servers to spot reconnaissance.

---

## Features

- `scan_port` (`scan_port(host: str, port: int, timeout: float = 0.5) -> tuple`): Attempt one TCP connect; return (is_open, latency_ms).
- `scan_ports` (`scan_ports(host: str, ports: list, timeout: float = 0.5, workers: int = 8) -> list`): Scan ports in parallel; return dicts sorted by port number.
- `check_target` (`check_target(host: str) -> None`): Exit with an error unless the host is a loopback address.
- `run_self_test` (`run_self_test(timeout: float, workers: int) -> int`): Scan around a dummy listener; exactly one port must be open.
- `run_scan` (`run_scan(host: str, ports: list, timeout: float, workers: int) -> int`): Scan an explicit port list on a loopback target and print a table.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Self-test by default; explicit scan with --ports.

---

## Tech Stack

Python 3.8+, stdlib: argparse, concurrent.futures, random, socket, sys, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Parallel TCP connect scan over a loopback target. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(p) connects over p ports, parallelized across worker threads. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/cybersecurity/localhost-port-scan-detector-port_scanner-intermediate
python3 src/main.py --help
python3 src/main.py
```
--ports scans an explicit list; --target must stay a loopback address; --timeout and --workers tune the scan.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints an open/closed table with per-port latency in ms, plus a PASS/FAIL self-test verdict in default mode.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
