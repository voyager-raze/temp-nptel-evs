# NPTEL EVS — 2-Day Exam Practice App

Offline-first static site for **NPTEL Environmental Science** (IIT Kharagpur).

## Phone / tablet (GitHub Pages + offline)

Live site:

**https://voyager-raze.github.io/temp-nptel-evs/**

### Install for offline (one-time on Wi‑Fi)

1. Open the link above on phone/tablet **while online**.
2. Wait ~10–20 seconds so the app finishes downloading (~3–4 MB).
3. **Android (Chrome):** menu → **Install app** / **Add to Home screen**.  
   **iPhone/iPad (Safari):** Share → **Add to Home Screen**.
4. Open the home-screen icon once online (confirms install).
5. After that you can practice **without internet** (airplane mode OK).

Progress still saves per device/browser. PDF backup: [exports/NPTEL_EVS_Complete_Practice.pdf](exports/NPTEL_EVS_Complete_Practice.pdf)

## How to open (laptop)

Do **not** open `index.html` as a `file://` URL — browsers block `fetch()` for JSON.

From this folder (`webapp/`):

```bash
# From the webapp/ folder — use a free port (8080 may be taken)
python -m http.server 8765

# or Node
npx --yes serve -p 8765
```

Then visit: **http://localhost:8765**

## Pages

| Page | Purpose |
|------|---------|
| Home | 2-day plan, progress, exam pattern |
| Assignments | 200 weekly **MCQ + MSQ** with solutions |
| Materials | Condensed cheat-sheet notes for 12 weeks |
| Notes | Full week study chapters (definitions → exam checklist) |
| Transcripts | 60 lecture one-pagers + search |
| Final Notes | Predicted **MCQ + MSQ**, formulas, flashcards, law palace |
| Mock Exam | 100-Q / 180-min CBT simulator (includes MSQs) |

## Answer trust

| Source | Count | Trust |
|--------|------:|-------|
| Assignments W1, W3–W12 | 190 | **PDF-verified** against your answer-key PDFs |
| Assignments Week 2 | 10 | **Best-guess** (your Week 2 PDF has questions only, no key) |
| Predicted (`final.html`) | 140 (20 MSQ) | **Practice only** — exam-style, not official NPTEL keys |

MSQs use checkbox multi-select; you must pick the **exact** correct set (NPTEL style).

## Keyboard shortcuts (practice)

- `1`–`4` — select / toggle option
- `N` / `Enter` — check or next
- `Space` — flip flashcard

Progress and weak questions save in **localStorage** in this browser.

Re-check MSQ keys anytime: `python scripts/verify_msq.py`

## Complete practice PDF

One print-ready PDF with cheat sheet → all 12 assignments (answers highlighted) → high-likelihood predicted extras:

```bash
# from webapp/
pip install -r scripts/requirements-pdf.txt
playwright install chromium   # first time only
python scripts/build_practice_pdf.py
```

Outputs: `exports/NPTEL_EVS_Complete_Practice.pdf` and preview `exports/practice.html`.
