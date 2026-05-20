"""
# Term/definition list — Two-column glossary-style term/definition rows

## Visual

```
   API           Application Programming Interface
   REST          Representational State Transfer
   GraphQL       Query language for APIs
```

Compact two-column layout where the term sits in a fixed-width left column
and the definition flows in the right column.

## Structure

- A `st_grid` with two columns: term (auto / fixed) + definition (1fr).
- Each row: `st_write(titles.subtitle, term)` + `st_write(body.paragraph, def)`.

## Styling rules

| Element | Style |
|---|---|
| term | titles.subtitle |
| definition | body.paragraph |
| separator | body.code (optional dotted border) |

## Extrapolation rules

### INVARIANTS
- Same column widths for every row in a list.
- Terms are short (1-3 words); long terms break visual rhythm.

### PARAMS
- ordered: alphabetical vs introduced-order
- emphasis: optional inline_emphasis on the term

### INTERDITS
- No more than 12 rows — split into multiple lists or use a glossary block.
- No multi-paragraph definitions.

## When to use

- A glossary slide.
- A vocabulary-introduction slide for a new domain.

## When NOT to use

- For comparing two options across criteria (use comparison_table).
- For freeform notes (use a body paragraph).

## Design system bundles required

- titles.subtitle
- body.paragraph
"""

from streamtex import st_grid, st_write

__component_meta__ = {
    "name": "term_definition_list",
    "description": "Compact two-column term/definition glossary list.",
    "tags": ["glossary", "list", "definition"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.subtitle", "body.paragraph"],
    "granularity": "composition",
}


def term_definition_list(*, design_system, items: list = None) -> None:
    """Render rows of (term, definition) pairs."""
    items = items or []
    with st_grid(cols="auto 1fr", gap="12px 24px") as g:
        for term, definition in items:
            with g.cell():
                st_write(design_system.titles.subtitle, term)
            with g.cell():
                st_write(design_system.body.paragraph, definition)
