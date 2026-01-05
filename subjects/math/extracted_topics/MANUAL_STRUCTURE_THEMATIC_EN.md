# Thematic Manual Structure: Mathematics Grades 5-9

This document provides the **hierarchical, thematically organized structure** for the consolidated mathematics manual from O Bichinho do Saber content.

**Purpose:** Cluster topics by mathematical concept rather than by grade, creating a unified manual that spans all 5 years.

**Format:**
- **Main Topics** (not from any specific grade - organizational categories)
- **Subtopics** (from specific grades) → `Grade X, Y, Z`

---

## 1. NUMBERS

### 1.1 Natural Numbers
- Natural numbers → Grade 5
- Natural numbers: prime numbers and decomposition into prime factors → Grade 6
- Multiples and divisors → (implied in Grade 5 content)

### 1.2 Integers
- Integers → Grade 6
- Integers – addition and subtraction → Grade 7

### 1.3 Rational Numbers
- Non-negative rational numbers → Grade 5
- Rational numbers – addition, subtraction, percentage and scientific notation → Grade 7
- Operations with rational numbers → Grade 8
- Finite and infinite periodic decimals → Grade 8

### 1.4 Real Numbers
- Real numbers – intervals, order relations and approximate values → Grade 9
- Square root and cube root → Grade 8

### 1.5 Powers and Scientific Notation
- Powers with natural exponents → Grade 6
- Rules of powers → Grade 8
- Scientific notation → Grade 8

---

## 2. ALGEBRA

### 2.1 Algebraic Expressions
- Algebraic expressions and properties of operations → Grade 5
- Numerical expressions and properties of operations → Grade 6
- Algebraic expressions and first-degree equations → Grade 7

### 2.2 Sequences and Patterns
- Sequences and regularities → Grades 6, 9
- Sequences and successions → Grade 7

### 2.3 Equations and Inequalities
- Algebraic expressions and first-degree equations → Grade 7
- Second-degree equations → Grade 9
- Inequalities → Grade 9

### 2.4 Functions
- Functions and direct proportionality → Grade 7
- Linear functions → Grade 8
- Functions (linear, inverse proportionality and quadratic) → Grade 9
- Direct proportionality → Grade 6

---

## 3. GEOMETRY

### 3.1 Basic Elements
- Angles, parallelism and perpendicularity → Grade 5
- Angle amplitude → Grade 5

### 3.2 Plane Figures
- Triangles and quadrilaterals → Grade 5
- Plane geometric figures → Grade 6
- Angles, quadrilaterals and areas → Grade 7
- Circumference and geometric loci → Grade 9

### 3.3 Geometric Transformations
- Plane isometries – Rotation and Reflection → Grade 6
- Vectors, translations and isometries → Grade 8
- Similar figures and similarity criteria → Grade 7

### 3.4 Geometric Solids
- Geometric solids and properties → Grade 6
- Regular polyhedra, prisms and pyramids → Grade 7

### 3.5 Trigonometry
- Pythagorean theorem → Grade 8
- Trigonometry → Grade 9

---

## 4. MEASUREMENT

### 4.1 Area
- Area → Grades 5, 6
- Angles, quadrilaterals and areas → Grade 7
- Areas and volumes → Grade 9

### 4.2 Volume
- Volume → Grade 6
- Areas and volumes → Grade 9

---

## 5. DATA ORGANIZATION AND TREATMENT

### 5.1 Data Representation
- Cartesian graphs → Grade 5
- Data representation and interpretation → Grades 5, 6

### 5.2 Statistics
- Statistical study → Grade 7
- Statistical study (histograms and box-and-whisker plots) → Grade 9

### 5.3 Probability
- Probability → Grades 7, 9

---

## Processing Instructions

### For Each Subtopic:

When running `/consolidate-topic`, use the subtopic name and all grades listed:

**Example 1 - Single grade:**
```
/consolidate-topic Trigonometry (9)
```

**Example 2 - Multiple grades:**
```
/consolidate-topic Area (5, 6)
/consolidate-topic Probability (7, 9)
/consolidate-topic Sequences and regularities (6, 9)
```

### Consolidated File Naming:

Use the subtopic name for the file:
- `natural_numbers.md` (consolidates Grade 5 + Grade 6 content)
- `probability.md` (consolidates Grade 7 + Grade 9 content)
- `area.md` (consolidates Grade 5 + Grade 6 content)

### Final Manual Assembly:

After all topics are processed, assemble them following this hierarchical structure:

```
1. NUMBERS
   1.1 Natural Numbers [from natural_numbers_final.md]
   1.2 Integers [from integers_final.md]
   ...
2. ALGEBRA
   2.1 Algebraic Expressions [from algebraic_expressions_final.md]
   ...
```

---

## Summary Statistics

**Main Topics:** 5 (Numbers, Algebra, Geometry, Measurement, Data)
**Subtopics:** ~30-35 consolidated subtopics
**Original Grade Topics:** 49 topics
**Consolidation Benefit:** ~30% reduction through intelligent clustering

---

## Topic Processing Priority

### High Priority (Foundation Topics):
1. Natural Numbers (5, 6)
2. Integers (6, 7)
3. Rational Numbers (5, 7, 8)
4. Algebraic Expressions (5, 6, 7)

### Medium Priority:
5. Plane Geometry (5, 6, 7)
6. Functions (6, 7, 8, 9)
7. Area and Volume (5, 6, 9)

### Lower Priority (Advanced Topics):
8. Trigonometry (8, 9)
9. Second-degree equations (9)
10. Advanced statistics (9)

---

## Notes

- Topics appearing in multiple grades will be consolidated into single files
- Grade information is preserved in the content metadata
- Main topics (NUMBERS, ALGEBRA, etc.) are organizational - no processing needed
- Subtopics are the actual processing units
- Some subtopics naturally span multiple grades (e.g., Area in 5 & 6)
