"""Entry point for a new GSE module.

Uses the `gse` design system from streamtex-pack-gse so the GSE-One brand
palette (amber highlight + G/S/E letter colors) is the default everywhere.
"""

from pathlib import Path

import streamlit as st
import streamtex as stx
from streamtex import st_book
from streamtex.styles import StxStyles as sts

from custom.themes import dark
import blocks

PROJECT_DIR = Path(__file__).parent

stx.set_static_sources([str(PROJECT_DIR / "static")])
sts.theme = dark
st.set_page_config(page_title="GSE_MODULE_NAME", layout="wide")

st_book(
    [blocks.bck_welcome],
    paginate=True,
)
