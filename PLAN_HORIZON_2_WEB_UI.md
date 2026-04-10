# Horizon 2: GitHub Pages Download Site + Cloudflare Image Upload UI

**Goal:** Send Ivone (or any client) a single link. They see a clean page listing all PDFs
to download. They can also drag-and-drop an image to add it to a manual — no coding required.
Updated PDFs appear automatically a few minutes later.

**Prerequisite:** Horizon 1 complete. All PDFs build cleanly from source.

**Note on GitHub Actions:** The auto-build pipeline is already live (set up in Phase 0 of
Horizon 1). This horizon only needs the GitHub Pages site and the Cloudflare Worker.

---

## Part A: GitHub Actions Auto-Build (ALREADY DONE — see Phase 0 of Horizon 1)

This is the foundation. Without it, the web UI has nowhere to trigger builds.

### What it does

On every push to `main`, GitHub Actions:
1. Installs pandoc + xelatex (via apt or a pre-built action)
2. Runs all `generate_*.sh` scripts for all subjects
3. Commits the regenerated PDFs back to the repo
4. (Optional) Posts a summary comment if triggered by a PR or issue

### Workflow file location

`.github/workflows/build-manuals.yml`

### Implementation

```yaml
name: Build Manuals

on:
  push:
    branches: [main]
  workflow_dispatch:  # allows manual trigger and API trigger
    inputs:
      subject:
        description: 'Subject to rebuild (math|physics|sciences|history|all)'
        default: 'all'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc texlive-xetex texlive-lang-portuguese \
            ghostscript poppler-utils

      - name: Build manuals
        run: bash build_all.sh ${{ github.event.inputs.subject || 'all' }}

      - name: Commit rebuilt PDFs
        run: |
          git config user.name "OMSN Build Bot"
          git config user.email "build@omsn.pt"
          git add -A "*.pdf"
          git diff --staged --quiet || git commit -m "Auto-rebuild PDFs [skip ci]"
          git push
```

**Note:** The `[skip ci]` in the commit message prevents the commit from triggering
another build loop.

**Cache the LaTeX install** to speed up subsequent builds (from ~8min to ~2min):
```yaml
      - name: Cache LaTeX packages
        uses: actions/cache@v4
        with:
          path: /usr/share/texmf
          key: texlive-${{ runner.os }}-v1
```

### Test it

After creating the workflow file, push any trivial change and watch the Actions tab.
Confirm all PDFs regenerate and are committed back.

---

## Part B: Cloudflare Worker Image Upload UI

This adds a real drag-and-drop web interface. The person visits a GitHub Pages URL,
drops an image, fills a simple form, clicks submit — and a few minutes later the
PDF is updated.

### Architecture

```
[GitHub Pages — static HTML/JS]
        ↓ (fetch POST with image + metadata)
[Cloudflare Worker — free tier, ~50 lines JS]
        ↓ (GitHub API: create blob, update file, commit)
[GitHub repo — image committed to images/]
        ↓ (push triggers GitHub Actions)
[GitHub Actions — regenerates PDFs, commits back]
        ↓
[GitHub Pages — updated PDF available for download]
```

### Step 1: GitHub Pages upload UI

Create `docs/add-image.html` in the repo. GitHub Pages serves it at
`https://projectliminality.github.io/OmsnTeachingManual/add-image.html`

**UI elements:**
- Drag-and-drop zone (or click to select) for image file
- Dropdown: which subject (Math / Physics-Chemistry / Natural Sciences / History & Geography)
- Dropdown: which section (populated from the manual's chapter list)
- Text field: caption (optional)
- Submit button
- Status area: "Uploading... ✅ Image added. Build started. Check back in ~5 minutes."
- Link to the PDF download once build completes

**Key UX principles:**
- No login required to use the form — the Cloudflare Worker holds the GitHub token server-side
- The form is in Portuguese (primary audience)
- After submit, show a direct link to the GitHub Actions run so they can watch progress

```html
<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>Adicionar Imagem ao Manual</title>
  <style>
    body { font-family: sans-serif; max-width: 600px; margin: 4rem auto; padding: 1rem; }
    .drop-zone { border: 2px dashed #aaa; border-radius: 8px; padding: 3rem; text-align: center;
                 cursor: pointer; transition: background 0.2s; }
    .drop-zone.dragover { background: #f0f8ff; border-color: #0066cc; }
    select, input, textarea { width: 100%; margin: 0.5rem 0 1rem; padding: 0.5rem;
                               font-size: 1rem; border: 1px solid #ccc; border-radius: 4px; }
    button { background: #0066cc; color: white; border: none; padding: 0.75rem 2rem;
             font-size: 1rem; border-radius: 4px; cursor: pointer; }
    button:disabled { background: #aaa; }
    #status { margin-top: 1rem; padding: 1rem; border-radius: 4px; display: none; }
    .success { background: #d4edda; color: #155724; }
    .error { background: #f8d7da; color: #721c24; }
  </style>
</head>
<body>
  <h1>Adicionar Imagem ao Manual</h1>
  <p>Arrasta uma imagem para a área abaixo ou clica para selecionar.</p>

  <div class="drop-zone" id="dropZone">
    <p>📁 Arrasta a imagem aqui</p>
    <input type="file" id="fileInput" accept="image/*" style="display:none">
    <p id="fileName" style="color:#666"></p>
  </div>

  <label>Disciplina</label>
  <select id="subject">
    <option value="math">Matemática</option>
    <option value="physics">Físico-Química</option>
    <option value="sciences">Ciências Naturais</option>
    <option value="history">História e Geografia</option>
  </select>

  <label>Capítulo / Secção</label>
  <input type="text" id="section" placeholder="Ex: 3.2 Figuras Planas">

  <label>Legenda (opcional)</label>
  <input type="text" id="caption" placeholder="Ex: Tipos de triângulos">

  <button id="submitBtn" disabled>Enviar Imagem</button>
  <div id="status"></div>

  <script>
    const WORKER_URL = 'https://omsn-image-upload.YOUR_SUBDOMAIN.workers.dev';
    // ... drag/drop logic, file reading as base64, fetch POST to Worker
    // ... on success: show status with link to Actions run
  </script>
</body>
</html>
```

### Step 2: Cloudflare Worker

Create a new Cloudflare Worker at `workers.cloudflare.com` (free tier: 100k req/day).

The Worker receives the POST, uses the GitHub API to:
1. Create an image blob in the repo
2. Place it in `subjects/{subject}/manual/images/{filename}`
3. Update `MANUAL_FINAL_PRINT.md` to insert the image reference at the specified section
4. Commit with message: `Add image: {filename} to {subject}/{section}`
5. Trigger `workflow_dispatch` on the build workflow for the specific subject
6. Return the GitHub Actions run URL to the frontend

```javascript
export default {
  async fetch(request, env) {
    if (request.method !== 'POST') return new Response('Method not allowed', { status: 405 });

    const { imageBase64, filename, subject, section, caption } = await request.json();

    const GITHUB_TOKEN = env.GITHUB_TOKEN;  // stored as Worker secret
    const REPO = 'ProjectLiminality/OmsnTeachingManual';
    const BASE = 'https://api.github.com';
    const headers = {
      'Authorization': `Bearer ${GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',
    };

    // 1. Upload image blob to repo
    const imagePath = `subjects/${subject}/manual/images/${filename}`;
    await fetch(`${BASE}/repos/${REPO}/contents/${imagePath}`, {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        message: `Add image: ${filename} to ${subject}/${section}`,
        content: imageBase64,
      }),
    });

    // 2. Read current manual source, insert image reference after section heading
    const subjectMap = {
      math: 'subjects/math/manual/MANUAL_FINAL_PRINT.md',
      physics: 'subjects/physics-chemistry/manual/MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md',
      sciences: 'subjects/sciences/manual/MANUAL_FINAL_SCIENCES_PRINT.md',
      history: 'subjects/history-geography/manual/MANUAL_FINAL_HISTORY_GEOGRAPHY_PRINT.md',
    };

    const manualPath = subjectMap[subject];
    const fileResp = await fetch(`${BASE}/repos/${REPO}/contents/${manualPath}`, { headers });
    const fileData = await fileResp.json();
    const content = atob(fileData.content.replace(/\n/g, ''));
    const sha = fileData.sha;

    // Insert image after matching section heading
    const imageMarkdown = `\n![${caption || filename}](images/${filename})\n`;
    const updated = content.replace(
      new RegExp(`(## ${section.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}[^\n]*\n)`),
      `$1${imageMarkdown}`
    );

    // 3. Commit updated manual
    await fetch(`${BASE}/repos/${REPO}/contents/${manualPath}`, {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        message: `Place image ${filename} at section ${section}`,
        content: btoa(updated),
        sha,
      }),
    });

    // 4. Trigger build workflow for this subject
    const triggerResp = await fetch(
      `${BASE}/repos/${REPO}/actions/workflows/build-manuals.yml/dispatches`,
      {
        method: 'POST',
        headers,
        body: JSON.stringify({ ref: 'main', inputs: { subject } }),
      }
    );

    // 5. Get the run URL
    await new Promise(r => setTimeout(r, 2000));
    const runsResp = await fetch(
      `${BASE}/repos/${REPO}/actions/runs?per_page=1`,
      { headers }
    );
    const runs = await runsResp.json();
    const runUrl = runs.workflow_runs?.[0]?.html_url || `https://github.com/${REPO}/actions`;

    return new Response(JSON.stringify({ success: true, runUrl }), {
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    });
  }
};
```

**GitHub token permissions needed:** `contents: write`, `actions: write`
Create a fine-grained Personal Access Token scoped to this repo only.
Store it as a Worker secret: `wrangler secret put GITHUB_TOKEN`

### Step 3: Deploy

```bash
# Install Wrangler (Cloudflare CLI)
npm install -g wrangler

# Login
wrangler login

# Create worker
wrangler init omsn-image-upload
# paste the worker code into src/index.js

# Add the GitHub token as a secret
wrangler secret put GITHUB_TOKEN

# Deploy
wrangler deploy
```

Update `WORKER_URL` in `add-image.html` with the deployed worker URL.

### Step 4: Enable GitHub Pages

In repo Settings → Pages → Source: `main` branch, `/docs` folder.
The upload UI is then live at `https://projectliminality.github.io/OmsnTeachingManual/add-image.html`

Add a link to this page in the repo README.

---

## Part C: Optional Enhancement — Image Position Preview

After Horizon 2 is working, a nice addition: before committing, the Worker could return
a preview of where in the manual the image will be inserted (the surrounding paragraphs).
The UI shows this in a confirmation step: "Your image will appear here: [context]". User
confirms, then the commit happens.

This requires reading the manual source in the Worker before inserting, which is already
done — just add the preview to the API response and a confirmation modal in the HTML.

---

## Validation Checklist for Horizon 2

- [ ] GitHub Actions workflow builds all PDFs on push (test with a trivial whitespace change)
- [ ] Workflow `workflow_dispatch` works with `subject` input (test via GitHub Actions UI)
- [ ] Committed PDFs are accessible in repo after build
- [ ] Cloudflare Worker deploys successfully
- [ ] Worker can commit an image and trigger a build (test via curl)
- [ ] `add-image.html` form submits and shows the Actions run URL
- [ ] A non-technical person can use the full flow without explanation (dogfood test)
- [ ] GitHub token is a fine-grained PAT scoped to this repo only (not a classic token)
- [ ] Worker secret is set, token is NOT in any source file

---

## Notes for AI Consultant Reuse

This pattern (GitHub Pages form → Cloudflare Worker → GitHub API → GitHub Actions → result
back to user) is a general-purpose architecture for zero-cost, serverless automation UIs.

Variations:
- **Any file processing workflow:** swap "image → PDF build" for "CSV → data transformation", "audio → transcript", etc.
- **Approval workflows:** Worker writes to a staging branch; a human approves via GitHub PR; merge triggers build
- **Multi-step forms:** Worker stores intermediate state in Cloudflare KV (free tier: 100k reads/day)
- **Notifications:** Worker posts to a webhook (Discord, Slack, email via SendGrid free tier) when build completes

The only limit: Cloudflare Worker free tier has a 10ms CPU time limit per request.
For anything CPU-heavy, use a Worker to trigger a GitHub Actions job and return immediately.
The actual work always happens in GitHub Actions (unlimited runtime on free public repos).
