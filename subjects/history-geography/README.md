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
- **Portuguese only:** MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf (194 pages)

### Known Issues

#### Content Gaps
- "Cultura popular e estilos românico e gótico" - minimal content (not available on source website)
- "Crises do século XIV" - verify if PowerPoint source has additional content

#### Formatting Issues (Remaining)
Some sections still have Unicode corruption from original document conversion:
- `￿` (U+FFFD replacement character) appearing inline
- Run-together paragraphs where line breaks were lost
- Tables rendered as continuous text (e.g., "Forma de relevo Características principais Montanhas...")

**Affected areas identified:**
- Geography sections on relief/landforms (vulcanismo, forças externas/internas)
- Relevo de Portugal section

**Fix approach needed:**
1. Search for `￿` character and fix surrounding context
2. Identify tables rendered as text and restore markdown table format
3. Check for missing paragraph breaks after punctuation

### Source Materials
The `source/` folder contains the original documents from the contributor who extracted content from O Bichinho do Saber website.

The `extracted_topics/` folder contains SlideShare PDF downloads and their markdown extractions for Geografia 8º ano chapters 6-10.

## Building the Manual

```bash
cd manual/
./generate_history_geography_pdf.sh
```
