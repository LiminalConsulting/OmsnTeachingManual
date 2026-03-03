# OMSN Teaching Manuals

Portuguese curriculum teaching manuals for **Mathematics**, **Natural Sciences**, **Physics-Chemistry**, and **History and Geography** (Grades 5-9).

Content extracted and adapted from [O Bichinho do Saber](https://www.obichinhodosaber.com/), organized thematically for coherent learning progression.

---

## Final Products

### Mathematics Manual (5º ao 9º Ano)
**Portuguese:** [subjects/math/manual/MANUAL_FINAL.pdf](subjects/math/manual/MANUAL_FINAL.pdf) (49 pages)
**English:** [subjects/math/manual/MANUAL_FINAL_EN.pdf](subjects/math/manual/MANUAL_FINAL_EN.pdf) (49 pages)
**Bilingual:** [subjects/math/manual/MANUAL_FINAL_BILINGUAL.pdf](subjects/math/manual/MANUAL_FINAL_BILINGUAL.pdf) (98 pages)
- 19 topics across 5 thematic sections
- Complete number systems, algebra, geometry, measurement, and statistics
- Perfect alignment - Portuguese and English versions match exactly

### Physics-Chemistry Manual (7º ao 9º Ano)
**Portuguese:** [subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf](subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf) (68 pages)
**English:** [subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf](subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf) (67 pages)
**Bilingual:** [subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY_BILINGUAL.pdf](subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY_BILINGUAL.pdf) (134 pages)
- 30 topics across 8 thematic sections
- Complete physics and chemistry curriculum: astronomy, mechanics, waves, electricity, matter, reactions, atomic structure
- Good alignment - Only 1 page difference between versions

### Natural Sciences Manual (7º ao 9º Ano)
**Portuguese:** [subjects/sciences/manual/MANUAL_FINAL_SCIENCES.pdf](subjects/sciences/manual/MANUAL_FINAL_SCIENCES.pdf) (82 pages)
**English:** [subjects/sciences/manual/MANUAL_FINAL_SCIENCES_EN.pdf](subjects/sciences/manual/MANUAL_FINAL_SCIENCES_EN.pdf) (80 pages)
**Bilingual:** [subjects/sciences/manual/MANUAL_FINAL_SCIENCES_BILINGUAL.pdf](subjects/sciences/manual/MANUAL_FINAL_SCIENCES_BILINGUAL.pdf) (160 pages)
- 46 topics across 4 thematic sections
- Geology, ecology, sustainability, and human biology

### History and Geography Manual (5º ao 9º Ano)
**Portuguese:** [subjects/history-geography/manual/MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf](subjects/history-geography/manual/MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf) (188 pages)
- 84 sections across all years (HGP, História, Geografia)
- Complete curriculum from Years 5-9
- **Scope:**
  - Years 5-6: Combined HGP (História e Geografia de Portugal) - 8 chapters
  - Years 7-9: História (History) - 23 chapters
  - Years 7-9: Geografia (Geography) - 30 chapters
- Authentic SlideShare content - Geografia 8º ano chapters 6-10 extracted from official presentations

---

## Repository Structure

```
OmsnTeachingManual/
├── subjects/                      # Subject holons (self-contained)
│   ├── math/
│   │   ├── curriculum/            # Official DGE PDFs (grades 5-9)
│   │   ├── extracted_topics/      # Raw topic markdown files
│   │   ├── manual/                # Final PDFs + build scripts
│   │   ├── visualizations/        # Manim scripts + rendered images
│   │   └── reference/             # Grade summaries
│   ├── physics-chemistry/
│   │   ├── curriculum/
│   │   ├── extracted_topics/
│   │   ├── manual/
│   │   └── reference/
│   ├── sciences/
│   │   ├── curriculum/
│   │   ├── extracted_topics/
│   │   └── manual/
│   └── history-geography/
│       ├── curriculum/
│       ├── extracted_topics/      # Includes SlideShare PDFs
│       ├── manual/
│       └── source/                # Original contributor files
│
├── shared/                        # Cross-subject resources
│   ├── extraction_pipeline/       # Pipeline documentation
│   └── teaching_phrases/          # Portuguese/English phrases
│
├── .claude/                       # Claude Code config
│   ├── agents/
│   └── CLAUDE.md
│
├── README.md
├── LICENSE
├── MundoTeens.png
└── TeachingManual.png
```

Each subject has its own README with specific details. See:
- [subjects/math/README.md](subjects/math/README.md)
- [subjects/physics-chemistry/README.md](subjects/physics-chemistry/README.md)
- [subjects/sciences/README.md](subjects/sciences/README.md)
- [subjects/history-geography/README.md](subjects/history-geography/README.md)

---

## Regenerating PDFs

Each subject's `manual/` directory has build scripts:

```bash
# Math
cd subjects/math/manual && ./generate_pdf.sh

# Physics-Chemistry
cd subjects/physics-chemistry/manual && ./generate_physics_chemistry_pdf.sh

# Sciences
cd subjects/sciences/manual && ./generate_sciences_pdf.sh

# History-Geography
cd subjects/history-geography/manual && ./generate_history_geography_pdf.sh
```

### Requirements

- **Pandoc** (version 3.6+)
- **XeLaTeX** (comes with BasicTeX or MacTeX)

Install on macOS:
```bash
brew install pandoc basictex
```

---

## How These Were Created

### The Automated Extraction Pipeline

**Links In → Manual Out** - A 7-step process:

1. **Document URLs** - Map all available topics by grade
2. **Define Structure** - Group topics thematically (not by grade)
3. **Extract Content** - Parallel web extraction using `topic-copier` agent
4. **Assemble Manual** - Combine topics following thematic structure
5. **Prepare Directory** - Organize files for PDF generation
6. **Generate PDF** - Pandoc + XeLaTeX for professional output
7. **Update Docs** - Maintain repository documentation

**Pipeline Documentation:** [shared/extraction_pipeline/](shared/extraction_pipeline/)

---

## Educational Context

These manuals support Portuguese curriculum standards for:
- **Mathematics**: Aprendizagens Essenciais, Grades 5-9
- **Natural Sciences**: Aprendizagens Essenciais, Grades 5-9
- **Physics-Chemistry**: Aprendizagens Essenciais, Grades 7-9
- **History & Geography**: Aprendizagens Essenciais, Grades 5-9

Official curriculum PDFs from DGE (Direção-Geral da Educação) are stored in each subject's `curriculum/` folder.

Content is organized thematically rather than by grade level, allowing students to:
- See progression within each domain
- Understand connections between related concepts
- Reference topics across multiple grade levels

---

## Source Attribution

All content extracted and adapted from:

**O Bichinho do Saber**
https://www.obichinhodosaber.com/

A comprehensive Portuguese educational website providing curriculum-aligned content, interactive exercises, video lessons, and study materials.

---

## License

This project is shared under the **GNU Affero General Public License v3.0** - a strong copyleft license ensuring this knowledge remains free and open for all.

See [LICENSE](AURYN/node_modules/qs/LICENSE.md) file for details.

---

## Acknowledgments

- **O Bichinho do Saber** for providing high-quality educational content
- **Claude Code** for enabling the automated extraction pipeline
- **Pandoc** and **XeLaTeX** for professional PDF generation
