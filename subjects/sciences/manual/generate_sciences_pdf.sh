#!/bin/bash
# Script to generate the Manual de Ciências Naturais PDF from Markdown

echo "🔄 Generating Sciences PDF with cover from MANUAL_FINAL_SCIENCES_PRINT.md..."

pandoc COVER.md MANUAL_FINAL_SCIENCES_PRINT.md \
  -o MANUAL_FINAL_SCIENCES.pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V lang=pt-PT \
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
  echo "✅ PDF generated successfully: MANUAL_FINAL_SCIENCES.pdf"
  ls -lh MANUAL_FINAL_SCIENCES.pdf
  echo ""
  pdfinfo MANUAL_FINAL_SCIENCES.pdf | grep "Pages:"
else
  echo "❌ Error generating PDF"
  exit 1
fi
