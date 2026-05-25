"""Validate every streamtex-pack-gse component against the contract surface."""

from __future__ import annotations

import importlib
import pkgutil

import pytest
from streamtex.core import validation

import streamtex_gse.components as components_pkg


def _iter_component_modules():
    for module_info in pkgutil.iter_modules(components_pkg.__path__):
        if module_info.name.startswith("_"):
            continue
        yield importlib.import_module(f"streamtex_gse.components.{module_info.name}")


COMPONENT_MODULES = list(_iter_component_modules())


@pytest.mark.parametrize("mod", COMPONENT_MODULES, ids=lambda m: m.__name__)
def test_component_validates(mod):
    issues = validation.validate_component(mod)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"{mod.__name__} errors: {errors}"


def test_two_components():
    """v0.1.0 ships transition_gse + gse_letter."""
    names = {m.__component_meta__["name"] for m in COMPONENT_MODULES}
    assert {"transition_gse", "gse_letter"}.issubset(names), f"Got {names}"


def test_gse_letter_requires_three_words():
    """The gse_letter component should reject phrases with fewer than 3 words."""
    from streamtex_gse.components.gse_letter import gse_letter
    from streamtex_gse.design_systems.gse import DesignSystem

    DS = DesignSystem()
    with pytest.raises(ValueError, match="at least 3 words"):
        # Calling outside of a Streamlit context — the validator raises BEFORE
        # any st_write call, so this works without a running app.
        gse_letter(design_system=DS, text="Only two")
