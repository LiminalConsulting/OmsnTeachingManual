#!/bin/bash
# Script to generate Natural Sciences Exercise Book PDFs from Markdown

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Generating Natural Sciences Exercise Book PDFs..."
echo ""

# Define chapters
declare -a PT_FILES=(
  "EXERCISES_CH1_GEOLOGIA"
  "EXERCISES_CH2_BIOLOGIA_ECOLOGIA"
  "EXERCISES_CH3_BIOLOGIA_HUMANA"
  "EXERCISES_CH4_SUSTENTABILIDADE"
)

declare -a EN_FILES=(
  "EXERCISES_CH1_GEOLOGIA_EN"
  "EXERCISES_CH2_BIOLOGIA_ECOLOGIA_EN"
  "EXERCISES_CH3_BIOLOGIA_HUMANA_EN"
  "EXERCISES_CH4_SUSTENTABILIDADE_EN"
)

SUCCESS=0
FAIL=0

# Generate Portuguese PDFs
echo "--- Portuguese Exercise Books ---"
for FILE in "${PT_FILES[@]}"; do
  echo "Generating ${FILE}.pdf..."
  pandoc "${FILE}.md" \
    -o "${FILE}.pdf" \
    --pdf-engine=xelatex \
    -V lang=pt-PT \
    -V geometry:margin=2.5cm \
    -V fontsize=12pt \
    -V documentclass=article \
    -V linestretch=1.3 \
    -V linkcolor=blue \
    -V urlcolor=blue \
    --include-in-header=<(echo '\usepackage{graphicx}') \
    2>&1 | grep -v "WARNING" | grep -v "Missing character"

  if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "  OK: ${FILE}.pdf"
    ls -lh "${FILE}.pdf"
    ((SUCCESS++))
  else
    echo "  FAIL: ${FILE}.pdf"
    ((FAIL++))
  fi
  echo ""
done

# Generate English PDFs
echo "--- English Exercise Books ---"
for FILE in "${EN_FILES[@]}"; do
  echo "Generating ${FILE}.pdf..."
  pandoc "${FILE}.md" \
    -o "${FILE}.pdf" \
    --pdf-engine=xelatex \
    -V lang=en-US \
    -V geometry:margin=2.5cm \
    -V fontsize=12pt \
    -V documentclass=article \
    -V linestretch=1.3 \
    -V linkcolor=blue \
    -V urlcolor=blue \
    --include-in-header=<(echo '\usepackage{graphicx}') \
    2>&1 | grep -v "WARNING" | grep -v "Missing character"

  if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "  OK: ${FILE}.pdf"
    ls -lh "${FILE}.pdf"
    ((SUCCESS++))
  else
    echo "  FAIL: ${FILE}.pdf"
    ((FAIL++))
  fi
  echo ""
done

echo "Done! ${SUCCESS} succeeded, ${FAIL} failed."
