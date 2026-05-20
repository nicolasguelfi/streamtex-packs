"""
# Feature walkthrough — Step-by-step demonstration of a feature

## Visual

```
   STEP 1   Install
   ─────────────────────────────────────
   $ pip install streamtex

   STEP 2   Write your first block
   ─────────────────────────────────────
   from streamtex import st_write
   st_write("Hello")

   STEP 3   Run
   ─────────────────────────────────────
   $ streamlit run book.py
```

A documentation-manual block that walks through a feature in 3-5 numbered
steps, each step pairing a short prose explanation with a code snippet.

## Structure

- Per step: `titles.subtitle` ("STEP N — label") + `body.paragraph` + `body.code`.

## Styling rules

| Element | Style |
|---|---|
| step_label | titles.subtitle |
| prose | body.paragraph |
| code | body.code |

## Extrapolation rules

### INVARIANTS
- Steps are numbered sequentially from 1.
- Every step has at least one of prose or code (often both).

### PARAMS
- 3 ≤ N ≤ 5 steps
- code is optional per step

### INTERDITS
- No nested walkthroughs.
- No deep code (≤ 5 lines per snippet).

## When to use

- Onboarding pages of a documentation manual.
- Tutorial slides for a workshop.

## When NOT to use

- Reference-style cards (use api_reference_card).
- Hero-level marketing pages (use stat_hero).

## Design system bundles required

- titles.subtitle
- body.paragraph
- body.code
"""

from streamtex import st_space, st_write

__component_meta__ = {
    "name": "feature_walkthrough",
    "description": "Numbered walkthrough of a feature (3-5 steps).",
    "tags": ["walkthrough", "tutorial", "feature"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.subtitle", "body.paragraph", "body.code"],
    "granularity": "block",
}


def feature_walkthrough(*, design_system, steps: list = None) -> None:
    """Render a numbered feature walkthrough. `steps` = [(label, prose, code), ...]."""
    steps = steps or []
    for idx, (label, prose, code) in enumerate(steps, 1):
        st_write(design_system.titles.subtitle, f"STEP {idx} — {label}")
        if prose:
            st_write(design_system.body.paragraph, prose)
        if code:
            st_write(design_system.body.code, code)
        st_space("v", 1.0)
