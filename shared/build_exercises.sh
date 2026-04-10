#!/bin/bash
# Unified PDF build script for OMSN Exercise Books
# Usage: build_exercises.sh <input.md> <output.pdf> [lang]
#   lang defaults to pt-PT; use en-US for English, bilingual for bilingual

set -e

INPUT="$1"
OUTPUT="$2"
LANG="${3:-pt-PT}"

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
fi

echo "Building $OUTPUT (lang=$LANG)..."

pandoc "$INPUT" \
  -o "$OUTPUT" \
  --pdf-engine=xelatex \
  -V lang="$LANG" \
  -V geometry:margin=2.5cm \
  -V fontsize=12pt \
  -V documentclass=article \
  -V linestretch=1.3 \
  -V linkcolor=blue \
  -V urlcolor=blue \
  --include-in-header=<(echo '\usepackage{graphicx}\usepackage{paracol}') \
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
