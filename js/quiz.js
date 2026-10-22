/* Interactive MCQ / MSQ / assertion-reason engine */
const QuizEngine = (() => {
  function create(container, opts = {}) {
    const state = {
      questions: opts.questions || [],
      index: 0,
      mode: opts.mode || "practice", // practice | quiz | rapid
      selections: {}, // id -> key or key[]
      revealed: {},
      score: { correct: 0, total: 0 },
      onComplete: opts.onComplete || null,
      title: opts.title || "Practice",
    };

    function current() {
      return state.questions[state.index];
    }

    function isMSQ(q) {
      return (
        q.multi === true ||
        q.type === "msq" ||
        Array.isArray(q.answer)
      );
    }

    function render() {
      const q = current();
      if (!q) {
        container.innerHTML = `<div class="empty">No questions in this set.</div>`;
        return;
      }
      const sel = state.selections[q.id];
      const revealed = !!state.revealed[q.id];
      const multi = isMSQ(q);
      const selList = multi
        ? Array.isArray(sel)
          ? sel
          : []
        : sel
          ? [sel]
          : [];

      const optionsHtml = (q.options || [])
        .map((o) => {
          const key = String(o.key).toLowerCase();
          let cls = `option ${multi ? "msq-opt" : "mcq-opt"}`;
          const selected = multi
            ? Array.isArray(sel) && sel.includes(key)
            : sel === key;
          if (selected) cls += " selected";
          if (revealed) {
            const ans = EVS.normalizeAnswer(q.answer);
            const isCorrect = multi
              ? Array.isArray(ans) && ans.includes(key)
              : ans === key;
            if (isCorrect) cls += " correct";
            else if (selected) cls += " wrong";
          }
          const mark = selected ? "✓" : "";
          return `<button type="button" class="${cls}" data-key="${key}" aria-pressed="${selected}">
            <span class="mark" aria-hidden="true">${mark}</span>
            <span class="key">${key.toUpperCase()}</span>
            <span>${escapeHtml(o.text)}</span>
          </button>`;
        })
        .join("");

      let feedback = "";
      if (revealed) {
        const ok = EVS.answersEqual(sel, q.answer);
        let detail = "";
        if (multi && !ok) {
          const correct = new Set(EVS.normalizeAnswer(q.answer) || []);
          const chosen = new Set(EVS.normalizeAnswer(sel) || []);
          const missing = [...correct].filter((x) => !chosen.has(x));
          const extra = [...chosen].filter((x) => !correct.has(x));
          detail = `<p style="margin:0.4rem 0 0;font-size:0.9rem">
            ${missing.length ? `Missing: <strong>${missing.map((x) => x.toUpperCase()).join(", ")}</strong>. ` : ""}
            ${extra.length ? `Extra (incorrect): <strong>${extra.map((x) => x.toUpperCase()).join(", ")}</strong>.` : ""}
            MSQ needs the <em>exact</em> set of correct options.
          </p>`;
        }
        feedback = `<div class="feedback ${ok ? "ok" : "bad"}">
          <strong>${ok ? "Correct" : "Not quite"}.</strong>
          ${multi ? "Correct options" : "Answer"}: <strong>${formatAnswer(q.answer)}</strong>
          ${detail}
          <p style="margin:0.5rem 0 0">${escapeHtml(q.explanation || "")}</p>
          ${q.verified === false ? '<p class="chip hot" style="margin-top:0.5rem">Week 2: answer not officially verified</p>' : ""}
        </div>`;
      }

      const msqBanner = multi
        ? `<div class="msq-banner">MSQ — Select ALL correct options
            <span class="sub">Tap options to toggle on/off (checkboxes). Partial sets score as wrong — same as NPTEL.</span>
           </div>`
        : "";

      container.innerHTML = `
        <div class="q-card card">
          <div class="q-meta">
            <span class="chip">Q ${state.index + 1} / ${state.questions.length}</span>
            <span class="chip">Week ${q.week || "?"}</span>
            <span class="chip ${multi ? "hot" : ""}">${multi ? "MSQ (multi-select)" : (q.type || "mcq").replace("_", " ")}</span>
            ${trustChip(q)}
            ${q.likelihood ? `<span class="chip hot">${q.likelihood} chance</span>` : ""}
            ${multi ? `<span class="sel-count">Selected: ${selList.length}</span>` : ""}
          </div>
          ${msqBanner}
          <div class="q-stem">${escapeHtml(q.stem)}</div>
          <div class="options">${optionsHtml}</div>
          ${feedback}
          <div class="actions" style="margin-top:1rem">
            ${
              state.mode === "practice" && !revealed
                ? `<button class="btn btn-primary" id="qCheck">Check${multi ? " all selected" : ""}</button>`
                : ""
            }
            ${
              state.mode === "practice" && revealed
                ? `<button class="btn btn-primary" id="qNext">Next <span class="kbd">N</span></button>`
                : ""
            }
            ${
              state.mode !== "practice"
                ? `<button class="btn btn-primary" id="qNext">${
                    state.index + 1 >= state.questions.length ? "Finish" : "Next"
                  } <span class="kbd">N</span></button>`
                : ""
            }
            <button class="btn btn-ghost" id="qPrev" ${state.index === 0 ? "disabled" : ""}>Prev</button>
            <button class="btn btn-ghost" id="qFlag">Flag weak</button>
            <span style="flex:1"></span>
            <span class="chip">Keys: <span class="kbd">1-4</span> ${multi ? "toggle" : "select"} · <span class="kbd">N</span> next</span>
          </div>
        </div>`;

      container.querySelectorAll(".option").forEach((btn) => {
        btn.addEventListener("click", () => {
          if (state.mode === "practice" && state.revealed[q.id]) return;
          const key = btn.dataset.key;
          if (multi) {
            const cur = Array.isArray(state.selections[q.id])
              ? [...state.selections[q.id]]
              : [];
            const i = cur.indexOf(key);
            if (i >= 0) cur.splice(i, 1);
            else cur.push(key);
            state.selections[q.id] = cur.sort();
          } else {
            state.selections[q.id] = key;
          }
          render();
        });
      });

      const check = container.querySelector("#qCheck");
      if (check) check.addEventListener("click", () => checkAnswer());
      const next = container.querySelector("#qNext");
      if (next) next.addEventListener("click", () => goNext());
      const prev = container.querySelector("#qPrev");
      if (prev) prev.addEventListener("click", () => {
        if (state.index > 0) {
          state.index--;
          render();
        }
      });
      const flag = container.querySelector("#qFlag");
      if (flag) flag.addEventListener("click", () => {
        EVS.markWeak(q.id, true);
        flag.textContent = "Flagged";
      });
    }

    function checkAnswer() {
      const q = current();
      if (!q) return;
      if (state.selections[q.id] == null || (Array.isArray(state.selections[q.id]) && !state.selections[q.id].length)) {
        alert("Select an option first.");
        return;
      }
      state.revealed[q.id] = true;
      const ok = EVS.answersEqual(state.selections[q.id], q.answer);
      EVS.recordAnswer(q.id, ok, q.week);
      if (ok) state.score.correct++;
      state.score.total++;
      render();
    }

    function goNext() {
      const q = current();
      if (state.mode !== "practice" && q && state.selections[q.id] != null) {
        // record on leave for quiz/rapid
        if (!state.revealed[q.id]) {
          const ok = EVS.answersEqual(state.selections[q.id], q.answer);
          EVS.recordAnswer(q.id, ok, q.week);
          state.revealed[q.id] = true;
          if (ok) state.score.correct++;
          state.score.total++;
        }
      }
      if (state.index + 1 >= state.questions.length) {
        finish();
        return;
      }
      state.index++;
      render();
    }

    function finish() {
      // grade unanswered in quiz mode
      if (state.mode !== "practice") {
        state.questions.forEach((q) => {
          if (!state.revealed[q.id] && state.selections[q.id] != null) {
            const ok = EVS.answersEqual(state.selections[q.id], q.answer);
            EVS.recordAnswer(q.id, ok, q.week);
            if (ok) state.score.correct++;
            state.score.total++;
            state.revealed[q.id] = true;
          }
        });
      }
      const total = state.questions.length;
      const correct = state.questions.filter((q) =>
        EVS.answersEqual(state.selections[q.id], q.answer)
      ).length;
      container.innerHTML = `
        <div class="card" style="text-align:center">
          <p class="chip ok">Session complete</p>
          <div class="score-big">${correct} / ${total}</div>
          <p>${Math.round((correct / Math.max(total, 1)) * 100)}% · Review weak flags on Home</p>
          <div class="actions" style="justify-content:center">
            <button class="btn btn-primary" id="restartQuiz">Try again</button>
            <button class="btn" id="reviewWrong">Review wrong</button>
          </div>
        </div>`;
      container.querySelector("#restartQuiz").addEventListener("click", () => {
        state.index = 0;
        state.selections = {};
        state.revealed = {};
        state.score = { correct: 0, total: 0 };
        render();
      });
      container.querySelector("#reviewWrong").addEventListener("click", () => {
        const wrong = state.questions.filter(
          (q) => !EVS.answersEqual(state.selections[q.id], q.answer)
        );
        if (!wrong.length) {
          alert("No wrong answers — nice!");
          return;
        }
        state.questions = wrong;
        state.index = 0;
        state.selections = {};
        state.revealed = {};
        state.mode = "practice";
        render();
      });
      if (state.onComplete) state.onComplete({ correct, total });
    }

    function onKey(e) {
      if (!container.isConnected) return;
      const q = current();
      if (!q) return;
      if (["1", "2", "3", "4"].includes(e.key)) {
        const opts = q.options || [];
        const idx = Number(e.key) - 1;
        if (opts[idx]) {
          const key = String(opts[idx].key).toLowerCase();
          if (isMSQ(q)) {
            const cur = Array.isArray(state.selections[q.id])
              ? [...state.selections[q.id]]
              : [];
            const i = cur.indexOf(key);
            if (i >= 0) cur.splice(i, 1);
            else cur.push(key);
            state.selections[q.id] = cur.sort();
          } else {
            state.selections[q.id] = key;
          }
          render();
        }
      }
      if (e.key === "n" || e.key === "N" || e.key === "Enter") {
        if (state.mode === "practice" && !state.revealed[q.id]) checkAnswer();
        else goNext();
      }
    }

    document.addEventListener("keydown", onKey);

    return {
      setQuestions(qs) {
        state.questions = (qs || []).map((q) =>
          typeof EVS.normalizeQuestion === "function" ? EVS.normalizeQuestion(q) : q
        );
        state.index = 0;
        state.selections = {};
        state.revealed = {};
        render();
      },
      setMode(m) {
        state.mode = m;
      },
      render,
      destroy() {
        document.removeEventListener("keydown", onKey);
      },
    };
  }

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function formatAnswer(ans) {
    if (Array.isArray(ans)) return ans.map((x) => String(x).toUpperCase()).join(", ");
    if (ans == null) return "(unknown)";
    return String(ans).toUpperCase();
  }

  function trustChip(q) {
    let t = q.trust;
    if (!t) {
      if (q.source === "predicted" || String(q.id || "").startsWith("p")) t = "predicted";
      else if (q.verified === false) t = "best_guess";
      else t = "pdf_verified";
    }
    if (t === "pdf_verified") return `<span class="chip ok">PDF-verified</span>`;
    if (t === "best_guess") return `<span class="chip hot">Best-guess (no key in PDF)</span>`;
    return `<span class="chip">Predicted practice</span>`;
  }

  return { create };
})();
