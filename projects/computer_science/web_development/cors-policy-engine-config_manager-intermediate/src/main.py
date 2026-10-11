#!/usr/bin/env python3
"""CORS Policy Engine: Config Manager.

Browsers block cross-origin reads by default; CORS lets servers opt in per origin, method, and header. The engine answers preflight OPTIONS requests with Access-Control-Allow-* headers, decides when credentials may ride along, and caches preflight results via max-age. An overly permissive policy (reflecting any origin with credentials) silently voids the whole protection.

Demo dataset idea: Feeds seeded cross-origin requests (simple, preflighted, credentialed) and checks the engine allows exactly the policy's intent..
"""

import argparse
import os
import random

SLUG = "cors-policy-engine-config_manager-intermediate"
PARAMS = {'allowed_origins': 'exact origins or patterns permitted', 'allow_credentials': 'whether cookies/auth may be sent', 'preflight_max_age': 'OPTIONS cache seconds'}

SCHEMA = {
    "host": {"type": str, "default": "127.0.0.1", "desc": "Bind address"},
    "port": {"type": int, "default": 8000, "desc": "Bind port"},
    "workers": {"type": int, "default": 4, "desc": "Worker threads"},
    "log_level": {"type": str, "default": "info", "desc": "Log verbosity"},
    "debug": {"type": bool, "default": False, "desc": "Debug mode"},
    "timeout_s": {"type": float, "default": 30.0, "desc": "Request timeout, seconds"},
}

# The "file" layer of the demo: an INI-style snippet parsed from a string.
SAMPLE_INI = """
# sample file layer for the CORS Policy Engine demo
port = 8080
log_level = debug
workers = 8
"""

TRUE_WORDS = {"true", "1", "yes", "on"}
FALSE_WORDS = {"false", "0", "no", "off"}


def coerce(raw: str, kind: type):
    """Convert a raw string to kind; raises ValueError on bad input."""
    text = raw.strip()
    if kind is bool:
        lowered = text.lower()
        if lowered in TRUE_WORDS:
            return True
        if lowered in FALSE_WORDS:
            return False
        raise ValueError("not a boolean: %r" % raw)
    if kind is int:
        return int(text)
    if kind is float:
        return float(text)
    return text


class Config:
    """Layered configuration: defaults < ini string < environment < CLI.

    Every key comes from SCHEMA with a type, a default, and a description.
    Each set records which layer supplied the value, so the demo can show
    exactly where every value came from.
    """

    def __init__(self, schema: dict):
        self._schema = schema
        self._values = {}
        self._sources = {}

    def load_defaults(self) -> None:
        """Layer 1: schema defaults."""
        for key, spec in self._schema.items():
            self._values[key] = spec["default"]
            self._sources[key] = "default"

    def load_ini(self, text: str) -> None:
        """Layer 2: parse flat key = value lines from an INI-style string."""
        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith(";"):
                continue
            if "=" not in stripped:
                raise ValueError("bad ini line %d: %r" % (lineno, line))
            key, _, raw = stripped.partition("=")
            key = key.strip()
            if key not in self._schema:
                raise ValueError("unknown config key %r on ini line %d" % (key, lineno))
            self._values[key] = coerce(raw, self._schema[key]["type"])
            self._sources[key] = "ini"

    def load_env(self, prefix: str) -> None:
        """Layer 3: PREFIX_KEY environment variables, e.g. DEMOAPP_PORT."""
        for key, spec in self._schema.items():
            env_name = prefix + "_" + key.upper()
            if env_name in os.environ:
                self._values[key] = coerce(os.environ[env_name], spec["type"])
                self._sources[key] = "env:" + env_name

    def set(self, key: str, raw: str) -> None:
        """Layer 4: a single CLI override in key=value form."""
        if key not in self._schema:
            raise ValueError("unknown config key %r" % key)
        self._values[key] = coerce(raw, self._schema[key]["type"])
        self._sources[key] = "cli"

    def get(self, key: str):
        """The resolved value for key."""
        return self._values[key]

    def as_dict(self) -> dict:
        """All resolved values as a plain dict."""
        return dict(self._values)

    def sources(self) -> dict:
        """Which layer supplied each key."""
        return dict(self._sources)

    def validate(self) -> list:
        """Return a list of human-readable problems; empty means valid."""
        problems = []
        port = self._values["port"]
        if not 1 <= port <= 65535:
            problems.append("port must be 1-65535, got %r" % port)
        if self._values["workers"] < 1:
            problems.append("workers must be >= 1, got %r" % self._values["workers"])
        if self._values["log_level"] not in ("debug", "info", "warning", "error"):
            problems.append("log_level must be debug/info/warning/error, got %r"
                            % self._values["log_level"])
        if self._values["timeout_s"] <= 0:
            problems.append("timeout_s must be > 0, got %r" % self._values["timeout_s"])
        return problems


def run_demo(seed: int, cli_overrides: list, env_prefix: str) -> int:
    """Resolve all four layers, print the table, and validate."""
    rng = random.Random(seed)
    session = "".join(rng.choice("abcdef0123456789") for _ in range(8))

    # The demo plants one env var so the env layer has something to show.
    os.environ[env_prefix + "_TIMEOUT_S"] = "12.5"

    config = Config(SCHEMA)
    config.load_defaults()
    config.load_ini(SAMPLE_INI)
    config.load_env(env_prefix)
    for override in cli_overrides:
        if "=" not in override:
            print("error: --set expects key=value, got %r" % override)
            return 2
        key, _, raw = override.partition("=")
        config.set(key.strip(), raw)

    print("CORS Policy Engine: Config Manager  (topic: CORS Policy Engine, seed=%d, session %s)" % (
        seed, session))
    print("Resolved configuration (defaults < ini < env < cli):\n")
    print("%-10s %-12s %-8s %-18s %s" % ("key", "value", "type", "source", "description"))
    sources = config.sources()
    for key in sorted(config.as_dict()):
        spec = SCHEMA[key]
        print("%-10s %-12s %-8s %-18s %s" % (
            key, repr(config.get(key)), spec["type"].__name__,
            sources[key], spec["desc"]))
    problems = config.validate()
    if problems:
        print("\nValidation FAILED:")
        for problem in problems:
            print("  - " + problem)
        return 1
    print("\nValidation passed: all %d keys look sane." % len(SCHEMA))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="CORS Policy Engine: Config Manager: Browsers block cross-origin reads by default; CORS lets servers opt in per origin, method, and header. The engine answers preflight OPTIONS requests with Access-Control-Allow-* headers, decides when credentials may ride along, and caches preflight results via max-age. An overly permissive policy (reflecting any origin with credentials) silently voids the whole protection."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--set", action="append", default=[],
                        help="CLI override as key=value; repeatable.")
    parser.add_argument("--env-prefix", type=str, default=None,
                        help="Environment variable prefix (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: parse flags and run the config demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    env_prefix = args.env_prefix or PARAMS.get("env_prefix", "DEMOAPP")
    return run_demo(args.seed, args.set, env_prefix)


if __name__ == "__main__":
    raise SystemExit(main())
