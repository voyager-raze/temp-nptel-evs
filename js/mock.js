/* CBT-style 100-question mock exam with timer + palette */
const MockExam = (() => {
  const DURATION = 3 * 60 * 60; // 180 minutes

  function create(root, bank) {
    let questions = [];
    let index = 0;
    let answers = {};
    let marked = new Set();
    let remaining = DURATION;
    let timerId = null;
    let started = false;
    let finished = false;

    function buildPaper(n = 100) {
      // Weight: assignments 60%, predicted 40%, prefer variety across weeks
      // Guarantee a share of MSQs (like real NPTEL papers)
      const assigns = (bank.assignments || []).map(EVS.normalizeQuestion);
      const predicted = (bank.predicted || []).map(EVS.normalizeQuestion);
      const all = [...assigns, ...predicted];
      const isMulti = (q) =>
        q.multi === true || q.type === "msq" || Array.isArray(q.answer);
      const msqPool = EVS.shuffle(all.filter(isMulti));
      const mcqPool = EVS.shuffle(all.filter((q) => !isMulti(q)));
      const msqTarget = Math.min(msqPool.length, Math.max(8, Math.round(n * 0.15)));
      const picked = [...msqPool.slice(0, msqTarget)];
      const byWeek = {};
      mcqPool.forEach((q) => {
        if (!byWeek[q.week]) byWeek[q.week] = [];
        byWeek[q.week].push(q);
      });
      const weeks = Object.keys(byWeek).map(Number).sort((a, b) => a - b);
      const remain = n - picked.length;
      const per = Math.floor(remain / Math.max(weeks.length, 1));
      weeks.forEach((w) => {
        picked.push(...(byWeek[w] || []).slice(0, per));
      });
      const used = new Set(picked.map((q) => q.id));
      for (const q of EVS.shuffle(all)) {
        if (picked.length >= n) break;
        if (!used.has(q.id)) {
          picked.push(q);
          used.add(q.id);
        }
      }
      return EVS.shuffle(picked).slice(0, n).map((q, i) => ({
        ...q,
        mockNo: i + 1,
      }));
    }

    function start(n = 100) {
      questions = buildPaper(n);
      index = 0;
      answers = {};
      marked = new Set();
      remaining = DURATION;
      finished = false;
      started = true;
      if (timerId) clearInterval(timerId);
      timerId = setInterval(() => {
        remaining--;
        updateTimer();
        if (remaining <= 0) submit(true);
      }, 1000);
      render();
    }

    function updateTimer() {
      const el = root.querySelector("#mockTimer");
      if (!el) return;
      el.textContent = EVS.formatTime(Math.max(0, remaining));
      el.classList.toggle("warn", remaining < 10 * 60);
    }

    function current() {
      return questions[index];
    }

    function render() {
      if (!started) {
        root.innerHTML = `
          <div class="card hero">
            <h1>Mock Final Exam</h1>
            <p>Mimics NPTEL CBT: <strong>100 MCQs</strong>, <strong>180 minutes</strong>, <strong>no negative marking</strong>. Attempt everything. Flag doubts and return later.</p>
            <div class="hero-meta">
              <span class="chip">On-screen calc only in real exam</span>
              <span class="chip hot">Leave no blank</span>
            </div>
            <div class="actions">
              <button class="btn btn-primary" id="startFull">Start 100-Q Mock</button>
              <button class="btn" id="startQuick">Quick 25-Q drill</button>
            </div>
          </div>`;
        root.querySelector("#startFull").onclick = () => start(100);
        root.querySelector("#startQuick").onclick = () => start(25);
        return;
      }

      if (finished) return renderResults();

      const q = current();
      const multi = q.multi === true || q.type === "msq" || Array.isArray(q.answer);
      const sel = answers[q.id];
      const selCount = multi && Array.isArray(sel) ? sel.length : sel ? 1 : 0;

      const optionsHtml = (q.options || [])
        .map((o) => {
          const key = String(o.key).toLowerCase();
          const selected = multi
            ? Array.isArray(sel) && sel.includes(key)
            : sel === key;
          const mark = selected ? "✓" : "";
          return `<button type="button" class="option ${multi ? "msq-opt" : "mcq-opt"} ${selected ? "selected" : ""}" data-key="${key}" aria-pressed="${selected}">
            <span class="mark" aria-hidden="true">${mark}</span>
            <span class="key">${key.toUpperCase()}</span>
            <span>${escapeHtml(o.text)}</span>
          </button>`;
        })
        .join("");

      const palette = questions
        .map((qq, i) => {
          let cls = "";
          if (i === index) cls += " current";
          if (answers[qq.id] != null && (!Array.isArray(answers[qq.id]) || answers[qq.id].length))
            cls += " answered";
          if (marked.has(qq.id)) cls += " marked";
          return `<button type="button" data-i="${i}" class="${cls.trim()}" title="Q${i + 1}">${i + 1}</button>`;
        })
        .join("");

      const answeredCount = questions.filter((qq) => {
        const a = answers[qq.id];
        return a != null && (!Array.isArray(a) || a.length);
      }).length;

      root.innerHTML = `
        <div class="toolbar">
          <span class="timer" id="mockTimer">${EVS.formatTime(remaining)}</span>
          <span class="chip">${answeredCount} / ${questions.length} answered</span>
          <span class="chip">${marked.size} marked</span>
          <span style="flex:1"></span>
          <button class="btn btn-accent" id="submitMock">Submit exam</button>
        </div>
        <div class="quiz-shell with-side">
          <div class="q-card card">
            <div class="q-meta">
              <span class="chip">Q ${index + 1}</span>
              <span class="chip">Week ${q.week}</span>
              <span class="chip ${multi ? "hot" : ""}">${multi ? "MSQ (multi-select)" : (q.type || "mcq").replace("_", " ")}</span>
              ${multi ? `<span class="sel-count">Selected: ${selCount}</span>` : ""}
            </div>
            ${
              multi
                ? `<div class="msq-banner">MSQ — Select ALL correct options
                    <span class="sub">Toggle checkboxes. Exact set required for full marks (NPTEL style).</span>
                   </div>`
                : ""
            }
            <div class="q-stem">${escapeHtml(q.stem)}</div>
            <div class="options">${optionsHtml}</div>
            <div class="actions">
              <button class="btn" id="prevQ" ${index === 0 ? "disabled" : ""}>Prev</button>
              <button class="btn btn-primary" id="nextQ">${index + 1 >= questions.length ? "Last Q" : "Save & Next"}</button>
              <button class="btn btn-ghost" id="markQ">${marked.has(q.id) ? "Unmark" : "Mark for review"}</button>
            </div>
          </div>
          <div class="card">
            <h3 style="margin-top:0">Palette</h3>
            <div class="palette">${palette}</div>
            <p style="font-size:0.8rem;color:var(--muted);margin-top:0.75rem">
              Green tint = answered · Orange ring = marked
            </p>
          </div>
        </div>`;

      root.querySelectorAll(".option").forEach((btn) => {
        btn.addEventListener("click", () => {
          const key = btn.dataset.key;
          if (multi) {
            const cur = Array.isArray(answers[q.id]) ? [...answers[q.id]] : [];
            const i = cur.indexOf(key);
            if (i >= 0) cur.splice(i, 1);
            else cur.push(key);
            answers[q.id] = cur.sort();
          } else {
            answers[q.id] = key;
          }
          render();
        });
      });
      root.querySelector("#prevQ").onclick = () => {
        if (index > 0) {
          index--;
          render();
        }
      };
      root.querySelector("#nextQ").onclick = () => {
        if (index + 1 < questions.length) {
          index++;
          render();
        }
      };
      root.querySelector("#markQ").onclick = () => {
        if (marked.has(q.id)) marked.delete(q.id);
        else marked.add(q.id);
        render();
      };
      root.querySelector("#submitMock").onclick = () => {
        if (confirm("Submit mock exam now?")) submit(false);
      };
      root.querySelectorAll(".palette button").forEach((b) => {
        b.onclick = () => {
          index = Number(b.dataset.i);
          render();
        };
      });
    }

    function submit(auto) {
      if (finished) return;
      finished = true;
      if (timerId) clearInterval(timerId);
      let correct = 0;
      const byWeek = {};
      questions.forEach((q) => {
        const ok = EVS.answersEqual(answers[q.id], q.answer);
        if (ok) correct++;
        EVS.recordAnswer(q.id, ok, q.week);
        if (!byWeek[q.week]) byWeek[q.week] = { c: 0, t: 0 };
        byWeek[q.week].t++;
        if (ok) byWeek[q.week].c++;
      });
      const result = {
        correct,
        total: questions.length,
        pct: Math.round((correct / questions.length) * 100),
        byWeek,
        t: Date.now(),
        auto: !!auto,
      };
      EVS.updateStore((s) => {
        s.mockHistory = s.mockHistory || [];
        s.mockHistory.push(result);
      });
      renderResults(result);
    }

    function renderResults(result) {
      if (!result) {
        const hist = EVS.getStore().mockHistory || [];
        result = hist[hist.length - 1];
      }
      const weekRows = Object.keys(result.byWeek || {})
        .sort((a, b) => a - b)
        .map((w) => {
          const x = result.byWeek[w];
          return `<tr><td>Week ${w}</td><td>${x.c}/${x.t}</td><td>${Math.round((x.c / x.t) * 100)}%</td></tr>`;
        })
        .join("");

      const reviewPalette = questions
        .map((q, i) => {
          const ok = EVS.answersEqual(answers[q.id], q.answer);
          return `<button type="button" data-i="${i}" class="${ok ? "ok-review" : "wrong-review"}">${i + 1}</button>`;
        })
        .join("");

      root.innerHTML = `
        <div class="card" style="text-align:center">
          <p class="chip ${result.pct >= 40 ? "ok" : "hot"}">${result.auto ? "Time up — auto submitted" : "Submitted"}</p>
          <div class="score-big">${result.correct} / ${result.total}</div>
          <p><strong>${result.pct}%</strong> · Exam target ≥40% for certificate component · Aim higher for full marks</p>
          <div class="actions" style="justify-content:center">
            <button class="btn btn-primary" id="reviewMock">Review answers</button>
            <button class="btn" id="retakeMock">Retake</button>
          </div>
        </div>
        <div class="card" style="margin-top:1rem">
          <h3 style="margin-top:0">Score by week</h3>
          <table class="compare"><thead><tr><th>Week</th><th>Score</th><th>%</th></tr></thead>
          <tbody>${weekRows}</tbody></table>
          <h3>Jump to question</h3>
          <div class="palette">${reviewPalette}</div>
          <div id="reviewPane" style="margin-top:1rem"></div>
        </div>`;

      root.querySelector("#retakeMock").onclick = () => {
        started = false;
        finished = false;
        render();
      };
      const showQ = (i) => {
        const q = questions[i];
        const ok = EVS.answersEqual(answers[q.id], q.answer);
        const your = answers[q.id];
        root.querySelector("#reviewPane").innerHTML = `
          <div class="feedback ${ok ? "ok" : "bad"}">
            <strong>Q${i + 1} · Week ${q.week} · ${ok ? "Correct" : "Wrong"}</strong>
            <p style="white-space:pre-wrap;margin:0.5rem 0">${escapeHtml(q.stem)}</p>
            <p>Your answer: <strong>${fmt(your)}</strong> · Correct: <strong>${fmt(q.answer)}</strong></p>
            <p style="margin:0">${escapeHtml(q.explanation || "")}</p>
          </div>`;
      };
      root.querySelector("#reviewMock").onclick = () => showQ(0);
      root.querySelectorAll(".palette button").forEach((b) => {
        b.onclick = () => showQ(Number(b.dataset.i));
      });
    }

    function fmt(ans) {
      if (ans == null) return "—";
      if (Array.isArray(ans)) return ans.map((x) => String(x).toUpperCase()).join(", ");
      return String(ans).toUpperCase();
    }

    function escapeHtml(str) {
      return String(str || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    }

    return { render, start };
  }

  return { create };
})();
