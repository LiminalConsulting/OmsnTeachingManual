#!/bin/bash
# Script to generate the English Physics-Chemistry Manual PDF

echo "🔄 Generating English PDF from MANUAL_FINAL_PHYSICS_CHEMISTRY_EN_PRINT.md..."

pandoc COVER_EN.md MANUAL_FINAL_PHYSICS_CHEMISTRY_EN_PRINT.md \
  -o MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V geometry:margin=2.5cm \
  -V documentclass=book \
  -V fontsize=11pt \
  -V linestretch=1.15 \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V lang=en-US \
  -V classoption=openany \
  --include-in-header=<(echo '\usepackage{graphicx}') \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

PDF_EXIT_CODE=${PIPESTATUS[0]}

if [ $PDF_EXIT_CODE -eq 0 ]; then
    echo "✅ English PDF generated successfully: MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf"
    ls -lh MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf
    pdfinfo MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf | grep "Pages:"
else
    echo "❌ PDF generation failed"
    exit 1
fi
