"""
# GSE letter — Inline highlight of the GSE initials in a phrase

## Visual

```
  Generative Software Engineering
  ^         ^        ^
  G(amber)  S(teal)  E(blue)
```

An inline rendering of a phrase where the first letter of each of three
words is colored with the GSE brand palette (G = amber, S = teal,
E = blue by default). The remaining letters of each word use the regular
body color.

## Structure

- The phrase is split on whitespace into words.
- The first 3 words are treated as the G / S / E words; their initials
  are wrapped in `<span>` with the corresponding letter color.
- Any remaining words are rendered with the default body color.

## Styling rules

| Element            | Source                              |
|--------------------|-------------------------------------|
| G initial          | `colors.g_letter`                   |
| S initial          | `colors.s_letter`                   |
| E initial          | `colors.e_letter`                   |
| body / remainder   | `body.paragraph`                    |

The initial styles are intentionally taken from `colors.*` rather than a
dedicated bundle so a downstream design system can override them by
declaring `g_letter`, `s_letter`, `e_letter` on its own `colors` bundle.

## Extrapolation rules

### INVARIANTS

- Exactly 3 words are colored — never fewer, never more. If the input
  has fewer than 3 words the component raises `ValueError`.
- The 3 colored letters are always the FIRST letter of each of the
  first 3 words (case preserved from input).

### PARAMS

- `text`: the phrase to render. Defaults to "Generative Software Engineering".
- `tag`: HTML tag for the outer element (default `span` so the result is
  inline-friendly).

### INTERDITS

- No mid-word coloring — the letter colored is always the leading
  character of the word.
- No skipping a word — if word #2 starts with a non-letter, its first
  character is still wrapped (the design system style applies regardless).

## When to use

- Anywhere the phrase "Generative Software Engineering" or any G/S/E
  triple needs to be visually anchored as the GSE brand.
- Inline within a sentence rendered via `st_write`.

## When NOT to use

- For a 1- or 2-word emphasis — use `inline_emphasis.strong` from
  streamtex-pack-design instead.
- For long-form paragraphs — the visual effect saturates quickly.

## Design system bundles required

- `colors.g_letter`, `colors.s_letter`, `colors.e_letter`
- `body.paragraph`
"""

from streamtex import st_write
from streamtex.enums import Tags as t
from streamtex.styles import Style

__component_meta__ = {
    "name": "gse_letter",
    "description": "Inline highlight of the G/S/E initials of a 3-word phrase using brand colors.",
    "tags": ["inline", "emphasis", "gse-one", "brand"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "colors.g_letter",
        "colors.s_letter",
        "colors.e_letter",
        "body.paragraph",
    ],
    "granularity": "primitive",
}


def gse_letter(
    *,
    design_system,
    text: str = "Generative Software Engineering",
    tag=t.span,
) -> None:
    """Render a phrase with the first letter of each of the first 3 words
    colored using the GSE brand palette."""
    words = text.split()
    if len(words) < 3:
        raise ValueError(
            f"gse_letter requires a phrase with at least 3 words, got {len(words)}: {text!r}"
        )

    letter_styles = [
        design_system.colors.g_letter,
        design_system.colors.s_letter,
        design_system.colors.e_letter,
    ]

    parts: list[str] = []
    for idx, word in enumerate(words):
        if idx < 3 and word:
            initial = word[0]
            rest = word[1:]
            color_css = letter_styles[idx].css
            parts.append(
                f'<span style="{color_css} font-weight: 700;">{initial}</span>{rest}'
            )
        else:
            parts.append(word)

    html_body = " ".join(parts)
    inline_style = Style(design_system.body.paragraph.css, "gse_letter_wrapper")
    st_write(inline_style, html_body, tag=tag)
