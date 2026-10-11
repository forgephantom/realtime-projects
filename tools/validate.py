#!/usr/bin/env python3
"""Validation gates for the mega repo build. Exit non-zero on any failure.

Gates:
 1. total projects == 12000; per-subdomain counts == quotas; per-domain sums.
 2. all slugs unique.
 3. grep all generated files for "@@", "lorem", "TODO", "coming soon"
    (case-insensitive) -> zero hits.
 4. python3 -m py_compile on EVERY generated .py -> 100% pass.
 5. random sample of 600 projects (seed 7): `python3 src/main.py --help` and
    `timeout 15 python3 src/main.py` with cwd=project dir; exit 0 on both;
    pass rate >= 98%.
 6. spot-check 20 random projects: README.md contains "src/main.py" and at
    least one class name from the type's meta.json.
 7. total repo size < 400MB.
"""

import json
import os
import random
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate

ROOT = generate.ROOT
PROJECTS_DIR = generate.PROJECTS_DIR
EXPECTED_TOTAL = generate.TOTAL_QUOTA  # 12000
FORBIDDEN = ["@@", "lorem", "todo", "coming soon"]


def iter_projects():
    """Yield (domain, subdomain, slug, dirpath) for every project dir."""
    for domain in sorted(os.listdir(PROJECTS_DIR)):
        dpath = os.path.join(PROJECTS_DIR, domain)
        if not os.path.isdir(dpath):
            continue
        for sub in sorted(os.listdir(dpath)):
            spath = os.path.join(dpath, sub)
            if not os.path.isdir(spath):
                continue
            for slug in sorted(os.listdir(spath)):
                ppath = os.path.join(spath, slug)
                if os.path.isdir(ppath):
                    yield domain, sub, slug, ppath


def gate1_counts(projects):
    ok = True
    total = len(projects)
    print("[gate1] total projects: {} (expected {})".format(
        total, EXPECTED_TOTAL))
    if total != EXPECTED_TOTAL:
        print("  FAIL: total != {}".format(EXPECTED_TOTAL))
        ok = False
    per_sub = {}
    per_domain = {}
    for domain, sub, slug, _ in projects:
        per_sub[sub] = per_sub.get(sub, 0) + 1
        per_domain[domain] = per_domain.get(domain, 0) + 1
    for sub, quota in generate.QUOTAS.items():
        got = per_sub.get(sub, 0)
        if got != quota:
            print("  FAIL: subdomain {} has {} projects, quota {}".format(
                sub, got, quota))
            ok = False
    extra = set(per_sub) - set(generate.QUOTAS)
    if extra:
        print("  FAIL: unexpected subdomains on disk: {}".format(sorted(extra)))
        ok = False
    # per-domain sums: each domain's count must equal the sum of its subdomains
    topics = generate.load_topics()
    for domain in per_domain:
        expected = sum(generate.QUOTAS[s] for s, q in generate.QUOTAS.items()
                       if topics[s]["domain"] == domain)
        if per_domain[domain] != expected:
            print("  FAIL: domain {} has {} projects, expected {}".format(
                domain, per_domain[domain], expected))
            ok = False
    print("  per-domain: {}".format(
        ", ".join("{}={}".format(d, per_domain[d]) for d in sorted(per_domain))))
    print("[gate1] {}".format("PASS" if ok else "FAIL"))
    return ok


def gate2_unique_slugs(projects):
    slugs = ["{}/{}/{}".format(d, s, sl) for d, s, sl, _ in projects]
    ok = len(slugs) == len(set(slugs)) == EXPECTED_TOTAL
    print("[gate2] {} unique slugs / {} projects -> {}".format(
        len(set(slugs)), len(slugs), "PASS" if ok else "FAIL"))
    return ok


def gate3_forbidden(projects):
    hits = []
    n_files = 0
    # scan generated trees: projects/, catalog/, indexes/, PROJECT_INDEX.md
    scan_roots = [PROJECTS_DIR, generate.CATALOG_DIR, generate.INDEXES_DIR]
    scan_files = [os.path.join(ROOT, "PROJECT_INDEX.md")]
    for root in scan_roots:
        for dirpath, dirnames, filenames in os.walk(root):
            # build artifacts, not generated content
            dirnames[:] = [d for d in dirnames if d != "__pycache__"]
            for fn in filenames:
                if fn.endswith((".pyc", ".pyo")):
                    continue
                scan_files.append(os.path.join(dirpath, fn))
    for path in scan_files:
        n_files += 1
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        low = text.lower()
        for token in FORBIDDEN:
            if token.lower() in low:
                # find first matching line for the report
                for i, line in enumerate(text.splitlines(), 1):
                    if token.lower() in line.lower():
                        hits.append((path, token, i, line.strip()[:120]))
                        break
                break
    ok = not hits
    print("[gate3] scanned {:,} files, {} forbidden-token hits -> {}".format(
        n_files, len(hits), "PASS" if ok else "FAIL"))
    for path, token, lineno, line in hits[:20]:
        print("  HIT {!r} in {}:{}: {}".format(token, path, lineno, line))
    return ok


def gate4_compile(projects):
    # compile() via the builtin: no .pyc/__pycache__ litter in the repo.
    py_files = []
    for _, _, _, ppath in projects:
        for dirpath, dirnames, filenames in os.walk(ppath):
            dirnames[:] = [d for d in dirnames if d != "__pycache__"]
            for fn in filenames:
                if fn.endswith(".py"):
                    py_files.append(os.path.join(dirpath, fn))
    fails = []
    for path in py_files:
        try:
            with open(path, encoding="utf-8") as fh:
                src = fh.read()
            compile(src, path, "exec")
        except (SyntaxError, ValueError, OSError) as exc:
            fails.append((path, str(exc).splitlines()[-1] if str(exc) else "?"))
    ok = not fails
    print("[gate4] py_compile on {:,} .py files: {} passed, {} failed -> {}".format(
        len(py_files), len(py_files) - len(fails), len(fails),
        "PASS" if ok else "FAIL"))
    for path, err in fails[:20]:
        print("  COMPILE FAIL {}: {}".format(path, err))
    return ok


def gate5_sample_runs(projects, sample_n=600, seed=7):
    rng = random.Random(seed)
    sample = rng.sample(projects, min(sample_n, len(projects)))
    passed = 0
    failures = []
    for domain, sub, slug, ppath in sample:
        entry = os.path.join(ppath, "src", "main.py")
        # --help
        try:
            r1 = subprocess.run([sys.executable, entry, "--help"],
                                capture_output=True, text=True, timeout=15,
                                cwd=ppath, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            failures.append((slug, "--help TIMEOUT"))
            continue
        if r1.returncode != 0:
            failures.append((slug, "--help exit={} stderr={!r}".format(
                r1.returncode, r1.stderr.strip().splitlines()[-2:])))
            continue
        # default run
        try:
            r2 = subprocess.run([sys.executable, entry],
                                capture_output=True, text=True, timeout=15,
                                cwd=ppath, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            failures.append((slug, "run TIMEOUT 15s"))
            continue
        if r2.returncode != 0:
            tail = r2.stderr.strip().splitlines()[-3:]
            failures.append((slug, "run exit={} stderr={!r}".format(
                r2.returncode, tail)))
            continue
        passed += 1
    rate = passed / len(sample) if sample else 0
    ok = rate >= 0.98
    print("[gate5] sample runs: {}/{} passed ({:.2%}, need >=98%) -> {}".format(
        passed, len(sample), rate, "PASS" if ok else "FAIL"))
    for slug, err in failures[:20]:
        print("  RUN FAIL {}: {}".format(slug, err))
    return ok


def gate6_readme_spotcheck(projects, n=20, seed=7):
    rng = random.Random(seed)
    sample = rng.sample(projects, min(n, len(projects)))
    types = generate.load_types()
    fails = []
    for domain, sub, slug, ppath in sample:
        readme = os.path.join(ppath, "README.md")
        try:
            with open(readme, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            fails.append((slug, "README.md missing"))
            continue
        # recover type: slug ends with -<type>-<difficulty>
        matched = None
        for tname in types:
            if "-{}-".format(tname) in slug or slug.endswith("-" + tname):
                # disambiguate by checking full "<type>-<difficulty>" tail
                for d in ("beginner", "intermediate", "advanced"):
                    if slug.endswith("-{}-{}".format(tname, d)):
                        matched = tname
                        break
            if matched:
                break
        problems = []
        if "src/main.py" not in text:
            problems.append("missing 'src/main.py'")
        if matched:
            class_names = [c["name"]
                           for c in types[matched]["meta"]["classes"]]
            if class_names and not any(cn in text for cn in class_names):
                problems.append("no class name {} in README".format(class_names))
        else:
            problems.append("could not determine type from slug")
        if problems:
            fails.append((slug, "; ".join(problems)))
    ok = not fails
    print("[gate6] README spot-check {}/{} -> {}".format(
        len(sample) - len(fails), len(sample), "PASS" if ok else "FAIL"))
    for slug, err in fails:
        print("  SPOTCHECK FAIL {}: {}".format(slug, err))
    return ok


def gate7_size(projects):
    total_bytes = 0
    n_files = 0
    for dirpath, _, filenames in os.walk(ROOT):
        # skip nothing: whole repo counts
        for fn in filenames:
            fp = os.path.join(dirpath, fn)
            try:
                total_bytes += os.path.getsize(fp)
                n_files += 1
            except OSError:
                pass
    mib = total_bytes / (1024 * 1024)
    ok = total_bytes < 400 * 1024 * 1024
    du = subprocess.run(["du", "-sh", ROOT], capture_output=True,
                        text=True).stdout.strip()
    print("[gate7] repo size: {} ({} files, {:.1f} MiB, limit 400MB) -> {}".format(
        du, n_files, mib, "PASS" if ok else "FAIL"))
    return ok


def main():
    t0 = __import__("time").time()
    print("collecting project dirs...", flush=True)
    projects = list(iter_projects())
    results = [
        gate1_counts(projects),
        gate2_unique_slugs(projects),
        gate3_forbidden(projects),
        gate4_compile(projects),
        gate5_sample_runs(projects),
        gate6_readme_spotcheck(projects),
        gate7_size(projects),
    ]
    dt = __import__("time").time() - t0
    print("validation: {}/7 gates passed in {:.0f}s".format(
        sum(results), dt))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
