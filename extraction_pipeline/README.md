# Extraction Pipeline

This directory documents the **fully automated** process for creating teaching manuals from O Bichinho do Saber content.

## 🎯 Links In → Manual Out

**Input:** Grade-level URLs from O Bichinho do Saber
**Output:** Professional PDF teaching manual, thematically organized

This is a **completely automated pipeline** from start to finish.

---

## The Complete Automated Workflow

### Phase 1: Planning Documents (Automated)

1. **`GRADE_URLS_[SUBJECT].md`** - Created first
   - Research and document all available topic URLs by grade
   - Maps the source material landscape from O Bichinho do Saber
   - Lists every topic URL that will be extracted

2. **`MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md`** - Created second
   - Analyze all available topics
   - Group topics thematically (NOT by grade)
   - Define hierarchical organization (sections, subsections)
   - Map which extracted topics go where in final manual
   - **This becomes the assembly blueprint**

3. **`ASSEMBLY_INSTRUCTIONS.md`** - Generic guide
   - Universal instructions for cleaning/assembling any subject
   - Defines what metadata to remove from extracted topics
   - Specifies formatting standards
   - Located in `extraction_pipeline/` (applies to all subjects)

### Phase 2: Content Extraction (Automated)

4. **Parallel Topic Extraction**
   - Use `topic-copier` agent for ALL topics simultaneously
   - Agent fetches content from each URL
   - Preserves Portuguese content exactly as published
   - Creates individual `.md` files in `extracted_topics/[subject]/`
   - **Critical:** Run all extractions in parallel for speed

### Phase 3: Manual Assembly (Automated)

5. **Combine Topics Following Structure**
   - Follow order defined in `MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md`
   - Remove metadata per `ASSEMBLY_INSTRUCTIONS.md`
   - Preserve core educational content
   - Create hierarchical numbering (1.1, 1.2, 2.1, etc.)
   - Output: `MANUAL_FINAL_[SUBJECT].md`

### Phase 4: PDF Generation (Automated)

6. **Generate Professional PDF**
   - Use Pandoc + XeLaTeX
   - Apply consistent styling
   - Generate table of contents
   - Output: `MANUAL_FINAL_[SUBJECT].pdf`

---

## 📋 Execution Checklist

When you receive grade-level URLs for a new subject, execute these steps **in order**:

### ✅ Step 1: Create GRADE_URLS_[SUBJECT].md
- Visit each provided grade URL
- Document all available topic URLs
- Organize by grade level
- Save in `extracted_topics/[subject]/GRADE_URLS_[SUBJECT].md`

### ✅ Step 2: Create MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md
- Analyze all topics from Step 1
- Group topics into thematic sections (NOT by grade)
- Define hierarchical organization
- Map which topics belong in each section/subsection
- Save in `extracted_topics/[subject]/MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md`

### ✅ Step 3: Extract All Topics (Parallel)
- Launch `topic-copier` agent for EVERY topic URL
- Run all extractions in parallel (critical for speed)
- Output individual topic `.md` files to `extracted_topics/[subject]/`

### ✅ Step 4: Assemble Manual
- Follow structure defined in Step 2
- Combine all topic files in thematic order
- Remove metadata per `ASSEMBLY_INSTRUCTIONS.md`
- Apply hierarchical numbering
- Create `extracted_topics/[subject]/MANUAL_FINAL_[SUBJECT].md`

### ✅ Step 5: Create Manual Directory Structure
```bash
manuals/[subject]/
├── MANUAL_FINAL_[SUBJECT].md (copy from extracted_topics)
├── MANUAL_FINAL_[SUBJECT]_PRINT.md (same content, for PDF)
├── generate_[subject]_pdf.sh (pandoc script)
└── MANUAL_FINAL_[SUBJECT].pdf (generated output)
```

### ✅ Step 6: Generate PDF
- Create `generate_[subject]_pdf.sh` script
- Run: `pandoc MANUAL_FINAL_[SUBJECT]_PRINT.md -o MANUAL_FINAL_[SUBJECT].pdf --pdf-engine=xelatex --toc --number-sections`
- Verify PDF quality and formatting

### ✅ Step 7: Update Repository Documentation
- Update main README.md with new manual info
- Add content coverage summary
- Update repository structure diagram
- Commit all work with clear message

---

## Files in This Directory

- **`topic-copier-agent.md`** - The agent that extracts web content
- **`ASSEMBLY_INSTRUCTIONS.md`** - Universal guide for cleaning and assembling topics
- **`pandoc-template.yaml`** - Advanced PDF styling template (optional)
- **`README.md`** - This file

---

## Example: Complete Math Manual Creation

```
INPUT: 5 grade URLs from O Bichinho do Saber

↓ Step 1: Document URLs
extracted_topics/math/GRADE_URLS.md (5 grades, 49 topic URLs documented)

↓ Step 2: Define thematic structure
extracted_topics/math/MANUAL_STRUCTURE_THEMATIC.md (5 sections, 19 consolidated topics)

↓ Step 3: Parallel extraction
extracted_topics/math/area.md
extracted_topics/math/numeros_naturais.md
... (19 topic files extracted simultaneously)

↓ Step 4: Assemble following structure
extracted_topics/math/MANUAL_FINAL.md (clean, thematically organized)

↓ Step 5: Prepare for PDF
manuals/math/MANUAL_FINAL_PRINT.md (copy)
manuals/math/generate_pdf.sh (created)

↓ Step 6: Generate PDF
manuals/math/MANUAL_FINAL.pdf (48 pages, professional formatting)

OUTPUT: Professional teaching manual PDF ✅
```

---

## Why This Approach Won

✅ **Fully Automated** - Links in, manual out with zero interruption
✅ **Simple** - One agent, clear linear process
✅ **Reliable** - Web content is authoritative source
✅ **Scalable** - Parallel extraction of all topics
✅ **Maintainable** - Clear separation of concerns
✅ **Reproducible** - Step-by-step checklist ensures consistency

## What Didn't Work (and was removed)

- ❌ PDF extraction pipelines (complex, unreliable)
- ❌ Multiple specialized agents (consolidator, reviewer, translator)
- ❌ Text file intermediates
- ❌ Complex consolidation workflows
- ❌ Manual topic-by-topic processing
- ❌ Semi-automated assembly requiring human intervention

The final solution: **Web → Planning Docs → Parallel Extraction → Assembly → PDF** (completely automated)

---

## Tools Used

- **Claude Code** with Task tool for parallel agent execution
- **WebFetch** for content extraction from O Bichinho do Saber
- **Pandoc** + **XeLaTeX** for professional PDF generation
- **Git** for version control and documentation

---

## Source Website

All content extracted from **O Bichinho do Saber**: https://www.obichinhodosaber.com/

Subjects covered:
- **Mathematics:** Grades 5-9 ✅
- **Natural Sciences:** Grades 7-9 ✅
- **Physics-Chemistry:** Grades 7-9 (next)
