# Thematic Manual Structure: Natural Sciences Grades 7-9

This document provides the **hierarchical, thematically organized structure** for the consolidated natural sciences manual from O Bichinho do Saber content.

**Purpose:** Cluster topics by scientific domain rather than by grade, creating a unified manual that spans all 3 years (grades 7-9).

**Format:**
- **Main Topics** (organizational categories - not from specific grades)
- **Subtopics** (from specific grades) → `Grade X, Y, Z`

---

## 1. GEOLOGIA (Geology & Earth Sciences)

### 1.1 Paisagens e Estrutura da Terra (Landscapes & Earth Structure)
- Paisagens geológicas → Grade 7
- Estrutura interna da Terra → Grade 7
- Subsistemas da Terra – A Terra como sistema → Grade 8

### 1.2 Rochas e Minerais (Rocks & Minerals)
- Rochas e minerais → Grade 7
- Rochas sedimentares → Grade 7
- Rochas magmáticas e rochas metamórficas → Grade 7
- Ciclo das rochas → Grade 7

### 1.3 Dinâmica da Terra (Earth Dynamics)
- Teoria da Deriva Continental → Grade 7
- Teoria da Tectónica de Placas → Grade 7
- Dobras e Falhas → Grade 7
- Vulcanismo → Grade 7
- Sismos → Grade 7

### 1.4 História da Terra (Earth History)
- Fósseis e datação de rochas → Grade 7
- Etapas da História da Terra → Grade 7

### 1.5 Sustentabilidade Geológica (Geological Sustainability)
- Exploração sustentável das rochas → Grade 7
- O contributo do conhecimento geológico → Grade 7

---

## 2. BIOLOGIA CELULAR E ECOLOGIA (Cell Biology & Ecology)

### 2.1 Condições para a Vida (Conditions for Life)
- Condições da Terra que permitem a existência de vida → Grade 8

### 2.2 Organização Celular (Cell Organization)
- O microscópio → Grade 8
- A célula e níveis de organização biológica → Grade 8

### 2.3 Ecossistemas (Ecosystems)
- Níveis de organização dos ecossistemas → Grade 8
- Fatores abióticos (influência do meio nos seres vivos) → Grade 8
- Fatores bióticos (relações entre os seres vivos) → Grade 8
- Cadeias alimentares e ciclos da matéria → Grade 8
- Sucessões ecológicas → Grade 8

---

## 3. SUSTENTABILIDADE E GESTÃO AMBIENTAL (Sustainability & Environmental Management)

### 3.1 Desenvolvimento Sustentável (Sustainable Development)
- Desenvolvimento sustentável → Grade 8
- Recursos naturais → Grade 8

### 3.2 Proteção Ambiental (Environmental Protection)
- Catástrofes → Grade 8
- Medidas de proteção dos ecossistemas → Grade 8
- Proteção e conservação da natureza → Grade 8

### 3.3 Gestão de Território e Recursos (Territory & Resource Management)
- Ordenamento e gestão do território → Grade 8
- Gestão de resíduos e da água → Grade 8

---

## 4. BIOLOGIA HUMANA (Human Biology)

### 4.1 Saúde e Organização do Corpo (Health & Body Organization)
- Saúde individual e comunitária → Grade 9
- Níveis estruturais do corpo humano → Grade 9

### 4.2 Nutrição e Digestão (Nutrition & Digestion)
- Alimentos, nutrientes e alimentação saudável → Grade 9
- Sistema digestivo → Grade 9

### 4.3 Sistema Circulatório e Imunitário (Circulatory & Immune System)
- Sangue → Grade 9
- Sistema cardiovascular → Grade 9
- Sistema linfático → Grade 9

### 4.4 Sistema Respiratório (Respiratory System)
- Sistema respiratório → Grade 9
- Suporte básico de vida → Grade 9

### 4.5 Sistema Excretor (Excretory System)
- Sistema excretor: sistema urinário → Grade 9
- Sistema excretor: pele → Grade 9

### 4.6 Coordenação e Regulação (Coordination & Regulation)
- Sistema neuro-hormonal: sistema nervoso → Grade 9
- Sistema neuro-hormonal: sistema hormonal → Grade 9

### 4.7 Reprodução e Hereditariedade (Reproduction & Heredity)
- Sistema reprodutor → Grade 9
- Hereditariedade → Grade 9

---

## Processing Instructions

### For Each Subtopic:

When running topic extraction, use the subtopic name and all grades listed:

**Example 1 - Single grade:**
```
Topic: Vulcanismo (Grade 7)
```

**Example 2 - Multiple grades (if applicable):**
```
Topic: Subsistemas da Terra (Grade 8)
```

### Consolidated File Naming:

Use the subtopic name for the file (snake_case):
- `paisagens_geologicas.md`
- `sistema_digestivo.md`
- `teoria_tectonica_placas.md`

### Final Manual Assembly:

After all topics are processed, assemble them following this hierarchical structure:

```
1. GEOLOGIA
   1.1 Paisagens e Estrutura da Terra
       - Paisagens geológicas [from paisagens_geologicas.md]
       - Estrutura interna da Terra [from estrutura_interna_terra.md]
       - Subsistemas da Terra [from subsistemas_terra.md]
   1.2 Rochas e Minerais
       - Rochas e minerais [from rochas_minerais.md]
       ...
2. BIOLOGIA CELULAR E ECOLOGIA
   ...
```

---

## Summary Statistics

**Main Topics:** 4 (Geologia, Biologia Celular e Ecologia, Sustentabilidade, Biologia Humana)
**Subtopics:** 46 individual topics
**Grade Distribution:**
- Grade 7: 15 topics (Geology focus)
- Grade 8: 16 topics (Ecology focus)
- Grade 9: 15 topics (Human biology focus)

---

## Topic Processing Priority

### High Priority (Foundation Topics):
1. Estrutura interna da Terra (Grade 7)
2. A célula e níveis de organização biológica (Grade 8)
3. Saúde individual e comunitária (Grade 9)
4. Níveis estruturais do corpo humano (Grade 9)

### Medium Priority:
5. Teoria da Tectónica de Placas (Grade 7)
6. Ecossistemas (Grade 8)
7. Human body systems (Grade 9)

### Lower Priority (Specialized Topics):
8. Exploração sustentável (Grade 7)
9. Gestão territorial (Grade 8)
10. Suporte básico de vida (Grade 9)

---

## Notes

- Topics are organized by scientific domain for pedagogical coherence
- Most topics appear in only one grade (unlike math where topics span multiple grades)
- Grade 7-9 curriculum shows clear progression: Earth → Environment → Human
- Some topics may be naturally related but taught separately (e.g., cell biology → human systems)
- All 46 topics will be extracted individually
