#!/usr/bin/env bash
# 验证 Arturo "字典 + 指针" 核心心智模型的六个元能力关键字
# 等同于运行 tests/modules/core/mental-model.art
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -n "${ARTURO_BIN:-}" ]]; then
  :
elif [[ -x "$ROOT/skills/arturo-language/bin/arturo" ]]; then
  ARTURO_BIN="$ROOT/skills/arturo-language/bin/arturo"
elif [[ -x "/tmp/arturo-language-skill/bin/arturo" ]]; then
  ARTURO_BIN="/tmp/arturo-language-skill/bin/arturo"
else
  echo "Arturo runtime not found."
  echo "  git clone https://github.com/scifx/arturo-language-skill.git skills/arturo-language"
  exit 1
fi

exec "$ARTURO_BIN" --no-color "$ROOT/tests/modules/core/mental-model.art"