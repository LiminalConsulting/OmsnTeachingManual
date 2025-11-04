# Pipeline Quickstart Guide
## Links In → Manual Out (Fully Automated)

This guide provides the complete execution flow for creating a teaching manual from O Bichinho do Saber URLs.

---

## 🎯 One-Command Summary

**Input:** Grade-level URLs from O Bichinho do Saber
**Output:** Professional PDF teaching manual

**Process:** Completely automated from start to finish following the 7-step checklist below.

---

## 📋 The 7-Step Automated Pipeline

### Step 1: Create GRADE_URLS_[SUBJECT].md
**Purpose:** Document all available topic URLs by grade

**Actions:**
1. Visit each provided grade URL
2. Extract all topic links from each grade page
3. Organize URLs by grade level
4. Create file: `extracted_topics/[subject]/GRADE_URLS_[SUBJECT].md`

**Output Example:**
```markdown
# Grade 7 Topics
- [Topic 1](https://www.obichinhodosaber.com/...)
- [Topic 2](https://www.obichinhodosaber.com/...)

# Grade 8 Topics
- [Topic 3](https://www.obichinhodosaber.com/...)
...
```

---

### Step 2: Create MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md
**Purpose:** Define thematic organization (NOT grade-based)

**Actions:**
1. Analyze all topics from Step 1
2. Group topics into logical thematic sections
3. Define hierarchical structure (main sections → subsections → topics)
4. Map which extracted topics belong in each section
5. Create file: `extracted_topics/[subject]/MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md`

**Output Example:**
```markdown
# 1. MAIN THEME 1

## 1.1 Sub-theme A
- Topic X (from grade 7)
- Topic Y (from grade 8)

## 1.2 Sub-theme B
- Topic Z (from grade 9)

# 2. MAIN THEME 2
...
```

**Key Principle:** Topics are grouped by THEME, showing natural progression, NOT separated by grade level.

---

### Step 3: Extract All Topics (Parallel Execution)
**Purpose:** Fetch all content from O Bichinho do Saber simultaneously

**Actions:**
1. For EVERY topic URL from Step 1, launch `topic-copier` agent
2. Run ALL extractions in PARALLEL (critical for speed)
3. Each agent creates one `.md` file in `extracted_topics/[subject]/`
4. Preserve Portuguese content exactly as published

**Agent Used:** `topic-copier` (see `extraction_pipeline/topic-copier-agent.md`)

**Output:** Individual topic files (e.g., `area.md`, `numeros_naturais.md`, etc.)

---

### Step 4: Assemble Manual
**Purpose:** Combine all topics into single, clean manual following thematic structure

**Actions:**
1. Follow order defined in `MANUAL_STRUCTURE_THEMATIC_[SUBJECT].md` (from Step 2)
2. For each topic file:
   - Remove metadata per `extraction_pipeline/ASSEMBLY_INSTRUCTIONS.md`
   - Keep core educational content
   - **Use plain headers WITHOUT manual numbering** (e.g., `# TITLE` not `# 1. TITLE`)
   - Pandoc will add automatic numbering during PDF generation
3. Apply formatting fixes:
   - Add blank lines before all lists (bullets and numbered)
   - Convert special lists (elements, etc.) to proper markdown bullets
   - Translate English labels to Portuguese (keep helpful English in parentheses)
   - Keep formulas in code blocks or as inline text (will be converted later)
4. Combine all cleaned topics in thematic order
5. Create file: `extracted_topics/[subject]/MANUAL_FINAL_[SUBJECT].md`

**Reference:** See `extraction_pipeline/ASSEMBLY_INSTRUCTIONS.md` for what to remove/keep

**CRITICAL FORMATTING RULES:**
- ❌ NO manual numbering: `# 1. TITLE` → `# TITLE`
- ✅ Blank line before lists: `**Header**\n\n- item` (not `**Header**\n- item`)
- ✅ Portuguese primary, English parenthetical: `**Força (Force)**`

---

### Step 5: Create Manual Directory Structure
**Purpose:** Prepare organized directory for PDF generation

**Actions:**
```bash
mkdir -p manuals/[subject]
cp extracted_topics/[subject]/MANUAL_FINAL_[SUBJECT].md manuals/[subject]/
cp manuals/[subject]/MANUAL_FINAL_[SUBJECT].md manuals/[subject]/MANUAL_FINAL_[SUBJECT]_PRINT.md
```

**Final Structure:**
```
manuals/[subject]/
├── MANUAL_FINAL_[SUBJECT].md
├── MANUAL_FINAL_[SUBJECT]_PRINT.md (for PDF generation)
├── generate_[subject]_pdf.sh (created in Step 6)
└── MANUAL_FINAL_[SUBJECT].pdf (generated in Step 6)
```

---

### Step 6: Generate PDF
**Purpose:** Convert markdown to professional PDF with preprocessing

**Actions:**
1. Create Python preprocessing script `fix_formatting.py`:
   - Removes manual numbering from headers
   - Adds blank lines before lists
   - Converts element lists to bullets
   - Converts formulas to LaTeX notation

2. Create `generate_[subject]_pdf.sh` script in `manuals/[subject]/`:

```bash
#!/bin/bash
echo "🔄 Fixing formatting (numbering, lists, formulas)..."
python3 fix_formatting.py

echo "🔄 Generating PDF..."
pandoc MANUAL_FINAL_[SUBJECT]_PRINT.md \
  -o MANUAL_FINAL_[SUBJECT].pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V lang=pt-PT \
  -V geometry:margin=2.5cm \
  -V fontsize=11pt \
  -V documentclass=book \
  -V linestretch=1.15 \
  -V linkcolor=blue \
  -V urlcolor=blue \
  2>&1 | grep -v "WARNING" | grep -v "Missing character"

PDF_EXIT_CODE=${PIPESTATUS[0]}
if [ $PDF_EXIT_CODE -eq 0 ]; then
  echo "✅ PDF generated successfully"
  pdfinfo MANUAL_FINAL_[SUBJECT].pdf | grep "Pages:"
fi
```

3. Make executable: `chmod +x generate_[subject]_pdf.sh`
4. Run: `./generate_[subject]_pdf.sh`
5. Verify PDF quality

**Key differences from old approach:**
- ✅ Python preprocessing before PDF generation
- ✅ No manual font specification (uses system fonts)
- ✅ Portuguese language support
- ✅ Book documentclass (better for manuals)
- ✅ Automatic section numbering via pandoc

**Requirements:** Pandoc 3.6+, XeLaTeX, Python 3 (install via: `brew install pandoc basictex`)

---

### Step 7: Update Repository Documentation
**Purpose:** Maintain clear documentation of all manuals

**Actions:**
1. Update main `README.md`:
   - Add new manual to "Final Products" section
   - Update content coverage summary
   - Update repository structure diagram
2. Commit all work:
   ```bash
   git add .
   git commit -m "Add [Subject] teaching manual for grades X-Y"
   ```

---

## 🔄 Complete Flow Diagram

```
INPUT: URLs (e.g., 3 physics-chemistry grade pages)
   ↓
Step 1: GRADE_URLS_PHYSICS_CHEMISTRY.md created
   ↓
Step 2: MANUAL_STRUCTURE_THEMATIC_PHYSICS_CHEMISTRY.md created
   ↓
Step 3: Parallel extraction → 30+ individual topic .md files
   ↓
Step 4: Assembly → MANUAL_FINAL_PHYSICS_CHEMISTRY.md (clean)
   ↓
Step 5: Directory setup → manuals/physics-chemistry/
   ↓
Step 6: PDF generation → MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf
   ↓
Step 7: Documentation updates → README.md, git commit
   ↓
OUTPUT: Professional PDF teaching manual ✅
```

---

## ⚡ Key Success Factors

1. **Follow exact order** - Steps build on each other sequentially
2. **Parallel extraction** - Step 3 must run all topic-copier agents simultaneously
3. **Thematic organization** - Step 2 groups by theme, NOT by grade
4. **Complete automation** - No manual intervention needed between steps
5. **Clean assembly** - Step 4 removes ALL metadata per assembly instructions

---

## 📚 Reference Documents

- **Detailed Pipeline:** `extraction_pipeline/README.md`
- **Assembly Guide:** `extraction_pipeline/ASSEMBLY_INSTRUCTIONS.md`
- **Topic Extractor:** `extraction_pipeline/topic-copier-agent.md`
- **Main README:** `README.md`

---

## ✅ Quality Checklist

Before considering the manual complete, verify:

- [ ] All topic URLs from Step 1 were extracted
- [ ] Thematic structure makes logical sense
- [ ] All metadata removed from assembled manual
- [ ] Hierarchical numbering is consistent (1.1, 1.2, 2.1, etc.)
- [ ] PDF generates without errors
- [ ] Table of contents is accurate
- [ ] Page count is reasonable (30-80 pages typical)
- [ ] Portuguese language preserved throughout
- [ ] Repository README updated with new manual info
- [ ] All work committed to git

---

## 🎓 Example: Math Manual (Reference)

See `manuals/math/` for a complete example of the final output:
- 19 topics across 5 thematic sections
- 48 pages, professionally formatted
- Grades 5-9 coverage
- Created using this exact pipeline
