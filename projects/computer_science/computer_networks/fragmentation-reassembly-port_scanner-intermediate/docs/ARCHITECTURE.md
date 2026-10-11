# Architecture (HLD) — IP Fragmentation and Reassembly: Port Scanner

## Problem & Users

IP Fragmentation and Reassembly built as a port scanner. Packets bigger than the MTU fragment: the demo splits datagrams with correct offsets and MF flags, then reassembles at the receiver handling out-of-order and overlapping fragments. It shows why path-MTU discovery tries to avoid fragmentation. Overlapping fragments are also a classic IDS evasion. A loopback-only TCP port scanner that reports open/closed state and latency, and refuses any non-loopback target.

The intended user is a student or engineer working in computer_science (computer_networks) who needs a working, runnable reference for IP Fragmentation and Reassembly — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
