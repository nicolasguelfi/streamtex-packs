# Extended pack artifacts (manifest 0.2+)

This guide explains the 8 categories of artifacts a StreamTeX pack can
ship under the `[pack.data]` section of its manifest. Use it as the
user-facing reference for both new packs and consumer documents.

Backward compatibility: format 0.1 packs (no `[pack.data]`) keep working
unchanged. The 0.2 format is **additive**.

## Why these 8 categories

Beyond the Python-canonical artifacts of format 0.1 (components, design
systems, kits, CLI templates, project blueprints), packs in real-world
use produce a wider range of reusable assets — colors expressed in JSON
so Figma can read them, AI image prompts as plain text, scene archetypes
documented in markdown, agent skills for Claude Code, logos with license
metadata, recipes for integrating the pack into third-party tools.

Format 0.2 promotes all of these to **first-class artifacts**: typed
discovery, validation, CLI, lifecycle. Single mechanism for all
categories, single source of truth, multi-runtime by default for
data-first ones.

## The 8 categories at a glance

| Category | Filesystem | Format | Canonical use |
|---|---|---|---|
| `palette` | `<pack>/palettes/<n>.json` | JSON | Colors + dimensions, Python view at import time |
| `ai_prompt` | `<pack>/ai_prompts/<n>/{prefix,suffix-*}.txt` | TXT | Reusable AI image-gen prompts |
| `archetype` | `<pack>/archetypes/<n>.md` | Markdown + YAML frontmatter | Reusable visual scene patterns |
| `guideline` | `<pack>/guidelines/<n>.md` | Markdown + YAML frontmatter | Opposable R-rules (R1, R2, …) |
| `skill` | `<pack>/skills/<n>.md` | Markdown + Claude Code frontmatter | Pack-scoped Claude skill |
| `agent` | `<pack>/agents/<n>.md` | Markdown + Claude Code frontmatter | Pack-scoped Claude agent |
| `asset` | `<pack>/assets/_manifest.toml` + binaries | TOML + bytes | Logos, fonts, images |
| `integration` | `<pack>/integrations/<framework>/` | Open | Recipe per third-party framework |

## Declaring artifacts in `_pack_manifest.toml`

```toml
[manifest]
format = "0.2"

[pack]
name = "streamtex-pack-gse"
version = "2.0.0"
# … usual fields …

[pack.data]
palettes      = ["main"]
ai_prompts    = ["scene_generation"]
archetypes    = ["bridge", "horizon", "balance", "cycle"]
guidelines    = ["graphic-line", "composition-rules"]
skills        = ["author-helper"]
agents        = []
assets        = []
integrations  = ["streamtex"]
```

A list entry that doesn't match a file/dir on disk is reported by
`stx artifact validate` as an error. A file present on disk but unlisted
is silently ignored (the manifest is the source of truth for discovery).

## Per-category schemas

### Palette

`palettes/main.json` :

```json
{
  "name": "main",
  "version": "1.0.0",
  "since": "2026-05-26",
  "colors": {
    "primary":  { "hex": "#7AB8F5", "role": "ideological dimension" },
    "accent":   { "hex": "#2EC4B6", "role": "technical dimension" },
    "highlight":{ "hex": "#F39C12", "role": "decisional dimension" }
  },
  "dimensions": {
    "ideological": "primary",
    "technical": "accent",
    "decisional": "highlight"
  }
}
```

Python view:
```python
from streamtex.core.artifacts.palette import load_palette
palette = load_palette("main", pack="streamtex-pack-gse")
palette.hex_for("primary")        # "#7AB8F5"
palette.hex_for("ideological")    # resolved via dimensions → "#7AB8F5"
palette.colors["primary"].as_style()  # composable Style atom
```

Multi-runtime: `jq -r '.colors.primary.hex' palettes/main.json` works
from anywhere.

### AI prompt

`ai_prompts/scene_generation/` :

```
prefix.txt              ← required
suffix-landscape.txt    ← at least one suffix required
suffix-portrait.txt
suffix-square.txt
```

Python view:
```python
from streamtex.core.artifacts.ai_prompt import load_ai_prompt
prompt = load_ai_prompt("scene_generation", pack="streamtex-pack-gse")
full = prompt.compose(orientation="landscape", scene="Two buildings on cliff edges…")
```

### Archetype

`archetypes/bridge.md` :

```markdown
---
name: bridge
description: Transition / 30-year horizon
orientation: landscape
status: validated
tags: [transition, narrative]
extrapolable: true
since: 2026-05-05
palette_refs: [primary, accent, highlight]
---

# Bridge

## Scene composition
…

## Variation rules
### INVARIANTS
- …
### PARAMS
- …
### INTERDITS
- …
```

### Guideline

`guidelines/composition-rules.md` :

```markdown
---
name: composition-rules
description: Universal slide composition rules R1-R13
rules: [R1, R2, R7, R11, R12, R13]
applies_to: [components, projects]
since: 2026-05-05
---

# Composition rules

## R1 — One idea per slide
…
```

### Skill / Agent

`skills/author-helper.md` :

```markdown
---
name: author-helper
description: Helps an author respect the pack's visual identity
---

# Author helper

When writing a new slide …
```

At `stx artifact install author-helper --kind skill`, the file is copied
to `<project>/.claude/custom/skills/<pack_slug>__author-helper.md` so
Claude Code picks it up. Confirmation prompt by default ; `--yes` skips.

### Asset

`assets/_manifest.toml` :

```toml
[[assets]]
path = "logos/brand-logo.svg"
kind = "logo"
license = "BUSL-1.1"
sha256 = "abc123…"      # optional
```

The binary files live alongside the manifest under `assets/`.

### Integration

`integrations/figma/` (or `integrations/streamtex/`, …) :

```
integrations/figma/
├── README.md           ← required (recipe documentation)
└── figma-plugin.js     ← any number of supporting files
```

Open contract for v0.2 — only the `README.md` is mandatory.

## Generic CLI

```bash
stx artifact list                            # all categories, all packs
stx artifact list --kind palette             # filter by category
stx artifact list --pack streamtex-pack-gse  # filter by pack

stx artifact show <name> --kind <kind>       # formatted view per category

stx artifact validate                        # validate every artifact
stx artifact validate --kind archetype

stx artifact install <name> --kind skill     # copy to .claude/custom/
stx artifact install <name> --kind agent --yes --overwrite
```

## Consuming an extended pack from a project

In your project `stx.toml` :

```toml
[[packs]]
type = "git"
name = "streamtex-pack-gse"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-gse"
rev = "pack-gse-v2.0.0"

[design_system]
use = "gse"
```

From your block code, the artifacts are at one import away :

```python
from streamtex.core.artifacts.palette import load_palette
from streamtex.core.artifacts.ai_prompt import load_ai_prompt
from streamtex.core.artifacts.archetype import load_archetype

palette = load_palette("main", pack="streamtex-pack-gse")
prompt  = load_ai_prompt("scene_generation", pack="streamtex-pack-gse")
bridge  = load_archetype("bridge", pack="streamtex-pack-gse")
```

## Authoring a new pack with extended artifacts

The recommended path is `/stx-pe:bootstrap --categories <list>` from
Claude Code. Manual scaffolding works too — just create the right
subdirs under your pack and declare them in `[pack.data]`.

`streamtex-pack-gse v2.0.0` is the **reference example** : it ships
all 6 of the data-first / documentation / Claude-asset categories
(palette, ai_prompt, archetype, guideline, skill, integration).

## Validation guarantees

Each category has a dedicated validator with stable error codes :

- `PAV001-PAV010` — palette
- `APV001-APV006` — AI prompt
- `ARV001-ARV007` — archetype
- `GLV001-GLV006` — guideline
- `SKV001-SKV004` — skill
- `AGV001-AGV004` — agent
- `ASV001-ASV005` — asset
- `INV001-INV003` — integration

Run `stx artifact validate` (no args) in any project to validate every
artifact across every installed pack. Exit code 0 = clean, 1 = errors.

## Migration from format 0.1

Existing packs (format 0.1) keep working untouched — no `[pack.data]`
means no extended artifacts. To opt in :

1. Bump `[manifest] format = "0.2"`.
2. Add `[pack.data]` listing your new artifact slugs.
3. Add the matching subdirectories with the required files.
4. Extend `[tool.setuptools.package-data]` to ship the new files :
   ```toml
   streamtex_yourpack = [
       "_pack_manifest.toml",
       "kits/*.toml",
       "palettes/*.json",
       "ai_prompts/**/*.txt",
       "archetypes/*.md",
       "guidelines/*.md",
       "skills/*.md",
       "agents/*.md",
       "integrations/**/*",
   ]
   ```
5. Run `stx artifact validate --pack streamtex-pack-yourpack` from a
   project that consumes it.

That's it — no breaking change for existing consumers.
