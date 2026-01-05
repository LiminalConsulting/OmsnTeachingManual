# Manual de Matemática (5º ao 9º Ano)

## Final Product

**📕 [MANUAL_FINAL.pdf](MANUAL_FINAL.pdf)** - 48 pages, professionally formatted

## Files

- **MANUAL_FINAL.pdf** - The final PDF (main output)
- **MANUAL_FINAL_PRINT.md** - Markdown with LaTeX math notation (PDF source)
- **MANUAL_FINAL.md** - Plain markdown version
- **generate_pdf.sh** - Script to regenerate the PDF

## Content Structure

The manual covers 19 mathematics topics organized thematically:

1. **NÚMEROS** (Numbers)
   - Números Naturais, Inteiros, Racionais, Reais
   - Potências e Notação Científica

2. **ÁLGEBRA** (Algebra)
   - Expressões Algébricas
   - Sequências e Padrões
   - Equações e Inequações
   - Funções

3. **GEOMETRIA** (Geometry)
   - Elementos Básicos
   - Figuras Planas
   - Transformações Geométricas
   - Sólidos Geométricos
   - Trigonometria

4. **MEDIDA** (Measurement)
   - Área
   - Volume

5. **ORGANIZAÇÃO E TRATAMENTO DE DADOS** (Data Organization)
   - Representação de Dados
   - Estatística
   - Probabilidades

## Regenerating the PDF

To regenerate the PDF from the markdown source:

```bash
./generate_pdf.sh
```

Or manually with pandoc:

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

### Requirements

- Pandoc (version 3.6+)
- XeLaTeX (comes with BasicTeX or MacTeX)

Install on macOS:
```bash
brew install pandoc basictex
```

## PDF Features

- ✅ Table of contents (3 levels)
- ✅ Section numbering (1.1, 1.2, etc.)
- ✅ Professional book-style layout
- ✅ LaTeX-rendered mathematical formulas
- ✅ Portuguese language support
- ✅ Print-ready A4 format (2.5cm margins)
- ✅ Clickable hyperlinks

## Source Attribution

Content extracted and adapted from **O Bichinho do Saber** (www.obichinhodosaber.com)
