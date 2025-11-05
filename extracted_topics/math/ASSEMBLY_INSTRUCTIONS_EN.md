# Final Manual Assembly Instructions

## Goal
Create a clean, printable mathematics teaching manual for grades 5-9, organized thematically (not by grade).

## Source Files
- **Structure guide:** `MANUAL_STRUCTURE_THEMATIC_EN.md`
- **Content:** All 19 files in `topics/*_EN.md`

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
- "Sections Available" (under construction, coming soon, etc.)
- "Content Status" (Coming soon notes)
- Any references to "PowerPoints, Videos, #StudyAtHome Lessons" **unless** they contain actual video links/resources

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
- "Essential Learning" (learning objectives)
- Curriculum competencies

## Structure of Final Manual

```
# Mathematics Manual: Grades 5-9
## Thematic Organization

[Brief introduction about manual structure]

## Table of Contents
[Table of contents with sections 1-5 and subsections]

---

# 1. NUMBERS

## 1.1 Natural Numbers

[Content from numeros_naturais_EN.md - CLEAN]
- Start with Grade 5 concepts
- Progress to Grade 6 concepts
- NO "Grade 5" headers, use concept progression instead

## 1.2 Integers
[Content from numeros_inteiros_EN.md - CLEAN]

[... continue through all 5 main sections ...]
```

## Grade Progression Style

Instead of:
```
## Grade 5
### NATURAL NUMBERS
Content...
## Grade 6
### More content...
```

Use natural concept progression:
```
## 1.1 Natural Numbers

### Fundamental Concepts
[Grade 5 foundational content]

### Prime Numbers and Decomposition
[Grade 6 advanced content]
```

## Formatting Rules

1. **Hierarchical numbering:** 1.1, 1.2, 2.1, 2.2, etc.
2. **Clean headers:** No metadata, just concept names
3. **Preserve examples:** Keep all worked examples exactly as written
4. **Preserve language:** All content in target language (English)
5. **Remove redundancy:** If same definition appears in multiple grades, keep the most complete version
6. **Footnote attribution:** Optional footer: "Content adapted from O Bichinho do Saber (www.obichinhodosaber.com)"

## Output

Single file: `MANUAL_FINAL_EN.md`
- Clean, professional formatting
- Ready for printing
- ~30,000-40,000 words
- Hierarchical organization following MANUAL_STRUCTURE_THEMATIC_EN.md
