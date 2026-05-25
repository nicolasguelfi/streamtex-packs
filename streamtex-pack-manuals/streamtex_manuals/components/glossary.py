"""
# Glossary — Term/definition reference list

## Visual

```
┌──────────────────────────────────────────────────────┐
│  Glossary                                           │
│                                                      │
│  ▾ A                                                 │
│    Agent      — An autonomous program that …        │
│    Attention  — A neural-network primitive …        │
│                                                      │
│  ▾ B                                                 │
│    Bundle     — A namespaced set of styles …        │
└──────────────────────────────────────────────────────┘
```

A vertical, alphabetically-grouped list of terms and definitions.
Similar in spirit to `term_definition_list` (pack-design) but adds
alphabetical grouping headers and per-letter TOC anchors so a long
glossary is navigable from the sidebar.

## Structure

- Section title via `titles.section`.
- For each letter group: a small letter heading rendered as a TOC entry
  at level +2.
- For each entry: bold term + em-dash + definition, sharing one line.

## Styling rules

- Letter heading: `titles.subtitle` + accent color from the design
  system, lowercased letter rendered uppercase via `text-transform`.
- Term: `body.paragraph` + bold.
- Definition: `body.paragraph`.

## Extrapolation rules

### INVARIANTS
- Entries are sorted alphabetically inside this component (case-folded);
  do not assume input order is preserved.
- Each letter group must have ≥ 1 entry — empty letters are skipped.

### PARAMS
- `title`: section heading (defaults to "Glossary").
- `entries`: list of `(term, definition)` tuples.
- `case_fold`: if True (default), letter grouping uses the first
  character of `term.upper()`. Non-ASCII letters fall under their
  ASCII-folded equivalent if `unicodedata` normalization succeeds, else
  they are grouped under "#".

### INTERDITS
- No cross-references / "see also" — those go in `references_list`.
- No images / inline media in definitions.

## When to use

- End-of-manual glossary for an extended training material.
- Appendix in a long-form manual.

## When NOT to use

- For an unordered short list (use `term_definition_list`).
- For citations / references (use `references_list`).

## Design system bundles required

- `titles.section` (glossary title)
- `titles.subtitle` (letter group headings)
- `body.paragraph` (term + definition)
- `colors.accent` (letter heading color)
"""

import unicodedata
from collections import defaultdict

from streamtex import st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "glossary",
    "description": "Alphabetically grouped term/definition list with per-letter TOC anchors.",
    "tags": ["glossary", "reference", "manual", "training"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "titles.section",
        "titles.subtitle",
        "body.paragraph",
        "colors.accent",
    ],
    "granularity": "composition",
}


def glossary(
    *,
    design_system,
    entries: list[tuple[str, str]],
    title: str = "Glossary",
    case_fold: bool = True,
) -> None:
    """Render a glossary block: section title + alphabetically grouped terms."""
    letter_style = Style.create(
        design_system.titles.subtitle + design_system.colors.accent + "text-transform: uppercase;",
        "gl_letter",
    )
    term_style = Style.create(
        design_system.body.paragraph + StxStyles.bold,
        "gl_term",
    )

    grouped: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for term, definition in entries:
        letter = _group_letter(term, case_fold)
        grouped[letter].append((term, definition))

    st_write(design_system.titles.section, title, tag=t.h2, toc_lvl="+1")
    st_space("v", 1)

    for letter in sorted(grouped.keys()):
        st_write(letter_style, letter, tag=t.h3, toc_lvl="+2")
        st_space("v", 0.5)
        for term, definition in sorted(grouped[letter], key=lambda pair: pair[0].lower()):
            st_write(term_style, f"{term} — ", tag=t.span)
            st_write(design_system.body.paragraph, definition, tag=t.span)
            st_space("v", 0.3)
        st_space("v", 0.6)


def _group_letter(term: str, case_fold: bool) -> str:
    if not term:
        return "#"
    first = term[0]
    if case_fold:
        first = first.upper()
    try:
        ascii_folded = unicodedata.normalize("NFKD", first).encode("ascii", "ignore").decode("ascii")
        if ascii_folded.isalpha():
            return ascii_folded.upper() if case_fold else ascii_folded
    except UnicodeError:
        pass
    return "#"
