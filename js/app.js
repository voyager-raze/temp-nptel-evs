/* Shared utilities, theme, progress for NPTEL EVS Practice App */
const EVS = (() => {
  const STORE_KEY = "nptel-evs-progress-v1";

  function loadStore() {
    try {
      return JSON.parse(localStorage.getItem(STORE_KEY)) || defaultStore();
    } catch {
      return defaultStore();
    }
  }

  function defaultStore() {
    return {
      theme: "light",
      weakIds: [],
      answered: {},
      notesRead: { materials: [], transcripts: [], notes: [] },
      flash: {},
      mockHistory: [],
      checklist: {},
    };
  }

  function saveStore(data) {
    localStorage.setItem(STORE_KEY, JSON.stringify(data));
  }

  function getStore() {
    return loadStore();
  }

  function updateStore(mutator) {
    const s = loadStore();
    mutator(s);
    saveStore(s);
    return s;
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme === "dark" ? "dark" : "light");
    updateStore((s) => {
      s.theme = theme;
    });
  }

  function initTheme() {
    const s = loadStore();
    applyTheme(s.theme || "light");
  }

  function toggleTheme() {
    const cur = document.documentElement.getAttribute("data-theme");
    applyTheme(cur === "dark" ? "light" : "dark");
  }

  async function fetchJSON(path) {
    const res = await fetch(path);
    if (!res.ok) throw new Error(`Failed to load ${path}`);
    return res.json();
  }

  function markWeak(id, isWeak) {
    updateStore((s) => {
      const set = new Set(s.weakIds || []);
      if (isWeak) set.add(id);
      else set.delete(id);
      s.weakIds = [...set];
    });
  }

  function recordAnswer(id, correct, week) {
    updateStore((s) => {
      s.answered[id] = { correct: !!correct, week, t: Date.now() };
      if (!correct) {
        const set = new Set(s.weakIds || []);
        set.add(id);
        s.weakIds = [...set];
      }
    });
  }

  function markNoteRead(kind, key) {
    updateStore((s) => {
      if (!s.notesRead[kind]) s.notesRead[kind] = [];
      if (!s.notesRead[kind].includes(key)) s.notesRead[kind].push(key);
    });
  }

  function progressStats(assignmentCount = 200, predictedCount = 120) {
    const s = loadStore();
    const answered = Object.keys(s.answered || {}).length;
    const correct = Object.values(s.answered || {}).filter((x) => x.correct).length;
    const mats = (s.notesRead.materials || []).length;
    const trans = (s.notesRead.transcripts || []).length;
    const flashDone = Object.keys(s.flash || {}).length;
    return {
      answered,
      correct,
      accuracy: answered ? Math.round((correct / answered) * 100) : 0,
      materialsRead: mats,
      transcriptsRead: trans,
      flashDone,
      weakCount: (s.weakIds || []).length,
      mocks: (s.mockHistory || []).length,
      totalPractice: assignmentCount + predictedCount,
    };
  }

  function weekWeakMap() {
    const s = loadStore();
    const map = {};
    for (const [id, info] of Object.entries(s.answered || {})) {
      if (!info.correct && info.week) {
        map[info.week] = (map[info.week] || 0) + 1;
      }
    }
    return map;
  }

  function normalizeAnswer(ans) {
    if (Array.isArray(ans)) return ans.map((x) => String(x).toLowerCase()).sort();
    if (ans == null) return null;
    return String(ans).toLowerCase();
  }

  function answersEqual(user, correct) {
    const a = normalizeAnswer(user);
    const b = normalizeAnswer(correct);
    if (a == null || b == null) return false;
    if (Array.isArray(a) || Array.isArray(b)) {
      const aa = Array.isArray(a) ? a : [a];
      const bb = Array.isArray(b) ? b : [b];
      return aa.length === bb.length && aa.every((v, i) => v === bb[i]);
    }
    return a === b;
  }

  function shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function normalizeQuestion(q) {
    const copy = { ...q };
    if (Array.isArray(copy.answer)) {
      copy.answer = copy.answer.map((x) => String(x).toLowerCase()).sort();
      copy.type = "msq";
      copy.multi = true;
    } else if (copy.answer != null) {
      copy.answer = String(copy.answer).toLowerCase();
      copy.multi = copy.multi === true || copy.type === "msq";
      if (copy.type === "msq" && !Array.isArray(copy.answer)) {
        copy.answer = [copy.answer];
        copy.multi = true;
      }
    }
    if (copy.options) {
      copy.options = copy.options.map((o) => ({
        ...o,
        key: String(o.key).toLowerCase(),
      }));
    }
    return copy;
  }

  function flattenAssignments(data) {
    const out = [];
    for (const w of data.weeks || []) {
      for (const q of w.questions || []) {
        out.push(
          normalizeQuestion({
            ...q,
            week: w.week,
            weekTitle: w.title,
            source: "assignment",
          })
        );
      }
    }
    return out;
  }

  function setActiveNav() {
    const page = (location.pathname.split("/").pop() || "index.html").toLowerCase();
    document.querySelectorAll(".nav a").forEach((a) => {
      const href = (a.getAttribute("href") || "").toLowerCase();
      a.classList.toggle("active", href === page || (page === "" && href === "index.html"));
    });
  }

  function renderNav(active) {
    /* pages include static nav; just highlight */
    setActiveNav();
    const btn = document.getElementById("themeToggle");
    if (btn) btn.addEventListener("click", toggleTheme);
  }

  function formatTime(sec) {
    const h = Math.floor(sec / 3600);
    const m = Math.floor((sec % 3600) / 60);
    const s = sec % 60;
    if (h > 0) return `${h}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
    return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  }

  return {
    fetchJSON,
    getStore,
    updateStore,
    initTheme,
    toggleTheme,
    markWeak,
    recordAnswer,
    markNoteRead,
    progressStats,
    weekWeakMap,
    answersEqual,
    normalizeAnswer,
    shuffle,
    flattenAssignments,
    normalizeQuestion,
    renderNav,
    formatTime,
  };
})();

document.addEventListener("DOMContentLoaded", () => {
  EVS.initTheme();
  EVS.renderNav();
});
