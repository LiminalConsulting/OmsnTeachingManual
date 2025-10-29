---
description: Process ALL subtopics from MANUAL_STRUCTURE_THEMATIC.md in parallel using topic-copier agents
---

# Process All Topics - Simplified Pipeline

This command reads the thematic manual structure and spawns parallel topic-copier agents to fetch and consolidate all topics from O Bichinho do Saber website.

## Your Task

Read `MANUAL_STRUCTURE_THEMATIC.md` and process every subtopic listed there by invoking the `topic-copier` sub-agent in parallel.

## Strategy

### 1. Read the Manual Structure

Read the file: `/Users/davidrug/OMSN/OmsnTeachingManual/MANUAL_STRUCTURE_THEMATIC.md`

This file contains the hierarchical structure with all subtopics and their grade coverage.

### 2. Extract All Subtopics

Parse the file to find all subtopics with grade information. Format:
```
### X.Y Subtopic Name
- Subtopic Name → Grade X
- Subtopic Name → Grades X, Y, Z
```

Examples:
- "Números Naturais → Grade 5" AND "Números naturais: números primos... → Grade 6"
  → Process as: "Números naturais (5, 6)"
- "Probabilidades → Grades 7, 9"
  → Process as: "Probabilidades (7, 9)"
- "Trigonometria → Grade 9"
  → Process as: "Trigonometria (9)"

### 3. Invoke topic-copier Agents in Parallel

For EACH subtopic, invoke the topic-copier sub-agent:

```
Use the topic-copier agent to process "[Subtopic Name] (Grades: X, Y, Z)"
Output: topics/[topic_slug].md
```

**IMPORTANT:** Invoke ALL topic-copier agents AT ONCE (in parallel) by making multiple Task tool calls in a single message. This enables maximum parallelization.

### 4. Track Progress

As agents complete, track which topics are done:
- ✅ Successfully copied
- ⚠️ Errors or issues
- ⏳ Still processing

## Expected Subtopics (from MANUAL_STRUCTURE_THEMATIC.md)

### NÚMEROS
1. Números Naturais (5, 6)
2. Números Inteiros (6, 7)
3. Números Racionais (5, 7, 8)
4. Números Reais (9)
5. Potências e Notação Científica (6, 8)

### ÁLGEBRA
6. Expressões Algébricas (5, 6, 7)
7. Sequências e Padrões (6, 7, 9)
8. Equações e Inequações (7, 9)
9. Funções (6, 7, 8, 9)

### GEOMETRIA
10. Elementos Básicos (5)
11. Figuras Planas (5, 6, 7, 9)
12. Transformações Geométricas (6, 7, 8)
13. Sólidos Geométricos (6, 7)
14. Trigonometria (8, 9)

### MEDIDA
15. Área (5, 6, 7, 9)
16. Volume (6, 9)

### DADOS
17. Representação de Dados (5, 6)
18. Estatística (7, 9)
19. Probabilidades (7, 9)

**Total:** ~19 consolidated subtopics (instead of 49 individual grade topics!)

## Final Report

After all topic-copier agents complete, provide:

### 1. Completion Summary
```
✅ Successfully processed: [X] topics
⚠️ Issues encountered: [Y] topics (list them)
📁 Files created: topics/*.md
```

### 2. Files Created
List all markdown files created in `topics/` directory:
```bash
ls -1 topics/*.md
```

### 3. Next Steps
The topics are now ready for final manual assembly:
1. Concatenate topic files following MANUAL_STRUCTURE_THEMATIC.md hierarchy
2. Add section headers (1. NÚMEROS, 2. ÁLGEBRA, etc.)
3. Result: Single unified manual spanning all grades 5-9

## Error Handling

- If a topic-copier agent fails, note it but continue with others
- If a topic isn't found on website, agent will note this in output file
- All errors should be reported in final summary

## Important Notes

**Parallel Execution:**
- Spawn ALL topic-copier agents at once (single message with ~19 Task calls)
- Each agent works independently on one topic
- No file conflicts (each writes to different file)

**No Post-Processing Needed:**
- No consolidation stage
- No deduplication stage
- Just copy-paste from website → markdown files

**Grade Progression Preserved:**
- Each topic file shows how concept develops across grades
- Grade 5 section → Grade 6 section → etc.
- Natural teaching progression maintained

---

**Ready to process all topics!** Read MANUAL_STRUCTURE_THEMATIC.md and spawn all topic-copier agents in parallel.
