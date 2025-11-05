#!/bin/bash
# Generate standalone bilingual cover page

echo "🎨 Generating bilingual cover page..."

pandoc COVER_BILINGUAL.md \
  -o COVER_BILINGUAL.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=0cm \
  -V papersize=letter \
  --include-in-header=<(echo '\usepackage{graphicx}') \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

if [ $? -eq 0 ]; then
  echo "✅ Bilingual cover generated: COVER_BILINGUAL.pdf"
  ls -lh COVER_BILINGUAL.pdf
  pdfinfo COVER_BILINGUAL.pdf | grep "Pages:"
else
  echo "❌ Error generating bilingual cover"
  exit 1
fi
