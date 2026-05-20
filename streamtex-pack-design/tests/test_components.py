"""Validate every streamtex-design component against the contract surface."""

from __future__ import annotations

import importlib
import pkgutil

import pytest
from streamtex.core import validation

import streamtex_design.components as components_pkg


def _iter_component_modules():
    for module_info in pkgutil.iter_modules(components_pkg.__path__):
        if module_info.name.startswith("_"):
            continue
        yield importlib.import_module(f"streamtex_design.components.{module_info.name}")


COMPONENT_MODULES = list(_iter_component_modules())


@pytest.mark.parametrize("mod", COMPONENT_MODULES, ids=lambda m: m.__name__)
def test_component_validates(mod):
    issues = validation.validate_component(mod)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"{mod.__name__} errors: {errors}"


def test_at_least_eighteen_components():
    assert len(COMPONENT_MODULES) >= 18, f"Expected ≥18, got {len(COMPONENT_MODULES)}"


def test_granularity_diversity():
    granularities = {m.__component_meta__["granularity"] for m in COMPONENT_MODULES}
    assert "primitive" in granularities
    assert "composition" in granularities
    assert "block" in granularities
