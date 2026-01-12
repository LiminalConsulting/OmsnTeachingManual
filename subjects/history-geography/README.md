# History & Geography (História e Geografia)

Portuguese history and geography curriculum for grades 5-9 (5º ao 9º Ano).

## Structure

```
history-geography/
├── curriculum/           # Official DGE Aprendizagens Essenciais PDFs
├── extracted_topics/     # Extracted markdown + SlideShare source PDFs
├── manual/               # Final manual files (PDF, build script)
├── reference/            # (currently empty)
└── source/               # Original contributor files (docx, txt)
```

## Contents

### Curriculum (8 PDFs)
Official "Aprendizagens Essenciais" from DGE:
- HGP (História e Geografia de Portugal) for grades 5-6
- História for grades 7-9
- Geografia for grades 7-9

### Topics Covered

**HGP (Grades 5-6):**
- Iberian Peninsula: location and natural features
- Early human communities, Romans, Muslims
- Formation of Portugal, medieval history
- Portuguese discoveries and expansion

**História (Grades 7-9):**
- Paleolithic through Neolithic
- Ancient civilizations (Egypt, Greece, Rome)
- Christianity, barbarian invasions, Islam
- Medieval society, Renaissance, Reformation
- Industrial Revolution, World Wars
- Portuguese Republic, Estado Novo, April 25th Revolution

**Geografia (Grades 7-9):**
- Cartography, map projections, orientation
- Climate, relief, rivers, coastlines
- Population, migration, cities
- Economic activities, natural resources
- Global development and trade

### Manual
- **Portuguese only:** MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf (~195 pages)

### Recent Improvements

#### Content Additions (January 2026)
The following curriculum content gaps have been filled:

**A Cultura Portuguesa Face aos Modelos Europeus:**
- O Ensino Medieval (escolas monásticas, catedrais, universidades)
- A Cultura Popular (festividades, tradição oral, artesanato)
- Os Estilos Românico e Gótico (características, exemplos portugueses, tabela comparativa)

**As Crises do Século XIV:**
- A Crise Europeia (causas: fome, peste, guerras; consequências)
- A Crise em Portugal (calamidades, Guerras Fernandinas)
- A Revolução de 1383-1385 (problema de sucessão, revolta popular, invasão castelhana)

#### Formatting Fixes (January 2026)
Multiple formatting issues from original document conversion have been fixed:
- Unicode markers (¬, ›, ι, ⤷, ») converted to proper markdown
- ALL CAPS titles converted to proper headings
- Garbage/duplicate index section removed
- Bullet patterns and whitespace cleaned up
- Tables converted from text to proper markdown format:
  - Formas de relevo
  - Principais rios e bacias de Portugal
  - BRICS countries
  - Natural risks
  - Population distribution factors
  - Românico vs Gótico comparison

### Known Issues

#### Minor Formatting
Some minor Unicode issues may still exist in isolated locations. If found, they can be fixed using:
```bash
grep -n '￿' MANUAL_FINAL_HISTORY_GEOGRAPHY_PRINT.md
```

### Source Materials
The `source/` folder contains the original documents from the contributor who extracted content from O Bichinho do Saber website.

The `extracted_topics/` folder contains SlideShare PDF downloads and their markdown extractions for Geografia 8º ano chapters 6-10.

## Building the Manual

```bash
cd manual/
./generate_history_geography_pdf.sh
```
