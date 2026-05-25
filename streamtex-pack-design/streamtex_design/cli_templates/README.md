# CLI templates

Ready-to-use skeletons for new StreamTeX documents that consume the pack
ecosystem (`streamtex-pack-design`, `streamtex-pack-manuals`,
`streamtex-pack-gse`). Each template is the **minimum viable starting
point** — copy it, rename the project, and start adding blocks.

## Templates

| Folder              | For                                        | Packs declared             |
|---------------------|--------------------------------------------|----------------------------|
| `new-manual/`       | New manual in the `family-stx-manuels` line | design + manuals           |
| `new-training/`     | New training session / instructor-led deck | design + manuals (training kit) |
| `new-gse-module/`   | New module in the `family-stx-gse` line    | design + gse               |

## What each template ships

- `stx.toml` — `[[packs]]` declarations, design system pinned, resolution
  preference set.
- `book.py` — minimal `st_book(...)` orchestration with one welcome block.
- `setup.py` — empty placeholder (most projects do not need it; remove if
  the project does not need to extend `sys.path`).
- `custom/styles.py` — slim project palette that **imports from the pack**
  (`from streamtex_design import Colors, Titles, Fonts`) instead of
  redefining the palette from scratch. The intent is that a new document's
  `custom/styles.py` stays at ~30–50 lines (vs. ~160 in pre-pack legacy
  documents).
- `custom/themes.py` — dark mode CSS overrides (project-specific only).
- `blocks/__init__.py` + `blocks/bck_welcome.py` — a single example block
  consuming a pack component (`pitch_hero` / `level_badge_hero` / etc.)
  so the project boots out of the box.

## Usage

Copy the template folder, rename it, then add to your parent
`pyproject.toml`:

```toml
dependencies = [
    "streamtex>=0.7.7",
    "streamtex-pack-design @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-design-v0.3.0#subdirectory=streamtex-pack-design",
    # plus pack-manuals / pack-gse depending on the template chosen
]
```

Run with `stx run` from inside the project folder.
