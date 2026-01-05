#!/bin/bash
# Split Sciences manual into 2 parts for translation

SOURCE="MANUAL_FINAL_SCIENCES_PRINT.md"
TOTAL_LINES=$(wc -l < "$SOURCE")
HALF=$((TOTAL_LINES / 2))

echo "📄 Splitting $SOURCE ($TOTAL_LINES lines) into 2 parts..."

# Part 1: First half
head -n $HALF "$SOURCE" > "${SOURCE%.md}_PART1.md"
echo "✅ Part 1: Lines 1-$HALF"

# Part 2: Second half
tail -n +$((HALF + 1)) "$SOURCE" > "${SOURCE%.md}_PART2.md"
echo "✅ Part 2: Lines $((HALF + 1))-$TOTAL_LINES"

echo ""
echo "Files created:"
ls -lh "${SOURCE%.md}_PART1.md" "${SOURCE%.md}_PART2.md"
