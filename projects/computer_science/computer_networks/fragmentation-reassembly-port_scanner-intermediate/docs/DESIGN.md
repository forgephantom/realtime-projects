# Design (LLD) — IP Fragmentation and Reassembly: Port Scanner

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
| scan_port | scan_port(host: str, port: int, timeout: float = 0.5) -> tuple | Attempt one TCP connect; return (is_open, latency_ms). |
| scan_ports | scan_ports(host: str, ports: list, timeout: float = 0.5, workers: int = 8) -> list | Scan ports in parallel; return dicts sorted by port number. |
| check_target | check_target(host: str) -> None | Exit with an error unless the host is a loopback address. |
| run_self_test | run_self_test(timeout: float, workers: int) -> int | Scan around a dummy listener; exactly one port must be open. |
| run_scan | run_scan(host: str, ports: list, timeout: float, workers: int) -> int | Scan an explicit port list on a loopback target and print a table. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Self-test by default; explicit scan with --ports. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for IP Fragmentation and Reassembly:

| Parameter | Meaning |
|---|---|
| mtu | link MTU |
| datagram | original datagram size |
| overlap | overlapping-fragment attack sim |

## Algorithm & Complexity

The core of this project is Parallel TCP connect scan over a loopback target.

- **Time complexity:** O(p) connects over p ports, parallelized across worker threads
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/computer_networks/fragmentation-reassembly-port_scanner-intermediate
python3 src/main.py --help
python3 src/main.py
```
--ports scans an explicit list; --target must stay a loopback address; --timeout and --workers tune the scan.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
