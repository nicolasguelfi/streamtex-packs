"""
# Changelog card — Manual / training "what's new" block

## Visual

```
┌──────────────────────────────────────────────────────┐
│  What's new                                         │
│                                                      │
│  ▸ v1.2.0 — 2026-05-23                              │
│      Added FAQ section, trainer profiles            │
│  ▸ v1.1.0 — 2026-04-12                              │
│      Reorganised the deployment chapter             │
└──────────────────────────────────────────────────────┘
```

A vertical list of the most recent changelog entries, each pinned to a
version + date. Used at the start of a manual / training module to
surface what changed since the last revision.

## Structure

- Section title via `titles.section` (defaults to "What's new").
- For each entry: version + date on one line (accent color), then a
  short body paragraph.

## Styling rules

- Version line: `body.paragraph` + bold + accent color, prefixed by `▸`.
- Body: `body.paragraph` (regular).

## Extrapolation rules

### INVARIANTS
- Entries are rendered in the order received — caller is responsible
  for sorting (typically newest first).
- The component shows at most `max_entries` items (default 5).

### PARAMS
- `title`: section heading (defaults to "What's new").
- `entries`: list of `(version, date, summary)` tuples.
- `max_entries`: cap on rendered entries (default 5).

### INTERDITS
- No links per entry — pair with `references_list` if a link to
  release notes is needed.
- No nested change lists — keep each `summary` to ≤ 2 lines.

## When to use

- First content slide of a training material after the cover.
- "Updates" section of a long-form manual.

## When NOT to use

- For an exhaustive changelog (use the project's `CHANGELOG.md`
  directly and link to it from `references_list`).

## Design system bundles required

- `titles.section`
- `body.paragraph`
- `colors.accent`
"""

from streamtex import st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "changelog_card",
    "description": "Vertical list of recent changelog entries with version + date + short summary.",
    "tags": ["changelog", "manual", "training", "updates"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "titles.section",
        "body.paragraph",
        "colors.accent",
    ],
    "granularity": "composition",
}


def changelog_card(
    *,
    design_system,
    entries: list[tuple[str, str, str]],
    title: str = "What's new",
    max_entries: int = 5,
) -> None:
    """Render a "what's new" block with the most recent changelog entries."""
    version_style = Style.create(
        design_system.body.paragraph + StxStyles.bold + design_system.colors.accent,
        "cc_version",
    )

    st_write(design_system.titles.section, title, tag=t.h2, toc_lvl="+1")
    st_space("v", 1)

    for version, date, summary in entries[:max_entries]:
        st_write(version_style, f"▸ {version} — {date}", tag=t.div)
        st_space("v", 0.3)
        st_write(design_system.body.paragraph, summary, tag=t.p)
        st_space("v", 0.6)
