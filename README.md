# OMSN Teaching Manuals

Portuguese curriculum teaching manuals for **Mathematics** and **Natural Sciences** (Grades 5-9).

Content extracted and adapted from [O Bichinho do Saber](https://www.obichinhodosaber.com/), organized thematically for coherent learning progression.

---

## 📚 Final Products

### Mathematics Manual (5º ao 9º Ano)
**📕 [manuals/math/MANUAL_FINAL.pdf](manuals/math/MANUAL_FINAL.pdf)**
- 19 topics across 5 thematic sections
- 48 pages, professionally formatted
- Complete number systems, algebra, geometry, measurement, and statistics

### Natural Sciences Manual (7º ao 9º Ano)
**📗 [manuals/sciences/MANUAL_FINAL_SCIENCES.pdf](manuals/sciences/MANUAL_FINAL_SCIENCES.pdf)**
- 46 topics across 4 thematic sections
- ~80 pages, professionally formatted
- Geology, ecology, sustainability, and human biology

Both manuals feature:
- ✅ Table of contents with 3 levels
- ✅ Hierarchical section numbering
- ✅ Professional book-style layout
- ✅ Print-ready A4 format
- ✅ Portuguese language throughout

---

## 🔄 How These Were Created

### The Extraction Pipeline

After several iterations, we developed a streamlined process:

1. **Source**: Web content from O Bichinho do Saber (not PDFs)
2. **Extraction**: Single `topic-copier` agent fetches all topics in parallel
3. **Organization**: Topics organized thematically (not by grade)
4. **Assembly**: Combined following thematic structure, metadata removed
5. **PDF Generation**: Pandoc + XeLaTeX for professional output

**Key insight**: The web is the source of truth. One simple agent, parallel execution, clean assembly.

See [`extraction_pipeline/README.md`](extraction_pipeline/README.md) for detailed documentation.

---

## 📁 Repository Structure

```
OmsnTeachingManual/
├── manuals/                    # 🎯 Final outputs (PDFs + sources)
│   ├── math/                   # Mathematics manual
│   │   ├── MANUAL_FINAL.pdf
│   │   ├── MANUAL_FINAL_PRINT.md
│   │   └── generate_pdf.sh
│   └── sciences/               # Natural Sciences manual
│       ├── MANUAL_FINAL_SCIENCES.pdf
│       ├── MANUAL_FINAL_SCIENCES_PRINT.md
│       └── generate_sciences_pdf.sh
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
│   └── sciences/               # 46 science topics + structure docs
│       ├── GRADE_URLS_SCIENCES.md
│       ├── MANUAL_STRUCTURE_THEMATIC_SCIENCES.md
│       ├── ASSEMBLY_INSTRUCTIONS_SCIENCES.md
│       └── [46 topic .md files]
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

---

## 🎓 Educational Context

These manuals support Portuguese curriculum standards for:
- **Mathematics**: Aprendizagens Essenciais, Grades 5-9
- **Natural Sciences**: Aprendizagens Essenciais, Grades 7-9

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

