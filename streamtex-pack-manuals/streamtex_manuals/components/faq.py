"""
# FAQ — Frequently Asked Questions

## Visual

```
┌──────────────────────────────────────────────────────┐
│  Frequently Asked Questions                         │
│                                                      │
│  Q1: How do I install streamtex-pack-design?        │
│      Add it to your stx.toml [[packs]] block …      │
│                                                      │
│  Q2: Which kit should I pick for a new manual?      │
│      `manual-default` covers the …                  │
└──────────────────────────────────────────────────────┘
```

A vertical list of question/answer pairs, each prefixed with the question
number. Used at the end of a manual or training module to surface common
follow-up questions in a scannable format.

## Structure

- Section title via `design_system.titles.section`.
- For each entry: bold question prefixed `Q{n}:`, followed by the answer
  paragraph using `design_system.body.paragraph`.
- Entries separated by a small vertical space.

## Styling rules

- Question style: `body.paragraph` + bold + accent color from the design
  system. Question label (`Q{n}:`) sits inline with the question text.
- Answer style: `body.paragraph` (regular).

## Extrapolation rules

### INVARIANTS
- Questions are numbered starting at 1, in input order.
- Each answer is a single paragraph (no nested lists, no inline images).
  Use a sibling component if richer answer formatting is needed.

### PARAMS
- `title`: section heading (defaults to "Frequently Asked Questions").
- `entries`: list of `(question, answer)` tuples.

### INTERDITS
- No collapse / expand behaviour — the FAQ is fully expanded. For an
  interactive collapsible variant, wrap individual entries in
  `st.expander` at the consumer level.
- No nested or numbered sub-questions inside an answer — split into
  multiple entries instead.

## When to use

- End of a manual chapter as a "common questions" wrap-up.
- Closing slide of a training session for follow-up clarifications.

## When NOT to use

- For terminology definitions — use `glossary` instead.
- For exhaustive reference content — use `references_list` or
  `comparison_table`.

## Design system bundles required

- `titles.section` (FAQ section title)
- `body.paragraph` (question + answer text)
- `colors.accent` (question label color)
"""

from streamtex import st_block, st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "faq",
    "description": "Vertical list of Q&A pairs used for end-of-manual follow-up questions.",
    "tags": ["faq", "qna", "manual", "training"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "titles.section",
        "body.paragraph",
        "colors.accent",
    ],
    "granularity": "composition",
}


def faq(
    *,
    design_system,
    entries: list[tuple[str, str]],
    title: str = "Frequently Asked Questions",
) -> None:
    """Render an FAQ block: section title + numbered Q/A pairs."""
    question_style = Style.create(
        design_system.body.paragraph + StxStyles.bold + design_system.colors.accent,
        "faq_question",
    )

    st_write(design_system.titles.section, title, tag=t.h2, toc_lvl="+1")
    st_space("v", 1)

    for idx, (question, answer) in enumerate(entries, start=1):
        with st_block(StxStyles.none):
            st_write(question_style, f"Q{idx}: {question}", tag=t.div)
            st_space("v", 0.3)
            st_write(design_system.body.paragraph, answer, tag=t.p)
        st_space("v", 0.8)
