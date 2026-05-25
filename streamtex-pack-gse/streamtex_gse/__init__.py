"""streamtex-pack-gse — Project-specific pack for the AI4SE / GSE training family.

One design system (`gse`, extending pack-design's default with the GSE-One
brand palette), two components (`transition_gse`, `gse_letter`), one kit.

Consume via:

    pip install streamtex-pack-gse
    stx pack add git:github.com/nicolasguelfi/streamtex-packs@pack-gse-v0.1.0

Public re-exports map to the ``gse`` design system bundles. For the generic
foundation, see ``streamtex_design``.
"""

from streamtex_gse.design_systems.gse import DesignSystem

__version__ = "0.1.0"

__all__ = ["DesignSystem"]
