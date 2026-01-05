# OMSN Teaching Manual - Project Instructions

## Visualization Color Scheme

For all manim visualizations, use only these colors:
- **Accent 1:** RED = `#FF644E` (OMSN_RED)
- **Accent 2:** BLUE = `#00A2FF` (OMSN_BLUE)

**Light mode (print):** WHITE background, BLACK strokes/text
**Dark mode (digital):** BLACK background, WHITE strokes/text

### Manim Usage
```python
# OMSN Color Scheme
OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

# Create two scene classes: <Name>Light and <Name>Dark
# Light: self.camera.background_color = WHITE, stroke_color = BLACK
# Dark:  self.camera.background_color = BLACK, stroke_color = WHITE
```

### Scene Structure
- **No titles** in graphics - handled by LaTeX figure captions
- Create both `<SceneName>Light` and `<SceneName>Dark` classes
- Use OMSN_RED and OMSN_BLUE for accents (same in both modes)

## Conda Environment

Manim is available in the `manim` conda environment:
```bash
eval "$(/opt/homebrew/Caskroom/miniconda/base/bin/conda shell.zsh hook)"
conda activate manim
```

---

## Tool Selection: Manim vs Image Generation AI

**Use the right tool for each visualization type:**

### Image Generation AI (e.g., GPT-4o, DALL-E, Midjourney)

**Best for:**
- ✅ **3D solids** (cones, pyramids, spheres, cylinders) - cleaner than manim's 3D
- ✅ Aesthetic/conceptual illustrations
- ✅ Diagrams where visual clarity matters more than geometric precision
- ✅ Quick iterations on visual style

**Limitations:**
- ❌ Struggles with precise geometric relationships
- ❌ Cannot reliably construct shapes that must align perfectly (e.g., squares on triangle sides)
- ❌ Labels sometimes garbled or misplaced
- ❌ May hallucinate extra elements

**Prompt tips for Image AI:**
- Keep prompts minimal - let the AI use its training knowledge
- Specify style (white background, black strokes, accent colors)
- Don't over-specify geometric construction steps
- Always request "no title" since LaTeX handles captions

### Manim (Programmatic)

**Best for:**
- ✅ **Precise 2D geometry** (Pythagorean theorem, angle relationships, constructions)
- ✅ Diagrams requiring exact mathematical relationships
- ✅ Consistent style across many figures
- ✅ Animations (if needed later)
- ✅ Reproducible outputs

**Limitations:**
- ❌ 3D rendering can be finicky (wireframes, camera angles)
- ❌ More time to iterate
- ❌ Text rendering sometimes has spacing issues

### Decision Matrix

| Concept Type | Recommended Tool |
|--------------|------------------|
| 3D solids (cone, pyramid, sphere, prism) | Image AI |
| Precise 2D geometry (theorems, constructions) | Manim |
| Transformations (rotation, reflection, translation) | Manim |
| Angle classifications, simple shapes | Either |
| Circle elements, labeled diagrams | Manim |
| Conceptual/aesthetic illustrations | Image AI |

---

## Automated Visualization Workflow

### Overview

```
[Manual MD]
    → Phase 1: AI scans headers, identifies visualizable concepts
    → [User reviews list]
    → Phase 2: N parallel subagents create + iterate + embed
    → [User reviews changes]
    → Phase 3: Build PDF
```

### Phase 1: Concept Discovery

**Goal:** Identify concepts that would benefit from visualization

**Method:**
1. Read only **table of contents / section headers** (first ~100 lines)
2. For promising sections, read **headers + first few lines** only
3. AI identifies visualizable concepts (geometry, 3D solids, graphs, transformations)
4. Output list with:
   - `concept_name` - Portuguese name
   - `concept_slug` - snake_case for filenames
   - `section_path` - where in manual hierarchy
   - `line_number` - approximate location
   - `visual_type` - "2D" or "3D"
   - `brief_description` - what to visualize

**User reviews and approves list before Phase 2**

### Phase 2: Parallel Visualization Creation

**Agent:** `visualization-creator` (see `.claude/agents/visualization-creator.md`)

**Per concept, subagent autonomously:**
1. Check idempotency (skip if image exists)
2. Read relevant section context (~30 lines)
3. Generate manim Python code (Light + Dark classes)
4. Render PNG
5. **View output and iterate if needed** (max 3 attempts)
6. Copy to `subjects/<subject>/manual/images/`
7. Insert markdown figure at correct location
8. Report: SUCCESS / SKIPPED / FLAGGED

**Error handling:**
- 3 successive failures → FLAGGED for manual review, move on

**All subagents run in parallel**

### Phase 3: Review & Build

**User reviews:**
- Changed files / diffs
- Any FLAGGED concepts

**Then:** Single `./generate_pdf.sh` to build final PDF

### Invoking the Workflow

**Phase 1 - Discovery:**
```
"Scan [manual path] for visualizable concepts"
```

**Phase 2 - Creation (after approval):**
```
"Create visualizations for approved concepts [list] in parallel"
```

**Phase 3 - Build:**
```
"Build the PDF"
```

### Manual Single-Concept Pipeline

For creating one visualization manually:

1. Write manim scene in `subjects/math/visualizations/<concept_slug>.py`
2. Render:
   ```bash
   eval "$(/opt/homebrew/Caskroom/miniconda/base/bin/conda shell.zsh hook)" && conda activate manim && manim -qh -s <file>.py <SceneName>Light -o <name>_light.png
   ```
3. View output with Read tool
4. Iterate if needed
5. Copy to manual: `cp subjects/math/visualizations/media/images/.../<name>_light.png subjects/math/manual/images/<name>.png`
6. Insert in markdown: `![Caption](images/<name>.png){width=X%}`
7. Build PDF: `./generate_pdf.sh`
