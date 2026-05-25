"""Re-exports for streamtex_gse components.

Each submodule defines ``__component_meta__`` and a public function with the
same name as the module. Import directly:

    from streamtex_gse.components.transition_gse import transition_gse
    from streamtex_gse.components.gse_letter import gse_letter

This package's __init__ is intentionally lean — components are discovered at
runtime via `streamtex.core.discovery.discover_components`.
"""
