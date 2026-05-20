"""Validate every streamtex-design design system."""

from __future__ import annotations

import importlib
import pkgutil

import pytest
from streamtex.core import validation

import streamtex_design.design_systems as ds_pkg


def _iter_design_systems():
    for module_info in pkgutil.iter_modules(ds_pkg.__path__):
        if module_info.ispkg:
            yield importlib.import_module(f"streamtex_design.design_systems.{module_info.name}")


DS_MODULES = list(_iter_design_systems())


@pytest.mark.parametrize("mod", DS_MODULES, ids=lambda m: m.__name__)
def test_design_system_validates(mod):
    issues = validation.validate_design_system(mod)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"{mod.__name__} errors: {errors}"


def test_three_design_systems():
    names = {m.DesignSystem.name for m in DS_MODULES}
    assert names == {"default", "modern_dark", "modern_light"}, f"Got {names}"


_BUNDLE_NAMES = (
    "callouts", "body", "titles", "stat_hero",
    "card_grid", "takeaways", "citation",
    "inline_emphasis", "comparison_table",
)


@pytest.mark.parametrize("mod", DS_MODULES, ids=lambda m: m.__name__)
def test_no_hardcoded_px_in_design_systems(mod):
    """Pack design systems must use ``var(--stx-scale-…)`` rather than hardcoded
    ``px`` in font-size declarations. Hardcoded ``px`` breaks responsive sizing
    for every downstream consumer."""
    ds = mod.DesignSystem
    offenders = []
    for bundle_name in _BUNDLE_NAMES:
        bundle = getattr(ds, bundle_name, None)
        if bundle is None:
            continue
        for attr_name in dir(bundle):
            if attr_name.startswith("_"):
                continue
            style = getattr(bundle, attr_name)
            css = getattr(style, "css", None)
            if not isinstance(css, str) or "font-size" not in css:
                continue
            font_size_value = css.split("font-size:", 1)[1].split(";", 1)[0]
            if "px" in font_size_value:
                offenders.append(
                    f"{mod.__name__}.{bundle_name}.{attr_name}: "
                    f"hardcoded px in font-size — got '{font_size_value.strip()}'"
                )
    assert not offenders, "\n".join(offenders)
