# Repository Architecture

## How the repo is organized

The repository has two layers: the **authoring layer** (topics, templates, and
the generator) and the **output layer** (the 12,000 generated projects).

```
realtime-projects/
├── topics/                  # AUTHORING: the topic catalog
│   ├── <subdomain>.json     # one JSON file per subdomain
├── templates/
│   └── docs/                # AUTHORING: five doc templates (.tpl)
├── tools/
│   └── generate.py          # AUTHORING: the generator
├── projects/                # OUTPUT: generated projects, never edited by hand
│   └── <domain>/<subdomain>/<project-slug>/
├── docs/                    # OUTPUT-adjacent: hand-written repo-level guides
└── README.md, LICENSE, COPYRIGHT.md, CONTRIBUTING.md
```

The rule is one-directional: the authoring layer feeds the output layer.
Nobody edits `projects/` by hand — fixes go into the topic, the template, or
the generator, and then the project is regenerated.

## The generator pipeline

`tools/generate.py` combines **topics × templates → projects**:

1. **Topics** — Each entry in `topics/<subdomain>.json` is a structured spec:
   title, slug, domain, subdomain, difficulty, duration, the topic name and
   concept, real-world use, description, tech stack, entrypoint, algorithm,
   complexity, key parameters, and presentation material (features, pitch,
   talking points, resume bullet, Q&A). All prose is authored originally.
2. **Templates** — `templates/docs/*.tpl` hold the document skeletons with
   `@@PLACEHOLDER@@` tokens. The shared set covers identity, concept, and
   tech (e.g. `@@PROJECT_TITLE@@`, `@@ALGORITHM@@`); the block tokens
   (`@@FILE_TABLE@@`, `@@COMPONENT_TABLE@@`, `@@DEMO_SCRIPT@@`, ...) are
   rendered as Markdown tables and code blocks from the topic's structured data.
3. **Generation** — For each topic, the generator writes the project source
   (stdlib-only Python with a seeded demo and `--help` CLI contract) and
   renders all five documents from the templates. Generation is deterministic:
   the same catalog commit produces the same tree.

## Catalog format

A topic entry is a JSON object. The essential fields:

```json
{
  "slug": "k-means-customer-segmentation",
  "title": "K-Means Customer Segmentation",
  "domain": "computer_science",
  "subdomain": "machine_learning",
  "difficulty": "intermediate",
  "duration_hours": 6,
  "topic_name": "K-means clustering",
  "topic_concept": "...",
  "real_world_use": "...",
  "description": "...",
  "tech_stack": ["Python 3.8+", "stdlib only"],
  "entrypoint": "main.py",
  "algorithm": "...",
  "complexity": "O(n·k·i)",
  "key_params": [
    {"name": "k", "type": "int", "default": 3, "meaning": "..."}
  ],
  "features": ["..."],
  "resume_bullet": "...",
  "pitch": "...",
  "talking_points": ["..."],
  "qa": [{"q": "...", "a": "..."}]
}
```

The generator validates every entry before building: required fields present,
slugs unique, entrypoints and file names consistent, and every cross-reference
between docs and code resolvable.

## Project directory contract

Every project under `projects/` contains exactly:

- `README.md` — overview, features, how to run, sample output
- `<entrypoint>.py` — the runnable program
- `docs/ARCHITECTURE.md` — high-level design
- `docs/DESIGN.md` — low-level design
- `docs/RUNBOOK.md` — demo script and troubleshooting
- `docs/PRESENTATION.md` — pitch, talking points, resume bullet, interview Q&A

If a project is missing any of these, it is a generator bug — fix the
generator, not the project.
