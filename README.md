# Ajay Aravindan — CV & Portfolio

This repo contains the CV builder (`build_cv.py`), a PDF extractor (`extract.py`), and a static portfolio site (`portfolio/index.html`).

**Live deployment:** Render (static site) — see [Section 7](#7--deploy-to-render).

---

## Prerequisites

| Tool | Required for |
|------|-------------|
| Python 3.11+ | CV builder, portfolio server |
| Node.js 18+ | Context7 MCP (AI documentation tool) |

---

## 1 — Set up the Virtual Environment

### First-time setup (PowerShell)

```powershell
# Allow scripts to run (required once per machine)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Create the venv (skip if ajay_cv_venv/ already exists)
python -m venv ajay_cv_venv

# Activate the venv
.\ajay_cv_venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt
```

> **Why `source` doesn't work on Windows:**  
> `source` is a Bash/Linux command. On PowerShell use `.\ajay_cv_venv\Scripts\Activate.ps1`.  
> On CMD use `ajay_cv_venv\Scripts\activate.bat`.

### Activate the venv (every subsequent session)

```powershell
.\ajay_cv_venv\Scripts\Activate.ps1
```

You'll see `(ajay_cv_venv)` in your prompt when it's active.

---

## 2 — Run the Portfolio Locally

The portfolio is a static HTML site. Serve it with Python's built-in HTTP server — **no extra packages needed**.

```powershell
# With venv active:
python -m http.server 8080 --directory portfolio

# Without activating venv:
& ".\ajay_cv_venv\Scripts\python.exe" -m http.server 8080 --directory portfolio
```

Then open **http://localhost:8080** in your browser. Press `Ctrl+C` to stop.

> You can also double-click `portfolio\index.html` to open directly without a server.

---

## 3 — Build the CV (PDF)

```powershell
# With venv active:
python build_cv.py

# Without activating venv:
& ".\ajay_cv_venv\Scripts\python.exe" build_cv.py
```

---

## 4 — Extract Text from PDF/DOCX

```powershell
python extract.py
```

Requires `AJAY ARAVINDAN.pdf` and the job description DOCX in the project root.

---

## 5 — Context7 MCP (AI Documentation in Copilot)

Context7 provides up-to-date library documentation inside GitHub Copilot Chat.

### Install Node.js first

Download from **https://nodejs.org** (LTS version).

### How it works

`.vscode/mcp.json` is already configured. Once Node.js is installed, VS Code auto-starts the Context7 server. In Copilot Chat, add **`use context7`** to any prompt to pull live docs.

---

## 6 — Update the CV PDF for Deployment

Whenever you update the CV, copy the new PDF into the portfolio folder so Render serves it:

```powershell
Copy-Item "CV\AJAY ARAVINDAN.pdf" -Destination "portfolio\CV\AJAY ARAVINDAN.pdf"
```

The portfolio links to `CV/AJAY ARAVINDAN.pdf` relative to the `portfolio/` folder.

---

## 7 — Deploy to Render

The repo includes a `render.yaml` — Render will auto-detect it.

### Steps

1. **Push this repo to GitHub** (if not already done):
   ```powershell
   git init
   git add .
   git commit -m "Initial portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Create a Render account** at [render.com](https://render.com) (free tier available).

3. **New Static Site:**
   - Dashboard → **New** → **Static Site**
   - Connect your GitHub account and select this repo
   - Render will detect `render.yaml` automatically

4. **If configuring manually** (without `render.yaml`):

   | Setting | Value |
   |---------|-------|
   | Build Command | *(leave blank)* |
   | Publish Directory | `portfolio` |

5. Click **Deploy**. Render will give you a URL like `https://ajay-aravindan-portfolio.onrender.com`.

### Re-deploy after changes

```powershell
git add .
git commit -m "Update portfolio"
git push
```

Render auto-deploys on every push to `main`.

### Custom domain (optional)

In Render dashboard → your site → **Settings** → **Custom Domains** → add your domain and update your DNS records as instructed.

---

## Project Structure

```
ajay_cv/
├── portfolio/
│   ├── index.html          # Portfolio site (edit this)
│   └── CV/
│       └── AJAY ARAVINDAN.pdf  # CV download (copy here before deploying)
├── CV/
│   └── AJAY ARAVINDAN.pdf  # Source CV
├── ajay_cv_venv/           # Python virtual environment (local only)
├── build_cv.py             # PDF CV generator (reportlab)
├── extract.py              # PDF/DOCX text extractor
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
└── .vscode/
    ├── mcp.json            # Context7 MCP configuration
    └── settings.json
```

---

## Python Packages

| Package | Version | Used by |
|---------|---------|---------|
| reportlab | 5.0.0 | `build_cv.py` |
| pymupdf | 1.28.2 | `extract.py` |
| python-docx | 1.2.0 | `extract.py` |
| pillow | 12.3.0 | reportlab dependency |

