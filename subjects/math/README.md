# Mathematics (Matemática)

Portuguese mathematics curriculum for grades 5-9 (5º ao 9º Ano).

## Structure

```
math/
├── curriculum/           # Official DGE Aprendizagens Essenciais PDFs
├── extracted_topics/     # Raw extracted markdown by topic (PT + EN)
├── manual/               # Final manual files (PDFs, build scripts)
├── visualizations/       # Manim scripts for geometric visualizations
└── reference/            # Grade summaries and draft materials
```

## Contents

### Curriculum (5 PDFs)
Official "Aprendizagens Essenciais" from DGE for grades 5-9.

### Topics Covered
- Numbers: Natural, Integers, Rationals, Reals
- Algebra: Expressions, Equations, Inequalities, Functions
- Geometry: Basic Elements, Plane Figures, Solids, Transformations
- Measurement: Area, Volume, Trigonometry
- Statistics & Probability

### Manuals
- **Portuguese:** MANUAL_FINAL_MATH.pdf (49 pages)
- **English:** MANUAL_FINAL_MATH_EN.pdf (49 pages)

### Visualizations
Manim Python scripts for generating geometric diagrams:
- Triangle classifications, angle types
- Geometric transformations (rotation, reflection, translation)
- 3D solids (prism, pyramid, cone, cylinder, sphere)
- Pythagorean theorem

## Building the Manual

```bash
cd manual/
./generate_math_pdf.sh          # Portuguese
./generate_pdf_en.sh            # English
./create_bilingual_pdf.sh       # Side-by-side bilingual
```

## Rendering Visualizations

```bash
cd visualizations/
./render.sh <script_name>       # Renders both light and dark versions
```

Requires: Manim (in `manim` conda environment)
