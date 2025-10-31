# Manual de Ciências Naturais (7º ao 9º Ano)

## Final Product

**📗 [MANUAL_FINAL_SCIENCES.pdf](MANUAL_FINAL_SCIENCES.pdf)** - ~80 pages, professionally formatted

## Files

- **MANUAL_FINAL_SCIENCES.pdf** - The final PDF (main output)
- **MANUAL_FINAL_SCIENCES_PRINT.md** - Markdown with LaTeX math notation (PDF source)
- **MANUAL_FINAL_SCIENCES.md** - Plain markdown version
- **generate_sciences_pdf.sh** - Script to regenerate the PDF

## Content Structure

The manual covers 46 Natural Sciences topics organized thematically:

1. **GEOLOGIA** (Geology & Earth Sciences) - Grade 7 Focus
   - Paisagens e Estrutura da Terra
   - Rochas e Minerais
   - Tectónica de Placas e Vulcanismo
   - Fósseis e História da Terra

2. **BIOLOGIA CELULAR E ECOLOGIA** (Cell Biology & Ecology) - Grade 8 Focus
   - A Célula e Organização Biológica
   - Ecossistemas e Fatores Ambientais
   - Cadeias Alimentares e Ciclos da Matéria
   - Sucessões Ecológicas

3. **SUSTENTABILIDADE E GESTÃO AMBIENTAL** (Sustainability) - Grade 8 Focus
   - Desenvolvimento Sustentável
   - Catástrofes Naturais e Antropogénicas
   - Recursos Naturais
   - Proteção e Conservação da Natureza
   - Gestão de Resíduos e Água

4. **BIOLOGIA HUMANA** (Human Biology) - Grade 9 Focus
   - Saúde e Qualidade de Vida
   - Sistemas do Corpo Humano (digestivo, cardiovascular, respiratório, etc.)
   - Sistema Neuro-hormonal
   - Sistema Reprodutor
   - Hereditariedade

## Regenerating the PDF

To regenerate the PDF from the markdown source:

```bash
./generate_sciences_pdf.sh
```

Or manually with pandoc:

```bash
pandoc MANUAL_FINAL_SCIENCES_PRINT.md \
  -o MANUAL_FINAL_SCIENCES.pdf \
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
- ✅ Portuguese language support
- ✅ Print-ready A4 format (2.5cm margins)
- ✅ Clickable hyperlinks

## Source Attribution

Content extracted and adapted from **O Bichinho do Saber** (www.obichinhodosaber.com)
