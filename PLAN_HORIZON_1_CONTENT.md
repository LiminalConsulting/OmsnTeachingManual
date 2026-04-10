# Horizon 1: Content Completion & Repo Cleanup

**Goal:** Every subject has a complete, clean set of PDFs — Portuguese, English, and Bilingual
versions of both the Teaching Manual and the Exercise Book — all properly formatted,
page-matched, and ready to print. The repo is clean with no clutter.

**Work entirely in Markdown source files. Never open PDFs to read content — that burns tokens fast.**

---

## Current State Audit

### Teaching Manuals

| Subject | PT source | EN source | Bilingual | Notes |
|---------|-----------|-----------|-----------|-------|
| Math | ✅ `MANUAL_FINAL_PRINT.md` | ✅ `MANUAL_FINAL_EN_PRINT.md` | ✅ PDF exists | Images exist in `images/` but NOT referenced in Markdown — skip for now |
| Physics-Chemistry | ✅ `MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md` | ✅ `MANUAL_FINAL_PHYSICS_CHEMISTRY_EN_PRINT.md` | ✅ PDF exists | |
| Natural Sciences | ✅ `MANUAL_FINAL_SCIENCES_PRINT.md` | ✅ `MANUAL_FINAL_SCIENCES_EN_PRINT.md` | ✅ PDF exists | |
| History & Geography | ✅ `MANUAL_FINAL_HISTORY_GEOGRAPHY_PRINT.md` (7878 lines) | ❌ MISSING | ❌ MISSING | Biggest gap |

### Exercise Books

| Subject | PT files | EN files | Bilingual | Notes |
|---------|----------|----------|-----------|-------|
| Math | ✅ CH2-CH6 PT | ✅ CH2-CH6 EN | ❌ MISSING | No CH1 (Numbers is CH2 — verify chapter numbering) |
| Physics-Chemistry | ✅ CH1-CH8 PT | ✅ CH1-CH8 EN | ❌ MISSING | Complete coverage |
| Natural Sciences | ✅ CH1-CH4 PT | ✅ CH1-CH4 EN | ❌ MISSING | Complete coverage |
| History & Geography | PT only: HGP5, HGP6, HISTORIA 7-9, GEOGRAFIA 7-9 | EN only: HGP5 | ❌ MISSING | EN missing for HGP6, HISTORIA 7-9, GEOGRAFIA 7-9 |

### Bilingual Page-Matching Problem

The current bilingual approach generates PT and EN PDFs independently then interleaves pages
with ghostscript — but ONLY if page counts match exactly. This is fragile.

**The fix:** Use LaTeX `paracol` package to compile both languages in a single pass.
Each section appears in a two-column layout: Portuguese left, English right. Page breaks
are computed once. No reconciliation needed.

This means: the bilingual source is a **new file** (e.g. `MANUAL_FINAL_BILINGUAL.md`)
that interleaves PT and EN content using paracol syntax, compiled with a single pandoc call.

---

## Phase 1: History & Geography — Fill the Gap

This is the largest missing piece. Work in the `subjects/history-geography/` directory.

### 1.1 — Produce the English Teaching Manual

Source: `manual/MANUAL_FINAL_HISTORY_GEOGRAPHY_PRINT.md` (7878 lines — work in sections)

Process each major section (HGP 5-6, Historia 7-9, Geografia 7-9) separately to stay
within context limits. Save as: `manual/MANUAL_FINAL_HISTORY_GEOGRAPHY_EN_PRINT.md`

Translation guidelines:
- Maintain the same structure, headings, chapter numbers, and page-break markers exactly
- Translate all content including tables, callout boxes, and exercises
- Keep Portuguese proper nouns (place names, person names) as-is
- Terminology: "HGP" stays as-is; "Geo-educators" stays; curriculum terms use standard English equivalents
- Target: same section count and approximate same length as PT version (critical for bilingual matching)

### 1.2 — Produce English Exercise Files

Files needed (translate from PT originals):
- `exercises/EXERCISES_HGP_6ANO_EN.md` (from HGP_6ANO.md)
- `exercises/EXERCISES_HISTORIA_7ANO_EN.md` (from HISTORIA_7ANO.md)
- `exercises/EXERCISES_HISTORIA_8ANO_EN.md` (from HISTORIA_8ANO.md)
- `exercises/EXERCISES_HISTORIA_9ANO_EN.md` (from HISTORIA_9ANO.md)
- `exercises/EXERCISES_GEOGRAFIA_7ANO_EN.md` (from GEOGRAFIA_7ANO.md)
- `exercises/EXERCISES_GEOGRAFIA_8ANO_EN.md` (from GEOGRAFIA_8ANO.md)
- `exercises/EXERCISES_GEOGRAFIA_9ANO_EN.md` (from GEOGRAFIA_9ANO.md)

### 1.3 — Add PDF generation scripts for History & Geography EN + exercises

Model after `subjects/sciences/exercises/generate_exercises_pdf.sh`.
Create `exercises/generate_exercises_pdf.sh` for History & Geography.
Update `manual/generate_history_geography_pdf.sh` to also produce EN PDF.

---

## Phase 2: Bilingual Teaching Manuals (All Subjects)

### The paracol approach

For each subject, create a bilingual source file and build script.

**Pandoc call:**
```bash
pandoc MANUAL_FINAL_BILINGUAL.md \
  -o MANUAL_FINAL_BILINGUAL.pdf \
  --pdf-engine=xelatex \
  --toc \
  -V geometry:"margin=1.5cm,landscape" \
  -V fontsize=9pt \
  -V documentclass=book \
  -V classoption=openany \
  --include-in-header=paracol_header.tex \
  2>&1 | grep -v "WARNING"
```

**`paracol_header.tex`** (place in `shared/`):
```latex
\usepackage{paracol}
\usepackage{graphicx}
\columnratio{0.5}
```

**Bilingual source structure** (in the `.md` file):
```
\begin{paracol}{2}

[Portuguese content for this section]

\switchcolumn

[English content for this section]

\switchcolumn*

[Next Portuguese section]

\switchcolumn

[Next English section]

\end{paracol}
```

Use `\switchcolumn*` (with asterisk) to force a synchronized page break — both columns
advance to the next page together. This is the key to guaranteed page matching.

**Files to create per subject:**
- `manual/MANUAL_FINAL_BILINGUAL_SRC.md` — the paracol source
- `manual/generate_bilingual_pdf.sh` — updated build script using paracol

Do Math first (smallest), then Physics-Chemistry, Sciences, then History & Geography.

### Cover files for bilingual

Each bilingual PDF needs a cover that says both languages. Model: `COVER_BILINGUAL.md`
already exists for Math — replicate for History & Geography.

Cover should state:
- Subject name in Portuguese AND English
- "Manual de Ensino / Teaching Manual" or "Caderno de Exercícios / Exercise Book"
- Grade range
- "Edição Bilingue / Bilingual Edition"

---

## Phase 3: Bilingual Exercise Books (All Subjects)

Same paracol approach as teaching manuals.

For each subject, create:
- A single bilingual exercise source per chapter: `EXERCISES_CHX_BILINGUAL.md`
- Or a combined bilingual exercise book: `EXERCISES_ALL_BILINGUAL.md`

**Recommendation:** one combined bilingual exercise book per subject (all chapters together)
is cleaner for printing — fewer files, one cover, continuous page numbering.

Exercise cover format:
```
[Subject] — Caderno de Exercícios / Exercise Book
[Grade range]
Edição Bilingue / Bilingual Edition
```

Exercise books do NOT need a TOC — they are thin enough to navigate without one.

---

## Phase 4: Repo Cleanup

### Files to delete (clutter)
In each `manual/` directory, remove:
- `*_BACKUP.pdf` files
- `*_PRE_RESTRUCTURE.md` files
- `*.md.bak` files
- `*_ALIGNED.md`, `*_PRINT_ALIGNED.md` files (superseded by clean approach)
- Intermediate Python scripts that were one-time-use fixes (`clean_english_manual.py`,
  `fix_formatting.py`, `add_section_breaks.py`, `analyze_page_alignment.py`,
  `assemble_english_manual.sh`, `split_manual.sh`)

### Files to keep
- `MANUAL_FINAL_PRINT.md` — PT source (canonical)
- `MANUAL_FINAL_EN_PRINT.md` — EN source (canonical)
- `MANUAL_FINAL_BILINGUAL_SRC.md` — bilingual paracol source
- `MANUAL_FINAL.pdf`, `MANUAL_FINAL_EN.pdf`, `MANUAL_FINAL_BILINGUAL.pdf` — outputs
- `COVER.md`, `COVER_EN.md`, `COVER_BILINGUAL.md` — covers
- `generate_pdf.sh`, `generate_pdf_en.sh`, `generate_bilingual_pdf.sh` — build scripts
- `images/` directory (even if unused for now — they'll be used in Horizon 2)
- Exercise `.md` files and their `generate_exercises_pdf.sh`

### README updates

Update `README.md` at repo root with accurate table of all produced PDFs, their page counts,
and a "How to regenerate" section. Each subject's `manual/README.md` should list
exactly what exists and the command to regenerate.

### Naming convention (enforce across all subjects)

Teaching manuals:
- `MANUAL_FINAL.pdf` — Portuguese
- `MANUAL_FINAL_EN.pdf` — English
- `MANUAL_FINAL_BILINGUAL.pdf` — Bilingual

Exercise books:
- `EXERCISES_FINAL.pdf` — Portuguese (all chapters combined)
- `EXERCISES_FINAL_EN.pdf` — English
- `EXERCISES_FINAL_BILINGUAL.pdf` — Bilingual

If per-chapter exercise PDFs also exist, keep them — but the combined book is the
primary deliverable.

---

## Phase 5: Validation Checklist

Before declaring Horizon 1 complete, verify:

**Teaching Manuals:**
- [ ] Math: PT ✅, EN ✅, Bilingual ✅ — page counts logged
- [ ] Physics-Chemistry: PT ✅, EN ✅, Bilingual ✅ — page counts logged
- [ ] Natural Sciences: PT ✅, EN ✅, Bilingual ✅ — page counts logged
- [ ] History & Geography: PT ✅, EN ✅, Bilingual ✅ — page counts logged
- [ ] All bilingual PDFs: PT and EN sections verified to be synchronized (spot-check 3 chapter boundaries)
- [ ] All covers correctly identify: subject, language, grade range, manual type

**Exercise Books:**
- [ ] Math: PT ✅, EN ✅, Bilingual ✅
- [ ] Physics-Chemistry: PT ✅, EN ✅, Bilingual ✅
- [ ] Natural Sciences: PT ✅, EN ✅, Bilingual ✅
- [ ] History & Geography: PT ✅, EN ✅, Bilingual ✅
- [ ] Page references in exercises match section numbers in corresponding teaching manual

**Repo:**
- [ ] No BACKUP, .bak, PRE_RESTRUCTURE, or intermediate script clutter
- [ ] Root README accurately describes all outputs
- [ ] Each subject README accurately lists its files
- [ ] All build scripts run cleanly from their directory
- [ ] `git status` is clean after all PDFs regenerated

---

## Execution Order

1. History & Geography EN manual (biggest single task — do in 2-3 context sessions by section)
2. History & Geography EN exercises (7 files)
3. History & Geography PDF scripts
4. Bilingual teaching manuals — Math (template for all others)
5. Bilingual teaching manuals — Physics, Sciences, History
6. Bilingual exercise books — all subjects
7. Repo cleanup (delete clutter, update READMEs)
8. Run full validation checklist

---

## Token Efficiency Notes

- Always read `.md` source files, never PDFs
- For History & Geography (7878 lines): split into HGP (5-6), Historia (7-9), Geografia (7-9)
  — translate one section per context session
- When creating bilingual source: read PT and EN side by side, interleave section by section
- After any content work: commit immediately so progress is never lost
- The build scripts exist — trust them. Don't rewrite them, just add missing ones.
