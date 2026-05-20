"""Re-exports for streamtex_design components.

Each submodule defines `__component_meta__` and a public function with the
same name as the module. Import directly:

    from streamtex_design.components.callout import callout
    from streamtex_design.components.title_slide import title_slide

This package's __init__ is intentionally lean — components are discovered at
runtime via `streamtex.core.discovery.discover_components`.
"""
