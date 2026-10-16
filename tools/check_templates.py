"""Lock a project made from each CLI template of streamtex-pack-design (streamtex-packs#2).

A template names a tag of each pack it uses (``[[packs]]`` in its stx.toml).
For every template, two throwaway projects declare those packs at those tags
and are locked with uv:

- the way ``stx pack sync`` writes them: dependencies by name, git sources;
- the way a Docker build installs them: direct URLs, ``--no-sources``.

The packs are read from THIS repository (``file://``), so the tags named by
the templates must exist locally (CI: checkout with tags).

Run from the repository root:  uv run --no-project -p 3.12 python tools/check_templates.py
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "streamtex-pack-design" / "streamtex_design" / "cli_templates"
REPO_REF = "github.com/nicolasguelfi/streamtex-packs"


def _packs(stx_toml: Path) -> list[dict]:
    packs = tomllib.loads(stx_toml.read_text(encoding="utf-8")).get("packs", [])
    return [p for p in packs if p.get("type") == "git"]


def _project(name: str, deps: list[str], sources: list[str]) -> str:
    text = (f'[project]\nname = "{name}"\nversion = "0.1.0"\nrequires-python = ">=3.11"\n'
            f"dependencies = [{', '.join(repr(d).replace(chr(39), chr(34)) for d in deps)}]\n")
    if sources:
        text += "\n[tool.uv.sources]\n" + "\n".join(sources) + "\n"
    return text


def _lock(directory: Path, *flags: str) -> tuple[bool, str]:
    env = {k: v for k, v in os.environ.items() if k != "UV_NO_SOURCES"}
    r = subprocess.run(["uv", "lock", "--quiet", *flags], cwd=directory, env=env,
                       capture_output=True, text=True)
    return r.returncode == 0, (r.stderr or r.stdout).strip()


def check(template: Path, work: Path) -> list[str]:
    packs = _packs(template / "stx.toml")
    url = ROOT.as_uri()
    for p in packs:
        if p.get("ref") != REPO_REF:
            return [f"{template.name}: pack {p.get('name')} is not in {REPO_REF}"]
    names = ["streamtex"] + [p["name"] for p in packs]
    sources = [f'{p["name"]} = {{ git = "{url}", rev = "{p["rev"]}", subdirectory = "{p["subdirectory"]}" }}'
               for p in packs]
    direct = ["streamtex"] + [f'{p["name"]} @ git+{url}@{p["rev"]}#subdirectory={p["subdirectory"]}'
                              for p in packs]
    failures = []
    for form, deps, src, flags in (("stx pack sync", names, sources, ()),
                                   ("docker --no-sources", direct, [], ("--no-sources",))):
        d = work / f"{template.name}-{form.split()[0]}"
        d.mkdir()
        (d / "pyproject.toml").write_text(_project(f"check-{template.name}", deps, src))
        ok, out = _lock(d, *flags)
        print(f"{'ok  ' if ok else 'FAIL'} {template.name:16} {form:20} "
              + ", ".join(f"{p['name']}@{p['rev']}" for p in packs), flush=True)
        if not ok:
            failures.append(f"{template.name} ({form}):\n{out}")
    return failures


def main() -> int:
    templates = sorted(t for t in TEMPLATES.iterdir() if (t / "stx.toml").is_file() and _packs(t / "stx.toml"))
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        for t in templates:
            failures += check(t, Path(tmp))
    for f in failures:
        print("\n" + f, file=sys.stderr)
    print(f"{len(templates)} templates, {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
