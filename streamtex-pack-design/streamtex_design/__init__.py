"""streamtex-design — Official StreamTeX design pack.

Three design systems (default, modern_dark, modern_light), 19 components
across primitive / composition / block granularities, 6 kits, foundation
bundles for typography/colors usable from consumer documents.

Consume via:

    pip install streamtex-design
    stx pack add git:github.com/nicolasguelfi/streamtex-design@v0.3.0

Public re-exports map to the ``default`` design system bundles, which is
the canonical reference for downstream consumers:

    from streamtex_design import DesignSystem, Colors, Titles, Fonts, Callouts, Body

For alternative design systems, import directly:

    from streamtex_design.design_systems.modern_dark import DesignSystem
"""

from streamtex_design.design_systems.default import (
    DesignSystem,
    _Body as Body,
    _Callouts as Callouts,
    _Colors as Colors,
    _Fonts as Fonts,
    _Titles as Titles,
)

__version__ = "0.3.0"

__all__ = [
    "DesignSystem",
    "Colors",
    "Titles",
    "Fonts",
    "Callouts",
    "Body",
]
