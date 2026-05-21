"""Slide components must propagate `toc_lvl` so the TOC / sidebar populates.

Regression guard for the GSE-ODOO finding: `title_slide` / `slide_heading`
rendered titles without ever registering a TOC entry, leaving the sidebar
empty. They now forward `toc_lvl` to `st_write`; `part_intro` registers
level "1" by default.
"""

from unittest.mock import patch

from streamtex_design.components.part_intro import part_intro
from streamtex_design.components.slide_heading import slide_heading
from streamtex_design.components.title_slide import title_slide
from streamtex_design.design_systems.modern_dark import DesignSystem as DS


def _toc_lvls(mock_write):
    """Collect the `toc_lvl` passed to each st_write call (None if absent)."""
    return [c.kwargs.get("toc_lvl") for c in mock_write.call_args_list]


class TestTocPropagation:
    def test_title_slide_forwards_toc_lvl(self):
        with patch("streamtex_design.components.title_slide.st_write") as w:
            title_slide(design_system=DS, title="Cover", toc_lvl="1")
        assert "1" in _toc_lvls(w)

    def test_title_slide_default_no_toc(self):
        with patch("streamtex_design.components.title_slide.st_write") as w:
            title_slide(design_system=DS, title="Cover")
        assert _toc_lvls(w) == [None]

    def test_slide_heading_forwards_toc_lvl(self):
        with patch("streamtex_design.components.slide_heading.st_write") as w:
            slide_heading(design_system=DS, title="Heading", toc_lvl="2")
        assert "2" in _toc_lvls(w)

    def test_slide_heading_default_no_toc(self):
        with patch("streamtex_design.components.slide_heading.st_write") as w:
            slide_heading(design_system=DS, title="Heading")
        # First call is the title; it must not register a TOC entry by default.
        assert _toc_lvls(w)[0] is None

    def test_part_intro_registers_level_1_by_default(self):
        with patch("streamtex_design.components.part_intro.st_write") as w:
            part_intro(design_system=DS, title="The cost of friction")
        assert "1" in _toc_lvls(w)

    def test_part_intro_toc_can_be_suppressed(self):
        with patch("streamtex_design.components.part_intro.st_write") as w:
            part_intro(design_system=DS, title="x", toc_lvl=None)
        assert all(lvl is None for lvl in _toc_lvls(w))
