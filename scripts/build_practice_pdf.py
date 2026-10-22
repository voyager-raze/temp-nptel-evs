#!/usr/bin/env python3
"""
Build NPTEL EVS Complete Practice PDF.

Order: cover + cheat sheet → all 12 assignment weeks (200 Q) → high-likelihood predicted (117).

Usage (from webapp/):
  pip install -r scripts/requirements-pdf.txt
  playwright install chromium
  python scripts/build_practice_pdf.py

Outputs:
  exports/practice.html
  exports/NPTEL_EVS_Complete_Practice.pdf
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

from jinja2 import Template

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
EXPORTS = ROOT / "exports"

CSS = r"""
@page {
  size: A4;
  margin: 12mm 12mm 14mm 12mm;
}
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Source Sans 3", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.38;
  color: #1a1f2e;
  margin: 0;
  background: #fff;
}
h1, h2, h3, h4 { font-weight: 700; color: #0f172a; margin: 0 0 0.35em; }
h1 { font-size: 20pt; letter-spacing: -0.02em; }
h2 { font-size: 14pt; margin-top: 0.6em; }
h3 { font-size: 11.5pt; }
a { color: inherit; text-decoration: none; }

.cover {
  border-bottom: 3px solid #0f766e;
  padding-bottom: 10px;
  margin-bottom: 12px;
}
.cover .sub {
  color: #475569;
  font-size: 10pt;
  margin-top: 2px;
}
.meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  margin-top: 8px;
  font-size: 9pt;
  color: #334155;
}
.legend {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 10px;
  padding: 8px 10px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 9pt;
}
.legend-item { display: inline-flex; align-items: center; gap: 6px; }
.swatch {
  display: inline-block;
  width: 14px; height: 14px;
  border-radius: 3px;
  background: #dcfce7;
  border: 1px solid #86efac;
}
.badge {
  display: inline-block;
  font-size: 8pt;
  font-weight: 700;
  letter-spacing: 0.02em;
  padding: 1px 7px;
  border-radius: 999px;
  vertical-align: middle;
}
.badge-msq { background: #e0e7ff; color: #3730a3; }
.badge-mcq { background: #ecfdf5; color: #065f46; }
.badge-ar { background: #fff7ed; color: #9a3412; }
.badge-match { background: #f0f9ff; color: #075985; }
.badge-num { background: #faf5ff; color: #6b21a8; }
.badge-guess { background: #fef3c7; color: #92400e; }
.badge-pred { background: #f1f5f9; color: #475569; }
.badge-high { background: #fee2e2; color: #991b1b; }

/* —— Cheat sheet —— */
.section-banner {
  background: #0f766e;
  color: #fff;
  padding: 7px 12px;
  border-radius: 6px;
  font-size: 12pt;
  font-weight: 700;
  margin: 14px 0 10px;
  page-break-after: avoid;
}
.cheat-grid {
  column-count: 2;
  column-gap: 12px;
}
.cheat-block {
  break-inside: avoid;
  page-break-inside: avoid;
  margin-bottom: 8px;
  padding: 7px 9px;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  background: #fafbfc;
}
.cheat-block h4 {
  font-size: 9.5pt;
  color: #0f766e;
  border-bottom: 1px solid #ccfbf1;
  padding-bottom: 3px;
  margin-bottom: 5px;
}
.cheat-block ul {
  margin: 0;
  padding-left: 1.05em;
  font-size: 8.6pt;
  color: #1e293b;
}
.cheat-block li { margin-bottom: 2px; }
.formula-row {
  font-size: 8.5pt;
  margin-bottom: 3px;
  line-height: 1.3;
}
.formula-row .name { font-weight: 600; color: #0f172a; }
.formula-row .eq {
  font-family: "Cambria Math", "Times New Roman", serif;
  color: #0f766e;
  font-weight: 600;
}
.law-step {
  font-size: 8.4pt;
  margin-bottom: 3px;
}
.law-step .n {
  display: inline-block;
  min-width: 1.2em;
  font-weight: 700;
  color: #0f766e;
}
.hook-line { font-size: 8.4pt; margin-bottom: 2px; }
.hook-line strong { color: #0f172a; }

/* —— Questions —— */
.week-banner {
  background: #134e4a;
  color: #fff;
  padding: 8px 12px;
  border-radius: 6px;
  margin: 16px 0 10px;
  page-break-before: always;
  page-break-after: avoid;
}
.week-banner.first { page-break-before: always; }
.week-banner .wk-title { font-size: 12.5pt; font-weight: 700; }
.week-banner .wk-meta { font-size: 9pt; opacity: 0.9; margin-top: 2px; }

.q {
  break-inside: avoid;
  page-break-inside: avoid;
  margin: 0 0 11px;
  padding: 8px 10px 9px;
  border: 1px solid #e2e8f0;
  border-radius: 7px;
  background: #fff;
}
.q-head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}
.q-num {
  font-weight: 800;
  font-size: 10.5pt;
  color: #0f172a;
}
.q-topic {
  font-size: 8pt;
  color: #64748b;
  margin-left: auto;
}
.stem {
  font-size: 10.5pt;
  font-weight: 600;
  margin: 2px 0 6px;
  color: #0f172a;
}
.opts { margin: 0; padding: 0; list-style: none; }
.opt {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  padding: 4px 8px;
  margin-bottom: 3px;
  border-radius: 5px;
  border: 1px solid transparent;
  font-size: 10pt;
  line-height: 1.35;
}
.opt .key {
  flex: 0 0 1.4em;
  font-weight: 700;
  color: #475569;
}
.opt.correct {
  background: #dcfce7;
  border-color: #86efac;
  color: #166534;
}
.opt.correct .key { color: #166534; font-weight: 800; }
.expl {
  margin-top: 5px;
  padding-top: 5px;
  border-top: 1px dashed #e2e8f0;
  font-size: 8.5pt;
  color: #475569;
  line-height: 1.35;
}
.expl strong { color: #334155; }
.ans-line {
  font-size: 8.5pt;
  font-weight: 700;
  color: #166534;
  margin-top: 4px;
}

.extra-intro {
  padding: 10px 12px;
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-radius: 6px;
  font-size: 9.5pt;
  color: #78350f;
  margin-bottom: 10px;
  page-break-before: always;
}
.footer-note {
  margin-top: 18px;
  font-size: 8.5pt;
  color: #64748b;
  text-align: center;
  border-top: 1px solid #e2e8f0;
  padding-top: 8px;
}
"""

HTML_TMPL = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>NPTEL EVS — Complete Practice PDF</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>{{ css }}</style>
</head>
<body>

<header class="cover">
  <h1>NPTEL Environmental Science</h1>
  <div class="sub">IIT Kharagpur · Complete Assignments + Cheat Sheet + High-Chance Extras</div>
  <div class="meta-row">
    <span><strong>{{ assignment_count }}</strong> assignment questions (12 weeks)</span>
    <span><strong>{{ msq_count }}</strong> MSQs</span>
    <span><strong>{{ predicted_count }}</strong> high-likelihood predicted</span>
  </div>
  <div class="legend">
    <span class="legend-item"><span class="swatch"></span> Green = correct answer(s)</span>
    <span class="legend-item"><span class="badge badge-msq">MSQ — select all</span></span>
    <span class="legend-item"><span class="badge badge-guess">best-guess</span> Week 2 keys</span>
    <span class="legend-item"><span class="badge badge-pred">predicted</span> Practice only — not official</span>
  </div>
</header>

<!-- ===================== CHEAT SHEET ===================== -->
<div class="section-banner">Cheat Sheet — Formulas, Must-Remember &amp; Law Path</div>

<div class="cheat-grid">

  <div class="cheat-block">
    <h4>Formulas ({{ formulas|length }})</h4>
    {% for f in formulas %}
    <div class="formula-row">
      <span class="name">W{{ f.week }} · {{ f.name }}:</span>
      <span class="eq"> {{ f.formula }}</span>
    </div>
    {% endfor %}
  </div>

  <div class="cheat-block">
    <h4>{{ memory_palace.title }}</h4>
    {% for s in memory_palace.steps %}
    <div class="law-step">
      <span class="n">{{ s.order }}.</span>
      <strong>{{ s.cue }}</strong> — {{ s.fact }}
    </div>
    {% endfor %}
  </div>

  <div class="cheat-block">
    <h4>Mnemonics</h4>
    <ul>
    {% for m in mnemonics %}
      <li><strong>{{ m.title }}:</strong> {{ m.expansion }} <em>({{ m.hook }})</em></li>
    {% endfor %}
    </ul>
  </div>

  <div class="cheat-block">
    <h4>Compare hooks</h4>
    {% for h in compare_hooks %}
    <div class="hook-line"><strong>{{ h.pair }}:</strong> {{ h.hook }}</div>
    {% endfor %}
  </div>

  {% for w in materials_weeks %}
  <div class="cheat-block">
    <h4>Week {{ w.week }} — {{ w.title }}</h4>
    <ul>
      {% for item in w.mustRemember %}
      <li>{{ item }}</li>
      {% endfor %}
      {% for flag in w.examFlags[:5] %}
      <li><em>{{ flag }}</em></li>
      {% endfor %}
      {% for n in w.numbers[:4] %}
      <li><strong>{{ n.label }}:</strong> {{ n.value }}{% if n.why %} — {{ n.why }}{% endif %}</li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}

</div>

<!-- ===================== ASSIGNMENTS ===================== -->
<div class="section-banner" style="page-break-before: always;">Assignments — All 12 Weeks ({{ assignment_count }} questions)</div>

{% for week in assignment_weeks %}
<div class="week-banner{% if loop.first %} first{% endif %}">
  <div class="wk-title">Week {{ week.week }} — {{ week.title }}</div>
  <div class="wk-meta">{{ week.questions|length }} questions
    · {{ week.msq_n }} MSQ · {{ week.mcq_n }} other
    {% if week.week == 2 %}· <span class="badge badge-guess">best-guess keys</span>{% endif %}
  </div>
</div>

{% for q in week.questions %}
<article class="q">
  <div class="q-head">
    <span class="q-num">Q{{ loop.index }}</span>
    <span class="badge {{ q.badge_class }}">{{ q.badge_label }}</span>
    {% if q.trust == 'best_guess' %}<span class="badge badge-guess">best-guess</span>{% endif %}
    {% if q.topic %}<span class="q-topic">{{ q.topic }}</span>{% endif %}
  </div>
  <div class="stem">{{ q.stem }}</div>
  <ul class="opts">
    {% for opt in q.options %}
    <li class="opt{% if opt.correct %} correct{% endif %}">
      <span class="key">{{ opt.key|upper }}.</span>
      <span>{{ opt.text }}</span>
    </li>
    {% endfor %}
  </ul>
  <div class="ans-line">Answer: {{ q.answer_display }}</div>
  {% if q.explanation %}
  <div class="expl"><strong>Why:</strong> {{ q.explanation }}</div>
  {% endif %}
</article>
{% endfor %}
{% endfor %}

<!-- ===================== PREDICTED ===================== -->
<div class="extra-intro">
  <strong>Extra — High-chance / important questions ({{ predicted_count }})</strong><br/>
  Predicted exam-style MCQ + MSQ from the course bank. <em>Practice only — not official NPTEL answer keys.</em>
  Green highlights mark the intended correct option set.
</div>
<div class="section-banner">High-Likelihood Predicted Questions</div>

{% for week in predicted_weeks %}
<div class="week-banner">
  <div class="wk-title">Predicted · Week {{ week.week }}</div>
  <div class="wk-meta">{{ week.questions|length }} high-likelihood questions</div>
</div>

{% for q in week.questions %}
<article class="q">
  <div class="q-head">
    <span class="q-num">{{ q.id }}</span>
    <span class="badge {{ q.badge_class }}">{{ q.badge_label }}</span>
    <span class="badge badge-high">high</span>
    <span class="badge badge-pred">predicted</span>
    {% if q.category %}<span class="q-topic">{{ q.category }}</span>{% endif %}
  </div>
  <div class="stem">{{ q.stem }}</div>
  <ul class="opts">
    {% for opt in q.options %}
    <li class="opt{% if opt.correct %} correct{% endif %}">
      <span class="key">{{ opt.key|upper }}.</span>
      <span>{{ opt.text }}</span>
    </li>
    {% endfor %}
  </ul>
  <div class="ans-line">Answer: {{ q.answer_display }}</div>
  {% if q.explanation %}
  <div class="expl"><strong>Why:</strong> {{ q.explanation }}</div>
  {% endif %}
</article>
{% endfor %}
{% endfor %}

<div class="footer-note">
  Regenerated from webapp/data JSON · Assignments W1, W3–W12 PDF-verified · Week 2 best-guess · Predicted practice-only<br/>
  Run: <code>python scripts/build_practice_pdf.py</code>
</div>

</body>
</html>
"""


def esc(s: object) -> str:
    if s is None:
        return ""
    return html.escape(str(s), quote=True)


def answer_keys(answer) -> set[str]:
    if isinstance(answer, list):
        return {str(a).lower().strip() for a in answer}
    if answer is None:
        return set()
    return {str(answer).lower().strip()}


def answer_display(answer) -> str:
    keys = sorted(answer_keys(answer))
    return ", ".join(k.upper() for k in keys) if keys else "—"


def type_badge(qtype: str, multi: bool) -> tuple[str, str]:
    t = (qtype or "").lower()
    if multi or t == "msq":
        return "badge-msq", "MSQ — select all"
    if t == "assertion_reason":
        return "badge-ar", "Assertion–Reason"
    if t == "match":
        return "badge-match", "Match"
    if t == "numerical":
        return "badge-num", "Numerical"
    return "badge-mcq", "MCQ"


def enrich_question(raw: dict) -> dict:
    keys = answer_keys(raw.get("answer"))
    multi = bool(raw.get("multi")) or raw.get("type") == "msq" or isinstance(raw.get("answer"), list)
    badge_class, badge_label = type_badge(raw.get("type", "mcq"), multi)
    options = []
    for opt in raw.get("options") or []:
        k = str(opt.get("key", "")).lower().strip()
        options.append(
            {
                "key": k,
                "text": esc(opt.get("text", "")),
                "correct": k in keys,
            }
        )
    return {
        "id": esc(raw.get("id", "")),
        "stem": esc(raw.get("stem", "")),
        "options": options,
        "explanation": esc(raw.get("explanation", "")),
        "topic": esc(raw.get("topic", "")),
        "category": esc(raw.get("category", "")),
        "trust": raw.get("trust", ""),
        "badge_class": badge_class,
        "badge_label": badge_label,
        "answer_display": answer_display(raw.get("answer")),
        "multi": multi,
    }


def load_json(name: str):
    path = DATA / name
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def build_context() -> dict:
    assignments = load_json("assignments.json")
    predicted = load_json("predicted.json")
    materials = load_json("materials-notes.json")
    formulas = load_json("formulas.json")
    mnemonics_data = load_json("mnemonics.json")

    assignment_weeks = []
    total_q = 0
    total_msq = 0
    for w in assignments["weeks"]:
        qs = [enrich_question(q) for q in w["questions"]]
        msq_n = sum(1 for q in qs if q["multi"])
        total_q += len(qs)
        total_msq += msq_n
        assignment_weeks.append(
            {
                "week": w["week"],
                "title": esc(w.get("title", "")),
                "questions": qs,
                "msq_n": msq_n,
                "mcq_n": len(qs) - msq_n,
            }
        )

    high = [q for q in predicted["questions"] if q.get("likelihood") == "high"]
    by_week: dict[int, list] = {}
    for q in high:
        by_week.setdefault(int(q.get("week", 0)), []).append(enrich_question(q))
    predicted_weeks = [
        {"week": wk, "questions": by_week[wk]}
        for wk in sorted(by_week.keys())
    ]

    materials_weeks = []
    for w in materials["weeks"]:
        materials_weeks.append(
            {
                "week": w["week"],
                "title": esc(w.get("title", "")),
                "mustRemember": [esc(x) for x in w.get("mustRemember") or []],
                "examFlags": [esc(x) for x in w.get("examFlags") or []],
                "numbers": [
                    {
                        "label": esc(n.get("label", "")),
                        "value": esc(n.get("value", "")),
                        "why": esc(n.get("why", "")),
                    }
                    for n in (w.get("numbers") or [])
                ],
            }
        )

    formulas_out = [
        {
            "week": f.get("week", ""),
            "name": esc(f.get("name", "")),
            "formula": esc(f.get("formula", "")),
        }
        for f in formulas
    ]

    mnemonics_out = [
        {
            "title": esc(m.get("title", "")),
            "expansion": esc(m.get("expansion", "")),
            "hook": esc(m.get("hook", "")),
        }
        for m in mnemonics_data.get("mnemonics") or []
    ]
    compare_hooks = [
        {
            "pair": esc(h.get("pair", "")),
            "hook": esc(h.get("hook", "")),
        }
        for h in mnemonics_data.get("compareHooks") or []
    ]
    palace = mnemonics_data.get("memoryPalace") or {"title": "Law Path", "steps": []}
    memory_palace = {
        "title": esc(palace.get("title", "Law Path")),
        "steps": [
            {
                "order": s.get("order", i + 1),
                "cue": esc(s.get("cue", "")),
                "fact": esc(s.get("fact", "")),
            }
            for i, s in enumerate(palace.get("steps") or [])
        ],
    }

    return {
        "css": CSS,
        "assignment_count": total_q,
        "msq_count": total_msq,
        "predicted_count": len(high),
        "assignment_weeks": assignment_weeks,
        "predicted_weeks": predicted_weeks,
        "materials_weeks": materials_weeks,
        "formulas": formulas_out,
        "mnemonics": mnemonics_out,
        "compare_hooks": compare_hooks,
        "memory_palace": memory_palace,
    }


def render_html(ctx: dict) -> str:
    return Template(HTML_TMPL).render(**ctx)


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle", timeout=120_000)
        # Give webfonts a moment
        page.wait_for_timeout(800)
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()


def qa_assert(ctx: dict) -> None:
    assert ctx["assignment_count"] == 200, f"expected 200 assignments, got {ctx['assignment_count']}"
    assert ctx["msq_count"] == 30, f"expected 30 MSQs, got {ctx['msq_count']}"
    assert ctx["predicted_count"] == 117, f"expected 117 high predicted, got {ctx['predicted_count']}"
    assert len(ctx["assignment_weeks"]) == 12
    assert len(ctx["materials_weeks"]) == 12
    assert len(ctx["formulas"]) == 24

    # Spot-check W1 MSQ a,b,d (first week, find multi with those answers in source)
    w1 = load_json("assignments.json")["weeks"][0]["questions"]
    msq = next(q for q in w1 if q.get("id") == "w1q6")
    assert set(answer_keys(msq["answer"])) == {"a", "b", "d"}

    # Rendered week 1 should have correct flags on options
    enriched = enrich_question(msq)
    correct = {o["key"] for o in enriched["options"] if o["correct"]}
    assert correct == {"a", "b", "d"}, correct
    print("QA OK: 200 assignments, 30 MSQ, 117 high predicted, W1q6 = A,B,D")


def main() -> int:
    EXPORTS.mkdir(parents=True, exist_ok=True)
    print("Loading data…")
    ctx = build_context()
    qa_assert(ctx)

    html_path = EXPORTS / "practice.html"
    pdf_path = EXPORTS / "NPTEL_EVS_Complete_Practice.pdf"

    print("Rendering HTML…")
    html_doc = render_html(ctx)
    html_path.write_text(html_doc, encoding="utf-8")
    print(f"  Wrote {html_path} ({len(html_doc):,} chars)")

    print("Printing PDF via Playwright Chromium…")
    try:
        html_to_pdf(html_path, pdf_path)
    except Exception as e:
        print(f"PDF export failed: {e}", file=sys.stderr)
        print("Install deps: pip install -r scripts/requirements-pdf.txt && playwright install chromium", file=sys.stderr)
        return 1

    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"  Wrote {pdf_path} ({size_mb:.2f} MB)")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
