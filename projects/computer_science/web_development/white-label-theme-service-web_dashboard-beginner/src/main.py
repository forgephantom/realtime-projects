#!/usr/bin/env python3
"""White-Label Theme Service: Web Dashboard: a small web dashboard for White-Label Theme Service.

White-label products reskin per customer: the theme service resolves the tenant's brand (colors, logos, fonts, copy overrides), serves themed assets with caching, and falls back to defaults for missing keys. Theme validation keeps contrast accessible. It lets one codebase wear many brands.
Data idea: Resolves seeded tenant themes (complete, partial, missing) verifying fallback correctness and asset URLs.

Default run: binds 127.0.0.1 on an ephemeral port, fetches the rendered
dashboard page and the JSON metrics endpoint with urllib, prints a summary,
and shuts the server down cleanly. Pass --serve to keep it running.
"""

import argparse
import json
import random
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PARAMS = {'themes': 'per-tenant theme definitions', 'fallback': 'default theme for missing keys', 'cache': 'theme asset cache TTL'}


def metric_rows(seed, count):
    """Generate `count` deterministic synthetic metric rows."""
    rng = random.Random(seed)
    names = ["throughput", "error_rate", "latency_p99", "queue_depth",
             "cpu_pct", "mem_pct", "disk_io", "net_io"]
    units = ["req/s", "%", "ms", "ops/s"]
    rows = []
    for i in range(count):
        base = names[i % len(names)]
        rows.append({
            "name": "{}-{}".format(base, i // len(names) + 1),
            "value": round(rng.uniform(0.1, 99.9), 1),
            "unit": units[i % len(units)],
        })
    return rows


def render_page(seed, count):
    """Render the full dashboard HTML page for White-Label Theme Service."""
    body_rows = "".join(
        "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            r["name"], r["value"], r["unit"])
        for r in metric_rows(seed, count))
    return (
        "<!doctype html>\n<html>\n<head>\n"
        "<title>White-Label Theme Service: Web Dashboard</title>\n"
        '<meta http-equiv="refresh" content="30">\n'
        "</head>\n<body>\n"
        "<h1>White-Label Theme Service Dashboard</h1>\n"
        "<p>White-label products reskin per customer: the theme service resolves the tenant's brand (colors, logos, fonts, copy overrides), serves themed assets with caching, and falls back to defaults for missing keys. Theme validation keeps contrast accessible. It lets one codebase wear many brands.</p>\n"
        '<table border="1">\n'
        "<tr><th>Metric</th><th>Value</th><th>Unit</th></tr>\n"
        + body_rows +
        "</table>\n</body>\n</html>\n"
    )


class DashboardHandler(BaseHTTPRequestHandler):
    """Serve the dashboard page and a JSON metrics endpoint."""

    seed = 42
    metric_count = 8

    def log_message(self, *args):
        pass

    def _send(self, code, content_type, body):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/":
            self._send(200, "text/html; charset=utf-8",
                       render_page(self.seed, self.metric_count))
        elif self.path == "/api/metrics":
            self._send(200, "application/json",
                       json.dumps({"metrics": metric_rows(
                           self.seed, self.metric_count)}))
        else:
            self._send(404, "text/plain; charset=utf-8", "not found")


def start_server(port, seed, count):
    """Bind a ThreadingHTTPServer on 127.0.0.1 and serve it in a thread."""
    DashboardHandler.seed = seed
    DashboardHandler.metric_count = count
    server = ThreadingHTTPServer(("127.0.0.1", port), DashboardHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread, server.server_address[1]


def run_self_test(base_url, seed, count):
    """Fetch the page and the metrics endpoint; print what came back."""
    random.seed(seed)
    with urllib.request.urlopen(base_url + "/", timeout=5) as resp:
        page = resp.read().decode("utf-8")
        page_status = resp.status
    with urllib.request.urlopen(base_url + "/api/metrics",
                                timeout=5) as resp:
        metrics = json.loads(resp.read().decode("utf-8"))["metrics"]
        api_status = resp.status
    title_ok = "White-Label Theme Service: Web Dashboard" in page
    data_rows = page.count("<tr><td>")
    print("GET /            -> {}  title present: {}  data rows: {}".format(
        page_status, title_ok, data_rows))
    print("GET /api/metrics -> {}  metrics returned: {}".format(
        api_status, len(metrics)))
    print("Sample metrics:")
    for row in metrics[:5]:
        print("  {:<14} {:>7} {}".format(row["name"], row["value"],
                                        row["unit"]))
    ok = page_status == 200 and api_status == 200 and title_ok \
        and data_rows == count and len(metrics) == count
    print("SELF-TEST " + ("PASSED" if ok else "FAILED"))


def main():
    parser = argparse.ArgumentParser(
        description="White-Label Theme Service: Web Dashboard: web dashboard for White-Label Theme Service.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--port", type=int, default=0,
                        help="port to bind (0 = ephemeral)")
    parser.add_argument("--metrics", type=int,
                        default=PARAMS.get("metrics", 8),
                        help="number of metric rows on the dashboard")
    parser.add_argument("--serve", action="store_true",
                        help="keep the server running instead of self-testing")
    args = parser.parse_args()
    random.seed(args.seed)

    server, thread, actual_port = start_server(args.port, args.seed,
                                               args.metrics)
    base_url = "http://127.0.0.1:{}".format(actual_port)
    if args.serve:
        print("Serving White-Label Theme Service dashboard at {} (Ctrl-C to stop)".format(
            base_url))
        try:
            thread.join()
        except KeyboardInterrupt:
            pass
        finally:
            server.shutdown()
    else:
        run_self_test(base_url, args.seed, args.metrics)
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
