# Exporting a Project's Docs to PDF

Any project's full document set — README plus all four `docs/` files — can be
combined into a single PDF with one command using
[pandoc](https://pandoc.org) (a free, open-source document converter).

## Install pandoc (one time)

```bash
# Debian / Ubuntu
sudo apt install pandoc wkhtmltopdf

# macOS
brew install pandoc wkhtmltopdf
```

`wkhtmltopdf` supplies the PDF engine pandoc uses in the command below. Any
LaTeX engine works too, but the wkhtmltopdf route needs no LaTeX installation.

## One-command export

From the repository root:

```bash
cd projects/<domain>/<subdomain>/<project-slug>

pandoc README.md docs/ARCHITECTURE.md docs/DESIGN.md docs/RUNBOOK.md \
  docs/PRESENTATION.md \
  -o <project-slug>-docs.pdf \
  --pdf-engine=wkhtmltopdf \
  --metadata title="<Project Title> — Documentation" \
  -V margin-top=20mm -V margin-bottom=20mm \
  -V margin-left=18mm -V margin-right=18mm
```

This produces `<project-slug>-docs.pdf` in the project folder: a single
document with the README first, then architecture, design, runbook, and
presentation guide, in that order.

## Options worth knowing

- **Table of contents:** add `--toc --toc-depth=2` to generate a TOC page.
- **Different styling:** add `-c style.css` with your own CSS to control fonts
  and headings (wkhtmltopdf honors most CSS).
- **Page numbers and header:** `-V header-html=header.html` puts a running
  header on every page.

## Troubleshooting

| Problem | Fix |
|---|---|
| `pandoc: command not found` | Install pandoc (see above) and open a new terminal |
| `wkhtmltopdf: cannot connect to X server` | Install `xvfb` and run pandoc under `xvfb-run`, or use the `--enable-local-file-access` flag |
| Missing glyphs / boxes in the PDF | The system font lacks coverage; install a full Unicode font (e.g. DejaVu) and reference it in a CSS file |
| PDF looks fine but links are dead | Internal `.md` links become plain text in print — this is expected; the PDF is a reading artifact, not a website |

The generated PDF is a convenience artifact. The Markdown files in the repo
remain the source of truth.
