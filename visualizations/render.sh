#!/bin/bash
# Manim visualization render script
# Usage: ./render.sh <python_file> <BaseSceneName> [output_name]
# Renders both Light and Dark versions automatically

set -e

# Activate conda environment
eval "$(/opt/homebrew/Caskroom/miniconda/base/bin/conda shell.bash hook)"
conda activate manim

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON_FILE="${1:-triangle_angles.py}"
BASE_SCENE="${2:-TriangleAnglesSum}"
OUTPUT_NAME="${3:-$(echo "$BASE_SCENE" | sed 's/\([A-Z]\)/_\L\1/g' | sed 's/^_//')}"

echo "Rendering ${BASE_SCENE}Light and ${BASE_SCENE}Dark from $PYTHON_FILE..."

# -qh = high quality, -s = save last frame as image
manim -qh -s "$PYTHON_FILE" "${BASE_SCENE}Light" -o "${OUTPUT_NAME}_light.png"
manim -qh -s "$PYTHON_FILE" "${BASE_SCENE}Dark" -o "${OUTPUT_NAME}_dark.png"

OUTDIR="media/images/$(basename "$PYTHON_FILE" .py)"
echo "Done!"
echo "  Light: $OUTDIR/${OUTPUT_NAME}_light.png"
echo "  Dark:  $OUTDIR/${OUTPUT_NAME}_dark.png"
