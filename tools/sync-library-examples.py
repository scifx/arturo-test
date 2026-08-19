#!/usr/bin/env python3
"""Copy/export upstream Arturo library examples into this repository's module folders.

This tool does not clone/fetch the upstream skill. Prepare it manually, then run:

    ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo \
    LIBRARY_INDEX=/tmp/arturo-language-skill/references/library-index.csv \
    python3 tools/sync-library-examples.py

Outputs:
- tests/modules/<module>/官方示例.md        all exported examples for review/feedback
- tests/modules/<module>/official-examples-smoke.art for modules empirically safe to run as raw examples
- examples/library/*.md                    central index copy
"""
from __future__ import annotations

import csv, json, os, subprocess, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTURO_BIN = Path(os.environ.get("ARTURO_BIN", "/tmp/arturo-language-skill/bin/arturo"))
LIBRARY_INDEX = Path(os.environ.get("LIBRARY_INDEX", "/tmp/arturo-language-skill/references/library-index.csv"))
MODULES_DIR = ROOT / "tests" / "modules"
EXAMPLES_DIR = ROOT / "examples" / "library"

# Full raw official examples for these modules passed in this sandbox/runtime.
# Other modules still get Markdown examples, but are not auto-executed because they
# need files/network/UI/input/external libs, contain known stale examples, or may hang.
EXECUTABLE_MODULES = {
    "arithmetic", "bitwise", "colors", "comparison", "crypto", "dates",
    "paths", "quantities", "sets", "statistics",
}

if not ARTURO_BIN.exists():
    raise SystemExit(f"ARTURO_BIN not found: {ARTURO_BIN}")
if not LIBRARY_INDEX.exists():
    raise SystemExit(f"LIBRARY_INDEX not found: {LIBRARY_INDEX}")

rows = list(csv.DictReader(LIBRARY_INDEX.open(newline="")))
by_module: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in rows:
    by_module[row["module"]].append(row)

cache: dict[str, list[str] | None] = {}
errors: list[tuple[str, str]] = []

def examples_for(symbol: str) -> list[str]:
    if symbol in cache:
        return cache[symbol] or []
    expr = f"write.json (info.get '{symbol} | get 'example) null | print"
    try:
        proc = subprocess.run([str(ARTURO_BIN), "--no-color", "-e", expr], cwd=ROOT,
                              text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
    except subprocess.TimeoutExpired:
        errors.append((symbol, "timeout while reading info.get example"))
        cache[symbol] = []
        return []
    if proc.returncode != 0:
        errors.append((symbol, proc.stderr.strip().splitlines()[0] if proc.stderr.strip() else "info.get failed"))
        cache[symbol] = []
        return []
    try:
        data = json.loads(proc.stdout)
    except Exception as exc:
        errors.append((symbol, f"JSON parse failed: {exc}"))
        data = []
    if not isinstance(data, list):
        data = []
    cache[symbol] = [str(x) for x in data]
    return cache[symbol] or []

EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
summary=[]

for module, mod_rows in sorted(by_module.items()):
    module_dir = MODULES_DIR / module
    module_dir.mkdir(parents=True, exist_ok=True)

    md = [
        f"# {module} 官方示例",
        "",
        "本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：",
        "",
        "```arturo",
        "info.get 'symbol | get 'example",
        "```",
        "",
        "它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。",
        "",
    ]
    smoke = [
        f"; Generated raw official examples smoke for module: {module}",
        "; Source: info.get 'symbol | get 'example from the prepared upstream skill/runtime.",
        "; This file intentionally runs only modules whose full raw examples passed locally.",
        "",
    ]
    symbol_count=0; example_count=0
    for row in sorted(mod_rows, key=lambda r: r["name"]):
        name=row["name"]; symbol_count+=1
        exs=examples_for(name); example_count += len(exs)
        md += [f"## `{name}`", "", f"Documentation: {row['stable_url']}", ""]
        if not exs:
            md += ["> 当前 runtime 未导出示例，或该 symbol 在当前 build 中不可解析。", ""]
        for i, code in enumerate(exs, 1):
            md += [f"### Example {i}", "", "```arturo", code.rstrip(), "```", ""]
            if module in EXECUTABLE_MODULES:
                smoke += [f"; --- {name} example {i} ---", code.rstrip(), ""]

    md_text="\n".join(md)
    (module_dir / "官方示例.md").write_text(md_text, encoding="utf-8")
    (EXAMPLES_DIR / f"{module}.md").write_text(md_text, encoding="utf-8")
    if module in EXECUTABLE_MODULES:
        smoke += [f'print "PASS official-examples/{module}"', ""]
        (module_dir / "official-examples-smoke.art").write_text("\n".join(smoke), encoding="utf-8")
    else:
        stale = module_dir / "official-examples-smoke.art"
        if stale.exists():
            stale.unlink()
    summary.append((module, symbol_count, example_count, module in EXECUTABLE_MODULES))

index = [
    "# Arturo Library Examples",
    "",
    "默认官方示例索引，来自上游 skill/runtime 的 `info.get 'symbol | get 'example`。",
    "",
    "本目录不包含上游 skill；只保存导出的示例文本。模块目录中的 `官方示例.md` 是主要工作区。",
    "",
    "| Module | Symbols | Examples | Raw smoke? | File |",
    "|---|---:|---:|---|---|",
]
for module, sc, ec, smoke in summary:
    index.append(f"| `{module}` | {sc} | {ec} | {'yes' if smoke else 'manual/curated'} | [`{module}.md`](./{module}.md) |")
index += ["", f"Total symbols: {sum(x[1] for x in summary)}", f"Total examples: {sum(x[2] for x in summary)}", ""]
if errors:
    index += ["## Export warnings", ""] + [f"- `{n}`: {m}" for n,m in errors]
(EXAMPLES_DIR / "README.md").write_text("\n".join(index), encoding="utf-8")

print(f"Synced {sum(x[2] for x in summary)} examples for {sum(x[1] for x in summary)} symbols")
print(f"Executable raw-smoke modules: {', '.join(sorted(EXECUTABLE_MODULES))}")
if errors:
    print(f"Export warnings: {len(errors)}", file=sys.stderr)
