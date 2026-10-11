#!/usr/bin/env python3
"""Deterministic generator for the 12,000-project mega repo.

Reads topics/*.json and templates/, renders every project, and writes:
  projects/<domain>/<subdomain>/<slug>/   README.md, src/*.py, docs/*.md
  catalog/<domain>.json
  indexes/<domain>.md
  PROJECT_INDEX.md

All render helpers are module-level so tools/materialize.py can import and
re-render a single project by slug. Deterministic: no RNG anywhere; the only
"seed" is the literal SEED=42 baked into generated code.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_DIR = os.path.join(ROOT, "topics")
CODE_TPL_DIR = os.path.join(ROOT, "templates", "code")
DOCS_TPL_DIR = os.path.join(ROOT, "templates", "docs")
PROJECTS_DIR = os.path.join(ROOT, "projects")
CATALOG_DIR = os.path.join(ROOT, "catalog")
INDEXES_DIR = os.path.join(ROOT, "indexes")

QUOTAS = {
    "web_development": 800,
    "machine_learning": 800,
    "data_science": 700,
    "software_engineering": 600,
    "cybersecurity": 600,
    "devops_sre": 600,
    "databases": 400,
    "computer_networks": 400,
    "algorithms_data_structures": 400,
    "cloud_computing": 350,
    "data_engineering": 350,
    "mobile_development": 250,
    "game_development": 200,
    "operating_systems": 150,
    "bioinformatics": 350,
    "genetics": 250,
    "ecology": 200,
    "cell_biology": 200,
    "physics": 800,
    "chemistry": 800,
    "mathematics": 700,
    "health_informatics": 300,
    "biostatistics": 250,
    "clinical_tools": 250,
    "electronics_engineering": 700,
    "environmental_science": 600,
}
TOTAL_QUOTA = sum(QUOTAS.values())

DIFF_ALLOW = {
    "beginner": ["beginner"],
    "intermediate": ["beginner", "intermediate"],
    "advanced": ["intermediate", "advanced"],
}
ALL_DIFFS = ["beginner", "intermediate", "advanced"]
DURATIONS = {
    "beginner": "2-4 hours",
    "intermediate": "4-8 hours",
    "advanced": "8-16 hours",
}
ENTRYPOINT = "src/main.py"

# Gate 3 of validate.py greps every generated file for these tokens
# (case-insensitive) and requires zero hits. The "todo-scanner" topic would
# inject the literal word "TODO" into its projects' titles, docstrings and
# docs, so its combos are skipped and backfilled with the next combos in the
# same deterministic walk order. This is the only deviation from the strict
# "first quota combos" rule, and it is logged.
FORBIDDEN_TOPIC_TOKENS = ("todo",)

DOC_TPL_MAP = [
    ("project_readme.md.tpl", "README.md"),
    ("architecture.md.tpl", "docs/ARCHITECTURE.md"),
    ("design.md.tpl", "docs/DESIGN.md"),
    ("runbook.md.tpl", "docs/RUNBOOK.md"),
    ("presentation.md.tpl", "docs/PRESENTATION.md"),
]


# ---------------------------------------------------------------- loading ---

def load_topics():
    """Return {subdomain: {'domain': str, 'topics': [topic dict]}}."""
    out = {}
    for fname in sorted(os.listdir(TOPICS_DIR)):
        if not fname.endswith(".json"):
            continue
        sub = fname[:-5]
        with open(os.path.join(TOPICS_DIR, fname), encoding="utf-8") as fh:
            data = json.load(fh)
        out[sub] = {"domain": data["domain"], "topics": data["topics"]}
    return out


def load_types():
    """Return {type: {'meta': dict, 'templates': {tpl_name: text}}}."""
    out = {}
    for tname in sorted(os.listdir(CODE_TPL_DIR)):
        tdir = os.path.join(CODE_TPL_DIR, tname)
        meta_path = os.path.join(tdir, "meta.json")
        if not os.path.isfile(meta_path):
            continue
        with open(meta_path, encoding="utf-8") as fh:
            meta = json.load(fh)
        tpls = {}
        for entry in meta["files"]:
            tpl_name = entry["template"]
            with open(os.path.join(tdir, tpl_name), encoding="utf-8") as fh:
                tpls[tpl_name] = fh.read()
        out[tname] = {"meta": meta, "templates": tpls}
    return out


def load_doc_templates():
    out = {}
    for tpl_name, _ in DOC_TPL_MAP:
        with open(os.path.join(DOCS_TPL_DIR, tpl_name), encoding="utf-8") as fh:
            out[tpl_name] = fh.read()
    return out


# ------------------------------------------------------- combo selection ---

def _topic_forbidden(topic):
    blob = (topic["slug_base"] + " " + topic["name"]).lower()
    return any(tok in blob for tok in FORBIDDEN_TOPIC_TOKENS)


def select_combos_for_subdomain(sub, sub_data):
    """Deterministic (topic, type, difficulty) walk.

    Pass 1: topics sorted by slug_base; suggested_types in listed order;
    difficulties restricted by the topic's own difficulty.
    Pass 2 (fallback): same order, all three difficulties per (topic, type).
    Combos whose topic name/slug contains a forbidden gate-3 token are
    skipped and backfilled from later in the same walk order.
    Returns (selected, used_fallback, skipped).
    Aborts the whole run with a deficit report if quota is unreachable.
    """
    quota = QUOTAS[sub]
    topics = sorted(sub_data["topics"], key=lambda t: t["slug_base"])
    walk1 = []
    for t in topics:
        for ty in t["suggested_types"]:
            for d in DIFF_ALLOW[t["difficulty"]]:
                walk1.append({"topic": t, "type": ty, "difficulty": d})
    seen = {(c["topic"]["slug_base"], c["type"], c["difficulty"]) for c in walk1}
    walk2 = []
    for t in topics:
        for ty in t["suggested_types"]:
            for d in ALL_DIFFS:
                key = (t["slug_base"], ty, d)
                if key not in seen:
                    walk2.append({"topic": t, "type": ty, "difficulty": d})
    full_walk = walk1 + walk2
    skipped = [c for c in full_walk if _topic_forbidden(c["topic"])]
    eligible = [c for c in full_walk if not _topic_forbidden(c["topic"])]
    if len(eligible) < quota:
        deficit = quota - len(eligible)
        print("DEFICIT REPORT — cannot reach quota for subdomain "
              "'{}':".format(sub), file=sys.stderr)
        print("  quota={}  pass1_combos={}  pass1+pass2_combos={}  "
              "forbidden_skipped={}  deficit={}".format(
                  quota, len(walk1), len(full_walk), len(skipped), deficit),
              file=sys.stderr)
        print("  max reachable = {} (need {} more distinct "
              "(topic, type, difficulty) combos)".format(len(eligible), deficit),
              file=sys.stderr)
        sys.exit(1)
    selected = eligible[:quota]
    used_fallback = len([c for c in walk1 if not _topic_forbidden(c["topic"])]) < quota
    for c in selected:
        c["subdomain"] = sub
        c["domain"] = sub_data["domain"]
    return selected, used_fallback, skipped


def select_all_combos(topics):
    """Select combos for every subdomain; abort with deficit report on shortfall."""
    # Build everything first so the deficit report covers all subdomains.
    per_sub = {}
    for sub in QUOTAS:
        per_sub[sub] = select_combos_for_subdomain(sub, topics[sub])
    return per_sub


# ------------------------------------------------------------------ slugs ---

def unique_slug(combo, used):
    base = "{}-{}-{}".format(
        combo["topic"]["slug_base"], combo["type"], combo["difficulty"])[:80]
    slug = base
    n = 2
    while slug in used:
        slug = "{}-{}".format(base, n)
        n += 1
    used.add(slug)
    return slug


# ---------------------------------------------------------------- records ---

def build_record(combo, slug, meta):
    topic = combo["topic"]
    difficulty = combo["difficulty"]
    title = "{}: {}".format(topic["name"], meta["label"].title())
    duration = DURATIONS[difficulty]
    description = "{} built as a {}. {} {}".format(
        topic["name"], meta["label"], topic["concept"],
        meta["description_sentence"])
    return {
        "slug": slug,
        "title": title,
        "domain": combo["domain"],
        "subdomain": combo["subdomain"],
        "type": combo["type"],
        "difficulty": difficulty,
        "duration": duration,                       # e.g. "2-4 hours"
        "duration_short": duration.replace(" hours", ""),  # e.g. "2-4"
        "description": description,
        "topic": topic,
        "path": "projects/{}/{}/{}".format(
            combo["domain"], combo["subdomain"], slug),
    }


def build_all_records():
    """Full deterministic build plan: list of records with globally unique slugs."""
    topics = load_topics()
    types = load_types()
    per_sub = select_all_combos(topics)
    records = []
    used = set()
    for sub in QUOTAS:  # deterministic subdomain order
        selected, _, _ = per_sub[sub]
        for combo in selected:
            slug = unique_slug(combo, used)
            records.append(build_record(combo, slug, types[combo["type"]]["meta"]))
    slugs = [r["slug"] for r in records]
    assert len(slugs) == len(set(slugs)) == TOTAL_QUOTA, \
        "slug uniqueness/count failure: {} records, {} unique".format(
            len(slugs), len(set(slugs)))
    return records


# ---------------------------------------------------------------- rendering ---

def md_table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def first_sentence(text):
    text = text.strip()
    m = re.match(r"(.+?\.)\s", text)
    s = m.group(1) if m else text
    return s if s.endswith(".") else s + "."


def code_level_subs(record):
    """Shared @@..@@ substitutions used in code templates (and embedded in
    some meta.json text, e.g. QA answers referencing @@TOPIC_PARAMS@@)."""
    topic = record["topic"]
    return {
        "@@PROJECT_TITLE@@": record["title"],
        "@@PROJECT_SLUG@@": record["slug"],
        "@@TOPIC_NAME@@": topic["name"],
        "@@TOPIC_CONCEPT@@": topic["concept"].replace('"""', '"\'\'"'),
        "@@TOPIC_PARAMS@@": repr(topic["key_params"]),
        "@@DATA_IDEA@@": topic["data_idea"],
        "@@SEED@@": "42",
    }


def render_code_files(record, type_data):
    """Render src/*.py. Returns {relpath: content}."""
    subs = code_level_subs(record)
    out = {}
    for entry in type_data["meta"]["files"]:
        text = type_data["templates"][entry["template"]]
        for k, v in subs.items():
            text = text.replace(k, v)
        assert "@@" not in text, \
            "unrendered placeholder in {}/{}".format(record["slug"], entry["path"])
        out[entry["path"]] = text
    return out


def build_doc_blocks(record, meta):
    """Build every substitution block the doc templates need."""
    topic = record["topic"]
    module = meta["modules"][0] if meta.get("modules") else "main"
    class_names = [c["name"] for c in meta["classes"]]

    file_table = md_table(
        ["File", "Purpose"],
        [[f["path"],
          "CLI entrypoint (argument parsing + demo orchestration)"
          if f.get("entrypoint") else "Supporting module"]
         for f in meta["files"]])

    component_rows = [[c["name"], module, c["desc"]] for c in meta["classes"]]
    component_rows.append(
        ["CLI entrypoint", module,
         "Argument parsing and demo orchestration via main()"])
    component_table = md_table(["Component", "Module", "Responsibility"],
                               component_rows)

    class_table = md_table(["Class", "Description"],
                           [[c["name"], c["desc"]] for c in meta["classes"]])

    function_table = md_table(
        ["Function", "Signature", "Description"],
        [[f["name"], f["signature"], f["desc"]] for f in meta["functions"]])

    param_table = md_table(
        ["Parameter", "Meaning"],
        [[k, v] for k, v in topic["key_params"].items()])

    data_flow = "```\n" + meta["data_flow_ascii"] + "\n```"

    run_lines = [
        "```",
        "cd {}".format(record["path"]),
        "python3 src/main.py --help",
        "python3 src/main.py",
        "```",
    ]
    if meta.get("run_notes"):
        run_lines.append(meta["run_notes"])
    run_commands = "\n".join(run_lines)

    features = []
    for c in meta["classes"]:
        features.append("- **{}**: {}".format(c["name"], c["desc"]))
    for f in meta["functions"]:
        features.append("- `{}` (`{}`): {}".format(
            f["name"], f["signature"], f["desc"]))
    features_block = "\n".join(features)

    algo = meta["algorithm"]
    demo_script = "\n".join([
        "1. Show the CLI contract: run `python3 src/main.py --help` and walk "
        "through each flag, its default value, and what it changes.",
        "2. Run the live demo: `python3 src/main.py` with no flags. Narrate "
        "each output section as it appears — the run is seeded, so the "
        "numbers are reproducible.",
        "3. Open `src/main.py` and point at the core algorithm — \"{}\" — "
        "then trace one input through the classes that implement it.".format(algo),
        "4. Re-run with a different seed: `python3 src/main.py --seed 7`. "
        "Show that the output changes but keeps the same shape, proving the "
        "demo is generated, not hardcoded.",
        "5. Open `docs/PRESENTATION.md` and use the Interview Q&A below for "
        "the last two minutes — answer one architecture question and one "
        "trade-off question out loud.",
    ])

    qa_blocks = []
    for item in meta["qa"]:
        qa_blocks.append("**Q:** {}\n\n**A:** {}".format(item["q"], item["a"]))
    qa_block = "\n\n".join(qa_blocks)

    talking_points = "\n".join([
        "- Components: {} plus the CLI entrypoint — each maps to a real "
        "module in `src/`, and the data-flow diagram shows how they connect.".format(
            ", ".join("`{}`".format(n) for n in class_names) or "a single module"),
        "- Algorithm: {}; runs in {}.".format(algo, meta["complexity"]),
        "- Honest scaling limit: {}".format(meta["scaling_note"]),
    ])

    extensions = "\n".join([
        "- Persist state in `sqlite3` (stdlib) so results survive restarts "
        "instead of living only in memory.",
        "- Load parameters from a JSON config file for repeatable, "
        "shareable runs without long flag lists.",
        "- Add an export/serve mode (CSV/JSON export or a small local "
        "server) to integrate with other tools.",
        "- Add a `unittest` suite covering the core classes and asserting "
        "the seeded demo output.",
    ])

    resume_bullet = meta["resume_bullet_template"].replace(
        "{topic}", topic["name"])
    pitch = meta["pitch_sentence"].replace("{topic}", topic["name"]) \
        + " " + first_sentence(topic["concept"])

    return {
        "@@PROJECT_TITLE@@": record["title"],
        "@@PROJECT_SLUG@@": record["slug"],
        "@@DOMAIN@@": record["domain"],
        "@@SUBDOMAIN@@": record["subdomain"],
        "@@DIFFICULTY@@": record["difficulty"],
        "@@DURATION_HOURS@@": record["duration_short"],
        "@@DESCRIPTION@@": record["description"],
        "@@TOPIC_NAME@@": topic["name"],
        "@@TOPIC_CONCEPT@@": topic["concept"],
        "@@REAL_WORLD_USE@@": topic["real_world_use"],
        "@@ALGORITHM@@": algo,
        "@@COMPLEXITY@@": meta["complexity"],
        "@@ENTRYPOINT@@": ENTRYPOINT,
        "@@FILE_TABLE@@": file_table,
        "@@COMPONENT_TABLE@@": component_table,
        "@@CLASS_TABLE@@": class_table,
        "@@FUNCTION_TABLE@@": function_table,
        "@@PARAM_TABLE@@": param_table,
        "@@DATA_FLOW@@": data_flow,
        "@@RUN_COMMANDS@@": run_commands,
        "@@FEATURES@@": features_block,
        "@@OUTPUT_SHAPE@@": meta["output_shape"],
        "@@DEMO_SCRIPT@@": demo_script,
        "@@QA@@": qa_block,
        "@@TALKING_POINTS@@": talking_points,
        "@@EXTENSIONS@@": extensions,
        "@@RESUME_BULLET@@": resume_bullet,
        "@@PITCH@@": pitch,
        "@@TECH_STACK@@": ", ".join(meta["tech_stack"]),
        "@@STORAGE_NOTE@@": meta["storage_note"],
        "@@SCALING_NOTE@@": meta["scaling_note"],
        "@@TRADEOFF_NOTE@@": meta["tradeoff_note"],
        "@@FAILURE_NOTE@@": meta["failure_note"],
    }


def render_doc_files(record, meta, doc_templates):
    """Render README.md + docs/*.md. Returns {relpath: content}."""
    blocks = build_doc_blocks(record, meta)
    code_subs = code_level_subs(record)
    out = {}
    for tpl_name, relpath in DOC_TPL_MAP:
        text = doc_templates[tpl_name]
        for k, v in blocks.items():
            text = text.replace(k, v)
        # second pass: meta.json text itself may embed code-level
        # placeholders (e.g. @@TOPIC_PARAMS@@ inside a QA answer)
        for k, v in code_subs.items():
            text = text.replace(k, v)
        assert "@@" not in text, \
            "unrendered placeholder in {}/{}".format(record["slug"], relpath)
        out[relpath] = text
    return out


def render_project_files(record, type_data, doc_templates):
    """Render every file of one project. Returns {relpath: content}."""
    files = render_code_files(record, type_data)
    files.update(render_doc_files(record, type_data["meta"], doc_templates))
    return files


# ----------------------------------------------------------------- writing ---

def project_dir(record):
    return os.path.join(PROJECTS_DIR, record["domain"],
                        record["subdomain"], record["slug"])


def write_project(root, record, files):
    """Write one project's files under <root>/projects/... (root=ROOT normally)."""
    base = os.path.join(root, "projects", record["domain"],
                        record["subdomain"], record["slug"])
    for relpath, content in files.items():
        full = os.path.join(base, relpath)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(content)
    return base


def write_indexes(records):
    os.makedirs(INDEXES_DIR, exist_ok=True)
    by_domain = {}
    for r in records:
        by_domain.setdefault(r["domain"], {}).setdefault(
            r["subdomain"], []).append(r)
    for domain in sorted(by_domain):
        lines = ["# {} — project index".format(domain), ""]
        for sub in sorted(by_domain[domain]):
            projs = sorted(by_domain[domain][sub], key=lambda x: x["slug"])
            lines.append("## {} ({} projects)".format(sub, len(projs)))
            lines.append("")
            lines.append("| Project | Type | Difficulty | Duration |")
            lines.append("|---|---|---|---|")
            for r in projs:
                link = "../{}/".format(r["path"])
                lines.append("| [{}]({}) | {} | {} | {} |".format(
                    r["title"], link, r["type"], r["difficulty"], r["duration"]))
            lines.append("")
        with open(os.path.join(INDEXES_DIR, domain + ".md"),
                  "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    return by_domain


def write_project_index(records):
    by_domain = {}
    for r in records:
        d = by_domain.setdefault(r["domain"], {"total": 0, "subs": {}})
        d["total"] += 1
        d["subs"][r["subdomain"]] = d["subs"].get(r["subdomain"], 0) + 1
    lines = ["# Project Index — {:,} real, runnable Python projects".format(
        len(records)), ""]
    lines.append("## Domains")
    lines.append("")
    for domain in sorted(by_domain):
        lines.append("- [{}](indexes/{}.md) — {:,} projects".format(
            domain, domain, by_domain[domain]["total"]))
    lines.append("")
    lines.append("## Totals by domain")
    lines.append("")
    lines.append("| Domain | Subdomains | Projects |")
    lines.append("|---|---|---|")
    for domain in sorted(by_domain):
        lines.append("| {} | {} | {:,} |".format(
            domain, len(by_domain[domain]["subs"]),
            by_domain[domain]["total"]))
    lines.append("| **Total** | **{}** | **{:,}** |".format(
        sum(len(v["subs"]) for v in by_domain.values()), len(records)))
    lines.append("")
    lines.append("## Projects by subdomain")
    lines.append("")
    lines.append("| Subdomain | Domain | Projects |")
    lines.append("|---|---|---|")
    for sub in QUOTAS:
        domain = next(r["domain"] for r in records if r["subdomain"] == sub)
        n = sum(1 for r in records if r["subdomain"] == sub)
        lines.append("| {} | {} | {:,} |".format(sub, domain, n))
    lines.append("")
    with open(os.path.join(ROOT, "PROJECT_INDEX.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# -------------------------------------------------------------------- main ---

def main():
    topics = load_topics()
    types = load_types()
    doc_templates = load_doc_templates()

    print("selecting combos...", flush=True)
    per_sub = select_all_combos(topics)
    fallbacks = sorted(sub for sub in QUOTAS if per_sub[sub][1])
    skipped = {sub: per_sub[sub][2] for sub in QUOTAS if per_sub[sub][2]}
    if fallbacks:
        print("pass-2 fallback used for: {}".format(", ".join(fallbacks)))
    for sub, sk in skipped.items():
        print("WARNING: skipped {} forbidden-token combo(s) in {}: {}".format(
            len(sk), sub,
            ", ".join("{}-{}-{}".format(c["topic"]["slug_base"], c["type"],
                                       c["difficulty"]) for c in sk)))

    print("rendering + writing {:,} projects...".format(TOTAL_QUOTA), flush=True)
    records = []
    used_slugs = set()
    catalog_meta = {}  # slug -> (tech_stack, resume_bullet)
    done = 0
    oversize = 0
    for sub in QUOTAS:  # deterministic subdomain order
        selected, _, _ = per_sub[sub]
        for combo in selected:
            slug = unique_slug(combo, used_slugs)
            record = build_record(combo, slug, types[combo["type"]]["meta"])
            type_data = types[combo["type"]]
            files = render_project_files(record, type_data, doc_templates)
            base = write_project(ROOT, record, files)
            size = sum(len(c.encode("utf-8")) for c in files.values())
            if size > 25 * 1024:
                oversize += 1
                print("WARNING: project dir > 25KB: {} ({} bytes)".format(
                    record["path"], size))
            blocks = build_doc_blocks(record, type_data["meta"])
            catalog_meta[slug] = (type_data["meta"]["tech_stack"],
                                  blocks["@@RESUME_BULLET@@"])
            records.append(record)
            done += 1
            if done % 1000 == 0:
                print("  ...{:,}/{:,} projects".format(done, TOTAL_QUOTA),
                      flush=True)

    slugs = [r["slug"] for r in records]
    assert len(slugs) == len(set(slugs)) == TOTAL_QUOTA, \
        "final slug check failed: {} records, {} unique".format(
            len(slugs), len(set(slugs)))
    print("wrote {:,} projects, {} unique slugs, {} oversize warnings".format(
        len(records), len(set(slugs)), oversize))

    print("writing catalogs...", flush=True)
    os.makedirs(CATALOG_DIR, exist_ok=True)
    by_domain = {}
    for r in records:
        by_domain.setdefault(r["domain"], []).append(r)
    for domain in sorted(by_domain):
        entries = []
        for r in sorted(by_domain[domain], key=lambda x: x["slug"]):
            tech_stack, resume_bullet = catalog_meta[r["slug"]]
            entries.append({
                "slug": r["slug"],
                "title": r["title"],
                "domain": r["domain"],
                "subdomain": r["subdomain"],
                "type": r["type"],
                "difficulty": r["difficulty"],
                "duration_hours": r["duration"],
                "description": r["description"],
                "tech_stack": tech_stack,
                "path": r["path"],
                "resume_bullet": resume_bullet,
                "tags": [r["domain"], r["subdomain"], r["type"],
                         r["difficulty"]],
            })
        with open(os.path.join(CATALOG_DIR, domain + ".json"),
                  "w", encoding="utf-8") as fh:
            json.dump(entries, fh, indent=1)
            fh.write("\n")
    print("catalogs: {}".format(", ".join(
        "{} ({} projects)".format(d, len(v)) for d, v in sorted(by_domain.items()))))

    print("writing indexes...", flush=True)
    write_indexes(records)
    write_project_index(records)
    print("done: {:,} projects, {:,} catalog domains, PROJECT_INDEX.md written".format(
        len(records), len(by_domain)))


if __name__ == "__main__":
    main()
