#!/bin/bash
# Unified PDF build script for OMSN Teaching Manuals
# Usage: build.sh <input.md> <output.pdf> [lang]
#   lang defaults to pt-PT; use en-US for English versions

set -e

INPUT="$1"
OUTPUT="$2"
LANG="${3:-pt-PT}"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: build.sh <input.md> <output.pdf> [lang]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found"
  exit 1
fi

# Cover file: COVER.md for PT, COVER_EN.md for EN, COVER_BILINGUAL.md for bilingual
if [ "$LANG" = "en-US" ]; then
  COVER="COVER_EN.md"
elif [ "$LANG" = "bilingual" ]; then
  COVER="COVER_BILINGUAL.md"
  LANG="pt-PT"  # paracol handles internal language; outer doc is PT
else
  COVER="COVER.md"
fi

echo "Building $OUTPUT (lang=$LANG)..."

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
  --include-in-header=<(echo '\usepackage{graphicx}\usepackage{paracol}') \
  --include-before-body="$COVER" \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

EXIT_CODE=${PIPESTATUS[0]}

if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ $OUTPUT"
  ls -lh "$OUTPUT"
  pdfinfo "$OUTPUT" 2>/dev/null | grep "Pages:" || true
else
  echo "❌ Failed: $OUTPUT"
  exit 1
fi
