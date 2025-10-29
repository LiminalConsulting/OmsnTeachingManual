---
description: Process a single topic through complete web-based extraction pipeline (extract → consolidate → deduplicate → review → translate)
argument-hint: [Topic Name (Grades: X, Y, Z)]
---

# Process Topic Through Web Extraction Pipeline

You will process **$ARGUMENTS** through the complete 5-stage web-based extraction pipeline.

## Context

This is the **production workflow** for extracting curriculum content from O Bichinho do Saber website. The pipeline has been tested and proven with the "Números primos" topic.

**Source:** O Bichinho do Saber website (obichinhodosaber.com)
**Pipeline:** Extract → Consolidate → Deduplicate → Review → Translate

## Your Task

Process the topic specified in the user's input through all 5 stages:

1. **EXTRACT**: Use web-topic-extractor for each grade mentioned
2. **CONSOLIDATE**: Use incremental-consolidator to merge grades
3. **DEDUPLICATE**: Use duplicate-remover to clean
4. **REVIEW**: Use web-quality-reviewer to validate (NOT quality-reviewer!)
5. **TRANSLATE**: Use translator to create English version

## Topic Information

**Topic:** $ARGUMENTS

Parse this input to extract:
- **Topic name**: Everything before the parentheses
- **Grades**: Numbers inside parentheses (e.g., "5, 6, 9" from "(5, 6, 9)")

Example input: "Números naturais (5, 6)"
- Topic: Números naturais
- Grades to process: 5, 6

## Grade URLs (Reference)

```
Grade 5: https://www.obichinhodosaber.com/matematica-5o-materia-de-matematica-5o-ano/
Grade 6: https://www.obichinhodosaber.com/matematica-6o-materia-de-matematica-6o-ano/
Grade 7: https://www.obichinhodosaber.com/matematica-7o-materia-de-matematica-7o-ano/
Grade 8: https://www.obichinhodosaber.com/resumos-e-exercicios-de-matematica-8o-ano/
Grade 9: https://www.obichinhodosaber.com/matematica-9o-materia-de-matematica-9o-ano/
```

## Topic Slug Generation

Convert topic name to snake_case for file naming:
- Remove accents: "Números" → "Numeros"
- Lowercase: "Numeros" → "numeros"
- Replace spaces with underscores: "numeros naturais" → "numeros_naturais"

## Complete Workflow

### Stage 1: Extract from All Specified Grades

For each grade number from the input:

```
Use web-topic-extractor agent to extract "[topic name]" from Grade [X]:
- URL: [appropriate grade URL from above]
- Topic: [topic name from input]
- Output: topics/raw/[topic_slug]_g[X].md
```

**Run all extractions** for the specified grades. If input says "(5, 6, 9)", extract from grades 5, 6, and 9 only.

### Stage 2: Incremental Consolidation

Process grades in order (5 → 6 → 7 → 8 → 9):

**First grade:**
```
Use incremental-consolidator agent with topics/raw/[topic_slug]_g[first_grade].md
- Creates new file: topics/consolidated/[topic_slug].md
- No duplicates to mark yet (first grade for this topic)
```

**Subsequent grades:**
```
Use incremental-consolidator agent for each remaining grade:
- Input: topics/raw/[topic_slug]_g[X].md
- Reads existing topics/consolidated/[topic_slug].md
- Compares new grade content with previous grades
- Marks exact duplicates with <!-- DUPLICATE --> comments
- Appends new grade section
- Updates consolidated file
```

### Stage 3: Deduplicate

```
Use duplicate-remover agent on topics/consolidated/[topic_slug].md
- Removes content marked with <!-- DUPLICATE --> comments
- Keeps first occurrence of duplicated content
- Preserves all unique content
- Output: topics/clean/[topic_slug]_final.md
```

### Stage 4: Quality Review

```
Use web-quality-reviewer agent on topics/clean/[topic_slug]_final.md
- Check language consistency (all Portuguese)
- Verify web content completeness
- Confirm source is O Bichinho do Saber website
- Validate conservative deduplication
- Report approval or issues
```

**CRITICAL:** Use `web-quality-reviewer` (NOT `quality-reviewer`). The old agent checks against PDF curriculum files!

### Stage 5: Translate to English

```
Use translator agent on topics/clean/[topic_slug]_final.md
- Translates all Portuguese content to English
- Preserves structure, examples, formatting
- Output: topics/clean/[topic_slug]_final_EN.md
```

## Final Report

After completing all 5 stages, provide:

### 1. Pipeline Summary
```
✅ Extraction: [X] grades processed
✅ Consolidation: Incremental merges completed
✅ Deduplication: Duplicates removed
✅ Review: Quality assessment completed
✅ Translation: English version created
```

### 2. Files Created
```
Raw extractions: topics/raw/[topic_slug]_g[X].md (one per grade)
Consolidated: topics/consolidated/[topic_slug].md
Final (Portuguese): topics/clean/[topic_slug]_final.md
Final (English): topics/clean/[topic_slug]_final_EN.md
```

### 3. Quality Status
- Reviewer approval: ✅/❌
- Any issues encountered: [describe]
- Topic successfully processed: ✅/❌

## Important Notes

**Web-Based Pipeline:**
- Source is O Bichinho do Saber website (NOT curriculum PDFs)
- Use `web-quality-reviewer` agent (understands web content)
- Only process grades specified in input (don't add others)

**Context Efficiency:**
- Each consolidated file = single topic (stays small)
- No risk of context overflow
- incremental-consolidator reads only relevant topic file

**Language Preservation:**
- Portuguese preserved through stages 1-4
- English translation is stage 5 only

**Error Handling:**
- If a grade extraction fails, continue with others
- If web page not found, note this and continue
- Report any failures in final summary

**Conservative Approach:**
- Preserve all unique content
- Only mark exact word-for-word duplicates
- Quality over aggressive compression

---

## Example Usage

```
/consolidate-topic Números naturais (5, 6)
```

This will:
1. Extract "Números naturais" from grades 5 and 6
2. Consolidate into single file
3. Deduplicate conservatively
4. Review with web-quality-reviewer
5. Translate to English
6. Report completion status

---

**Ready to process!** The topic information is: $ARGUMENTS
