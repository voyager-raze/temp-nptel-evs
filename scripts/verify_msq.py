"""Verify every assignment MSQ answer against PDF text for weeks 3-6; list all MSQs."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "assignments.json").read_text(encoding="utf-8"))
raw = root / "data" / "raw" / "assignments"

errors = []
msqs = []

for w in data["weeks"]:
    for q in w["questions"]:
        multi = q.get("multi") or q.get("type") == "msq" or isinstance(q.get("answer"), list)
        if multi:
            if not isinstance(q["answer"], list) or len(q["answer"]) < 1:
                errors.append(f"{q['id']}: MSQ without list answer")
            if q.get("type") != "msq":
                errors.append(f"{q['id']}: multi but type={q.get('type')}")
            msqs.append(q["id"])

for week in (3, 4, 5, 6):
    text = (raw / f"week{week}.txt").read_text(encoding="utf-8", errors="replace")
    parts = re.split(r"QUESTION\s+(\d+)\s*:", text, flags=re.I)
    it = iter(parts[1:])
    bodies = {int(n): b for n, b in zip(it, it)}
    jw = next(w for w in data["weeks"] if w["week"] == week)
    for q in jw["questions"]:
        n = int(re.search(r"q(\d+)$", q["id"]).group(1))
        if n < 11:
            continue
        body = bodies[n]
        m = re.search(
            r"Correct answer\(s\)?\s*:\s*(.*?)(?=\n\s*Solution:|\Z)",
            body,
            re.I | re.S,
        )
        if not m:
            # w4q14 uses Correct answer: with multiple letters
            m = re.search(
                r"Correct answer\s*:\s*(.*?)(?=\n\s*Solution:|\Z)",
                body,
                re.I | re.S,
            )
        if not m:
            errors.append(f"{q['id']}: no answer block in PDF")
            continue
        letters = sorted(
            set(re.findall(r"(?:^|\n)\s*([a-dA-D])\s*[\.\)]", m.group(1)))
        )
        letters = [x.lower() for x in letters]
        jans = sorted(q["answer"])
        if letters != jans:
            errors.append(f"{q['id']}: JSON {jans} != PDF {letters}")

# Week 1 manual expected MSQs from solutions
expected_w1 = {
    "w1q6": ["a", "b", "d"],
    "w1q11": ["a", "b", "d"],
    "w1q15": ["a", "b", "c"],
    "w1q16": ["a", "c"],
    "w1q19": ["a", "b", "c", "d"],
    "w1q20": ["a", "b", "d"],
}
w1 = next(w for w in data["weeks"] if w["week"] == 1)
for q in w1["questions"]:
    if q["id"] in expected_w1:
        if sorted(q["answer"]) != expected_w1[q["id"]]:
            errors.append(f"{q['id']}: expected {expected_w1[q['id']]} got {q['answer']}")

expected_w11 = {
    "w11q5": ["a", "b", "d"],
    "w11q6": ["a", "c", "d"],
    "w11q13": ["b", "c"],
    "w11q14": ["a", "b", "c"],
}
w11 = next(w for w in data["weeks"] if w["week"] == 11)
for q in w11["questions"]:
    if q["id"] in expected_w11:
        if sorted(q["answer"]) != expected_w11[q["id"]]:
            errors.append(f"{q['id']}: expected {expected_w11[q['id']]} got {q['answer']}")

print(f"MSQ ids ({len(msqs)}): {', '.join(msqs)}")
if errors:
    print("ERRORS:")
    for e in errors:
        print(" ", e)
    raise SystemExit(1)
print("All MSQ checks passed.")
