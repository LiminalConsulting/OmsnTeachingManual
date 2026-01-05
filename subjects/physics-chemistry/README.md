# Physics & Chemistry (Físico-Química)

Portuguese physics and chemistry curriculum for grades 7-9 (7º ao 9º Ano).

## Structure

```
physics-chemistry/
├── curriculum/           # Official DGE Aprendizagens Essenciais PDFs
├── extracted_topics/     # Raw extracted markdown by topic
├── manual/               # Final manual files (PDFs, build scripts)
└── reference/            # Draft materials
```

## Contents

### Curriculum (3 PDFs)
Official "Aprendizagens Essenciais" from DGE for grades 7-9.

### Topics Covered

**Physics:**
- Universe, Solar System, Earth's movements
- Light propagation, optical phenomena
- Sound production, waves, acoustic phenomena
- Forces, movement, energy
- Electrical current and effects

**Chemistry:**
- Properties of materials
- Physical and chemical transformations
- Separation of substances
- Atomic structure, periodic table
- Chemical bonding and reactions

### Manuals
- **Portuguese:** MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf (68 pages)
- **English:** MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf (67 pages)

## Building the Manual

```bash
cd manual/
./generate_physics_chemistry_pdf.sh    # Portuguese
./generate_pdf_en.sh                   # English
```
