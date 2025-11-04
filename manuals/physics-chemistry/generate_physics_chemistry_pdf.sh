#!/bin/bash

# Generate Physics-Chemistry Teaching Manual PDF
# Uses Pandoc with XeLaTeX engine for professional book-style output

echo "🔄 Fixing formatting (numbering, lists, formulas)..."
python3 fix_formatting.py

echo "🔄 Generating Physics-Chemistry Manual PDF..."

pandoc MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md \
  -o MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf \
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
  -V lang=pt-PT \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

PDF_EXIT_CODE=${PIPESTATUS[0]}

if [ $PDF_EXIT_CODE -eq 0 ]; then
    echo "✅ PDF generated successfully: MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf"
    echo "📄 Location: $(pwd)/MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf"
else
    echo "❌ PDF generation failed. Check error messages above."
    exit 1
fi
