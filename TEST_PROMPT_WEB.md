# Test Prompt: Validate Complete Web Pipeline with "Números Primos"

## Context

We've built a web-based, year-by-year agent pipeline to refactor Portuguese mathematics curriculum from **O Bichinho do Saber website**. This test validates the entire workflow using a single topic across multiple grades.

**IMPORTANT**: All agents are in English but preserve original Portuguese content. Translation happens in the final step only.

## Your Task

Process **"Números primos" (Prime Numbers)** through the complete 5-stage incremental pipeline to validate everything works:

1. **EXTRACT**: Invoke web-topic-extractor for each grade (5-9)
2. **CONSOLIDATE**: Invoke incremental-consolidator to merge incrementally
3. **DEDUPLICATE**: Invoke duplicate-remover for cleanup
4. **REVIEW**: Invoke quality-reviewer to validate
5. **TRANSLATE**: Invoke translator to create English version

After completing all stages, **STOP** and report results.

## Test Topic: "Números Primos" (Prime Numbers)

**Expected Coverage:**
- Grade 5: Números naturais (includes prime numbers)
- Grade 6: Números primos e decomposição em fatores primos (dedicated topic)
- Grades 7-9: May or may not appear (test graceful handling)

**Why This Topic:**
- Appears explicitly in some grades
- Part of broader topics in others
- Tests topic discovery and name variation handling
- Small enough to validate quickly

## Files & Infrastructure

### Source URLs
```
Grade 5: https://www.obichinhodosaber.com/matematica-5o-materia-de-matematica-5o-ano/
Grade 6: https://www.obichinhodosaber.com/matematica-6o-materia-de-matematica-6o-ano/
Grade 7: https://www.obichinhodosaber.com/matematica-7o-materia-de-matematica-7o-ano/
Grade 8: https://www.obichinhodosaber.com/resumos-e-exercicios-de-matematica-8o-ano/
Grade 9: https://www.obichinhodosaber.com/matematica-9o-materia-de-matematica-9o-ano/
```

### Sub-Agents (Already Configured)
```
.claude/agents/web-topic-extractor.md        # Extracts from website
.claude/agents/incremental-consolidator.md   # Incremental merge
.claude/agents/duplicate-remover.md          # Removes marked duplicates
.claude/agents/web-quality-reviewer.md       # Reviews web-based quality (NOT quality-reviewer.md!)
.claude/agents/translator.md                 # Translates to English
```

**IMPORTANT:** Use `web-quality-reviewer` agent (NOT `quality-reviewer`). The `quality-reviewer` agent is for the OLD PDF-based pipeline. The `web-quality-reviewer` agent understands this is O Bichinho do Saber website content.

### Expected Output Files
```
topics/raw/numeros_primos_g5.md
topics/raw/numeros_primos_g6.md
topics/raw/numeros_primos_g7.md  (may note "not covered")
topics/raw/numeros_primos_g8.md  (may note "not covered")
topics/raw/numeros_primos_g9.md
topics/consolidated/numeros_primos.md
topics/clean/numeros_primos_final.md
topics/clean/numeros_primos_final_EN.md
```

## Test Workflow

### Stage 1: Extract from All 5 Grades

**Step 1.1: Extract Grade 5**
```
Use the web-topic-extractor agent to extract "Números primos" content from:
- URL: https://www.obichinhodosaber.com/matematica-5o-materia-de-matematica-5o-ano/
- Topic: Look under "Números naturais" for prime numbers content
- Output: topics/raw/numeros_primos_g5.md
```

**Step 1.2: Extract Grade 6**
```
Use the web-topic-extractor agent to extract "Números primos" from:
- URL: https://www.obichinhodosaber.com/matematica-6o-materia-de-matematica-6o-ano/
- Topic: "Números naturais: números primos e decomposição em fatores primos"
- Output: topics/raw/numeros_primos_g6.md
```

**Steps 1.3-1.5: Extract Grades 7, 8, 9**
```
Use web-topic-extractor for each remaining grade
- Search for prime numbers content in available topics
- If not found, note "Este tópico não é abordado" in output file
- Outputs: topics/raw/numeros_primos_g7.md, g8.md, g9.md
```

**Expected Behavior:**
- web-topic-extractor navigates from index page to topic page
- Extracts complete content (objectives, examples, tables)
- Handles missing topics gracefully
- Preserves original Portuguese

### Stage 2: Incremental Consolidation

**Step 2.1: Consolidate Grade 5 (Create Initial File)**
```
Use incremental-consolidator agent with topics/raw/numeros_primos_g5.md
- Creates new file: topics/consolidated/numeros_primos.md
- No duplicates to mark yet (first grade)
```

**Step 2.2: Add Grade 6 (First Merge)**
```
Use incremental-consolidator agent with topics/raw/numeros_primos_g6.md
- Reads existing topics/consolidated/numeros_primos.md
- Compares Grade 6 content with Grade 5 content
- Marks exact duplicates with <!-- DUPLICATE --> comments
- Appends Grade 6 section
- Updates consolidated file
```

**Steps 2.3-2.5: Add Grades 7, 8, 9**
```
Use incremental-consolidator for each remaining grade
- Reads existing consolidated file
- Compares new content with all previous grades
- Marks duplicates, appends new grade section
- Handles empty grades gracefully
```

**Expected Behavior:**
- Each merge only reads the single topic file (stays small)
- Identifies exact duplicates across grades
- Preserves all unique content
- Content remains in Portuguese

### Stage 3: Deduplicate

**Step 3: Clean Consolidated File**
```
Use duplicate-remover agent on topics/consolidated/numeros_primos.md
- Removes content marked with <!-- DUPLICATE --> comments
- Keeps first occurrence of duplicated content
- Preserves all unique content
- Output: topics/clean/numeros_primos_final.md
```

**Expected Behavior:**
- Only removes explicitly marked duplicates
- Maintains grade structure
- Content remains in Portuguese
- Conservative approach (keeps if uncertain)

### Stage 4: Quality Review

**Step 4: Validate Final Output**
```
Use web-quality-reviewer agent on topics/clean/numeros_primos_final.md
- Check language consistency (all Portuguese)
- Verify web content completeness (explanations, examples, tables, exercises present)
- Confirm source is O Bichinho do Saber website (NOT curriculum PDFs)
- Confirm conservative deduplication (no loss of unique content)
- Validate structure (organized by grade)
- Report approval or issues
```

**CRITICAL:** Use `web-quality-reviewer` (NOT `quality-reviewer`). The old agent checks against PDF curriculum files!

**Expected Behavior:**
- Identifies any critical issues (language mixing, missing content)
- Provides constructive feedback
- Approves if meets quality criteria

### Stage 5: Translate to English

**Step 5: Create English Version**
```
Use translator agent on topics/clean/numeros_primos_final.md
- Translates all Portuguese content to English
- Preserves structure, examples, formatting
- Output: topics/clean/numeros_primos_final_EN.md
```

**Expected Behavior:**
- Complete translation of all content
- Structure and formatting preserved
- Both Portuguese and English versions available

## Stop and Report

After completing all 5 stages, **STOP** and provide:

### 1. Pipeline Summary
```
✅ Extraction: [X] files created (some may note "not covered")
✅ Consolidation: Incremental merges completed
✅ Deduplication: Duplicates removed
✅ Review: Quality assessment completed
✅ Translation: English version created
```

### 2. File Statistics
```
- Raw extractions: [count] files, [total lines]
- Consolidated: [line count], [grades covered]
- Final clean: [line count] (Portuguese)
- Final translated: [line count] (English)
- Duplicates removed: [estimated count/percentage]
```

### 3. Quality Assessment
```
- Language: ✅ Portuguese preserved through stages 1-4
- Translation: ✅ English version created in stage 5
- Completeness: ✅ All objectives, examples, tables present
- Structure: ✅ Organized by grade
- Deduplication: ✅ Conservative (no unique content lost)
- Reviewer approval: ✅/❌
```

### 4. Sample Content Preview
Show 15-20 lines from `topics/clean/numeros_primos_final.md` demonstrating:
- Portuguese content
- Grade organization
- Preserved examples/tables

### 5. Issues Encountered (if any)
```
- Topic not found in certain grades: [list]
- Name variations handled: [examples]
- Duplicate detection challenges: [describe]
- Any errors or warnings: [list]
```

## Success Criteria

This test passes if:
- ✅ All 5 stages complete without critical errors
- ✅ Web extraction successfully navigates and fetches content
- ✅ Incremental consolidation merges grades progressively
- ✅ Context limits never exceeded (each agent handles small scope)
- ✅ All content in Portuguese through stages 1-4
- ✅ English translation successful in stage 5
- ✅ Final output preserves ALL original detail
- ✅ Only exact duplicates removed
- ✅ Quality reviewer approves final output

## Important Notes

**Topic Discovery:**
- "Números primos" may be part of broader "Números naturais" topic in some grades
- web-topic-extractor should search within related pages
- Test validates flexible topic name handling

**Context Efficiency:**
- Each consolidated file = single topic only
- incremental-consolidator only reads relevant topic file
- No risk of context overflow

**Graceful Degradation:**
- If topic doesn't exist in a grade, extraction notes this
- Consolidator handles empty/minimal grade content
- Pipeline continues without breaking

**Conservative Approach:**
- Only mark as duplicate if word-for-word identical
- Preserve similar-but-different content
- Quality over aggressive compression

---

**Ready to test!** Begin with Stage 1: Extract from all 5 grades.
