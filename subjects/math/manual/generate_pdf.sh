#!/bin/bash
# Script to generate the Manual de Matemática PDF from Markdown

echo "🔄 Generating PDF with cover from MANUAL_FINAL_PRINT.md..."

pandoc MANUAL_FINAL_PRINT.md \
  -o MANUAL_FINAL.pdf \
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
  --include-before-body=COVER.md \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

PDF_EXIT_CODE=${PIPESTATUS[0]}

if [ $PDF_EXIT_CODE -eq 0 ]; then
  echo "✅ PDF generated successfully: MANUAL_FINAL.pdf"
  ls -lh MANUAL_FINAL.pdf
  echo ""
  pdfinfo MANUAL_FINAL.pdf | grep "Pages:"
else
  echo "❌ Error generating PDF"
  exit 1
fi
