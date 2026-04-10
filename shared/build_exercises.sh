#!/bin/bash
# Unified PDF build script for OMSN Exercise Books
# Usage: build_exercises.sh <input.md> <output.pdf> [lang]
#   lang defaults to pt-PT; use en-US for English, bilingual for bilingual

INPUT="$1"
OUTPUT="$2"
LANG="${3:-pt-PT}"
IS_BILINGUAL=false

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: build_exercises.sh <input.md> <output.pdf> [lang]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found"
  exit 1
fi

if [ "$LANG" = "bilingual" ]; then
  LANG="pt-PT"
  IS_BILINGUAL=true
fi

echo "Building $OUTPUT (lang=${3:-pt-PT})..."

HEADER_FILE=$(mktemp /tmp/omsn-header-XXXX.tex)
if [ "$IS_BILINGUAL" = true ]; then
  cat > "$HEADER_FILE" <<'TEXEOF'
\usepackage{graphicx}
\usepackage{paracol}
\usepackage{tabulary}
TEXEOF
else
  cat > "$HEADER_FILE" <<'TEXEOF'
\usepackage{graphicx}
TEXEOF
fi

set +e
pandoc "$INPUT" \
  -o "$OUTPUT" \
  --pdf-engine=xelatex \
  --from markdown-yaml_metadata_block \
  -V lang="$LANG" \
  -V geometry:margin=2.5cm \
  -V fontsize=12pt \
  -V documentclass=article \
  -V linestretch=1.3 \
  -V linkcolor=blue \
  -V urlcolor=blue \
  --include-in-header="$HEADER_FILE" \
  2>&1
EXIT_CODE=$?
set -e

rm -f "$HEADER_FILE"

if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ $OUTPUT"
  ls -lh "$OUTPUT"
  pdfinfo "$OUTPUT" 2>/dev/null | grep "Pages:" || true
else
  echo "❌ Failed: $OUTPUT (exit code $EXIT_CODE)"
  exit 1
fi
