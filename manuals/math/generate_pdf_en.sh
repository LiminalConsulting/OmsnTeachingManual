#!/bin/bash
# Script to generate the English Mathematics Manual PDF from Markdown

echo "🔄 Generating English PDF from MANUAL_FINAL_EN_PRINT.md..."

pandoc COVER_EN.md MANUAL_FINAL_EN_PRINT.md \
  -o MANUAL_FINAL_EN.pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V lang=en-US \
  -V geometry:margin=2.5cm \
  -V fontsize=11pt \
  -V documentclass=book \
  -V linestretch=1.15 \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V classoption=openany \
  --include-in-header=<(echo '\usepackage{graphicx}') \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

PDF_EXIT_CODE=${PIPESTATUS[0]}

if [ $PDF_EXIT_CODE -eq 0 ]; then
  echo "✅ English PDF generated successfully: MANUAL_FINAL_EN.pdf"
  ls -lh MANUAL_FINAL_EN.pdf
  echo ""
  pdfinfo MANUAL_FINAL_EN.pdf | grep "Pages:"
else
  echo "❌ Error generating English PDF"
  exit 1
fi
