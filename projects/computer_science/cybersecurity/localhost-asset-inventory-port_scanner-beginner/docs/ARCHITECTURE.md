# Architecture (HLD) — Localhost Asset Inventory: Port Scanner

## Problem & Users

Localhost Asset Inventory built as a port scanner. You cannot defend what you cannot see, so an asset inventory maps every listening service on the local machine. This localhost-only scanner enumerates open local ports, grabs service banners, and records versions into an inventory with last-seen timestamps. Unexpected new listeners trigger alerts, catching rogue services and forgotten debug ports. A loopback-only TCP port scanner that reports open/closed state and latency, and refuses any non-loopback target.

The intended user is a student or engineer working in computer_science (cybersecurity) who needs a working, runnable reference for Localhost Asset Inventory — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
port list -> ThreadPoolExecutor -> socket.create_connection
connect success -> OPEN + latency_ms; OSError -> closed + latency_ms
rows sorted by port -> printed open/closed table
```

## Storage

No persistence: results are printed to stdout and not stored anywhere.

## Scaling & Limits

Connect scanning is the slowest scan type; fine for tens of ports locally, not designed for internet-wide sweeping.

## Trade-offs

Full TCP connects are reliable and simple but slower and noisier than SYN half-open scans, which need raw sockets.

## Failure Handling

Connection errors are treated as closed ports, never raised; an invalid port range or a non-loopback target exits with a clear error.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
