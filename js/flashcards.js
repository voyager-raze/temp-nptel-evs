/* Lightweight spaced-recall flashcards (SM-2 lite) */
const Flashcards = (() => {
  function create(container, cards) {
    let deck = EVS.shuffle(cards || []);
    let index = 0;
    let flipped = false;

    function dueCards() {
      const store = EVS.getStore();
      const now = Date.now();
      return (cards || []).filter((c) => {
        const st = store.flash[c.id];
        if (!st) return true;
        return (st.due || 0) <= now;
      });
    }

    function schedule(id, grade) {
      // grade: again=0, good=1, easy=2
      EVS.updateStore((s) => {
        const prev = s.flash[id] || { ef: 2.5, interval: 0, reps: 0 };
        let { ef, interval, reps } = prev;
        if (grade === 0) {
          reps = 0;
          interval = 0;
        } else {
          reps += 1;
          if (reps === 1) interval = 1;
          else if (reps === 2) interval = 3;
          else interval = Math.round(interval * ef);
          if (grade === 2) ef = Math.min(3.0, ef + 0.15);
          else ef = Math.max(1.3, ef - 0.05);
        }
        const minutes = interval === 0 ? 1 : interval * 12; // compressed for 2-day prep
        s.flash[id] = {
          ef,
          interval,
          reps,
          due: Date.now() + minutes * 60 * 1000,
          last: Date.now(),
        };
      });
    }

    function current() {
      return deck[index];
    }

    function render() {
      const c = current();
      if (!c) {
        container.innerHTML = `<div class="empty">No cards left in this filter. Reset or change week.</div>`;
        return;
      }
      container.innerHTML = `
        <div class="card">
          <div class="q-meta">
            <span class="chip">${index + 1} / ${deck.length}</span>
            <span class="chip">Week ${c.week}</span>
            ${(c.tags || []).map((t) => `<span class="chip">${t}</span>`).join("")}
          </div>
          <div class="flash-card" id="flashFace" role="button" tabindex="0">
            <div>
              <div style="font-size:1.15rem;font-weight:600;white-space:pre-wrap">${escapeHtml(
                flipped ? c.back : c.front
              )}</div>
              <div class="hint">${flipped ? "Answer revealed" : "Tap to reveal"} · <span class="kbd">Space</span></div>
            </div>
          </div>
          <div class="actions" style="justify-content:center;margin-top:1rem">
            ${
              flipped
                ? `
              <button class="btn" data-g="0" style="border-color:var(--bad);color:var(--bad)">Again</button>
              <button class="btn btn-primary" data-g="1">Good</button>
              <button class="btn btn-accent" data-g="2">Easy</button>`
                : `<button class="btn btn-primary" id="revealBtn">Reveal</button>`
            }
          </div>
        </div>`;

      const face = container.querySelector("#flashFace");
      const flip = () => {
        flipped = true;
        render();
      };
      face.addEventListener("click", () => {
        if (!flipped) flip();
      });
      const rev = container.querySelector("#revealBtn");
      if (rev) rev.addEventListener("click", flip);
      container.querySelectorAll("[data-g]").forEach((btn) => {
        btn.addEventListener("click", () => {
          schedule(c.id, Number(btn.dataset.g));
          flipped = false;
          if (index + 1 >= deck.length) {
            deck = EVS.shuffle(dueCards().length ? dueCards() : cards);
            index = 0;
          } else index++;
          render();
        });
      });
    }

    function onKey(e) {
      if (!container.isConnected) return;
      if (e.key === " " || e.key === "Enter") {
        e.preventDefault();
        if (!flipped) {
          flipped = true;
          render();
        }
      }
    }
    document.addEventListener("keydown", onKey);

    return {
      setCards(list, dueOnly = false) {
        cards = list;
        deck = EVS.shuffle(dueOnly ? dueCards() : list);
        if (!deck.length) deck = EVS.shuffle(list);
        index = 0;
        flipped = false;
        render();
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
      .replace(/>/g, "&gt;");
  }

  return { create };
})();
