# Ajay Aravindan — CV & Portfolio: Copilot Instructions

## Source of Truth

The CV PDF at `CV/AJAY ARAVINDAN.pdf` is the **single source of truth** for all content on the portfolio page (`portfolio/index.html`).

Whenever the portfolio is being edited, **always extract the CV text first**:

```powershell
& ".\ajay_cv_venv\Scripts\python.exe" -c "import pymupdf; doc = pymupdf.open('CV/AJAY ARAVINDAN.pdf'); [print(p.get_text()) for p in doc]"
```

Then use that output as the reference for every content change.

---

## CV → Portfolio Mapping

| CV Section | Portfolio Section | Notes |
|---|---|---|
| Personal Statement | Hero `.subtitle` | Condensed to 1–2 sentences |
| Skills | `#skills` `.skills-grid` | Mirror CV's 5 categories exactly |
| Portfolio Projects | `#projects` slides | Bullet points must match CV verbatim |
| Experience | `#experience` `.exp-timeline` | Job titles, dates, org names from CV |
| Education | `#education` `.edu-grid` | Degree names, institutions, dates, modules from CV |
| Location / availability | Hero tag, About meta, Footer | Never add specifics (e.g. "London") not in the CV |

---

## Rules When Updating

1. **Always read the CV before editing the portfolio.** Do not rely on memory of prior CV content.
2. **Skills:** Replace the entire skills grid; do not append — use only what the CV lists.
3. **Relocation language:** Use "within the UK" — never a specific city unless the CV states one.
4. **CV download link:** Both the hero button and the contact chip must point to `CV/AJAY ARAVINDAN.pdf` (relative to `portfolio/`).
5. **After any CV update**, copy the new PDF:
   ```powershell
   Copy-Item "CV\AJAY ARAVINDAN.pdf" -Destination "portfolio\CV\AJAY ARAVINDAN.pdf"
   ```
6. **Google Drive embeds:** Audio files cannot be embedded via iframe (Google blocks cross-domain). Use direct `/view` links only. Video `/preview` embeds work fine.
7. **Do not invent details** not present in the CV (e.g. specific event counts, bar team leadership details).

---

## Key File Locations

| File | Purpose |
|------|---------|
| `CV/AJAY ARAVINDAN.pdf` | Source CV — read this first |
| `portfolio/index.html` | The portfolio page — the only file to edit for content |
| `portfolio/CV/AJAY ARAVINDAN.pdf` | CV served by the live site (copy from above) |
| `render.yaml` | Render deployment config (publish dir: `portfolio`) |
| `requirements.txt` | Python deps: reportlab, pymupdf, python-docx |
| `.vscode/mcp.json` | Context7 MCP config (requires Node.js) |
