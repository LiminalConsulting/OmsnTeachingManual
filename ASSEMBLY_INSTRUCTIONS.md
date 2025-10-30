# Final Manual Assembly Instructions

## Goal
Create a clean, printable mathematics teaching manual for grades 5-9, organized thematically (not by grade).

## Source Files
- **Structure guide:** `MANUAL_STRUCTURE_THEMATIC.md`
- **Content:** All 19 files in `topics/*.md`

## What to REMOVE (Metadata Clutter)

### Remove from every topic:
- `# [Topic Name]` (first line - redundant, we'll add proper headers)
- `**Source:** O Bichinho do Saber`
- `**Grades:** X, Y, Z`
- `**Extraction Date:** 2025-10-29`
- `---` (divider after metadata)
- `## Grade X` headers (replace with cleaner progression)
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

✅ All mathematical content:
- Definitions and concepts
- Formulas and notation
- Examples with numbers/calculations
- Properties and theorems
- Problem-solving methods
- "Aprendizagens Essenciais" (learning objectives)
- Curriculum competencies

## Structure of Final Manual

```
# Manual de Matemática: 5º ao 9º Ano
## Organização Temática

[Brief introduction about manual structure]

## Índice
[Table of contents with sections 1-5 and subsections]

---

# 1. NÚMEROS

## 1.1 Números Naturais

[Content from numeros_naturais.md - CLEAN]
- Start with Grade 5 concepts
- Progress to Grade 6 concepts
- NO "Grade 5" headers, use concept progression instead

## 1.2 Números Inteiros
[Content from numeros_inteiros.md - CLEAN]

[... continue through all 5 main sections ...]
```

## Grade Progression Style

Instead of:
```
## Grade 5
### NÚMEROS NATURAIS
Content...
## Grade 6
### More content...
```

Use natural concept progression:
```
## 1.1 Números Naturais

### Conceitos Fundamentais
[Grade 5 foundational content]

### Números Primos e Decomposição
[Grade 6 advanced content]
```

## Formatting Rules

1. **Hierarchical numbering:** 1.1, 1.2, 2.1, 2.2, etc.
2. **Clean headers:** No metadata, just concept names
3. **Preserve examples:** Keep all worked examples exactly as written
4. **Preserve Portuguese:** No translation, all content in original language
5. **Remove redundancy:** If same definition appears in multiple grades, keep the most complete version
6. **Footnote attribution:** Optional footer: "Conteúdo adaptado de O Bichinho do Saber (www.obichinhodosaber.com)"

## Output

Single file: `MANUAL_FINAL.md`
- Clean, professional formatting
- Ready for printing
- ~30,000-40,000 words
- Hierarchical organization following MANUAL_STRUCTURE_THEMATIC.md
