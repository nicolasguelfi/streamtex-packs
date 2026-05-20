"""
# Cite — Bibliographic source attribution

## Visual

```
   — *Smith et al., 2024 — Nature 612, 491*
```

A small inline or bottom-of-block citation rendered in muted italic style,
used to attribute a quote, statistic, or claim.

## Structure

- A single-line `st_write` using `citation.source` (italic, muted).
- Optional `citation.author` style for author-only attribution.

## Styling rules

| Element | Style | Notes |
|---|---|---|
| source | citation.source | italic, muted, smaller than body |
| author | citation.author | non-italic alternative |

## Extrapolation rules

### INVARIANTS
- One short line, never multi-line.
- Always muted to recede behind the cited content.

### PARAMS
- source: full bibliographic string
- prefix: optional "—" or "Source:" sigil

### INTERDITS
- No bullet points inside a cite block.
- No emphasis colors — citations stay muted.

## When to use

- Below a hero stat to credit the source.
- After a quote in a callout.

## When NOT to use

- For long quoted passages — use a paragraph with `body.emphasis` instead.
- For inline author attribution within a sentence — write it inline.

## Design system bundles required

- citation.source
- citation.author
"""

from streamtex import st_write

__component_meta__ = {
    "name": "cite",
    "description": "One-line bibliographic source attribution.",
    "tags": ["citation", "source", "attribution"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["citation.source", "citation.author"],
    "granularity": "primitive",
}


def cite(*, design_system, source: str = "", prefix: str = "— ") -> None:
    """Render a one-line source attribution."""
    st_write(design_system.citation.source, f"{prefix}{source}")
