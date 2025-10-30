# PDF Generation Guide

## Overview

This document explains how to generate a professional, print-ready PDF from the mathematics manual.

## Files

- **MANUAL_FINAL.md** - Original assembled manual with plain text/Unicode math
- **MANUAL_FINAL_PRINT.md** - Enhanced version with LaTeX math notation
- **MANUAL_FINAL.pdf** - Generated PDF (44 pages, 128KB)
- **generate_pdf.sh** - Automated script to regenerate the PDF
- **pandoc-template.yaml** - Advanced template (optional, for custom styling)

## Quick Start

To regenerate the PDF:

```bash
./generate_pdf.sh
```

Or manually:

```bash
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
  -V linestretch=1.15
```

## Requirements

- **Pandoc** (version 3.6.1 or later)
- **XeLaTeX** (comes with BasicTeX or MacTeX)

Install on macOS:
```bash
brew install pandoc basictex
```

## Mathematical Notation

The enhanced Markdown file (`MANUAL_FINAL_PRINT.md`) uses LaTeX math notation:

### Inline Math
```markdown
The formula is $a^2 + b^2 = c^2$.
```

### Display Math
```markdown
$$\frac{a \times b}{2}$$
```

### Common Notations

| Concept | LaTeX | Output |
|---------|-------|--------|
| Fractions | `$\frac{a}{b}$` | a/b |
| Square root | `$\sqrt{a}$` | √a |
| Cube root | `$\sqrt[3]{a}$` | ∛a |
| Exponents | `$x^2$` | x² |
| Sets | `$\mathbb{N}$` | ℕ |
| Greek | `$\pi$, $\alpha$` | π, α |
| Relations | `$\leq$, `\neq$` | ≤, ≠ |

## PDF Features

The generated PDF includes:

- ✅ **Table of Contents** - Automatically generated with 3 levels
- ✅ **Section Numbering** - Hierarchical (1.1, 1.2, 2.1, etc.)
- ✅ **Professional Typography** - Book-style layout
- ✅ **Beautiful Math** - LaTeX-rendered formulas
- ✅ **Portuguese Support** - Full UTF-8 encoding
- ✅ **Print-Ready** - A4 format with proper margins (2.5cm)
- ✅ **Clickable Links** - Blue hyperlinks in TOC and cross-references

## Document Structure

```
Manual de Matemática: 5º ao 9º Ano

1. NÚMEROS
   1.1 Números Naturais
   1.2 Números Inteiros
   1.3 Números Racionais
   1.4 Números Reais
   1.5 Potências e Notação Científica

2. ÁLGEBRA
   2.1 Expressões Algébricas
   2.2 Sequências e Padrões
   2.3 Equações e Inequações
   2.4 Funções

3. GEOMETRIA
   3.1 Elementos Básicos
   3.2 Figuras Planas
   3.3 Transformações Geométricas
   3.4 Sólidos Geométricos
   3.5 Trigonometria

4. MEDIDA
   4.1 Área
   4.2 Volume

5. ORGANIZAÇÃO E TRATAMENTO DE DADOS
   5.1 Representação de Dados
   5.2 Estatística
   5.3 Probabilidades
```

## Customization

### Change Page Margins

Edit the geometry setting:
```bash
-V geometry:margin=3cm  # Larger margins
```

### Change Font Size

```bash
-V fontsize=12pt  # Larger text
```

### Change Line Spacing

```bash
-V linestretch=1.5  # More spacing between lines
```

### Use Custom Fonts

```bash
-V mainfont="Libertinus Serif" \
-V sansfont="Libertinus Sans"
```

Note: Fonts must be installed on your system.

## Advanced: Custom Template

For more control, use the YAML template:

```bash
pandoc MANUAL_FINAL_PRINT.md \
  --metadata-file=pandoc-template.yaml \
  -o MANUAL_FINAL.pdf \
  --pdf-engine=xelatex
```

Edit `pandoc-template.yaml` to customize:
- Headers and footers
- Chapter styling
- Title page
- Typography details

## Troubleshooting

### "withBinaryFile: does not exist"
This error occurs with very long command lines. Use the script instead:
```bash
./generate_pdf.sh
```

### Missing character warnings
These are cosmetic - the PDF still generates. They occur for special Unicode symbols (✓, etc.) that aren't in the default font.

### LaTeX errors
Check `MANUAL_FINAL_PRINT.md` for:
- Unclosed math delimiters (`$...$`)
- Invalid LaTeX commands
- Nested equation environments

## Output Specifications

- **Format:** PDF 1.5
- **Pages:** 48
- **Size:** ~130KB
- **Paper:** A4 (210 × 297mm)
- **Margins:** 2.5cm all sides
- **Font Size:** 11pt base
- **Line Height:** 1.15
- **Language:** Portuguese (pt-PT)

## Source Attribution

Content adapted from **O Bichinho do Saber** (www.obichinhodosaber.com)

---

*Generated with Pandoc and XeLaTeX*
