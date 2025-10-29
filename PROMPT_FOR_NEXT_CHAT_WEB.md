# Prompt for Next Chat: Process Complete Web Curriculum Year-by-Year

## Context

We have an agent-based pipeline to extract Portuguese mathematics curriculum (grades 5-9) from the **O Bichinho do Saber website** and refactor it thematically. The system processes **year-by-year** to enable intelligent topic clustering while avoiding context limits.

**IMPORTANT**: All agents are in English but explicitly preserve original Portuguese content. Translation only happens in the final step.

## Your Task

Process the complete mathematics curriculum using our 5-stage incremental pipeline:

1. **EXTRACT** (per grade): Invoke web-topic-extractor for each topic in grade
2. **CONSOLIDATE** (per topic): Invoke incremental-consolidator to merge into existing or create new
3. **DEDUPLICATE** (per topic): Invoke duplicate-remover for final cleanup
4. **REVIEW** (per topic): Invoke web-quality-reviewer to validate output (NOT quality-reviewer!)
5. **TRANSLATE** (per topic): Invoke translator to create English version

## Year-by-Year Processing Strategy

### Grade 5 (Foundation)
1. Extract all 9 topics from Grade 5
2. Consolidate each topic (creates initial consolidated files)
3. Deduplicate, review, translate

### Grades 6-9 (Incremental Addition)
For each grade:
1. Extract all topics for that grade
2. For each extracted topic:
   - If consolidated file exists → incremental merge
   - If new topic → create consolidated file
3. Deduplicate updated/new files
4. Review and translate

**Advantage:** Topics naturally cluster as similar content is detected during incremental consolidation.

## Files & Infrastructure

### Source URLs (See grade_urls.md)
```
Grade 5: https://www.obichinhodosaber.com/matematica-5o-materia-de-matematica-5o-ano/
Grade 6: https://www.obichinhodosaber.com/matematica-6o-materia-de-matematica-6o-ano/
Grade 7: https://www.obichinhodosaber.com/matematica-7o-materia-de-matematica-7o-ano/
Grade 8: https://www.obichinhodosaber.com/resumos-e-exercicios-de-matematica-8o-ano/
Grade 9: https://www.obichinhodosaber.com/matematica-9o-materia-de-matematica-9o-ano/
```

### Sub-Agents (Already Configured)
```
.claude/agents/web-topic-extractor.md        # Extracts from website by grade/topic
.claude/agents/incremental-consolidator.md   # Merges new grade into existing topic file
.claude/agents/duplicate-remover.md          # Removes marked duplicates
.claude/agents/web-quality-reviewer.md       # Reviews web-based final output (NOT quality-reviewer!)
.claude/agents/translator.md                 # Translates Portuguese to English
```

**CRITICAL:** Use `web-quality-reviewer` agent (NOT `quality-reviewer`). The `quality-reviewer` agent is for the OLD PDF-based curriculum pipeline. The `web-quality-reviewer` agent understands this is O Bichinho do Saber website content.

### Output Structure
```
topics/raw/[topic_slug]_g[5-9].md       # Web extractions (Portuguese)
topics/consolidated/[topic_slug].md     # Consolidated by topic (Portuguese)
topics/clean/[topic_slug]_final.md      # Deduplicated (Portuguese)
topics/clean/[topic_slug]_final_EN.md   # English translations
```

## Detailed Workflow

### Phase 1: Grade 5 Foundation

**Step 1: Extract All Grade 5 Topics (9 topics)**
```
Use web-topic-extractor agent to extract from Grade 5:
1. Números naturais
2. Números racionais não negativos
3. Ângulos, paralelismo e perpendicularidade
4. Triângulos e quadriláteros
5. Amplitude de ângulos
6. Área
7. Expressões algébricas e propriedades das operações
8. Gráficos cartesianos
9. Representação e interpretação de dados

For each topic, output to: topics/raw/[topic_slug]_g5.md
```

**Step 2: Consolidate Each Topic**
```
Use incremental-consolidator agent for each of the 9 topics
(Creates new consolidated file since none exist yet)
Output: topics/consolidated/[topic_slug].md
```

**Step 3: Process Each Topic**
```
For each of the 9 topics:
1. Use duplicate-remover → topics/clean/[topic_slug]_final.md
2. Use web-quality-reviewer (validate web-based output)
3. Use translator → topics/clean/[topic_slug]_final_EN.md
```

### Phase 2: Add Grade 6

**Step 1: Extract All Grade 6 Topics (12 topics)**
```
Use web-topic-extractor for all Grade 6 topics (see grade_urls.md for list)
Output to: topics/raw/[topic_slug]_g6.md
```

**Step 2: Incremental Consolidation**
```
For each Grade 6 topic:
- Use incremental-consolidator to merge into existing consolidated file
- If topic is new (not in Grade 5), creates new consolidated file
- Agent checks if file exists, reads it, compares, marks duplicates, appends
```

**Step 3: Process Updated/New Topics**
```
For topics that were updated or newly created:
1. Use duplicate-remover (update clean file)
2. Use web-quality-reviewer (validate web content)
3. Use translator (update or create English version)
```

### Phases 3-5: Add Grades 7, 8, 9

Repeat Phase 2 process for each remaining grade:
- Extract all topics for grade
- Incrementally consolidate each
- Process updated/new files

## Topic Count Reference

- Grade 5: 9 topics
- Grade 6: 12 topics
- Grade 7: 10 topics
- Grade 8: 8 topics
- Grade 9: 10 topics

**Total raw extractions:** ~49 files
**Consolidated topics:** ~30-40 unique topics (some overlap across grades)

## Progress Tracking

Create/update `web_extraction_progress.md` to track:
```markdown
# Web Extraction Progress

## Grade 5 [✅/⏳/❌]
- [ ] Números naturais
- [ ] Números racionais não negativos
...

## Grade 6 [✅/⏳/❌]
- [ ] Números primos e decomposição
...

[Continue for all grades]

## Consolidated Topics Status
- [ ] numeros_naturais.md [extracted: 5,6,7,8,9 | consolidated | cleaned | translated]
...
```

## Batch Processing Recommendation

Process in batches to maintain quality control:

**Batch 1: Grade 5 Complete (9 topics)**
- Extract → Consolidate → Clean → Review → Translate
- Report completion status

**Batch 2: Grade 6 Complete (12 topics)**
- Extract → Merge → Clean → Review → Translate
- Report which topics were updated vs new

**Batches 3-5: Grades 7-9**
- Same process for each grade

## Important Notes

**Topic Name Variations:**
- Website topic names may differ slightly from grade to grade
- incremental-consolidator agent handles this by content comparison
- Use topic slug naming consistently for files

**Context Efficiency:**
- Each consolidated file = single topic (stays small)
- Agents work with one topic at a time
- No risk of context overflow

**Language Preservation:**
- Portuguese preserved through stages 1-4
- English translation is stage 5 (final step)

**Quality Control:**
- web-quality-reviewer checks each final file (understands web source material)
- Ensures completeness, language consistency, alignment with web-based objectives
- Validates source is O Bichinho do Saber (NOT curriculum PDFs)

## Success Criteria

When all grades are processed:
1. ✅ All ~49 raw extractions created
2. ✅ All ~30-40 unique consolidated topics created
3. ✅ All topics deduplicated and cleaned
4. ✅ All topics reviewed and approved
5. ✅ All topics translated (Portuguese + English versions)
6. ✅ Ready to assemble final thematic manuals

## How to Invoke Sub-Agents

Use natural language to request specific agents:

```
Use the web-topic-extractor agent to extract "Números naturais" from Grade 5
(https://www.obichinhodosaber.com/matematica-5o-materia-de-matematica-5o-ano/)
and save to topics/raw/numeros_naturais_g5.md
```

```
Use the incremental-consolidator agent to merge topics/raw/numeros_naturais_g6.md
into the existing topics/consolidated/numeros_naturais.md file
```

The agents automatically activate when mentioned by name with task description.

---

**Ready to begin!** Start with Grade 5, Batch 1.
