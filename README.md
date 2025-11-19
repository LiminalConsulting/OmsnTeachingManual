# OMSN Teaching Manuals

Portuguese curriculum teaching manuals for **Mathematics**, **Natural Sciences**, **Physics-Chemistry**, and **History and Geography** (Grades 5-9).

Content extracted and adapted from [O Bichinho do Saber](https://www.obichinhodosaber.com/), organized thematically for coherent learning progression.

---

## 📚 Final Products

### Mathematics Manual (5º ao 9º Ano)
**📕 Portuguese:** [manuals/math/MANUAL_FINAL.pdf](manuals/math/MANUAL_FINAL.pdf) (49 pages)
**📙 English:** [manuals/math/MANUAL_FINAL_EN.pdf](manuals/math/MANUAL_FINAL_EN.pdf) (49 pages)
**📖 Bilingual:** [manuals/math/MANUAL_FINAL_BILINGUAL.pdf](manuals/math/MANUAL_FINAL_BILINGUAL.pdf) (98 pages)
- 19 topics across 5 thematic sections
- Complete number systems, algebra, geometry, measurement, and statistics
- ✅ **Perfect alignment** - Portuguese and English versions match exactly

### Physics-Chemistry Manual (7º ao 9º Ano)
**📘 Portuguese:** [manuals/physics-chemistry/MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf](manuals/physics-chemistry/MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf) (68 pages)
**📗 English:** [manuals/physics-chemistry/MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf](manuals/physics-chemistry/MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf) (67 pages)
**📖 Bilingual:** [manuals/physics-chemistry/MANUAL_FINAL_PHYSICS_CHEMISTRY_BILINGUAL.pdf](manuals/physics-chemistry/MANUAL_FINAL_PHYSICS_CHEMISTRY_BILINGUAL.pdf) (134 pages)
- 30 topics across 8 thematic sections
- Complete physics and chemistry curriculum: astronomy, mechanics, waves, electricity, matter, reactions, atomic structure
- ✅ **Good alignment** - Only 1 page difference between versions

### Natural Sciences Manual (7º ao 9º Ano)
**📗 Portuguese:** [manuals/sciences/MANUAL_FINAL_SCIENCES.pdf](manuals/sciences/MANUAL_FINAL_SCIENCES.pdf) (82 pages)
**📙 English:** [manuals/sciences/MANUAL_FINAL_SCIENCES_EN.pdf](manuals/sciences/MANUAL_FINAL_SCIENCES_EN.pdf) (80 pages)
**📖 Bilingual:** [manuals/sciences/MANUAL_FINAL_SCIENCES_BILINGUAL.pdf](manuals/sciences/MANUAL_FINAL_SCIENCES_BILINGUAL.pdf) (160 pages)
- 46 topics across 4 thematic sections
- Geology, ecology, sustainability, and human biology
- ⚠️ **Needs work** - 2 page difference, bilingual alignment could be improved

### History and Geography Manual (5º ao 9º Ano)
**📙 Portuguese:** [manuals/history-geography/MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf](manuals/history-geography/MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf) (188 pages)
- 84 sections across all years (HGP, História, Geografia)
- Complete curriculum from Years 5-9
- **Scope:**
  - Years 5-6: Combined HGP (História e Geografia de Portugal) - 8 chapters
  - Years 7-9: História (History) - 23 chapters
  - Years 7-9: Geografia (Geography) - 30 chapters
- ✅ **Professional formatting** - Matches Math manual standards with proper lists and equations
- ✅ **Hybrid approach successful** - Salvaged existing manual + PowerPoint extractions
- ✅ **Authentic SlideShare content** - Geografia 8º ano chapters 6-10 extracted from official presentations

### Manual Features
- ✅ Table of contents with 3 levels
- ✅ Hierarchical section numbering
- ✅ Professional book-style layout
- ✅ Print-ready A4 format
- ✅ **Bilingual editions** - Portuguese and English side-by-side for language learning
- ✅ Standalone bilingual cover pages available

---

## 🌍 Bilingual Manual Creation

### English Translation & Side-by-Side Alignment

After creating the Portuguese manuals, we developed a complete translation pipeline to create perfectly aligned bilingual editions:

**Translation Process:**
1. **Direct Translation** - Translate the final cleaned Portuguese markdown (`MANUAL_FINAL_PRINT.md`) directly to English
   - For larger manuals (Physics-Chemistry, Sciences): Split into 2 parts to stay within token limits
   - Parallel translation using Claude agents
   - Preserve all formatting, LaTeX notation, and structure exactly
2. **PDF Generation** - Generate English PDFs with matching styling
3. **Alignment Verification** - Compare page counts and ensure structural alignment
4. **Bilingual Assembly** - Interleave Portuguese and English pages using ghostscript
   - Odd pages: Portuguese
   - Even pages: English translation of the same content
   - Each spread shows both languages side-by-side

**Status:**
- ✅ **Math**: Perfect 49-49 page match
- ✅ **Physics-Chemistry**: Excellent 68-67 page match (1 page off)
- ⚠️ **Sciences**: Good 82-80 page match (needs minor alignment improvement)

**Files Created:**
- `MANUAL_FINAL_EN_PRINT.md` - English markdown source
- `MANUAL_FINAL_EN.pdf` - English PDF
- `MANUAL_FINAL_BILINGUAL.pdf` - Interleaved bilingual PDF
- `COVER_EN.md` / `COVER_BILINGUAL.md` - Translated covers

---

## 🔄 How These Were Created

### The Fully Automated Extraction Pipeline

**Links In → Manual Out** - A completely automated 7-step process:

1. **Document URLs** - Map all available topics by grade
2. **Define Structure** - Group topics thematically (not by grade)
3. **Extract Content** - Parallel web extraction using `topic-copier` agent
4. **Assemble Manual** - Combine topics following thematic structure
5. **Prepare Directory** - Organize files for PDF generation
6. **Generate PDF** - Pandoc + XeLaTeX for professional output
7. **Update Docs** - Maintain repository documentation

**Key insight**: The web is the source of truth. Fully automated from URLs to PDF with zero manual intervention.

**📖 Documentation:**
- **Quick Start:** [`PIPELINE_QUICKSTART.md`](PIPELINE_QUICKSTART.md) - Step-by-step execution guide
- **Detailed Process:** [`extraction_pipeline/README.md`](extraction_pipeline/README.md) - Complete pipeline documentation

---

## 📁 Repository Structure

```
OmsnTeachingManual/
├── manuals/                    # 🎯 Final outputs (PDFs + sources)
│   ├── math/                   # Mathematics manual
│   │   ├── MANUAL_FINAL.pdf
│   │   ├── MANUAL_FINAL_PRINT.md
│   │   └── generate_pdf.sh
│   ├── sciences/               # Natural Sciences manual
│   │   ├── MANUAL_FINAL_SCIENCES.pdf
│   │   ├── MANUAL_FINAL_SCIENCES_PRINT.md
│   │   └── generate_sciences_pdf.sh
│   └── physics-chemistry/      # Physics-Chemistry manual
│       ├── MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf
│       ├── MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md
│       └── generate_physics_chemistry_pdf.sh
│
├── extraction_pipeline/        # 🔧 The process that created them
│   ├── topic-copier-agent.md  # The ONE agent that worked
│   ├── pandoc-template.yaml   # PDF styling
│   └── README.md              # Pipeline documentation
│
├── extracted_topics/           # 📝 Raw topic files (ingredients)
│   ├── math/                   # 19 math topics + structure docs
│   │   ├── grade_urls.md
│   │   ├── MANUAL_STRUCTURE_THEMATIC.md
│   │   ├── ASSEMBLY_INSTRUCTIONS.md
│   │   └── [19 topic .md files]
│   ├── sciences/               # 46 science topics + structure docs
│   │   ├── GRADE_URLS_SCIENCES.md
│   │   ├── MANUAL_STRUCTURE_THEMATIC_SCIENCES.md
│   │   ├── ASSEMBLY_INSTRUCTIONS_SCIENCES.md
│   │   └── [46 topic .md files]
│   └── physics-chemistry/      # 30 physics-chemistry topics + structure docs
│       ├── GRADE_URLS_PHYSICS_CHEMISTRY.md
│       ├── MANUAL_STRUCTURE_THEMATIC_PHYSICS_CHEMISTRY.md
│       └── [30 topic .md files]
│
├── source_documents/           # 📄 Original curriculum PDFs
│   ├── math_curriculum/        # Grades 5-9 math PDFs
│   └── sciences_curriculum/    # Chemistry/Physics curriculum PDF
│
└── reference_materials/        # 📚 Converted docs (not used in final)
    ├── Grade summaries (PDF→MD conversions)
    ├── Early unified manual attempts
    └── Teaching phrase references
```

---

## 🛠️ Regenerating PDFs

Each manual directory has its own `generate_pdf.sh` script:

```bash
# Regenerate Math manual
cd manuals/math
./generate_pdf.sh

# Regenerate Sciences manual
cd manuals/sciences
./generate_sciences_pdf.sh

# Regenerate Physics-Chemistry manual
cd manuals/physics-chemistry
./generate_physics_chemistry_pdf.sh
```

### Requirements

- **Pandoc** (version 3.6+)
- **XeLaTeX** (comes with BasicTeX or MacTeX)

Install on macOS:
```bash
brew install pandoc basictex
```

See individual README files in each manual directory for more details.

---

## 📖 Content Coverage

### Mathematics (19 Topics)

**1. NÚMEROS** - Natural, Integer, Rational, Real numbers; Powers & Scientific Notation

**2. ÁLGEBRA** - Algebraic Expressions, Sequences & Patterns, Equations & Inequalities, Functions

**3. GEOMETRIA** - Basic Elements, Plane Figures, Geometric Transformations, 3D Solids, Trigonometry

**4. MEDIDA** - Area, Volume

**5. ORGANIZAÇÃO E TRATAMENTO DE DADOS** - Data Representation, Statistics, Probability

### Natural Sciences (46 Topics)

**1. GEOLOGIA** (15 topics)
- Geological landscapes, rocks & minerals, plate tectonics, volcanism, earthquakes, fossils, Earth history

**2. BIOLOGIA CELULAR E ECOLOGIA** (8 topics)
- Cells, ecosystems, biotic/abiotic factors, food chains, ecological succession

**3. SUSTENTABILIDADE** (8 topics)
- Sustainable development, natural disasters, natural resources, conservation, waste management

**4. BIOLOGIA HUMANA** (15 topics)
- Health, all body systems (digestive, cardiovascular, respiratory, nervous, reproductive, etc.)

### Physics-Chemistry (30 Topics)

**PARTE I - FÍSICA (17 topics)**

**1. ASTRONOMIA E FORÇAS GRAVITACIONAIS** - Universe, solar system, Earth-Moon movements, forces, weight and mass

**2. MECÂNICA: MOVIMENTO E FORÇAS** - Motion on Earth, forces and movement, energy and dynamics, forces and fluids

**3. ONDAS: SOM E LUZ** - Wave characteristics, sound production and propagation, sound attributes, acoustic phenomena, light propagation, optical phenomena

**4. ELETRICIDADE** - Electric current and circuits, effects of electric current and electrical energy

**5. ENERGIA** - Energy sources and energy transfers

**PARTE II - QUÍMICA (13 topics)**

**6. CONSTITUIÇÃO E PROPRIEDADES DA MATÉRIA** - Laboratory materials, material world, physical and chemical properties, transformations, substance separation

**7. REAÇÕES QUÍMICAS** - Explanation and representation of reactions, Lavoisier's Law, types of reactions (combustion, acid-base, precipitation), reaction speed

**8. ESTRUTURA ATÓMICA E TABELA PERIÓDICA** - Atomic structure, periodic table and material properties, chemical bonding

---

## 🎓 Educational Context

These manuals support Portuguese curriculum standards for:
- **Mathematics**: Aprendizagens Essenciais, Grades 5-9
- **Natural Sciences**: Aprendizagens Essenciais, Grades 7-9
- **Physics-Chemistry**: Aprendizagens Essenciais, Grades 7-9

Content is organized thematically rather than by grade level, allowing students to:
- See progression within each mathematical or scientific domain
- Understand connections between related concepts
- Reference topics across multiple grade levels

---

## 📜 Source Attribution

All content extracted and adapted from:

**O Bichinho do Saber**
https://www.obichinhodosaber.com/

A comprehensive Portuguese educational website providing:
- Curriculum-aligned content
- Interactive exercises
- Video lessons
- Study materials

We are grateful for their excellent educational resources.

---

## 📄 License

This project is shared under the **GNU Affero General Public License v3.0** - a strong copyleft license ensuring this knowledge remains free and open for all.

See [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **O Bichinho do Saber** for providing high-quality educational content
- **Claude Code** for enabling the automated extraction pipeline
- **Pandoc** and **XeLaTeX** for professional PDF generation

