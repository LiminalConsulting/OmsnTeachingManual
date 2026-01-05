# Final Manual Assembly Instructions - Natural Sciences

## Goal
Create a clean, printable Natural Sciences teaching manual for grades 7-9, organized thematically (not by grade).

## Source Files
- **Structure guide:** `MANUAL_STRUCTURE_THEMATIC_SCIENCES.md`
- **Content:** All 46 files in `topics_sciences/*.md`

## What to REMOVE (Metadata Clutter)

### Remove from every topic:
- `# [Topic Name]` (first line - redundant, we'll add proper headers)
- `**Source:** O Bichinho do Saber`
- `**Grades:** X`
- `**Extraction Date:** 2025-10-29`
- `---` (divider after metadata)
- `## Grade X` headers (most topics are single-grade)
- `**Source URL:** https://...`
- `**Page Title:** ...`
- `**Author:** Luis Carrilho`
- `**Publication Date:** ...`
- `**Last Modified:** ...`
- `**Website:** O Bichinho do Saber`
- "Sections Available" (em construção, em breve, etc.)
- "Estado do Conteúdo" (Coming soon notes)
- Any references to "PowerPoints, Vídeos, Aulas #EstudoEmCasa" **unless** they contain actual video links/resources

### Keep only if they have actual links:
- Video lesson tables with RTP links
- PDF worksheet links
- Interactive exercise URLs

## What to KEEP (Core Content)

✅ All scientific content:
- Definitions and concepts
- Scientific processes and phenomena
- Classifications and taxonomies
- Examples and case studies
- Diagrams descriptions
- "Aprendizagens Essenciais" (learning objectives)
- Curriculum competencies
- Health recommendations
- Conservation measures

## Structure of Final Manual

```
# Manual de Ciências Naturais: 7º ao 9º Ano
## Organização Temática

[Brief introduction about manual structure]

## Índice
[Table of contents with sections 1-4 and subsections]

---

# 1. GEOLOGIA (Geology & Earth Sciences)

## 1.1 Paisagens e Estrutura da Terra

### Paisagens geológicas
[Content from paisagens_geologicas.md - CLEAN]

### Estrutura interna da Terra
[Content from estrutura_interna_terra.md - CLEAN]

### Subsistemas da Terra
[Content from subsistemas_terra.md - CLEAN]

## 1.2 Rochas e Minerais
[Content from rochas_minerais.md - CLEAN]
...

[... continue through all 4 main sections ...]
```

## Thematic Organization

Follow the structure in `MANUAL_STRUCTURE_THEMATIC_SCIENCES.md`:

1. **GEOLOGIA** (15 topics, Grade 7 focus)
2. **BIOLOGIA CELULAR E ECOLOGIA** (8 topics, Grade 8 focus)
3. **SUSTENTABILIDADE E GESTÃO AMBIENTAL** (8 topics, Grade 8 focus)
4. **BIOLOGIA HUMANA** (15 topics, Grade 9 focus)

## Grade Progression Notes

Unlike math, most science topics appear in ONLY ONE grade:
- **Grade 7:** Geology and Earth Sciences
- **Grade 8:** Ecology and Environmental Sciences
- **Grade 9:** Human Biology and Health

Therefore, less need for progression markers. Simply present content cleanly by thematic organization.

## Formatting Rules

1. **Hierarchical numbering:** 1.1, 1.2, 2.1, 2.2, etc.
2. **Clean headers:** No metadata, just concept names
3. **Preserve examples:** Keep all worked examples exactly as written
4. **Preserve Portuguese:** No translation, all content in original language
5. **Preserve tables:** Keep classification tables, comparison charts
6. **Remove redundancy:** If same definition appears multiple times, keep the most complete version
7. **Footnote attribution:** Optional footer: "Conteúdo adaptado de O Bichinho do Saber (www.obichinhodosaber.com)"

## Special Considerations for Sciences

### Missing/Incomplete Content:
- **O microscópio:** Content not available on website (noted in extraction)
- **Níveis estruturais do corpo humano:** Redirects to "Saúde individual" (noted in extraction)

Handle these by:
- Including available content
- Adding brief note if topic is referenced but content unavailable
- Cross-reference to related topics that may cover concepts

### Image/Diagram References:
Many science topics reference diagrams and images. When encountering:
- Keep descriptive text about diagrams
- Preserve captions and labels
- Note "[Diagrama: ...]" or "[Imagem: ...]" where appropriate

### Health and Safety Information:
Preserve all:
- Disease prevention measures
- Health recommendations
- Safety protocols (e.g., earthquake safety, basic life support)
- Environmental conservation guidelines

## Output

Single file: `MANUAL_FINAL_SCIENCES.md`
- Clean, professional formatting
- Ready for printing
- ~40,000-50,000 words estimated
- Hierarchical organization following MANUAL_STRUCTURE_THEMATIC_SCIENCES.md

---

## Processing Notes

**Total Topics:** 46 across 3 grades
- Grade 7: 15 topics (Geologia)
- Grade 8: 16 topics (Ecologia e Sustentabilidade)
- Grade 9: 15 topics (Biologia Humana)

**File Location:** All extracted topics in `topics_sciences/`

**Next Step:** Manual assembly in new chat session with larger context window for processing all 46 topic files simultaneously.
