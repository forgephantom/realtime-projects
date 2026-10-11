#!/usr/bin/env python3
"""Bulk CSV Loader: File Organizer.

Bulk loading beats row-by-row inserts by orders of magnitude: the loader streams CSV in batches inside one transaction, validates per row with error quarantine, and uses the fastest path available. It reports throughput and rejects. ETL lands data with bulk loaders.

Demo dataset idea: Loads seeded CSVs with planted bad rows and verifies throughput, counts, and quarantine..
"""

import argparse
import os
import random
import shutil

SLUG = "bulk-loader-csv-file_organizer-beginner"
PARAMS = {'batch': 'rows per batch', 'validate': 'per-row validation', 'quarantine': 'bad-row handling'}
ROOT = "demo_workspace"  # everything happens inside this runtime-created folder
SAMPLE_BASENAMES = ["photo", "scan", "notes", "report", "data", "export", "memo", "readme"]


def make_sample_files(root: str, n: int, rng: random.Random) -> list:
    """Create n seeded sample files directly inside root; return their names."""
    mapping = PARAMS.get("extension_map", {})
    extensions = [ext for exts in mapping.values() for ext in exts] + [".xyz", ".tmp"]
    names = []
    for i in range(n):
        ext = rng.choice(extensions)
        name = "%s_%02d%s" % (rng.choice(SAMPLE_BASENAMES), i, ext)
        with open(os.path.join(root, name), "w") as handle:
            handle.write("sample %s file %d from the Bulk CSV Loader demo\n" % (ext, i))
            handle.write("".join(rng.choice("abcdef0123456789") for _ in range(64)))
            handle.write("\n")
        names.append(name)
    return sorted(names)


def list_tree(root: str) -> list:
    """Relative paths of everything under root, directories first, sorted."""
    paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        for dirname in sorted(dirnames):
            paths.append(os.path.relpath(os.path.join(dirpath, dirname), root) + "/")
        for filename in sorted(filenames):
            paths.append(os.path.relpath(os.path.join(dirpath, filename), root))
    return sorted(paths)


class FileOrganizer:
    """Sorts the top-level files of a folder into subfolders by extension."""

    def __init__(self, root: str, extension_map: dict):
        self.root = root
        self.extension_map = extension_map

    def category_for(self, filename: str) -> str:
        """Folder name for a file's extension, or 'misc' when unknown."""
        ext = os.path.splitext(filename)[1].lower()
        for category, exts in self.extension_map.items():
            if ext in exts:
                return category
        return "misc"

    def plan(self) -> list:
        """[(source, destination), ...] for every top-level file in root."""
        moves = []
        for name in sorted(os.listdir(self.root)):
            source = os.path.join(self.root, name)
            if os.path.isfile(source):
                dest = os.path.join(self.root, self.category_for(name), name)
                moves.append((source, dest))
        return moves

    def execute(self, plan: list) -> list:
        """Carry out a plan from plan(); return the moves that happened."""
        done = []
        for source, dest in plan:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.move(source, dest)
            done.append((source, dest))
        return done

    def report(self, moves: list) -> str:
        """One-line-per-move human-readable summary."""
        lines = []
        for source, dest in moves:
            lines.append("%s -> %s" % (
                os.path.relpath(source, self.root), os.path.relpath(dest, self.root)))
        return "\n".join(lines)


def run_demo(seed: int, n_files: int, dry_run: bool) -> int:
    """Generate sample files, show before/after, then organize them."""
    rng = random.Random(seed)
    mapping = PARAMS.get("extension_map", {})
    if os.path.isdir(ROOT):
        shutil.rmtree(ROOT)
    os.makedirs(ROOT)
    make_sample_files(ROOT, n_files, rng)

    organizer = FileOrganizer(ROOT, mapping)
    plan = organizer.plan()

    print("Bulk CSV Loader: File Organizer  (topic: Bulk CSV Loader, seed=%d)" % seed)
    print("Working inside ./%s\n" % ROOT)
    print("Before (%d files):" % n_files)
    for path in list_tree(ROOT):
        print("  " + path)
    print("\nPlan: %d moves into %d folders" % (
        len(plan), len({os.path.dirname(d) for _, d in plan})))
    if dry_run:
        print("(dry run - nothing moved)")
        print(organizer.report(plan))
        return 0
    moves = organizer.execute(plan)
    print("\nAfter:")
    for path in list_tree(ROOT):
        print("  " + path)
    print("\nMoved %d files." % len(moves))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Bulk CSV Loader: File Organizer: Bulk loading beats row-by-row inserts by orders of magnitude: the loader streams CSV in batches inside one transaction, validates per row with error quarantine, and uses the fastest path available. It reports throughput and rejects. ETL lands data with bulk loaders."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--files", type=int, default=None,
                        help="Sample files to generate (see the topic params).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the move plan without moving anything.")
    return parser


def main(argv=None) -> int:
    """Entry point: parse flags and run the organizer demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    n_files = args.files or int(PARAMS.get("num_files", 12))
    return run_demo(args.seed, n_files, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
