#!/usr/bin/env python3
"""Re-render ONE project by slug: python3 tools/materialize.py <slug>.

Rebuilds the deterministic build plan via generate.build_all_records(),
finds the record with the matching slug, re-renders all of its files, and
rewrites them in place. No git operations.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate


def main(argv):
    if len(argv) != 2:
        print("usage: python3 tools/materialize.py <slug>")
        return 2
    slug = argv[1]
    records = generate.build_all_records()
    record = next((r for r in records if r["slug"] == slug), None)
    if record is None:
        print("unknown slug: {}".format(slug))
        return 1
    types = generate.load_types()
    doc_templates = generate.load_doc_templates()
    files = generate.render_project_files(
        record, types[record["type"]], doc_templates)
    generate.write_project(generate.ROOT, record, files)
    print("re-rendered {} ({} files) -> {}".format(
        slug, len(files), record["path"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
