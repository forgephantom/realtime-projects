#!/usr/bin/env python3
"""Localhost Asset Inventory: Port Scanner.

You cannot defend what you cannot see, so an asset inventory maps every listening service on the local machine. This localhost-only scanner enumerates open local ports, grabs service banners, and records versions into an inventory with last-seen timestamps. Unexpected new listeners trigger alerts, catching rogue services and forgotten debug ports.

Demo dataset idea: A seeded RNG simulates localhost port states with services appearing and disappearing..
"""

import argparse
import concurrent.futures
import random
import socket
import sys
import time

SLUG = "localhost-asset-inventory-port_scanner-beginner"
PARAMS = {'scan_ports': 'local port ranges inventoried', 'banner_grab': 'whether service banners are captured', 'alert_on_new': 'whether new listeners raise alerts', 'rescan_interval_minutes': 'inventory refresh cadence'}
LOOPBACK = {"127.0.0.1", "localhost", "::1"}  # the only legal scan targets


def scan_port(host: str, port: int, timeout: float = 0.5) -> tuple:
    """Attempt one TCP connect; return (is_open, latency_ms)."""
    start = time.perf_counter()
    try:
        conn = socket.create_connection((host, port), timeout=timeout)
    except OSError:
        return (False, (time.perf_counter() - start) * 1000.0)
    conn.close()
    return (True, (time.perf_counter() - start) * 1000.0)


def scan_ports(host: str, ports: list, timeout: float = 0.5, workers: int = 8) -> list:
    """Scan ports in parallel; return dicts sorted by port number."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        future_to_port = {pool.submit(scan_port, host, p, timeout): p for p in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            is_open, latency_ms = future.result()
            results.append({"port": future_to_port[future],
                            "open": is_open,
                            "latency_ms": latency_ms})
    return sorted(results, key=lambda row: row["port"])


def check_target(host: str) -> None:
    """Refuse anything that is not the loopback interface."""
    if host not in LOOPBACK:
        print("error: refusing to scan non-loopback target %r; "
              "this tool only scans 127.0.0.1." % host, file=sys.stderr)
        raise SystemExit(2)


def _dummy_listener():
    """Open a throwaway listening socket on an ephemeral loopback port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 0))
    sock.listen(1)
    return sock, sock.getsockname()[1]


def run_self_test(timeout: float, workers: int) -> int:
    """Scan a tiny range around a dummy listener: exactly one port must be open."""
    listener, open_port = _dummy_listener()
    ports = [p for p in (open_port - 1, open_port, open_port + 1) if 1 <= p <= 65535]
    ports += [9, 59999]  # almost certainly closed on loopback
    try:
        results = scan_ports("127.0.0.1", ports, timeout=timeout, workers=workers)
    finally:
        listener.close()

    print("Localhost Asset Inventory: Port Scanner  (topic: Localhost Asset Inventory)")
    print("Self-test: scanning 127.0.0.1 around a dummy listener on port %d" % open_port)
    print("%6s %-6s %10s" % ("port", "state", "latency_ms"))
    found_open = 0
    for row in results:
        state = "OPEN" if row["open"] else "closed"
        found_open += 1 if row["open"] else 0
        print("%6d %-6s %10.1f" % (row["port"], state, row["latency_ms"]))
    ok = found_open == 1 and any(r["port"] == open_port and r["open"] for r in results)
    print("\nSelf-test: %s (expected exactly the dummy port %d open)" % (
        "PASS" if ok else "FAIL", open_port))
    return 0 if ok else 1


def run_scan(host: str, ports: list, timeout: float, workers: int) -> int:
    """Scan an explicit port list on a loopback target and print a table."""
    check_target(host)
    results = scan_ports(host, ports, timeout=timeout, workers=workers)
    print("Localhost Asset Inventory: Port Scanner  (topic: Localhost Asset Inventory)")
    print("Scanning %s" % host)
    print("%6s %-6s %10s" % ("port", "state", "latency_ms"))
    for row in results:
        print("%6d %-6s %10.1f" % (
            row["port"], "OPEN" if row["open"] else "closed", row["latency_ms"]))
    n_open = sum(1 for row in results if row["open"])
    print("\n%d of %d ports open." % (n_open, len(results)))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Localhost Asset Inventory: Port Scanner: You cannot defend what you cannot see, so an asset inventory maps every listening service on the local machine. This localhost-only scanner enumerates open local ports, grabs service banners, and records versions into an inventory with last-seen timestamps. Unexpected new listeners trigger alerts, catching rogue services and forgotten debug ports."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed (default: 42).")
    parser.add_argument("--target", type=str, default="127.0.0.1",
                        help="Scan target; only loopback addresses are allowed.")
    parser.add_argument("--ports", type=str, default=None,
                        help="Comma-separated ports to scan (default: self-test around a dummy listener).")
    parser.add_argument("--timeout", type=float, default=0.5,
                        help="Per-port connect timeout in seconds (default: 0.5).")
    parser.add_argument("--workers", type=int, default=8,
                        help="Parallel scan threads (default: 8).")
    return parser


def main(argv=None) -> int:
    """Entry point: self-test by default, explicit scan with --ports."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    if args.ports:
        ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]
        return run_scan(args.target, ports, args.timeout, args.workers)
    check_target(args.target)
    return run_self_test(args.timeout, args.workers)


if __name__ == "__main__":
    raise SystemExit(main())
