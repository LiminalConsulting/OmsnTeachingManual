# Natural Sciences (Ciências Naturais)

Portuguese natural sciences curriculum for grades 5-9 (5º ao 9º Ano).

## Structure

```
sciences/
├── curriculum/           # Official DGE Aprendizagens Essenciais PDFs
├── extracted_topics/     # Raw extracted markdown by topic
├── manual/               # Final manual files (PDFs, build scripts)
└── reference/            # (currently empty)
```

## Contents

### Curriculum (6 PDFs)
Official "Aprendizagens Essenciais" from DGE for grades 5-9, plus metas curriculares.

### Topics Covered

**Geology:**
- Geological landscapes
- Rocks and minerals (sedimentary, magmatic, metamorphic)
- Plate tectonics, volcanism, earthquakes
- Fossils and Earth's history

**Biology & Ecology:**
- Cell organization
- Ecosystems, food chains
- Biotic and abiotic factors

**Human Biology:**
- Digestive, respiratory, circulatory systems
- Excretory, nervous, hormonal systems
- Reproductive system
- Heredity

**Environment & Sustainability:**
- Natural resources management
- Territory planning
- Sustainability

### Manuals
- **Portuguese:** MANUAL_FINAL_SCIENCES.pdf (82 pages)
- **English:** MANUAL_FINAL_SCIENCES_EN.pdf (80 pages)
- **Bilingual:** MANUAL_FINAL_SCIENCES_BILINGUAL.pdf

## Building the Manual

```bash
cd manual/
./generate_sciences_pdf.sh       # Portuguese
./generate_pdf_en.sh             # English
./create_bilingual_pdf.sh        # Side-by-side bilingual
```
