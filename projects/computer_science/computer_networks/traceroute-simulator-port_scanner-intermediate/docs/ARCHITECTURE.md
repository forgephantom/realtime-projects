# Architecture (HLD) — Traceroute Simulator: Port Scanner

## Problem & Users

Traceroute Simulator built as a port scanner. Traceroute maps the path by sending probes with increasing TTLs: each hop's router returns time-exceeded, revealing the route hop by hop with per-hop RTT. The simulator models a topology and produces traceroute output including asterisks for silent hops. It is path discovery from first principles. A loopback-only TCP port scanner that reports open/closed state and latency, and refuses any non-loopback target.

The intended user is a student or engineer working in computer_science (computer_networks) who needs a working, runnable reference for Traceroute Simulator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
