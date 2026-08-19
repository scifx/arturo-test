#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# This repository does not vendor or auto-fetch the upstream skill.
# Prepare it yourself when needed, then point this runner at its runtime.
# Defaults keep local runs fast and offline after the skill has been prepared once.
if [[ -n "${ARTURO_BIN:-}" ]]; then
  :
elif [[ -n "${ARTURO_SKILL_DIR:-}" ]]; then
  ARTURO_BIN="$ARTURO_SKILL_DIR/bin/arturo"
elif [[ -x "$ROOT/skills/arturo-language/bin/arturo" ]]; then
  ARTURO_BIN="$ROOT/skills/arturo-language/bin/arturo"
elif [[ -x "/tmp/arturo-language-skill/bin/arturo" ]]; then
  ARTURO_BIN="/tmp/arturo-language-skill/bin/arturo"
else
  echo "Arturo runtime not found." >&2
  echo "Prepare the upstream skill manually, for example:" >&2
  echo "  git clone https://github.com/scifx/arturo-language-skill.git /tmp/arturo-language-skill" >&2
  echo "Then run one of:" >&2
  echo "  ARTURO_SKILL_DIR=/tmp/arturo-language-skill ./tests/run-all.sh" >&2
  echo "  ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo ./tests/run-all.sh" >&2
  exit 1
fi

if [[ ! -x "$ARTURO_BIN" ]]; then
  echo "Arturo runtime not found or not executable: $ARTURO_BIN" >&2
  exit 1
fi

echo "Using Arturo runtime: $ARTURO_BIN"
"$ARTURO_BIN" --version
echo

status=0
count=0
while IFS= read -r -d '' file; do
  count=$((count + 1))
  rel="${file#$ROOT/}"
  echo "==> $rel"
  if ! "$ARTURO_BIN" --no-color "$file"; then
    status=1
  fi
  echo
done < <(find "$ROOT/tests/official-library" "$ROOT/tests/modules" "$ROOT/tests/projects" -type f -name '*.art' -print0 | sort -z)

echo "Ran $count Arturo test file(s)."
exit "$status"
