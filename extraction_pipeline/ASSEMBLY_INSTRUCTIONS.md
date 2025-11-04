# Final Manual Assembly Instructions
## Universal Guide for All Subjects

This document provides generic assembly instructions applicable to all teaching manuals (Math, Sciences, Physics-Chemistry, etc.).

---

## Goal
Create a clean, printable teaching manual organized thematically (not by grade).

## Source Files
- **Structure guide:** `MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md` in subject directory
- **Content:** All extracted topic files in `extracted_topics/[subject]/`

---

## What to REMOVE (Metadata Clutter)

### Remove from every topic:
- `# [Topic Name]` (first line - redundant, proper headers added during assembly)
- `**Source:** O Bichinho do Saber`
- `**Grades:** X, Y, Z` or `**Grades:** X`
- `**Extraction Date:** YYYY-MM-DD`
- `---` (divider after metadata)
- `## Grade X` headers (replace with thematic concept progression)
- `**Source URL:** https://...`
- `**Page Title:** ...`
- `**Author:** Luis Carrilho`
- `**Publication Date:** ...`
- `**Last Modified:** ...`
- `**Website:** O Bichinho do Saber`
- "Sections Available" (em construção, em breve, etc.)
- "Estado do Conteúdo" (Coming soon notes)
- Any references to "PowerPoints, Vídeos, Aulas #EstudoEmCasa" **unless** they contain actual video/resource links

### Keep only if they have actual links:
- Video lesson tables with RTP links
- PDF worksheet links
- Interactive exercise URLs
- External educational resources

---

## What to KEEP (Core Content)

✅ All educational content:
- **Definitions and concepts**
- **Formulas, theorems, properties** (Math)
- **Scientific processes and phenomena** (Sciences)
- **Examples with calculations/demonstrations**
- **Classifications and taxonomies**
- **Problem-solving methods**
- **"Aprendizagens Essenciais"** (curriculum learning objectives)
- **Curriculum competencies**
- **Health recommendations** (Sciences)
- **Conservation measures** (Sciences)
- **Diagrams and image descriptions**
- **Tables and charts** (classifications, comparisons)

---

## Manual Structure Pattern

```markdown
# Manual de [SUBJECT]: [Grade Range]
## Organização Temática

[Brief introduction about manual structure and thematic organization]

## Índice
[Table of contents - auto-generated or manual, with hierarchical numbering]

---

# 1. [MAIN THEME 1]

## 1.1 [Sub-theme Title]

### [Concept/Topic Title]
[Clean content from topic file]

### [Another Concept]
[Clean content]

## 1.2 [Another Sub-theme]
[Content...]

# 2. [MAIN THEME 2]
[Continue pattern...]
```

---

## Grade Progression Handling

### Multi-Grade Topics (e.g., Math)
Instead of:
```markdown
## Grade 5
### NÚMEROS NATURAIS
Content...
## Grade 6
### More content...
```

Use natural concept progression:
```markdown
## 1.1 Números Naturais

### Conceitos Fundamentais
[Grade 5 foundational content]

### Números Primos e Decomposição
[Grade 6 advanced content]
```

### Single-Grade Topics (e.g., Sciences)
Most science topics appear in only one grade:
- Simply present content cleanly by thematic organization
- No need for progression markers within topics
- Thematic grouping creates natural learning flow

---

## Formatting Rules

1. **Hierarchical numbering:** `1.1`, `1.2`, `2.1`, `2.2`, etc.
2. **Clean headers:** No metadata, just concept names
3. **Preserve examples:** Keep all worked examples exactly as written
4. **Preserve Portuguese:** No translation, all content in original language
5. **Preserve tables:** Keep classification tables, comparison charts, data tables
6. **Remove redundancy:** If same definition appears in multiple grades, keep the most complete version
7. **Footnote attribution:** Optional footer: `"Conteúdo adaptado de O Bichinho do Saber (www.obichinhodosaber.com)"`

---

## Special Considerations

### Missing/Incomplete Content
Handle unavailable topics by:
- Including available content
- Adding brief note if topic is referenced but content unavailable
- Cross-reference to related topics that may cover concepts

### Image/Diagram References
When encountering visual content references:
- Keep descriptive text about diagrams
- Preserve captions and labels
- Note `[Diagrama: ...]` or `[Imagem: ...]` where appropriate
- Keep measurement diagrams, geometric figures, anatomical diagrams, etc.

### Subject-Specific Content
- **Health and Safety:** Preserve all disease prevention, health recommendations, safety protocols
- **Environmental:** Keep conservation guidelines, sustainability practices
- **Mathematical:** Preserve all formulas, notation, worked examples

---

## Output Specification

**Single file:** `MANUAL_FINAL_[SUBJECT].md`
- Clean, professional formatting
- Ready for PDF generation
- Hierarchical organization following `MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md`
- Estimated length: 30,000-50,000 words depending on subject
- Portuguese language throughout

---

## Next Step

After assembly, use subject-specific `generate_pdf.sh` script to create final PDF using Pandoc + XeLaTeX.
