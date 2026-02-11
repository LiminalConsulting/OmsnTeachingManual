#!/bin/bash
# Script to generate Physics-Chemistry Exercise Book PDFs from Markdown

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Generating Physics-Chemistry Exercise Book PDFs..."
echo ""

# Define all chapters
declare -A PT_FILES
PT_FILES=(
  ["CH1_ASTRONOMIA"]="EXERCISES_CH1_ASTRONOMIA"
  ["CH2_MECANICA"]="EXERCISES_CH2_MECANICA"
  ["CH3_ENERGIA"]="EXERCISES_CH3_ENERGIA"
  ["CH4_ONDAS"]="EXERCISES_CH4_ONDAS"
  ["CH5_ELETRICIDADE"]="EXERCISES_CH5_ELETRICIDADE"
  ["CH6_MATERIAIS"]="EXERCISES_CH6_MATERIAIS"
  ["CH7_REACOES"]="EXERCISES_CH7_REACOES"
  ["CH8_ESTRUTURA_ATOMICA"]="EXERCISES_CH8_ESTRUTURA_ATOMICA"
)

declare -A EN_FILES
EN_FILES=(
  ["CH1_ASTRONOMY"]="EXERCISES_CH1_ASTRONOMY_EN"
  ["CH2_MECHANICS"]="EXERCISES_CH2_MECHANICS_EN"
  ["CH3_ENERGY"]="EXERCISES_CH3_ENERGY_EN"
  ["CH4_WAVES"]="EXERCISES_CH4_WAVES_EN"
  ["CH5_ELECTRICITY"]="EXERCISES_CH5_ELECTRICITY_EN"
  ["CH6_MATERIALS"]="EXERCISES_CH6_MATERIALS_EN"
  ["CH7_REACTIONS"]="EXERCISES_CH7_REACTIONS_EN"
  ["CH8_ATOMIC_STRUCTURE"]="EXERCISES_CH8_ATOMIC_STRUCTURE_EN"
)

TOTAL=0
SUCCESS=0
FAIL=0

# Generate Portuguese PDFs
echo "Generating Portuguese Exercise Books..."
echo ""
for key in $(echo "${!PT_FILES[@]}" | tr ' ' '\n' | sort); do
  FILE="${PT_FILES[$key]}"
  if [ -f "${FILE}.md" ]; then
    echo "  ${FILE}..."
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
      echo "  OK ${FILE}.pdf"
      SUCCESS=$((SUCCESS + 1))
    else
      echo "  ERROR generating ${FILE}.pdf"
      FAIL=$((FAIL + 1))
    fi
  else
    echo "  SKIP ${FILE}.md not found"
  fi
done

echo ""

# Generate English PDFs
echo "Generating English Exercise Books..."
echo ""
for key in $(echo "${!EN_FILES[@]}" | tr ' ' '\n' | sort); do
  FILE="${EN_FILES[$key]}"
  if [ -f "${FILE}.md" ]; then
    echo "  ${FILE}..."
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
      echo "  OK ${FILE}.pdf"
      SUCCESS=$((SUCCESS + 1))
    else
      echo "  ERROR generating ${FILE}.pdf"
      FAIL=$((FAIL + 1))
    fi
  else
    echo "  SKIP ${FILE}.md not found"
  fi
done

echo ""
echo "Results: ${SUCCESS}/${TOTAL} successful, ${FAIL} failed"
echo "Done!"
