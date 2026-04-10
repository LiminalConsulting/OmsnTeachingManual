#!/bin/bash
# Unified PDF build script for OMSN Teaching Manuals
# Usage: build.sh <input.md> <output.pdf> [lang]
#   lang defaults to pt-PT; use en-US for English versions

INPUT="$1"
OUTPUT="$2"
LANG="${3:-pt-PT}"
IS_BILINGUAL=false

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: build.sh <input.md> <output.pdf> [lang]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found"
  exit 1
fi

# Cover file: COVER.md for PT, COVER_EN.md for EN, COVER_BILINGUAL.md for bilingual
COVER_ARGS=""
if [ "$LANG" = "en-US" ]; then
  COVER="COVER_EN.md"
elif [ "$LANG" = "bilingual" ]; then
  COVER="COVER_BILINGUAL.md"
  LANG="pt-PT"
  IS_BILINGUAL=true
else
  COVER="COVER.md"
fi

if [ -f "$COVER" ]; then
  COVER_ARGS="--include-before-body=$COVER"
else
  echo "Warning: Cover file $COVER not found, building without cover"
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
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V lang="$LANG" \
  -V geometry:margin=2.5cm \
  -V fontsize=11pt \
  -V documentclass=book \
  -V linestretch=1.15 \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V classoption=openany \
  --include-in-header="$HEADER_FILE" \
  $COVER_ARGS \
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
