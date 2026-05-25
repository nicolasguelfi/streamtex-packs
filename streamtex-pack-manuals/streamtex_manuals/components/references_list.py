"""
# References list — Bibliographic references block

## Visual

```
┌──────────────────────────────────────────────────────┐
│  References                                         │
│                                                      │
│  [1] Smith, J. (2024). Foo theory. Journal X, 12.   │
│      https://doi.org/…                              │
│  [2] Doe, A. (2025). Bar applied. Conference Y.     │
│      https://…                                      │
└──────────────────────────────────────────────────────┘
```

A numbered list of bibliographic references, each with author, title,
venue/year, and optional URL. Designed to pair with `streamtex.bib`
citations (rendered inline via `cite("smith2024")`) so a manual can
have both inline cites and a full reference list at the back.

## Structure

- Section title via `titles.section`.
- For each entry: bracketed index, author + title + venue, then optional
  URL on its own line.

## Styling rules

- Index `[N]`: `body.paragraph` + bold + accent color.
- Citation body: `citation.source` (small + italic + muted).
- URL line: `body.code` (monospace, dimmed background).

## Extrapolation rules

### INVARIANTS
- Indices are 1-based and follow input order.
- One reference per `(citation_text, url)` tuple; multi-paragraph
  references are NOT supported — pre-format them upstream.

### PARAMS
- `title`: section heading (defaults to "References").
- `entries`: list of `(citation_text, url)` tuples; `url` can be `None`.

### INTERDITS
- No automatic BibTeX parsing — pre-format your entries upstream
  (e.g. via `streamtex.bib.cite_list` or a custom formatter).
- No "see also" cross-links inside an entry.

## When to use

- End of a manual or training session to list all cited works.
- Appendix in a long-form manual.

## When NOT to use

- For inline citations (use `cite` from streamtex-pack-design).
- For a glossary of terms (use `glossary`).

## Design system bundles required

- `titles.section`
- `body.paragraph`
- `citation.source`
- `body.code`
- `colors.accent`
"""

from streamtex import st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "references_list",
    "description": "Numbered list of bibliographic references with optional URLs.",
    "tags": ["references", "bibliography", "manual", "training"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "titles.section",
        "body.paragraph",
        "citation.source",
        "body.code",
        "colors.accent",
    ],
    "granularity": "composition",
}


def references_list(
    *,
    design_system,
    entries: list[tuple[str, str | None]],
    title: str = "References",
) -> None:
    """Render a numbered references list with optional URLs."""
    index_style = Style.create(
        design_system.body.paragraph + StxStyles.bold + design_system.colors.accent,
        "rl_index",
    )

    st_write(design_system.titles.section, title, tag=t.h2, toc_lvl="+1")
    st_space("v", 1)

    for idx, (citation_text, url) in enumerate(entries, start=1):
        st_write(index_style, f"[{idx}] ", tag=t.span)
        st_write(design_system.citation.source, citation_text, tag=t.span)
        if url:
            st_space("v", 0.2)
            st_write(design_system.body.code, url, tag=t.div)
        st_space("v", 0.6)
