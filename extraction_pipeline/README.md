# Extraction Pipeline

This directory documents the process used to create both teaching manuals.

## The Process That Worked

After several iterations, we landed on a simple, effective pipeline:

### 1. Web Extraction (Source of Truth)

Instead of extracting from PDFs, we extracted directly from **O Bichinho do Saber** website, which provides:
- Clean, structured content
- Complete topic coverage
- Portuguese curriculum alignment
- Up-to-date educational materials

### 2. Single Agent: topic-copier

The entire extraction uses ONE agent (`topic-copier-agent.md`) that:
- Fetches content from specified grade/topic URLs
- Copies all content into markdown files
- Preserves Portuguese language exactly as published
- Outputs to `extracted_topics/math/` or `extracted_topics/sciences/`

### 3. Manual Assembly

For each manual (Math and Sciences):
1. **Grade URLs** - Document all topic URLs by grade
2. **Thematic Structure** - Organize topics by theme (not by grade)
3. **Assembly Instructions** - Define what to keep/remove from extracted topics
4. **Parallel Extraction** - Run topic-copier on all topics simultaneously
5. **Manual Assembly** - Combine all topics following thematic structure
6. **PDF Generation** - Convert markdown to professional PDF using pandoc

## Files in This Directory

- **topic-copier-agent.md** - The agent configuration that powers the extraction
- **pandoc-template.yaml** - Advanced PDF styling template (optional)
- **README.md** - This file

## Example: Math Manual Extraction

```bash
# Step 1: Document URLs
grade_urls.md (5 grades, 49 topics total)

# Step 2: Define structure
MANUAL_STRUCTURE_THEMATIC.md (5 main sections, 19 consolidated topics)

# Step 3: Extract all topics in parallel
# (Using topic-copier agent for each topic)
math_topics/area.md
math_topics/numeros_naturais.md
... (19 topic files)

# Step 4: Assemble following structure
MANUAL_FINAL.md (assembled, metadata removed)

# Step 5: Generate PDF
./generate_pdf.sh → MANUAL_FINAL.pdf
```

## Why This Approach Won

✅ **Simple** - One agent, clear process
✅ **Reliable** - Web content is authoritative source
✅ **Scalable** - Parallel extraction of all topics
✅ **Maintainable** - Clear separation of concerns
✅ **Reproducible** - Well-documented steps

## What Didn't Work (and was removed)

- ❌ PDF extraction pipelines (complex, unreliable)
- ❌ Multiple specialized agents (consolidator, reviewer, translator, etc.)
- ❌ Text file intermediates
- ❌ Complex consolidation workflows
- ❌ Manual topic-by-topic processing

The final solution is elegant: **Web → topic-copier → Assembly → PDF**

## Tools Used

- **Claude Code** with Task tool for parallel agent execution
- **WebFetch** for content extraction
- **Pandoc** + **XeLaTeX** for PDF generation
- **Git** for version control

## Source Website

All content extracted from **O Bichinho do Saber**: https://www.obichinhodosaber.com/
- Mathematics: Grades 5-9
- Natural Sciences: Grades 7-9
