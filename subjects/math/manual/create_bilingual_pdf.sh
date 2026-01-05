#!/bin/bash
# Create bilingual PDF by interleaving Portuguese and English pages
# Uses pdftk-like approach with gs (ghostscript)

PT_PDF="MANUAL_FINAL.pdf"
EN_PDF="MANUAL_FINAL_EN.pdf"
OUTPUT_PDF="MANUAL_FINAL_BILINGUAL.pdf"
TEMP_DIR="./temp_bilingual"

echo "📖 Creating bilingual PDF..."

# Get page counts
PT_PAGES=$(pdfinfo "$PT_PDF" | grep "Pages:" | awk '{print $2}')
EN_PAGES=$(pdfinfo "$EN_PDF" | grep "Pages:" | awk '{print $2}')

echo "Portuguese pages: $PT_PAGES"
echo "English pages: $EN_PAGES"

if [ "$PT_PAGES" -ne "$EN_PAGES" ]; then
    echo "⚠️  Warning: Page counts don't match!"
    exit 1
fi

# Create temp directory
mkdir -p "$TEMP_DIR"

echo "Extracting pages..."

# Extract individual pages
for i in $(seq 1 $PT_PAGES); do
    # Extract Portuguese page
    gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
       -dFirstPage=$i -dLastPage=$i \
       -sOutputFile="$TEMP_DIR/pt_page_$(printf %03d $i).pdf" \
       "$PT_PDF" 2>/dev/null

    # Extract English page
    gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
       -dFirstPage=$i -dLastPage=$i \
       -sOutputFile="$TEMP_DIR/en_page_$(printf %03d $i).pdf" \
       "$EN_PDF" 2>/dev/null

    if [ $((i % 10)) -eq 0 ]; then
        echo "Extracted $i/$PT_PAGES page pairs..."
    fi
done

echo "Merging pages..."

# Build file list for merging (interleaved)
FILE_LIST=""
for i in $(seq 1 $PT_PAGES); do
    FILE_LIST="$FILE_LIST $TEMP_DIR/pt_page_$(printf %03d $i).pdf"
    FILE_LIST="$FILE_LIST $TEMP_DIR/en_page_$(printf %03d $i).pdf"
done

# Merge all pages
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
   -sOutputFile="$OUTPUT_PDF" \
   $FILE_LIST 2>/dev/null

# Clean up
rm -rf "$TEMP_DIR"

TOTAL_PAGES=$((PT_PAGES * 2))

echo ""
echo "✅ Bilingual PDF created: $OUTPUT_PDF"
echo "📄 Total pages: $TOTAL_PAGES ($PT_PAGES Portuguese + $EN_PAGES English)"
echo ""
echo "📖 Reading guide:"
echo "   - Odd pages (1, 3, 5...): Portuguese"
echo "   - Even pages (2, 4, 6...): English"
echo "   - Each spread shows the same content side-by-side"
