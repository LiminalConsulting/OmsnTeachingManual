# Complete Topic List: O Bichinho do Saber Mathematics (Grades 5-9)

This file lists ALL 49 mathematics topics from O Bichinho do Saber website, organized by grade with suggested topic slugs for file naming.

**Source:** Extracted from `grade_urls.md`
**Format:** `Topic Name` → `topic_slug`
**Usage:** Copy topic name when running `/consolidate-topic` command

---

## Grade 5 (9 topics)

1. **Números naturais** (5) → `numeros_naturais`
2. **Números racionais não negativos** (5) → `numeros_racionais_nao_negativos`
3. **Ângulos, paralelismo e perpendicularidade** (5) → `angulos_paralelismo_perpendicularidade`
4. **Triângulos e quadriláteros** (5) → `triangulos_quadrilateros`
5. **Amplitude de ângulos** (5) → `amplitude_angulos`
6. **Área** (5) → `area_g5`
7. **Expressões algébricas e propriedades das operações** (5) → `expressoes_algebricas_propriedades_g5`
8. **Gráficos cartesianos** (5) → `graficos_cartesianos`
9. **Representação e interpretação de dados** (5) → `representacao_interpretacao_dados_g5`

---

## Grade 6 (12 topics)

1. **Números naturais: números primos e decomposição em fatores primos** (6) → `numeros_primos_decomposicao` ✅ COMPLETED as "numeros_primos"
2. **Potências de expoente natural** (6) → `potencias_expoente_natural`
3. **Números inteiros** (6) → `numeros_inteiros_g6`
4. **Figuras geométricas planas** (6) → `figuras_geometricas_planas`
5. **Isometrias do plano – Rotação e Reflexão** (6) → `isometrias_plano_rotacao_reflexao`
6. **Sólidos geométricos e propriedades** (6) → `solidos_geometricos_propriedades`
7. **Área** (6) → `area_g6`
8. **Volume** (6) → `volume`
9. **Expressões numéricas e propriedades das operações** (6) → `expressoes_numericas_propriedades`
10. **Sequências e regularidades** (6) → `sequencias_regularidades_g6`
11. **Proporcionalidade direta** (6) → `proporcionalidade_direta`
12. **Representação e interpretação de dados** (6) → `representacao_interpretacao_dados_g6`

---

## Grade 7 (10 topics)

1. **Números inteiros – adição e subtração** (7) → `numeros_inteiros_adicao_subtracao`
2. **Números racionais – adição, subtração, percentagem e notação científica** (7) → `numeros_racionais_adicao_subtracao_percentagem`
3. **Sequências e sucessões** (7) → `sequencias_sucessoes`
4. **Expressões algébricas e equações do 1º grau** (7) → `expressoes_algebricas_equacoes_1grau`
5. **Funções e proporcionalidade direta** (7) → `funcoes_proporcionalidade_direta`
6. **Estudo estatístico** (7) → `estudo_estatistico_g7`
7. **Probabilidades** (7) → `probabilidades_g7`
8. **Ângulos, quadriláteros e áreas** (7) → `angulos_quadrilateros_areas`
9. **Figuras semelhantes e critérios de semelhança** (7) → `figuras_semelhantes_semelhanca`
10. **Poliedros regulares, prismas e pirâmides** (7) → `poliedros_prismas_piramides`

---

## Grade 8 (8 topics)

1. **Dízimas finitas e infinitas periódicas** (8) → `dizimas_finitas_infinitas_periodicas`
2. **Operações com números racionais** (8) → `operacoes_numeros_racionais`
3. **Regras das potências** (8) → `regras_potencias`
4. **Raiz quadrada e raiz cúbica** (8) → `raiz_quadrada_cubica`
5. **Notação científica** (8) → `notacao_cientifica`
6. **Funções afim** (8) → `funcoes_afim`
7. **Teorema de Pitágoras** (8) → `teorema_pitagoras`
8. **Vetores, translações e isometrias** (8) → `vetores_translacoes_isometrias`

---

## Grade 9 (10 topics)

1. **Números reais – intervalos, relação de ordem e valores aproximados** (9) → `numeros_reais_intervalos`
2. **Circunferência e lugares geométricos** (9) → `circunferencia_lugares_geometricos`
3. **Áreas e volumes** (9) → `areas_volumes`
4. **Trigonometria** (9) → `trigonometria`
5. **Sequências e regularidades** (9) → `sequencias_regularidades_g9`
6. **Equações do 2º grau** (9) → `equacoes_2grau`
7. **Inequações** (9) → `inequacoes`
8. **Funções (afim, de proporcionalidade inversa e quadrática)** (9) → `funcoes_afim_inversa_quadratica`
9. **Estudo estatístico (histogramas e diagrama de extremos e quartis)** (9) → `estudo_estatistico_histogramas`
10. **Probabilidades** (9) → `probabilidades_g9`

---

## Topics That Appear in Multiple Grades

Some topics appear or are similar across grades - these may be consolidated during processing:

- **Área**: Grades 5, 6 (may consolidate or keep separate as `area_g5` and `area_g6`)
- **Representação e interpretação de dados**: Grades 5, 6
- **Números inteiros**: Grades 6, 7 (different focus - 6 is general, 7 is addition/subtraction)
- **Sequências**: Grades 6, 7, 9 (different names: "regularidades" vs "sucessões")
- **Probabilidades**: Grades 7, 9
- **Estudo estatístico**: Grades 7, 9 (different focus)
- **Funções**: Grades 7, 8, 9 (different types)

**Note:** The consolidation agent will handle these intelligently - if content is similar, it will merge; if different, it will keep separate sections.

---

## Summary Statistics

**Total topics:** 49 topics across all grades
**Grade distribution:**
- Grade 5: 9 topics
- Grade 6: 12 topics
- Grade 7: 10 topics
- Grade 8: 8 topics
- Grade 9: 10 topics

**Expected unique topics after consolidation:** ~40-45 topics
(Some topics appear in multiple grades and will be merged into single files)

---

## Usage Instructions

### For Parallel Processing:

1. Open multiple Claude Code chat sessions (as many as you want to run in parallel)
2. In each session, run: `/consolidate-topic`
3. Copy-paste one topic name from above with its grade number
4. Format: `Topic Name (Grade)`
5. Agent processes that topic through complete pipeline

### Example Commands:

```
/consolidate-topic Números naturais (5)
/consolidate-topic Potências de expoente natural (6)
/consolidate-topic Trigonometria (9)
```

### Progress Tracking:

Check which topics are complete:
```bash
ls -1 topics/clean/*_final.md
```

Or count completed topics:
```bash
ls topics/clean/*_final.md | wc -l
```

---

## Notes

- ✅ marks completed topics
- Topic slugs use snake_case for consistency
- Grade numbers in parentheses indicate which grade(s) to process
- Some topics may naturally merge during consolidation if content overlaps
- Each topic processes independently - safe for parallel execution
