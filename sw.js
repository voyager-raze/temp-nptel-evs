/* NPTEL EVS — offline service worker */
const CACHE = "nptel-evs-v1";

const PRECACHE = [
  "./",
  "./index.html",
  "./assignments.html",
  "./materials.html",
  "./notes.html",
  "./transcripts.html",
  "./final.html",
  "./mock.html",
  "./css/styles.css",
  "./js/app.js",
  "./js/quiz.js",
  "./js/mock.js",
  "./js/flashcards.js",
  "./manifest.webmanifest",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./data/assignments.json",
  "./data/predicted.json",
  "./data/materials-notes.json",
  "./data/week-notes.json",
  "./data/transcript-notes.json",
  "./data/flashcards.json",
  "./data/formulas.json",
  "./data/mnemonics.json",
  "./data/weeks.json",
  "./exports/NPTEL_EVS_Complete_Practice.pdf",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(CACHE)
      .then((cache) => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);
  // Only same-origin (this GitHub Pages site)
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;

      return fetch(req)
        .then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(CACHE).then((cache) => cache.put(req, copy));
          }
          return res;
        })
        .catch(() => {
          if (req.mode === "navigate") {
            return caches.match("./index.html");
          }
          return new Response("Offline", { status: 503, statusText: "Offline" });
        });
    })
  );
});
