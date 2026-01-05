# Formatting Checklist for Manual Assembly
## Common Issues and How to Fix Them

This checklist documents lessons learned from creating the Physics-Chemistry manual.
Use it to ensure proper formatting during assembly (Step 4) and avoid manual corrections later.

---

## ✅ Assembly Phase Checklist

### 1. Header Numbering
- [ ] **Remove ALL manual numbering from headers**
  - ❌ Bad: `# 1. ASTRONOMIA`, `## 1.1 O Universo`
  - ✅ Good: `# ASTRONOMIA`, `## O Universo`
  - **Why:** Pandoc's `--number-sections` adds automatic numbering
  - **Problem if wrong:** Double numbering (1. 1. Title)

### 2. List Formatting
- [ ] **Add blank line before ALL lists**
  - ❌ Bad:
    ```markdown
    **Telescópios**
    - instrumentos de ampliação
    ```
  - ✅ Good:
    ```markdown
    **Telescópios**

    - instrumentos de ampliação
    ```
  - **Why:** Markdown requires blank line to recognize lists
  - **Problem if wrong:** Lists render as inline text with dashes

### 3. Element Lists
- [ ] **Convert element patterns to markdown lists**
  - ❌ Bad:
    ```markdown
    **Exemplos (Z≤20):**

    1H – 1
    2He – 2
    ```
  - ✅ Good:
    ```markdown
    **Exemplos (Z≤20):**

    - 1H – 1
    - 2He – 2
    ```
  - **Pattern to detect:** Lines starting with `\d+[A-Z][a-z]?\s*–`
  - **Problem if wrong:** Elements appear as plain text, not list

### 4. Language: Portuguese Primary, English Supplementary
- [ ] **Translate main teaching labels to Portuguese**
  - ❌ Bad: `Represented by: **F**`, `Unit: **newton (N)**`
  - ✅ Good: `Representada por: **F**`, `Unidade: **newton (N)**`
  - **Labels to translate:**
    - "Represented by" → "Representada por"
    - "Unit" → "Unidade"
    - "Measured with" → "Medida com"
    - "Characterized by" → "Caracterizada por"
    - "As a vector quantity" → "Como grandeza vetorial"
    - "or" → "ou", "and" → "e"

- [ ] **Keep English in parentheses as helpful translations**
  - ✅ Good: `**Tipos de Movimento (Movement Types)**`
  - ✅ Good: `Velocidade crescente (increasing)`
  - **Why:** Primary content in Portuguese for students, English as reference

### 5. Formula Formatting
- [ ] **Inline formulas with subscripts need LaTeX notation**
  - ❌ Bad: `F_colisão = -m × (v_colisão / Δt)`
  - ✅ Good: `$$F_{colisão} = -m \times (v_{colisão} / Δt)$$`
  - **Pattern:** Convert `_` to `_{subscript}` in formulas
  - **Math symbols:** `×` → `\times`, `÷` → `\div`

- [ ] **Code block formulas**
  - Can leave in code blocks (preprocessing will handle)
  - Or convert to `$$display math$$` manually if preferred

---

## 🔧 Preprocessing Script Requirements

The `fix_formatting.py` script should handle:

1. **Remove manual numbering** from headers
   - Pattern: `^(#{1,6})\s+\d+(\.\d+)*\.?\s+` → `\1 `

2. **Add blank lines before lists**
   - Detect list items: `^\s*[-*+]\s+` or `^\s*\d+\.\s+`
   - If previous line not blank and not a list item, insert blank line

3. **Convert element lists to bullets**
   - Detect: `^\d+[A-Z][a-z]?\s*–\s*`
   - After "Exemplos" header, add `- ` prefix to each element

4. **Convert inline formulas to LaTeX**
   - Pattern: `**Fórmula[^:]*:**\s+([^\n]+[=×÷±∆Δ][^\n]+)`
   - Replace with: `**Fórmula:**\n\n$$formula$$`
   - Convert subscripts: `([A-Za-z]+)_([A-Za-z]+)` → `\1_{\2}`

---

## 📋 Pre-Generation Verification

Before running PDF generation, check:

- [ ] No headers with manual numbers (`grep -E "^#{1,3} \d+\." MANUAL_FINAL.md`)
- [ ] No lists without blank lines above them
- [ ] All main labels in Portuguese
- [ ] English only in parentheses for supplementary info
- [ ] Element lists have bullet formatting

---

## 🎯 Expected Outcomes

**After proper formatting:**
- ✅ PDF has clean automatic section numbering (1, 1.1, 1.2, 2, 2.1, etc.)
- ✅ All bullet lists render as proper lists (not inline text)
- ✅ Element examples display as readable lists
- ✅ All primary teaching content in Portuguese
- ✅ Formulas render beautifully with LaTeX
- ✅ Math subscripts display correctly (F_{colisão} not F_colisão)

**Page count guidelines:**
- Math manual: ~48 pages (19 topics)
- Sciences manual: ~80 pages (46 topics)
- Physics-Chemistry: ~74 pages (30 topics)

Blank lines increase page count slightly but are necessary for proper rendering.

---

## 🚨 Common Mistakes to Avoid

1. **Don't manually number headers** - Pandoc does this automatically
2. **Don't skip blank lines before lists** - They won't render properly
3. **Don't leave main labels in English** - Students need Portuguese
4. **Don't remove helpful English translations** - Keep in parentheses
5. **Don't forget element list formatting** - They need bullet prefixes
6. **Don't mix manual and automatic numbering** - Choose one (automatic)

---

## 📚 Reference Implementation

See `manuals/physics-chemistry/fix_formatting.py` for complete working example.
