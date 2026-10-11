#!/usr/bin/env python3
"""Knowledge Base Sync Tool: Backup Tool.

A knowledge-base sync tool watches source documents for changes and updates the index incrementally instead of rebuilding from scratch. Change detection hashes each document and re-embeds only what changed. Deletion handling removes stale vectors so retired documents stop appearing.

Demo dataset idea: Generates seeded document sets with edits and deletions, then verifies index freshness after sync..
"""

import argparse
import hashlib
import json
import os
import random
import shutil

SLUG = "knowledge-base-sync-backup_tool-intermediate"
PARAMS = {'delete_policy': 'how removals are handled', 'hash_algorithm': 'change detection method', 'sync_interval': 'how often to check for changes'}
ROOT = "demo_workspace"  # everything happens inside this runtime-created folder


def make_sample_files(source: str, n: int, rng: random.Random) -> list:
    """Create n seeded text and binary files under source; return rel paths."""
    os.makedirs(source, exist_ok=True)
    names = []
    for i in range(n):
        if i % 3 == 2:
            name = "blob_%02d.bin" % i
            with open(os.path.join(source, name), "wb") as handle:
                handle.write(rng.randbytes(256 + i * 32))
        else:
            name = "doc_%02d.txt" % i
            with open(os.path.join(source, name), "w") as handle:
                handle.write("Knowledge Base Sync Tool backup demo file %d\n" % i)
                handle.write("".join(rng.choice("abcdef0123456789") for _ in range(128)))
                handle.write("\n")
        names.append(name)
    return sorted(names)


class BackupJob:
    """Copies a source tree to a destination and verifies it with SHA-256."""

    def __init__(self, source: str, dest: str, chunk_kb: int = 64):
        self.source = source
        self.dest = dest
        self.chunk_size = chunk_kb * 1024

    def collect(self) -> list:
        """Relative paths of every file under the source, sorted."""
        found = []
        for dirpath, _, filenames in os.walk(self.source):
            for filename in filenames:
                full = os.path.join(dirpath, filename)
                found.append(os.path.relpath(full, self.source))
        return sorted(found)

    def _sha256(self, path: str) -> str:
        digest = hashlib.sha256()
        with open(path, "rb") as handle:
            while True:
                chunk = handle.read(self.chunk_size)
                if not chunk:
                    break
                digest.update(chunk)
        return digest.hexdigest()

    def run(self) -> dict:
        """Copy every file, write a JSON manifest of SHA-256 checksums."""
        if os.path.isdir(self.dest):
            shutil.rmtree(self.dest)
        entries = []
        total_bytes = 0
        for rel in self.collect():
            source_path = os.path.join(self.source, rel)
            dest_path = os.path.join(self.dest, rel)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(source_path, dest_path)
            checksum = self._sha256(dest_path)
            size = os.path.getsize(dest_path)
            total_bytes += size
            entries.append({"path": rel, "size": size, "sha256": checksum})
        manifest_path = os.path.join(self.dest, "manifest.json")
        with open(manifest_path, "w") as handle:
            json.dump({"files": entries}, handle, indent=2)
        return {"files": entries, "bytes": total_bytes, "manifest": manifest_path}

    def verify(self) -> dict:
        """Re-hash every backed-up file and compare against the manifest."""
        with open(os.path.join(self.dest, "manifest.json")) as handle:
            entries = json.load(handle)["files"]
        ok, failed = [], []
        for entry in entries:
            actual = self._sha256(os.path.join(self.dest, entry["path"]))
            (ok if actual == entry["sha256"] else failed).append(entry["path"])
        return {"ok": ok, "failed": failed}


def run_demo(seed: int, n_files: int, chunk_kb: int) -> int:
    """Generate sample files, back them up with checksums, then verify."""
    rng = random.Random(seed)
    if os.path.isdir(ROOT):
        shutil.rmtree(ROOT)
    source = os.path.join(ROOT, "source")
    dest = os.path.join(ROOT, "backup")
    make_sample_files(source, n_files, rng)

    job = BackupJob(source, dest, chunk_kb=chunk_kb)
    outcome = job.run()

    print("Knowledge Base Sync Tool: Backup Tool  (topic: Knowledge Base Sync Tool, seed=%d)" % seed)
    print("Backing up ./%s -> ./%s\n" % (source, dest))
    print("%-16s %8s %-12s" % ("file", "bytes", "sha256"))
    for entry in outcome["files"]:
        print("%-16s %8d %s" % (entry["path"], entry["size"], entry["sha256"][:12]))
    print("\nWrote manifest: ./%s (%d files, %d bytes)." % (
        os.path.relpath(outcome["manifest"], "."), len(outcome["files"]), outcome["bytes"]))

    check = job.verify()
    print("Verify: %d/%d files match their checksums - %s." % (
        len(check["ok"]), len(outcome["files"]),
        "OK" if not check["failed"] else "FAILED: " + ", ".join(check["failed"])))
    return 0 if not check["failed"] else 1


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Knowledge Base Sync Tool: Backup Tool: A knowledge-base sync tool watches source documents for changes and updates the index incrementally instead of rebuilding from scratch. Change detection hashes each document and re-embeds only what changed. Deletion handling removes stale vectors so retired documents stop appearing."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--files", type=int, default=None,
                        help="Sample files to back up (see the topic params).")
    parser.add_argument("--chunk-kb", type=int, default=None,
                        help="Hash read chunk size in KB (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: parse flags and run the backup demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    n_files = args.files or int(PARAMS.get("num_files", 8))
    chunk_kb = args.chunk_kb or int(PARAMS.get("chunk_kb", 64))
    return run_demo(args.seed, n_files, chunk_kb)


if __name__ == "__main__":
    raise SystemExit(main())
