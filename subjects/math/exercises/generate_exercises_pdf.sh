#!/bin/bash
# Script to generate Exercise Book PDFs from Markdown

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📚 Generating Exercise Book PDFs..."
echo ""

# Define all chapters
declare -A PT_FILES
PT_FILES=(
  ["CH2_NUMEROS"]="EXERCISES_CH2_NUMEROS"
  ["CH3_ALGEBRA"]="EXERCISES_CH3_ALGEBRA"
  ["CH4_GEOMETRIA"]="EXERCISES_CH4_GEOMETRIA"
  ["CH5_MEDIDA"]="EXERCISES_CH5_MEDIDA"
  ["CH6_DADOS"]="EXERCISES_CH6_DADOS"
)

declare -A EN_FILES
EN_FILES=(
  ["CH2_NUMBERS"]="EXERCISES_CH2_NUMBERS_EN"
  ["CH3_ALGEBRA"]="EXERCISES_CH3_ALGEBRA_EN"
  ["CH4_GEOMETRY"]="EXERCISES_CH4_GEOMETRY_EN"
  ["CH5_MEASUREMENT"]="EXERCISES_CH5_MEASUREMENT_EN"
  ["CH6_DATA"]="EXERCISES_CH6_DATA_EN"
)

TOTAL=0
SUCCESS=0
FAIL=0

# Generate Portuguese PDFs
echo "🇵🇹 Generating Portuguese Exercise Books..."
echo ""
for key in $(echo "${!PT_FILES[@]}" | tr ' ' '\n' | sort); do
  FILE="${PT_FILES[$key]}"
  if [ -f "${FILE}.md" ]; then
    echo "  📖 ${FILE}..."
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

    EXIT_CODE=${PIPESTATUS[0]}
    TOTAL=$((TOTAL + 1))

    if [ $EXIT_CODE -eq 0 ]; then
      echo "  ✅ ${FILE}.pdf"
      SUCCESS=$((SUCCESS + 1))
    else
      echo "  ❌ Error generating ${FILE}.pdf"
      FAIL=$((FAIL + 1))
    fi
  else
    echo "  ⚠️  ${FILE}.md not found, skipping"
  fi
done

echo ""

# Generate English PDFs
echo "🇬🇧 Generating English Exercise Books..."
echo ""
for key in $(echo "${!EN_FILES[@]}" | tr ' ' '\n' | sort); do
  FILE="${EN_FILES[$key]}"
  if [ -f "${FILE}.md" ]; then
    echo "  📖 ${FILE}..."
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

    EXIT_CODE=${PIPESTATUS[0]}
    TOTAL=$((TOTAL + 1))

    if [ $EXIT_CODE -eq 0 ]; then
      echo "  ✅ ${FILE}.pdf"
      SUCCESS=$((SUCCESS + 1))
    else
      echo "  ❌ Error generating ${FILE}.pdf"
      FAIL=$((FAIL + 1))
    fi
  else
    echo "  ⚠️  ${FILE}.md not found, skipping"
  fi
done

echo ""
echo "📊 Results: ${SUCCESS}/${TOTAL} successful, ${FAIL} failed"
echo "📖 Done!"
