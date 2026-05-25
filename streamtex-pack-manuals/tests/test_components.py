"""Validate every streamtex-pack-manuals component against the contract surface."""

from __future__ import annotations

import importlib
import pkgutil

import pytest
from streamtex.core import validation

import streamtex_manuals.components as components_pkg


def _iter_component_modules():
    for module_info in pkgutil.iter_modules(components_pkg.__path__):
        if module_info.name.startswith("_"):
            continue
        yield importlib.import_module(f"streamtex_manuals.components.{module_info.name}")


COMPONENT_MODULES = list(_iter_component_modules())


@pytest.mark.parametrize("mod", COMPONENT_MODULES, ids=lambda m: m.__name__)
def test_component_validates(mod):
    issues = validation.validate_component(mod)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"{mod.__name__} errors: {errors}"


def test_at_least_ten_components():
    """Pack-manuals 0.2.0 ships 3 original + 7 training components = 10."""
    assert len(COMPONENT_MODULES) >= 10, f"Expected ≥10, got {len(COMPONENT_MODULES)}"


def test_training_components_present():
    """Verify the 7 training components introduced in v0.2.0 are wired up."""
    names = {m.__component_meta__["name"] for m in COMPONENT_MODULES}
    expected = {
        "faq",
        "trainer_profile",
        "training_header",
        "training_footer",
        "glossary",
        "references_list",
        "changelog_card",
    }
    missing = expected - names
    assert not missing, f"Missing training components: {missing}"
