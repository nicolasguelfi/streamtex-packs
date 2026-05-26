# streamtex integration recipe — streamtex-pack-gse

This recipe describes how to consume `streamtex-pack-gse` from a StreamTeX
document. It supersedes the legacy file-copy integration that lived in
`streamtex-shared/graphic-designs/gse/integrations/streamtex/` (now
removed).

## stx.toml

```toml
[[packs]]
type = "git"
name = "streamtex-pack-design"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-design"
rev = "pack-design-v0.3.0"

[[packs]]
type = "git"
name = "streamtex-pack-gse"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-gse"
rev = "pack-gse-v2.0.0"

[design_system]
use = "gse"

[resolution]
prefer = ["streamtex-pack-gse", "streamtex-pack-design"]
```

## Block example

```python
from streamtex_gse.design_systems.gse import DesignSystem
from streamtex_gse.components.gse_letter import gse_letter
from streamtex_gse.components.transition_gse import transition_gse

DS = DesignSystem()

def build():
    gse_letter(design_system=DS, text="Generative Software Engineering")
    transition_gse(
        design_system=DS,
        title="The Methodological Gap",
        pivot="Today: beyond VibeEngineering → GSE-One",
    )
```

## Using the palette directly

The canonical palette is reachable from any Python code:

```python
from streamtex.core.artifacts.palette import load_palette

palette = load_palette("main", pack="streamtex-pack-gse")
print(palette.hex_for("amber"))       # → "#F39C12"
print(palette.hex_for("decisional"))  # → "#F39C12" (resolved via dimensions)
```

## Composing AI image prompts

```python
from streamtex.core.artifacts.ai_prompt import load_ai_prompt

prompt = load_ai_prompt("scene_generation", pack="streamtex-pack-gse")
full = prompt.compose(
    orientation="landscape",
    scene="Two stylised buildings on opposite cliffs, an amber arc bridges them …",
)
```

## Multi-runtime usage

The palette JSON and AI prompt text files are pure data and can be read
by any tool:

```bash
jq -r '.colors.amber.hex' streamtex_gse/palettes/main.json
cat streamtex_gse/ai_prompts/scene_generation/prefix.txt
```

## Installing the pack-shipped skill

To make the `gse-author` skill available to Claude Code inside your
project:

```bash
stx artifact install gse-author --kind skill
```

The skill is copied to `.claude/custom/skills/gse__gse-author.md`.
