#!/usr/bin/env python3
"""Scope 1-2-3 Emissions Ledger: Rest Api Service: a tiny REST API for Scope 1-2-3 Emissions Ledger.

Corporate carbon accounting splits emissions into scope 1 (direct), scope 2 (purchased energy), and scope 3 (value chain) following the GHG Protocol. The ledger ingests activity records, applies emission factors, and rolls everything into an auditable inventory.
Data idea: Seeded RNG generates company activity records across all three scopes for the ledger to compile.

Default run: binds 127.0.0.1 on an ephemeral port, exercises every endpoint
with urllib, prints the results, and shuts the server down cleanly.
Pass --serve to keep the server running instead.
"""

import argparse
import json
import random
import threading
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PARAMS = {'activities': 'list of activity records', 'factors': 'emission factor table'}
TOPIC_SLUG = "scope-emissions-ledger-rest_api-beginner"


def seed_records(seed, count):
    """Generate `count` deterministic synthetic records for Scope 1-2-3 Emissions Ledger."""
    rng = random.Random(seed)
    records = []
    for i in range(count):
        records.append({
            "id": i + 1,
            "name": "{}-{:03d}".format(TOPIC_SLUG, i + 1),
            "value": round(rng.uniform(1.0, 100.0), 2),
            "active": rng.random() > 0.2,
        })
    return records


class Store:
    """In-memory record collection backing the Scope 1-2-3 Emissions Ledger API."""

    def __init__(self, seed, count):
        self.records = seed_records(seed, count)

    def list_records(self):
        """Return a copy of all stored records."""
        return list(self.records)

    def add_record(self, payload):
        """Append a record built from the posted JSON payload."""
        record = {"id": max((r["id"] for r in self.records), default=0) + 1}
        if isinstance(payload, dict):
            record.update(payload)
        self.records.append(record)
        return record

    def stats(self):
        """Aggregate record count, mean value, and active-record count."""
        values = [r["value"] for r in self.records
                  if isinstance(r.get("value"), (int, float))]
        return {
            "count": len(self.records),
            "mean_value": round(sum(values) / len(values), 2) if values else 0.0,
            "active": sum(1 for r in self.records if r.get("active")),
        }


class ApiHandler(BaseHTTPRequestHandler):
    """Route HTTP requests to the shared Store. Bound to 127.0.0.1 only."""

    store = None

    def log_message(self, *args):
        pass

    def _send_json(self, code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}

    def do_GET(self):
        if self.path == "/health":
            self._send_json(200, {"status": "ok", "topic": "Scope 1-2-3 Emissions Ledger"})
        elif self.path == "/items":
            self._send_json(200, {"items": self.store.list_records()})
        elif self.path == "/stats":
            self._send_json(200, self.store.stats())
        else:
            self._send_json(404, {"error": "not found: " + self.path})

    def do_POST(self):
        if self.path == "/items":
            self._send_json(201, self.store.add_record(self._read_json()))
        else:
            self._send_json(404, {"error": "not found: " + self.path})


def start_server(port, seed, count):
    """Bind a ThreadingHTTPServer on 127.0.0.1 and serve it in a thread."""
    ApiHandler.store = Store(seed, count)
    server = ThreadingHTTPServer(("127.0.0.1", port), ApiHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread, server.server_address[1]


def _request(base_url, method, path, payload=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(base_url + path, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8") or "{}"
        return exc.code, json.loads(body)


def run_self_test(base_url, seed):
    """Exercise every endpoint with urllib and print a results table."""
    random.seed(seed)
    print("Self-test against {}".format(base_url))
    print("{:<6} {:<10} {:<4} {}".format("METHOD", "PATH", "CODE", "SUMMARY"))
    print("-" * 60)

    code, health = _request(base_url, "GET", "/health")
    print("{:<6} {:<10} {:<4} status={}".format(
        "GET", "/health", code, health.get("status")))

    code, items = _request(base_url, "GET", "/items")
    rows = items.get("items", [])
    print("{:<6} {:<10} {:<4} {} records".format(
        "GET", "/items", code, len(rows)))

    code, created = _request(base_url, "POST", "/items",
                             {"name": TOPIC_SLUG + "-new",
                              "value": 42.5, "active": True})
    print("{:<6} {:<10} {:<4} id={}".format(
        "POST", "/items", code, created.get("id")))

    code, stats = _request(base_url, "GET", "/stats")
    print("{:<6} {:<10} {:<4} count={} mean={} active={}".format(
        "GET", "/stats", code, stats.get("count"),
        stats.get("mean_value"), stats.get("active")))

    code, missing = _request(base_url, "GET", "/nope")
    print("{:<6} {:<10} {:<4} {}".format(
        "GET", "/nope", code, missing.get("error")))

    ok = (health.get("status") == "ok"
          and created.get("id") is not None and code == 404)
    print("-" * 60)
    print("SELF-TEST " + ("PASSED" if ok else "FAILED"))


def main():
    parser = argparse.ArgumentParser(
        description="Scope 1-2-3 Emissions Ledger: Rest Api Service: REST API for Scope 1-2-3 Emissions Ledger.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--port", type=int, default=0,
                        help="port to bind (0 = ephemeral)")
    parser.add_argument("--records", type=int,
                        default=PARAMS.get("records", 25),
                        help="initial synthetic records")
    parser.add_argument("--serve", action="store_true",
                        help="keep the server running instead of self-testing")
    args = parser.parse_args()
    random.seed(args.seed)

    server, thread, actual_port = start_server(args.port, args.seed,
                                               args.records)
    base_url = "http://127.0.0.1:{}".format(actual_port)
    if args.serve:
        print("Serving Scope 1-2-3 Emissions Ledger API at {} (Ctrl-C to stop)".format(
            base_url))
        try:
            thread.join()
        except KeyboardInterrupt:
            pass
        finally:
            server.shutdown()
    else:
        run_self_test(base_url, args.seed)
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
