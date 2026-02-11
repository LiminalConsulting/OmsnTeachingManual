#!/bin/bash
# Script to generate Exercise Book PDFs from Markdown

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📚 Generating Exercise Book PDFs..."
echo ""

# Generate Portuguese PDF
echo "🇵🇹 Generating Portuguese Exercise Book..."
pandoc EXERCISES_CH2_NUMEROS.md \
  -o EXERCISES_CH2_NUMEROS.pdf \
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

PT_EXIT_CODE=${PIPESTATUS[0]}

if [ $PT_EXIT_CODE -eq 0 ]; then
  echo "✅ Portuguese PDF generated: EXERCISES_CH2_NUMEROS.pdf"
  ls -lh EXERCISES_CH2_NUMEROS.pdf
else
  echo "❌ Error generating Portuguese PDF"
fi

echo ""

# Generate English PDF
echo "🇬🇧 Generating English Exercise Book..."
pandoc EXERCISES_CH2_NUMBERS_EN.md \
  -o EXERCISES_CH2_NUMBERS_EN.pdf \
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

EN_EXIT_CODE=${PIPESTATUS[0]}

if [ $EN_EXIT_CODE -eq 0 ]; then
  echo "✅ English PDF generated: EXERCISES_CH2_NUMBERS_EN.pdf"
  ls -lh EXERCISES_CH2_NUMBERS_EN.pdf
else
  echo "❌ Error generating English PDF"
fi

echo ""
echo "📖 Done!"
