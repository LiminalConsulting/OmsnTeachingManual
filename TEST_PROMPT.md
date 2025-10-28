# Test Prompt: Validate Complete Pipeline with Prime Numbers

## Context

We've built a 4-stage agent-based pipeline to refactor the Portuguese mathematics curriculum (grades 5-9) from grade-organized PDFs into a thematically-organized teaching manual. This test will validate the entire workflow using a single topic.

**IMPORTANT**: All agents are defined in **English** but explicitly instructed to **preserve the original language** of source documents (Portuguese). Do NOT translate content - only reorganize it.

## Your Task

Process **one complete topic** ("Números primos") through the full 4-stage pipeline to validate that everything works correctly:

1. **EXTRACT**: Invoke topic-extractor sub-agent for each grade (5-9)
2. **CONSOLIDATE**: Invoke topic-consolidator sub-agent to merge grades
3. **DEDUPLICATE**: Invoke duplicate-remover sub-agent for final cleanup
4. **REVIEW**: Invoke quality-reviewer sub-agent to validate output

After completing all stages, stop and report results for validation.

## How to Invoke Sub-Agents

Use natural language to request specific sub-agents. Example:

```
Use the topic-extractor sub-agent to extract "Números primos" from
text_versions/grade5_math.txt and save to topics/raw/prime_numbers_g5.md
```

The agents will automatically activate when you mention them by name and describe the task.

## Files & Infrastructure

### Text Versions (Ready to Use)
```
text_versions/grade5_math.txt (140KB)
text_versions/grade6_math.txt (128KB)
text_versions/grade7_math.txt (154KB)
text_versions/grade8_math.txt (132KB)
text_versions/grade9_math.txt (132KB)
```

### Sub-Agents (Already Configured)
```
.claude/agents/topic-extractor.md      # Extracts topic from single grade text file
.claude/agents/topic-consolidator.md   # Merges extractions from all 5 grades
.claude/agents/duplicate-remover.md    # Removes marked duplicates conservatively
.claude/agents/quality-reviewer.md     # Reviews final output for quality issues
```

**Agent Features:**
- All agents written in English for clarity
- Explicit "PRESERVE ORIGINAL LANGUAGE" instructions
- topic-extractor uses table of contents + offset/limit for efficient reading
- quality-reviewer checks language consistency, completeness, and alignment

### Output Structure
```
topics/raw/prime_numbers_g[5-9].md       # Extraction outputs (5 files)
topics/consolidated/prime_numbers.md     # Consolidated output (1 file)
topics/clean/prime_numbers_final.md      # Final deduplicated version (1 file)
```

## Test Workflow: Process "Números primos"

### Step 1: Extract from all 5 grades

Invoke the topic-extractor sub-agent 5 times to extract "Números primos" from each grade:

```
Use the topic-extractor sub-agent to extract "Números primos" from:
- text_versions/grade5_math.txt → topics/raw/prime_numbers_g5.md
- text_versions/grade6_math.txt → topics/raw/prime_numbers_g6.md
- text_versions/grade7_math.txt → topics/raw/prime_numbers_g7.md
- text_versions/grade8_math.txt → topics/raw/prime_numbers_g8.md
- text_versions/grade9_math.txt → topics/raw/prime_numbers_g9.md
```

**Expected behavior:**
- topic-extractor reads table of contents to find line numbers
- Uses Read with offset/limit to extract only relevant sections
- Some grades may not have this topic (handle gracefully)
- All content preserved in original Portuguese

### Step 2: Consolidate

Invoke the topic-consolidator sub-agent to merge all extractions:

```
Use the topic-consolidator sub-agent to merge all prime_numbers_g[5-9].md files
from topics/raw/ into topics/consolidated/prime_numbers.md
```

**Expected behavior:**
- Combines all 5 grade extractions into single file
- Organizes by grade with clear headers
- Marks exact duplicates with <!-- DUPLICATE: ... --> comments
- Preserves ALL content (no removal yet)
- Content remains in Portuguese

### Step 3: Deduplicate

Invoke the duplicate-remover sub-agent to clean up:

```
Use the duplicate-remover sub-agent to clean topics/consolidated/prime_numbers.md
and output to topics/clean/prime_numbers_final.md
```

**Expected behavior:**
- Removes only content explicitly marked as <!-- DUPLICATE -->
- Keeps first occurrence of duplicated content
- Preserves all unique content unchanged
- Content remains in Portuguese

### Step 4: Quality Review

Invoke the quality-reviewer sub-agent to validate the final output:

```
Use the quality-reviewer sub-agent to review topics/clean/prime_numbers_final.md
and check for language consistency, completeness, and alignment with objectives
```

**Expected behavior:**
- Verifies all content is in Portuguese (no English translation)
- Checks completeness (learning objectives, examples, tables present)
- Validates structure (organized by grade, well formatted)
- Confirms conservative deduplication (no loss of unique content)
- Reports any issues or confirms approval

## Stop and Report

After completing all 4 stages, **STOP** and provide:

### 1. Pipeline Summary
- How many extraction files were created (should be 5, some may be empty/notes)
- Size of consolidated file (line count)
- Size of final deduplicated file (line count)
- Any topics that were missing from certain grades

### 2. Quality Assessment
- Report from quality-reviewer sub-agent
- Any language issues detected (should be none - all Portuguese)
- Any content completeness issues
- Overall approval status

### 3. Sample Content
Show a brief preview (10-20 lines) from the final output to demonstrate:
- Content is in Portuguese
- Structure is clean and organized
- Examples and details are preserved

### 4. Files Created
List all files created during this test:
```
topics/raw/prime_numbers_g5.md
topics/raw/prime_numbers_g6.md
topics/raw/prime_numbers_g7.md
topics/raw/prime_numbers_g8.md
topics/raw/prime_numbers_g9.md
topics/consolidated/prime_numbers.md
topics/clean/prime_numbers_final.md
```

## Success Criteria

This test passes if:
- ✅ All 4 stages complete without errors
- ✅ All content is in Portuguese (no translation occurred)
- ✅ Final output preserves ALL original detail from source PDFs
- ✅ Only exact duplicates were removed
- ✅ Structure is clean and organized by grade
- ✅ quality-reviewer approves the final output
- ✅ Agents used table of contents + offset/limit (no context issues)

## Important Notes

**Topic Coverage**: "Números primos" appears in grades 5, 6, and 9, but NOT in grades 7 and 8. The agents should handle this gracefully.

**Language Preservation**: The most critical test - verify NO Portuguese→English translation occurred anywhere in the pipeline.

**Table of Contents Strategy**: Watch for the topic-extractor to read the table of contents first, identify line numbers, then use Read with offset/limit. This is the efficient approach.

**Conservative Deduplication**: Only word-for-word identical content should be marked/removed. Similar-but-different content should be preserved.

Let me know when you're ready to begin the test!
