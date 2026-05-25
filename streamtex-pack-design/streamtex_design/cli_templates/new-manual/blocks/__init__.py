"""Block registry for MANUAL_NAME.

Each `bck_*` module exposes a `build()` function called by the engine when
the block is rendered. Add new modules here.
"""

from blocks import bck_welcome

__all__ = ["bck_welcome"]
