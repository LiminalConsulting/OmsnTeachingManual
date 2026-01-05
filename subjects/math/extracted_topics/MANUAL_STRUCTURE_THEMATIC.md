# Thematic Manual Structure: Mathematics Grades 5-9

This document provides the **hierarchical, thematically organized structure** for the consolidated mathematics manual from O Bichinho do Saber content.

**Purpose:** Cluster topics by mathematical concept rather than by grade, creating a unified manual that spans all 5 years.

**Format:**
- **Main Topics** (not from any specific grade - organizational categories)
- **Subtopics** (from specific grades) → `Grade X, Y, Z`

---

## 1. NÚMEROS (Numbers)

### 1.1 Números Naturais (Natural Numbers)
- Números naturais → Grade 5
- Números naturais: números primos e decomposição em fatores primos → Grade 6
- Múltiplos e divisores → (implied in Grade 5 content)

### 1.2 Números Inteiros (Integers)
- Números inteiros → Grade 6
- Números inteiros – adição e subtração → Grade 7

### 1.3 Números Racionais (Rational Numbers)
- Números racionais não negativos → Grade 5
- Números racionais – adição, subtração, percentagem e notação científica → Grade 7
- Operações com números racionais → Grade 8
- Dízimas finitas e infinitas periódicas → Grade 8

### 1.4 Números Reais (Real Numbers)
- Números reais – intervalos, relação de ordem e valores aproximados → Grade 9
- Raiz quadrada e raiz cúbica → Grade 8

### 1.5 Potências e Notação Científica (Powers and Scientific Notation)
- Potências de expoente natural → Grade 6
- Regras das potências → Grade 8
- Notação científica → Grade 8

---

## 2. ÁLGEBRA (Algebra)

### 2.1 Expressões Algébricas (Algebraic Expressions)
- Expressões algébricas e propriedades das operações → Grade 5
- Expressões numéricas e propriedades das operações → Grade 6
- Expressões algébricas e equações do 1º grau → Grade 7

### 2.2 Sequências e Padrões (Sequences and Patterns)
- Sequências e regularidades → Grades 6, 9
- Sequências e sucessões → Grade 7

### 2.3 Equações e Inequações (Equations and Inequalities)
- Expressões algébricas e equações do 1º grau → Grade 7
- Equações do 2º grau → Grade 9
- Inequações → Grade 9

### 2.4 Funções (Functions)
- Funções e proporcionalidade direta → Grade 7
- Funções afim → Grade 8
- Funções (afim, de proporcionalidade inversa e quadrática) → Grade 9
- Proporcionalidade direta → Grade 6

---

## 3. GEOMETRIA (Geometry)

### 3.1 Elementos Básicos (Basic Elements)
- Ângulos, paralelismo e perpendicularidade → Grade 5
- Amplitude de ângulos → Grade 5

### 3.2 Figuras Planas (Plane Figures)
- Triângulos e quadriláteros → Grade 5
- Figuras geométricas planas → Grade 6
- Ângulos, quadriláteros e áreas → Grade 7
- Circunferência e lugares geométricos → Grade 9

### 3.3 Transformações Geométricas (Geometric Transformations)
- Isometrias do plano – Rotação e Reflexão → Grade 6
- Vetores, translações e isometrias → Grade 8
- Figuras semelhantes e critérios de semelhança → Grade 7

### 3.4 Sólidos Geométricos (Geometric Solids)
- Sólidos geométricos e propriedades → Grade 6
- Poliedros regulares, prismas e pirâmides → Grade 7

### 3.5 Trigonometria (Trigonometry)
- Teorema de Pitágoras → Grade 8
- Trigonometria → Grade 9

---

## 4. MEDIDA (Measurement)

### 4.1 Área (Area)
- Área → Grades 5, 6
- Ângulos, quadriláteros e áreas → Grade 7
- Áreas e volumes → Grade 9

### 4.2 Volume (Volume)
- Volume → Grade 6
- Áreas e volumes → Grade 9

---

## 5. ORGANIZAÇÃO E TRATAMENTO DE DADOS (Data Organization and Treatment)

### 5.1 Representação de Dados (Data Representation)
- Gráficos cartesianos → Grade 5
- Representação e interpretação de dados → Grades 5, 6

### 5.2 Estatística (Statistics)
- Estudo estatístico → Grade 7
- Estudo estatístico (histogramas e diagrama de extremos e quartis) → Grade 9

### 5.3 Probabilidades (Probability)
- Probabilidades → Grades 7, 9

---

## Processing Instructions

### For Each Subtopic:

When running `/consolidate-topic`, use the subtopic name and all grades listed:

**Example 1 - Single grade:**
```
/consolidate-topic Trigonometria (9)
```

**Example 2 - Multiple grades:**
```
/consolidate-topic Área (5, 6)
/consolidate-topic Probabilidades (7, 9)
/consolidate-topic Sequências e regularidades (6, 9)
```

### Consolidated File Naming:

Use the subtopic name for the file:
- `numeros_naturais.md` (consolidates Grade 5 + Grade 6 content)
- `probabilidades.md` (consolidates Grade 7 + Grade 9 content)
- `area.md` (consolidates Grade 5 + Grade 6 content)

### Final Manual Assembly:

After all topics are processed, assemble them following this hierarchical structure:

```
1. NÚMEROS
   1.1 Números Naturais [from numeros_naturais_final.md]
   1.2 Números Inteiros [from numeros_inteiros_final.md]
   ...
2. ÁLGEBRA
   2.1 Expressões Algébricas [from expressoes_algebricas_final.md]
   ...
```

---

## Summary Statistics

**Main Topics:** 5 (Números, Álgebra, Geometria, Medida, Dados)
**Subtopics:** ~30-35 consolidated subtopics
**Original Grade Topics:** 49 topics
**Consolidation Benefit:** ~30% reduction through intelligent clustering

---

## Topic Processing Priority

### High Priority (Foundation Topics):
1. Números Naturais (5, 6)
2. Números Inteiros (6, 7)
3. Números Racionais (5, 7, 8)
4. Expressões Algébricas (5, 6, 7)

### Medium Priority:
5. Geometria Plana (5, 6, 7)
6. Funções (6, 7, 8, 9)
7. Área e Volume (5, 6, 9)

### Lower Priority (Advanced Topics):
8. Trigonometria (8, 9)
9. Equações 2º grau (9)
10. Estatística avançada (9)

---

## Notes

- Topics appearing in multiple grades will be consolidated into single files
- Grade information is preserved in the content metadata
- Main topics (NÚMEROS, ÁLGEBRA, etc.) are organizational - no processing needed
- Subtopics are the actual processing units
- Some subtopics naturally span multiple grades (e.g., Área in 5 & 6)
