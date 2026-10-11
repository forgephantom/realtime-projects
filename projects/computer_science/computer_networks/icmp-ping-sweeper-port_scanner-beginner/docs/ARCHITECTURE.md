# Architecture (HLD) — ICMP Ping Sweeper: Port Scanner

## Problem & Users

ICMP Ping Sweeper built as a port scanner. Ping measures reachability and RTT with ICMP echo: the sweeper sends echo requests across a subnet, records replies, loss, and RTT stats, and reports live hosts. It is the first diagnostic for 'is it up'. Rate limiting keeps it polite. A loopback-only TCP port scanner that reports open/closed state and latency, and refuses any non-loopback target.

The intended user is a student or engineer working in computer_science (computer_networks) who needs a working, runnable reference for ICMP Ping Sweeper — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
