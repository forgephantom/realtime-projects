#!/usr/bin/env python3
"""Expansion run: +2,800 projects (new ai + business_analyst domains, healthcare x2).

Reuses tools/generate.py's functions; never modifies generate.py, existing
topics, existing templates, or any existing project. Run from repo root:
    python3 tools/expand.py
"""

import json
import os
import sys

sys.path.insert(0, "tools")
import generate as gen  # noqa: E402

NEW_QUOTAS = {
    "llm_applications": 150, "ai_agents": 150, "rag_systems": 150,
    "prompt_engineering": 120, "vector_databases": 120,
    "model_evaluation": 120, "generative_ai": 120, "mlops": 90,
    "ai_safety_redteaming": 90, "mcp_integrations": 90,
    "medical_imaging": 150, "drug_discovery": 150, "genomics": 150,
    "telemedicine": 120, "hospital_operations": 120, "mental_health_tech": 110,
    "kpi_dashboards": 150, "financial_modeling": 150,
    "data_visualization": 120, "requirements_management": 120,
    "process_modeling": 100, "market_research": 80, "stakeholder_reporting": 80,
}
assert sum(NEW_QUOTAS.values()) == 2800, "NEW_QUOTAS must sum to 2,800"

AI_SUBS = {"llm_applications", "ai_agents", "rag_systems", "prompt_engineering",
           "vector_databases", "model_evaluation", "generative_ai", "mlops",
           "ai_safety_redteaming", "mcp_integrations"}
HEALTH_SUBS = {"medical_imaging", "drug_discovery", "genomics", "telemedicine",
               "hospital_operations", "mental_health_tech"}
BA_SUBS = {"kpi_dashboards", "financial_modeling", "data_visualization",
           "requirements_management", "process_modeling", "market_research",
           "stakeholder_reporting"}

# Old subdomain quotas hardcoded from tools/generate.py (for PROJECT_INDEX.md)
OLD_QUOTAS = {
    "web_development": 800, "machine_learning": 800, "data_science": 700,
    "software_engineering": 600, "cybersecurity": 600, "devops_sre": 600,
    "databases": 400, "computer_networks": 400,
    "algorithms_data_structures": 400, "cloud_computing": 350,
    "data_engineering": 350, "mobile_development": 250, "game_development": 200,
    "operating_systems": 150, "bioinformatics": 350, "genetics": 250,
    "ecology": 200, "cell_biology": 200, "physics": 800, "chemistry": 800,
    "mathematics": 700, "health_informatics": 300, "biostatistics": 250,
    "clinical_tools": 250, "electronics_engineering": 700,
    "environmental_science": 600,
}


def main():
    print("loading...", flush=True)
    topics = gen.load_topics()
    types = gen.load_types()
    doc_templates = gen.load_doc_templates()

    # Seed used_slugs from ALL existing catalog entries (12,000 old projects)
    used_slugs = set()
    catalog_dir = os.path.join(gen.ROOT, "catalog")
    for fname in sorted(os.listdir(catalog_dir)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(catalog_dir, fname), encoding="utf-8") as fh:
            for entry in json.load(fh):
                used_slugs.add(entry["slug"])
    print("seeded {} existing slugs".format(len(used_slugs)), flush=True)

    # Select combos per new subdomain (aborts with deficit report if unreachable)
    gen.QUOTAS = dict(NEW_QUOTAS)
    per_sub = {}
    for sub in NEW_QUOTAS:
        per_sub[sub] = gen.select_combos_for_subdomain(sub, topics[sub])
    print("combo selection ok", flush=True)

    # Render + write new projects in NEW_QUOTAS order
    new_records = []      # full record dicts
    catalog_meta = {}     # slug -> (tech_stack, resume_bullet)
    oversize = 0
    done = 0
    for sub in NEW_QUOTAS:  # deterministic subdomain order
        selected, _, _ = per_sub[sub]
        for combo in selected:
            slug = gen.unique_slug(combo, used_slugs)
            type_data = types[combo["type"]]
            record = gen.build_record(combo, slug, type_data["meta"])
            files = gen.render_project_files(record, type_data, doc_templates)
            base = gen.write_project(gen.ROOT, record, files)
            size = sum(len(c.encode("utf-8")) for c in files.values())
            if size > 25 * 1024:
                oversize += 1
                print("WARNING: project dir > 25KB: {} ({} bytes)".format(
                    record["path"], size))
            blocks = gen.build_doc_blocks(record, type_data["meta"])
            catalog_meta[slug] = (type_data["meta"]["tech_stack"],
                                  blocks["@@RESUME_BULLET@@"])
            new_records.append(record)
            done += 1
            if done % 500 == 0:
                print("  ...{:,}/{:,} new projects".format(done, 2800),
                      flush=True)

    slugs = [r["slug"] for r in new_records]
    assert len(slugs) == len(set(slugs)) == 2800, \
        "new slug check failed: {} records, {} unique".format(
            len(slugs), len(set(slugs)))
    print("wrote {:,} new projects, {} unique, {} oversize warnings".format(
        len(new_records), len(set(slugs)), oversize))

    # Catalog entries in the exact format generate.main() uses
    def entry_for(r):
        tech_stack, resume_bullet = catalog_meta[r["slug"]]
        return {
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
            "tags": [r["domain"], r["subdomain"], r["type"], r["difficulty"]],
        }

    by_domain = {}
    for r in new_records:
        by_domain.setdefault(r["domain"], []).append(r)
    new_entries = {d: [entry_for(r) for r in sorted(v, key=lambda x: x["slug"])]
                   for d, v in by_domain.items()}

    with open(os.path.join(catalog_dir, "ai.json"), "w",
              encoding="utf-8") as fh:
        json.dump(new_entries["ai"], fh, indent=1)
        fh.write("\n")
    with open(os.path.join(catalog_dir, "business_analyst.json"), "w",
              encoding="utf-8") as fh:
        json.dump(new_entries["business_analyst"], fh, indent=1)
        fh.write("\n")
    hc_path = os.path.join(catalog_dir, "healthcare.json")
    with open(hc_path, encoding="utf-8") as fh:
        hc_old = json.load(fh)
    hc_all = sorted(hc_old + new_entries["healthcare"],
                    key=lambda e: e["slug"])
    with open(hc_path, "w", encoding="utf-8") as fh:
        json.dump(hc_all, fh, indent=1)
        fh.write("\n")
    print("catalogs: ai={} business_analyst={} healthcare={} (old {})".format(
        len(new_entries["ai"]), len(new_entries["business_analyst"]),
        len(hc_all), len(hc_old)))

    # Minimal record dicts for write_indexes (keys it needs)
    def minimal(e):
        return {"domain": e["domain"], "subdomain": e["subdomain"],
                "slug": e["slug"], "title": e["title"], "type": e["type"],
                "difficulty": e["difficulty"], "duration": e["duration_hours"],
                "path": e["path"]}

    index_records = ([minimal(e) for e in new_entries["ai"]] +
                     [minimal(e) for e in new_entries["business_analyst"]] +
                     [minimal(e) for e in hc_all])
    gen.write_indexes(index_records)
    print("indexes written for ai, business_analyst, healthcare", flush=True)

    # PROJECT_INDEX.md over ALL domains: load every catalog entry
    all_entries = []
    for fname in sorted(os.listdir(catalog_dir)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(catalog_dir, fname), encoding="utf-8") as fh:
            all_entries.extend(json.load(fh))
    all_records = [minimal(e) for e in all_entries]
    gen.QUOTAS = {**OLD_QUOTAS, **NEW_QUOTAS}
    gen.write_project_index(all_records)
    print("PROJECT_INDEX.md written from {:,} total records".format(
        len(all_records)), flush=True)

    # README.md updates
    readme_path = os.path.join(gen.ROOT, "README.md")
    with open(readme_path, encoding="utf-8") as fh:
        readme = fh.read()
    readme = readme.replace("12,000", "14,800")
    readme = readme.replace("projects-12%2C000-blue", "projects-14%2C800-blue")
    readme = readme.replace("| healthcare | 800 |", "| healthcare | 1,600 |")
    total_line = "| **Total** | **14,800** |"
    assert total_line in readme, "Total row not found after replacement"
    readme = readme.replace(
        total_line,
        "| ai | 1,200 |\n| business_analyst | 800 |\n" + total_line)
    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write(readme)
    print("README.md updated", flush=True)

    # Per-subdomain count report
    print("\nnew subdomain counts:")
    for sub in NEW_QUOTAS:
        n = sum(1 for r in new_records if r["subdomain"] == sub)
        print("  {}: {}".format(sub, n))
    print("\nexpansion complete: {:,} new projects".format(len(new_records)))


if __name__ == "__main__":
    main()
