"""Re-exports for streamtex_manuals components.

Each submodule defines ``__component_meta__`` and a public function with the
same name as the module. Import directly:

    from streamtex_manuals.components.level_badge_hero import level_badge_hero
    from streamtex_manuals.components.column_features import column_features
    from streamtex_manuals.components.pitch_hero import pitch_hero

This package's __init__ is intentionally lean — components are discovered at
runtime via `streamtex.core.discovery.discover_components`.
"""
