#!/usr/bin/env python3
"""DNS Load Distribution: Api Client Sim.

DNS spreads load by returning different address orderings (round-robin) or geo-aware answers: the demo rotates A records per query and measures distribution, plus weighted variants. It is the oldest load-balancing trick on the internet. Short TTLs make it adaptive.

Demo dataset idea: Queries seeded zones repeatedly and verifies even distribution across addresses..
"""

import argparse
import random
import time

SLUG = "dns-load-distribution-api_client_sim-intermediate"
PARAMS = {'records': 'address pool', 'rotate': 'round-robin vs weighted', 'ttl': 'rotation TTL'}


class APIError(Exception):
    """Raised when a simulated request fails after all retries."""

    def __init__(self, status: int, body: dict):
        super().__init__("request failed with status %d: %r" % (status, body))
        self.status = status
        self.body = body


class FakeAPI:
    """An in-process fake HTTP-like API: no sockets, no network.

    Serves GET /items with page/per_page pagination and GET /items/{id}.
    The first `fail_first` calls return a simulated 500 so the client demo
    can show its retry logic working.
    """

    def __init__(self, seed: int, num_items: int = 12, fail_first: int = 1):
        rng = random.Random(seed)
        self.items = [{"id": i + 1,
                       "name": "%s-item-%02d" % (SLUG, i + 1),
                       "value": rng.randint(1, 999)} for i in range(num_items)]
        self._failures_left = fail_first
        self.calls = 0

    def handle(self, method: str, path: str, params: dict) -> tuple:
        """Process one request; return (status_code, body_dict)."""
        self.calls += 1
        if self._failures_left > 0:
            self._failures_left -= 1
            return (500, {"error": "simulated internal error"})
        if method == "GET" and path == "/items":
            page = int(params.get("page", 1))
            per_page = int(params.get("per_page", 5))
            start = (page - 1) * per_page
            chunk = self.items[start:start + per_page]
            return (200, {"items": chunk, "page": page,
                          "per_page": per_page, "total": len(self.items)})
        if method == "GET" and path.startswith("/items/"):
            try:
                item_id = int(path.rsplit("/", 1)[1])
            except ValueError:
                return (404, {"error": "not found"})
            for item in self.items:
                if item["id"] == item_id:
                    return (200, item)
            return (404, {"error": "not found"})
        return (404, {"error": "unknown path %r" % path})


class APIClient:
    """A tiny REST-style client with retries and pagination helpers."""

    def __init__(self, api: FakeAPI, max_retries: int = 3):
        self.api = api
        self.max_retries = max_retries
        self.history = []  # one dict per attempt: method, path, status, attempt

    def request(self, method: str, path: str, params: dict = None) -> dict:
        """Send one request, retrying simulated 500s with a small backoff."""
        params = params or {}
        attempts = 0
        while True:
            attempts += 1
            status, body = self.api.handle(method, path, params)
            self.history.append({"method": method, "path": path,
                                 "status": status, "attempt": attempts})
            if status == 200:
                return body
            if status == 500 and attempts <= self.max_retries:
                time.sleep(0.01 * attempts)
                continue
            raise APIError(status, body)

    def list_all(self, per_page: int = 5) -> list:
        """Fetch every page of /items and return the combined item list."""
        items = []
        page = 1
        while True:
            body = self.request("GET", "/items", {"page": page, "per_page": per_page})
            items.extend(body["items"])
            if len(items) >= body["total"]:
                break
            page += 1
        return items


def run_demo(seed: int, per_page: int, max_retries: int) -> int:
    """Paginate through the fake API (surviving simulated 500s) and report."""
    num_items = int(PARAMS.get("items", 12))
    fail_first = int(PARAMS.get("fail_first", 2))
    api = FakeAPI(seed, num_items=num_items, fail_first=fail_first)
    client = APIClient(api, max_retries=max_retries)

    print("DNS Load Distribution: Api Client Sim  (topic: DNS Load Distribution, seed=%d)" % seed)
    print("Fake API holds %d items; first %d call(s) simulate HTTP 500.\n" % (
        num_items, fail_first))

    items = client.list_all(per_page=per_page)
    print("Fetched %d items across pages of %d:" % (len(items), per_page))
    print("%4s %-22s %5s" % ("id", "name", "value"))
    for item in items:
        print("%4d %-22s %5d" % (item["id"], item["name"], item["value"]))

    single = client.request("GET", "/items/3")
    print("\nSingle fetch GET /items/3 -> %r" % (single,))

    print("\nRequest history (method path status attempt):")
    for entry in client.history:
        print("  %s %s -> %d (attempt %d)" % (
            entry["method"], entry["path"], entry["status"], entry["attempt"]))
    retries = sum(1 for e in client.history if e["attempt"] > 1)
    print("\nDone: %d attempts total, %d of them retries after simulated 500s." % (
        len(client.history), retries))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="DNS Load Distribution: Api Client Sim: DNS spreads load by returning different address orderings (round-robin) or geo-aware answers: the demo rotates A records per query and measures distribution, plus weighted variants. It is the oldest load-balancing trick on the internet. Short TTLs make it adaptive."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--per-page", type=int, default=None,
                        help="Items per page (see the topic params).")
    parser.add_argument("--max-retries", type=int, default=None,
                        help="Retries per request on 500 (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: parse flags and run the API client demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    per_page = args.per_page or int(PARAMS.get("per_page", 5))
    max_retries = args.max_retries if args.max_retries is not None else int(
        PARAMS.get("max_retries", 3))
    return run_demo(args.seed, per_page, max_retries)


if __name__ == "__main__":
    raise SystemExit(main())
