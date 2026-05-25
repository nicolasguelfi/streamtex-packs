"""
# Trainer profile — Speaker / instructor identity card

## Visual

```
┌─────────────────────────────────────────────────────┐
│  ╔══════════╗   Name LASTNAME                       │
│  ║          ║   Role · Affiliation                  │
│  ║  PHOTO   ║                                       │
│  ║   30%    ║   Short bio paragraph framing the     │
│  ║          ║   trainer's expertise and the angle   │
│  ╚══════════╝   they bring to this session.         │
└─────────────────────────────────────────────────────┘
```

A two-column trainer / speaker card: portrait on the left, identity and
bio on the right. Used early in a training deck to introduce the
instructor(s), and on a manual's about page.

## Structure

- `st_grid(cols="30% 70%")` with photo cell and identity cell.
- Photo cell: optional `st_image` (centered, rounded if `rounded=True`).
- Identity cell: name (large bold), role line (muted color), then bio
  paragraph via `body.paragraph`.

## Styling rules

- Name style: `titles.subtitle` + bold + primary color.
- Role line: `body.paragraph` + muted color (from `colors.muted`).
- Bio: `body.paragraph`.

## Extrapolation rules

### INVARIANTS
- The photo column is always 30% — keeps the layout consistent across
  several trainer cards stacked vertically.
- Name is always rendered above the role line.

### PARAMS
- `name`: full name as displayed (e.g. "Nicolas Guelfi").
- `role`: e.g. "Trainer", "Professor", "Lead Designer".
- `affiliation`: e.g. "University of Luxembourg".
- `bio`: 1–3 short paragraphs (joined with double newlines in input).
- `photo_uri`: optional image URI. If omitted, the photo cell renders a
  neutral placeholder block.
- `rounded`: if True, photo is rendered with `border-radius: 50%`
  (round portrait); else square with rounded corners.

### INTERDITS
- No social links / CTAs inside the card. Use `pitch_hero` if the page
  is meant to drive a call to action.
- No multi-trainer rendering in a single call — call the component once
  per trainer (or use `card_grid` from pack-design for a side-by-side
  layout of compact trainer cards).

## When to use

- First slide(s) of a training session to introduce instructors.
- "About the author" page of a manual.

## When NOT to use

- For multiple trainer profiles inline as a grid — use `card_grid` with
  trainer cards as items.

## Design system bundles required

- `titles.subtitle` (name)
- `body.paragraph` (role + bio)
- `colors.primary` (name color accent)
- `colors.muted` (role line)
"""

from streamtex import st_block, st_grid, st_image, st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "trainer_profile",
    "description": "Two-column identity card: portrait on the left, name/role/bio on the right.",
    "tags": ["trainer", "speaker", "profile", "training", "manual"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "titles.subtitle",
        "body.paragraph",
        "colors.primary",
        "colors.muted",
    ],
    "granularity": "composition",
}


def trainer_profile(
    *,
    design_system,
    name: str,
    role: str,
    affiliation: str = "",
    bio: str = "",
    photo_uri: str | None = None,
    rounded: bool = True,
) -> None:
    """Render a trainer identity card: photo + name + role + bio."""
    name_style = Style.create(
        design_system.titles.subtitle + StxStyles.bold + design_system.colors.primary,
        "tp_name",
    )
    role_style = Style.create(
        design_system.body.paragraph + design_system.colors.muted,
        "tp_role",
    )
    photo_style = Style(
        f"width: 100%; height: auto; "
        f"border-radius: {'50%' if rounded else '8px'};",
        "tp_photo",
    )
    placeholder = Style(
        "width: 100%; aspect-ratio: 1 / 1; "
        f"background: rgba(255,255,255,0.05); "
        f"border-radius: {'50%' if rounded else '8px'};",
        "tp_placeholder",
    )

    with st_grid(cols="30% 70%", gap="20px") as g:
        with g.cell():
            if photo_uri:
                st_image(photo_style, uri=photo_uri)
            else:
                with st_block(placeholder):
                    pass
        with g.cell():
            st_write(name_style, name, tag=t.div, toc_lvl="+2")
            role_line = role if not affiliation else f"{role} · {affiliation}"
            st_write(role_style, role_line, tag=t.div)
            if bio:
                st_space("v", 0.8)
                st_write(design_system.body.paragraph, bio, tag=t.p)
