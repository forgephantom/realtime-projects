# realtime-projects

A library of **12,000 real, runnable, documented projects** written in Python. Every project is a complete working program: it runs with the standard library alone, ships with a seeded demo that reproduces byte-for-byte, and is documented the way a professional team documents software — README, high-level design, low-level design, runbook, and presentation guide. No stubs, no placeholders, no "exercise left to the reader."

## Domain coverage

| Domain | Projects |
|---|---|
| computer_science | 6,600 |
| biology | 1,000 |
| physics | 800 |
| chemistry | 800 |
| mathematics | 700 |
| healthcare | 800 |
| electronics_engineering | 700 |
| environmental_science | 600 |
| **Total** | **12,000** |

The majority are computer science because that is where runnable, dependency-free projects compose best; the remaining seven domains carry the same quality bar — every project runs, every demo is seeded, every document exists.

## Repo layout

```
realtime-projects/
├── README.md                 # this file
├── LICENSE                   # MIT
├── COPYRIGHT.md                # originality pledge
├── CONTRIBUTING.md             # how to add a project
├── docs/
│   ├── REPO_ARCHITECTURE.md    # how the repo is organized
│   ├── EXPORT_TO_PDF.md        # turn any project's docs into a PDF
│   ├── PRESENTING_GUIDE.md     # how to demo a project in 5 minutes
│   └── RESUME_GUIDE.md         # how to list these projects on a resume
├── topics/                     # machine-readable topic catalog (one JSON per subdomain)
├── templates/docs/             # doc templates the generator fills per project
├── tools/
│   └── generate.py             # the project generator (topics × templates → projects)
└── projects/
    └── <domain>/
        └── <subdomain>/
            └── <project-slug>/
                ├── README.md
                ├── <entrypoint>.py
                └── docs/
                    ├── ARCHITECTURE.md
                    ├── DESIGN.md
                    ├── RUNBOOK.md
                    └── PRESENTATION.md
```

## Run any project in 30 seconds

```bash
# pick any project directory
cd projects/computer_science/algorithms/bubble-sort-visualizer

# the demo runs with zero setup — Python 3.8+, no pip install
python3 main.py

# every flag is documented in the CLI itself
python3 main.py --help
```

That is the entire contract: if it is in `projects/`, it runs.

## How to present a project

Each project ships a `docs/PRESENTATION.md` with a 60-second pitch, architecture talking points, a copy-paste resume bullet, and an interview Q&A. For general guidance on structuring a live demo, read [docs/PRESENTING_GUIDE.md](docs/PRESENTING_GUIDE.md).

## PDF export

Any project's full document set (README + all four docs/) can be exported to a single PDF with one command. See [docs/EXPORT_TO_PDF.md](docs/EXPORT_TO_PDF.md).

## Contributing

New projects are added through the generator, not by hand: add a topic to `topics/<subdomain>.json` and run `tools/generate.py`. Full instructions and the code/docs standards are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE) and the originality pledge in [COPYRIGHT.md](COPYRIGHT.md).
