# CLAUDE.md

Jekyll-based GitHub Pages academic website for Xiangjun Tang (Postdoc Fellow at KAUST).

## Key Commands

```bash
bundle exec jekyll serve                    # local dev server
python markdown_generator/pubsFromBib.py   # regenerate _publications/ from source folders
python markdown_generator/showcase_generator.py  # regenerate showcase index
```

## Common Tasks

### Add or update a paper

All paper data lives in `assets/files/publications/<FolderName>/`. **Never edit `_publications/` directly — it is auto-generated.**

1. Edit files in the paper folder (see structure below)
2. Run `python markdown_generator/pubsFromBib.py`

**Folder structure:**

| File | Description |
|------|-------------|
| `citation.txt` | BibTeX entry (required) — source of title, authors, year, venue |
| `extra.json` | Extra links and metadata (optional) |
| `teaser.*` | Cover image (any filename containing "teaser") |
| `main.pdf` | Auto-generates "Paper" link |
| `appendix.pdf` | Auto-generates "Supplementary" link |
| `content.md` | Body content for the paper page |

### Mark a paper as Oral (or other highlight)

Add `"highlight": "Oral"` to the paper's `extra.json`, then rerun the script. This generates `highlight: "Oral"` and `pub_ab: "CVPR Oral"` in the markdown.

```json
{
    "highlight": "Oral",
    "Arxiv": "...",
    "Project": "..."
}
```

### Add external links to a paper

Add keys to `extra.json`. Keys are auto-capitalized and truncated at `_`. Display order: Paper → Arxiv → Project → Supplementary → Video → Code.

### Add a new co-author's homepage link

Edit the `authors_info` dict in `markdown_generator/pubsFromBib.py`.

### Mark a paper as selected (shown on homepage)

Automatic: any paper where `Xiangjun Tang` is the **first author** is marked `selected: true`.

## Key Config Files

- `_data/profile.yml` — name, position, bio, social links
- `_data/display.yml` — which sections appear on homepage
- `_data/navigation.yml` — nav bar
- `_data/authors.yml` — author link mapping (legacy; script uses `authors_info` in `pubsFromBib.py`)
- `assets/css/global.css` — custom styles
