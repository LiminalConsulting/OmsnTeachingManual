# Prompt for Next Chat: Batch Process Remaining Topics

## Context

We've successfully created an agent-based pipeline to refactor the Portuguese mathematics curriculum (grades 5-9) from grade-organized PDFs into a thematically-organized teaching manual. The infrastructure is complete and tested.

**IMPORTANT**: All agents are defined in **English** but explicitly instructed to **preserve the original language** of source documents (Portuguese) during the reorganization process. Translation only happens in the final step.

## Your Task

Process the remaining mathematics topics using our established 5-stage pipeline:

1. **EXTRACT**: Invoke topic-extractor sub-agent for each grade (5-9)
2. **CONSOLIDATE**: Invoke topic-consolidator sub-agent to merge grades
3. **DEDUPLICATE**: Invoke duplicate-remover sub-agent for final cleanup
4. **REVIEW**: Invoke quality-reviewer sub-agent to validate output
5. **TRANSLATE**: Invoke translator sub-agent to create English version

**NOTE**: "Números primos" has already been completed as a proof-of-concept. Skip this topic and start with the remaining ~39 topics.

## How to Invoke Sub-Agents

Use natural language to request specific sub-agents. Example:

```
Use the topic-extractor sub-agent to extract "Múltiplos e divisores" from
text_versions/grade5_math.txt and save to topics/raw/multiples_divisors_g5.md
```

The agents will automatically activate when you mention them by name and describe the task.

## Batch Processing Strategy (Option B)

Process **5-10 topics at a time** in batches. After each batch:
- Report completion status
- Show sample output from one topic for quality validation
- Wait for approval before proceeding to next batch

This allows for quality control without overwhelming the workflow.

## Files & Infrastructure (Already Created)

### Text Versions (Ready to Use)
```
text_versions/grade5_math.txt (140KB)
text_versions/grade6_math.txt (128KB)
text_versions/grade7_math.txt (154KB)
text_versions/grade8_math.txt (134KB)
text_versions/grade9_math.txt (132KB)
```

### Sub-Agents (Already Configured)
```
.claude/agents/topic-extractor.md      # Extracts topic from single grade text file
.claude/agents/topic-consolidator.md   # Merges extractions from all 5 grades
.claude/agents/duplicate-remover.md    # Removes marked duplicates conservatively
.claude/agents/quality-reviewer.md     # Reviews final output for quality issues
.claude/agents/translator.md           # Translates Portuguese final to English
```

**Agent Features:**
- All agents written in English for clarity
- First 4 agents: Explicit "PRESERVE ORIGINAL LANGUAGE" instructions
- topic-extractor uses table of contents + offset/limit for efficient reading
- quality-reviewer checks language consistency, completeness, and alignment
- translator creates English version as final step

### Progress Tracker
```
topic_index.md  # Contains ~40 topics to process
```

### Output Structure
```
topics/raw/[topic]_g[5-9].md       # Extraction outputs (Portuguese)
topics/consolidated/[topic].md     # Consolidated outputs (Portuguese)
topics/clean/[topic]_final.md      # Final deduplicated versions (Portuguese)
topics/clean/[topic]_final_EN.md   # English translations
```

## Topic List (From topic_index.md)

### NÚMEROS (Numbers) - ~12 topics
- [✅] Números primos (COMPLETE - skip this one)
- [ ] Múltiplos e divisores
- [ ] Potências
- [ ] Frações equivalentes
- [ ] Percentagem
- [ ] Comparação e ordenação
- [ ] Valores aproximados
- [ ] Adição e subtração de frações
- [ ] Multiplicação entre naturais e frações
- [ ] Multiplicação com decimais
- [ ] Divisão com decimais
- [ ] Cálculo mental

### ÁLGEBRA - ~5 topics
- [ ] Regularidades em sequências
- [ ] Sequências de crescimento
- [ ] Leis de formação
- [ ] Expressões algébricas com letras
- [ ] Expressões algébricas equivalentes

### DADOS - ~11 topics
- [ ] Questões estatísticas
- [ ] Fontes e métodos de recolha de dados
- [ ] Questionários
- [ ] Tabela de frequências
- [ ] Gráficos circulares
- [ ] Gráficos de barras
- [ ] Gráficos de barras justapostas
- [ ] Análise crítica de gráficos
- [ ] Resumo dos dados - média
- [ ] Interpretação e conclusão
- [ ] Comunicação e divulgação de um estudo
- [ ] Probabilidades

### GEOMETRIA E MEDIDA - ~12 topics
- [ ] Retas, semirretas e segmentos de reta
- [ ] Posição relativa de retas
- [ ] Amplitude de um ângulo
- [ ] Construção de ângulos
- [ ] Classificação de triângulos
- [ ] Construção de triângulos
- [ ] Critérios de congruência de triângulos
- [ ] Equivalência de figuras planas
- [ ] Área do paralelogramo
- [ ] Área do triângulo
- [ ] Propriedades de poliedros
- [ ] Planificações de poliedros

## Workflow for Each Topic

### Example: Process "Frações equivalentes"

**Step 1: Extract from all 5 grades**

Invoke the topic-extractor sub-agent 5 times (can be done in sequence or requesting all at once):

```
Use the topic-extractor sub-agent to extract "Frações equivalentes" from:
- text_versions/grade5_math.txt → topics/raw/fractions_equiv_g5.md
- text_versions/grade6_math.txt → topics/raw/fractions_equiv_g6.md
- text_versions/grade7_math.txt → topics/raw/fractions_equiv_g7.md
- text_versions/grade8_math.txt → topics/raw/fractions_equiv_g8.md
- text_versions/grade9_math.txt → topics/raw/fractions_equiv_g9.md
```

**Step 2: Consolidate**

```
Use the topic-consolidator sub-agent to merge all fractions_equiv_g[5-9].md files
into topics/consolidated/fractions_equiv.md
```

**Step 3: Deduplicate**

```
Use the duplicate-remover sub-agent to clean topics/consolidated/fractions_equiv.md
and output to topics/clean/fractions_equiv_final.md
```

**Step 4: Quality Review**

```
Use the quality-reviewer sub-agent to review topics/clean/fractions_equiv_final.md
and check for language consistency, completeness, and alignment with objectives
```

**Step 5: Translate to English**

```
Use the translator sub-agent to translate topics/clean/fractions_equiv_final.md
to English and save as topics/clean/fractions_equiv_final_EN.md
```

**Step 6: Update Progress**

Mark "Frações equivalentes" with [✅] in topic_index.md

## Important Notes

**Topic Keywords**: Some topics may have different Portuguese names or be split across sections. Use context clues and grep to locate content.

**Missing Topics**: Like "Números primos", some topics may not appear in all grades. Agents should handle this gracefully (already tested).

**Quality Preservation**: Agents are configured to preserve ALL detail from source PDFs. Only exact duplicates are removed. Portuguese content is preserved through steps 1-4, then translated to English in step 5.

**Table of Contents Strategy**: The topic-extractor uses the table of contents in each text file to identify exact line numbers, then uses Read with offset/limit to extract only the necessary lines. This avoids context limit issues.

**Translation**: The final step creates an English translation of the deduplicated content. This gives you both versions side-by-side: `[topic]_final.md` (Portuguese) and `[topic]_final_EN.md` (English).

**Progress Tracking**: Update topic_index.md after each batch completion.

## Suggested First Batch (5 topics)

Start with these NÚMEROS topics:
1. Múltiplos e divisores
2. Potências
3. Frações equivalentes
4. Percentagem
5. Comparação e ordenação

After completing this batch, show me:
- Updated topic_index.md status
- One sample output (e.g., fractions_equiv_final.md preview)
- Batch statistics (files created, total lines)

Then await approval before proceeding to next batch.

## Success Criteria

When all ~39 remaining topics are processed (remember: Números primos is already done):
1. All topic_index.md items marked [✅]
2. All topics have both Portuguese and English files in `topics/clean/`
3. Each topic has: `[topic]_final.md` (Portuguese) and `[topic]_final_EN.md` (English)
4. Ready to assemble into final manuals (Portuguese and English versions)

Let me know when you're ready to begin!
