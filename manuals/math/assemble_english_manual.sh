#!/bin/bash

# Script to assemble English Mathematics Manual from translated topics
# Follows the thematic structure defined in MANUAL_STRUCTURE_THEMATIC_EN.md

TOPICS_DIR="../../extracted_topics/math"
OUTPUT_FILE="MANUAL_FINAL_EN.md"

echo "📚 Assembling English Mathematics Manual..."

# Create header with introduction
cat > "$OUTPUT_FILE" << 'EOF'
# Mathematics Manual: Grades 5-9
## Thematic Organization

This manual presents essential mathematics content for grades 5-9, organized by mathematical themes rather than by grade level. This approach provides an integrated view of conceptual progression, facilitating understanding of the natural evolution of concepts throughout the five years.

---

## Table of Contents

### NUMBERS
- Natural Numbers
- Integers
- Rational Numbers
- Real Numbers
- Powers and Scientific Notation

### ALGEBRA
- Algebraic Expressions
- Sequences and Patterns
- Equations and Inequalities
- Functions

### GEOMETRY
- Basic Elements
- Plane Figures
- Geometric Transformations
- Geometric Solids
- Trigonometry

### MEASUREMENT
- Area
- Volume

### DATA ORGANIZATION AND TREATMENT
- Data Representation
- Statistics
- Probability

---

# NUMBERS

EOF

# Append each topic in order
echo "Adding: Natural Numbers..."
cat "$TOPICS_DIR/numeros_naturais_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Integers..."
cat "$TOPICS_DIR/numeros_inteiros_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Rational Numbers..."
cat "$TOPICS_DIR/numeros_racionais_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Real Numbers..."
cat "$TOPICS_DIR/numeros_reais_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Powers and Scientific Notation..."
cat "$TOPICS_DIR/potencias_notacao_cientifica_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat >> "$OUTPUT_FILE" << 'EOF'

# ALGEBRA

EOF

echo "Adding: Algebraic Expressions..."
cat "$TOPICS_DIR/expressoes_algebricas_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Sequences and Patterns..."
cat "$TOPICS_DIR/sequencias_padroes_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Equations and Inequalities..."
cat "$TOPICS_DIR/equacoes_inequacoes_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Functions..."
cat "$TOPICS_DIR/funcoes_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat >> "$OUTPUT_FILE" << 'EOF'

# GEOMETRY

EOF

echo "Adding: Basic Elements..."
cat "$TOPICS_DIR/elementos_basicos_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Plane Figures..."
cat "$TOPICS_DIR/figuras_planas_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Geometric Transformations..."
cat "$TOPICS_DIR/transformacoes_geometricas_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Geometric Solids..."
cat "$TOPICS_DIR/solidos_geometricos_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Trigonometry..."
cat "$TOPICS_DIR/trigonometria_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat >> "$OUTPUT_FILE" << 'EOF'

# MEASUREMENT

EOF

echo "Adding: Area..."
cat "$TOPICS_DIR/area_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Volume..."
cat "$TOPICS_DIR/volume_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat >> "$OUTPUT_FILE" << 'EOF'

# DATA ORGANIZATION AND TREATMENT

EOF

echo "Adding: Data Representation..."
cat "$TOPICS_DIR/representacao_dados_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Statistics..."
cat "$TOPICS_DIR/estatistica_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Adding: Probability..."
cat "$TOPICS_DIR/probabilidades_EN.md" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Add footer
cat >> "$OUTPUT_FILE" << 'EOF'

---

**Content adapted from:** O Bichinho do Saber (www.obichinhodosaber.com)
EOF

echo "✅ English manual assembled: $OUTPUT_FILE"
wc -l "$OUTPUT_FILE"
