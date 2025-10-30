# Manual de Ciências Naturais - Documentation

## Overview

Professional, print-ready manual covering Natural Sciences (Ciências Naturais) for grades 7-9, organized thematically rather than by grade level.

## Files

- **MANUAL_FINAL_SCIENCES.md** - Original combined manual (Parts 1 & 2)
- **MANUAL_FINAL_SCIENCES_PRINT.md** - Enhanced, print-ready version
- **MANUAL_FINAL_SCIENCES.pdf** - Generated PDF (82 pages, 212KB)
- **generate_sciences_pdf.sh** - Automated PDF generation script

## Quick Start

To regenerate the PDF:

```bash
./generate_sciences_pdf.sh
```

Or manually:

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

## Content Structure

The manual covers 4 major domains:

### 1. GEOLOGIA (Geology)
- **Paisagens e Estrutura da Terra** - Geological landscapes, Earth's internal structure, Earth's subsystems
- **Rochas e Minerais** - Rocks and minerals, sedimentary rocks, igneous and metamorphic rocks, rock cycle
- **Dinâmica da Terra** - Continental drift theory, plate tectonics, folds and faults, volcanism, earthquakes
- **História da Terra** - Fossils and rock dating, stages of Earth's history
- **Sustentabilidade Geológica** - Sustainable rock exploitation, contribution of geological knowledge

### 2. BIOLOGIA CELULAR E ECOLOGIA (Cell Biology and Ecology)
- **Condições para a Vida** - Conditions on Earth that allow life
- **Organização Celular** - The microscope, cell and levels of biological organization
- **Ecossistemas** - Ecosystem organization levels, abiotic factors, biotic factors, food chains and matter cycles, ecological succession

### 3. SUSTENTABILIDADE E GESTÃO AMBIENTAL (Sustainability and Environmental Management)
- **Recursos e Proteção** - Natural resources, ecosystem protection, nature conservation
- **Gestão Territorial** - Land planning and management, disaster risk management
- **Gestão de Resíduos** - Waste and water management, sustainable development

### 4. BIOLOGIA HUMANA (Human Biology)
- **Sistemas Fundamentais** - Digestive, respiratory, cardiovascular, lymphatic systems
- **Sistemas Reguladores** - Blood, nervous system, hormonal system
- **Sistemas de Suporte** - Excretory system, skin, reproductive system
- **Hereditariedade** - Genetics and heredity
- **Saúde** - Individual and community health, basic life support

## Transformations Applied

### 1. Unified Structure (8 references removed)
- Removed "Parte 1" and "Parte 2" division
- Merged separate indices into one comprehensive TOC
- Removed transition markers and part references
- Created seamless flow across all 4 domains

### 2. Clean Headers (56 fixes)
- Removed manual numbering from all headers
- Pandoc auto-numbers with `--number-sections` flag
- Result: Clean "1.1 Paisagens" instead of "2.1 1.1 Paisagens"

### 3. Professional List Formatting (139 fixes)
- Added blank lines after bold headers before lists
- Ensures proper vertical rendering in PDF
- Eliminates inline list appearance

### 4. LaTeX Scientific Notation (12 enhancements)
- Chemical formulas: $\text{CO}_2$, $\text{H}_2\text{O}$, $\text{O}_2$
- Proper subscripts and superscripts
- Scientific percentages and units

## PDF Features

- ✅ **Table of Contents** - Auto-generated with 3 levels
- ✅ **Section Numbering** - Hierarchical (1.1, 1.2, 2.1, etc.)
- ✅ **Professional Typography** - Book-style layout
- ✅ **Scientific Notation** - LaTeX-rendered formulas
- ✅ **Portuguese Support** - Full UTF-8 encoding
- ✅ **Print-Ready** - A4 format with 2.5cm margins
- ✅ **Clickable Links** - Blue hyperlinks in TOC

## Document Specifications

- **Format:** PDF 1.5
- **Pages:** 82
- **Size:** ~212KB
- **Paper:** A4 (210 × 297mm)
- **Margins:** 2.5cm all sides
- **Font Size:** 11pt base
- **Line Height:** 1.15
- **Language:** Portuguese (pt-PT)

## Quality Standards

Following the same professional standards as the mathematics manual:

- ✅ No manual numbering in headers
- ✅ No Part 1/Part 2 references
- ✅ Proper list formatting throughout
- ✅ Scientific notation where appropriate
- ✅ Unified, comprehensive index
- ✅ Publication-ready formatting

## Customization

### Change margins:
```bash
-V geometry:margin=3cm
```

### Change font size:
```bash
-V fontsize=12pt
```

### Change line spacing:
```bash
-V linestretch=1.5
```

## Source Attribution

Content adapted from **O Bichinho do Saber** (www.obichinhodosaber.com)

---

*Generated with Pandoc and XeLaTeX*
