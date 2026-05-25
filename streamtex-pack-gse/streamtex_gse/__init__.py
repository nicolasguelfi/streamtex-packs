"""streamtex-pack-gse — pack for the AI4SE / GSE training family (manifest 0.2).

Contents:

* ``gse`` design system (palette generated at import from ``palettes/main.json``)
* Two components (``transition_gse``, ``gse_letter``) and a default kit
* **Palette artifact** ``palettes/main.json`` — canonical GSE palette (7 tokens
  + 4 semantic dimensions), readable by any tool (Figma, Midjourney, …)
* **AI prompt artifact** ``ai_prompts/scene_generation/`` — prefix + 3
  orientation-specific suffixes for AI image generation in the GSE register

Consume via:

    pip install streamtex-pack-gse
    stx pack add git:github.com/nicolasguelfi/streamtex-packs@pack-gse-v2.0.0

Public re-exports map to the ``gse`` design system bundles.
"""

from streamtex_gse.design_systems.gse import DesignSystem

__version__ = "2.0.0"

__all__ = ["DesignSystem"]
