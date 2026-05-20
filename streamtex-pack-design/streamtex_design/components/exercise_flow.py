"""
# Exercise flow — Multi-step exercise prompt with numbered steps

## Visual

```
   STEP 1   Read the abstract
   STEP 2   Identify the main hypothesis
   STEP 3   Compare with the conclusion
```

A horizontal or vertical sequence of numbered steps that scaffold an
exercise or guided activity. Each step has a short prompt.

## Structure

- A `st_grid` of step columns (or a stacked vertical layout).
- Each step: a "STEP N" header + a short prompt body.

## Styling rules

| Element | Style |
|---|---|
| step_label | titles.subtitle |
| step_body | body.paragraph |

## Extrapolation rules

### INVARIANTS
- Steps are numbered sequentially from 1.
- Each step prompt is one to two short sentences.

### PARAMS
- orientation: horizontal | vertical
- 3 ≤ N ≤ 6 steps

### INTERDITS
- No nested steps.
- No multi-paragraph prompts.

## When to use

- Workshop activities with sequential steps.
- Lab exercise instructions.

## When NOT to use

- Long instruction manuals (use `manual_section`).
- Decision trees (use a flowchart export).

## Design system bundles required

- titles.subtitle
- body.paragraph
"""

from streamtex import st_grid, st_write

__component_meta__ = {
    "name": "exercise_flow",
    "description": "Numbered sequence of exercise steps.",
    "tags": ["exercise", "steps", "flow"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.subtitle", "body.paragraph"],
    "granularity": "block",
}


def exercise_flow(*, design_system, steps: list = None, orientation: str = "horizontal") -> None:
    """Render a numbered exercise flow."""
    steps = steps or []
    if orientation == "horizontal":
        with st_grid(cols=f"repeat({len(steps) or 1}, 1fr)", gap="24px") as g:
            for idx, step in enumerate(steps, 1):
                with g.cell():
                    st_write(design_system.titles.subtitle, f"STEP {idx}")
                    st_write(design_system.body.paragraph, step)
    else:
        for idx, step in enumerate(steps, 1):
            st_write(design_system.titles.subtitle, f"STEP {idx}")
            st_write(design_system.body.paragraph, step)
