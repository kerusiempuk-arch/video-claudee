// Jana compositions/captions.html (caption karaoke gaya style 2) dari transcript.json + captions.config.json.
// Guna: node gen-captions.mjs <projek>
// captions.config.json:
// { "cuts": [[a,b],...],                       // potongan dalam masa SUMBER
//   "end": 22.4,                                // tamat sumber yang digunakan
//   "chunks": [[idxPerkataanPertama, tamatSumber, ["Token", "[kotak]", "{serif}"]], ...] }
// Token dipadan 1:1 dengan perkataan transcript.json bermula idxPerkataanPertama (untuk masa).
// [x] = kotak putih teks hitam, {x} = serif italik dalam kotak lut sinar. Max ~4 perkataan / baris.
import fs from "node:fs";
const proj = process.argv[2];
const W = JSON.parse(fs.readFileSync(proj + "/transcript.json", "utf8"));
const cfg = JSON.parse(fs.readFileSync(proj + "/captions.config.json", "utf8"));
const CUTS = cfg.cuts.slice().sort((x, y) => x[0] - y[0]);
const map = t => { let off = 0; for (const [a, b] of CUTS) { if (t >= b) off += b - a; else if (t > a) return +(a - off).toFixed(3); } return +(t - off).toFixed(3); };
const chunks = cfg.chunks;
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const STARTS = chunks.map(([wi]) => Math.max(0, map(W[wi].start - 0.05)));
let html = "", js = "";
chunks.forEach(([wi, end, toks], i) => {
  const id = `cap${i + 1}`;
  const start = STARTS[i];
  const spans = toks.map((t, j) => {
    let cls = "w", inner = t;
    if (t.startsWith("[")) { cls = "w kw-box"; inner = t.slice(1, -1); }
    else if (t.startsWith("{")) { cls = "w kw-serif"; inner = t.slice(1, -1); }
    const wt = map(W[wi + j] ? W[wi + j].start : W[wi].start);
    js += `    tl.fromTo("#${id}-w${j}", { opacity: 0.3 }, { opacity: 1, duration: 0.1, ease: "none" }, ${Math.max(start, wt - 0.03).toFixed(2)});\n`;
    return `<span class="${cls}" id="${id}-w${j}">${esc(inner)}</span>`;
  }).join(" ");
  const dur = Math.min(map(end), STARTS[i + 1] ?? 1e9) - start;
  html += `    <div id="${id}" class="clip cap" data-start="${start}" data-duration="${dur.toFixed(2)}"><div class="cap-line">${spans}</div></div>\n`;
});
const top = cfg.top ?? 545; // y caption (px). Letak di dada, bawah muka.
const out = `<template>
  <style>
    #root { position: absolute; inset: 0; }
    .cap { position: absolute; left: 120px; top: ${top}px; width: 840px; height: 110px; z-index: 1;
      display: flex; align-items: center; justify-content: center; }
    .cap-line { font: 700 56px "Inter", sans-serif; color: #fff; text-align: center; white-space: nowrap;
      padding: 6px 22px; border-radius: 18px; background: rgba(10,14,28,.42);
      text-shadow: 0 2px 10px rgba(0,0,0,.5); }
    .w { display: inline-block; }
    .kw-box { background: #fff; color: #111; padding: 0 14px; border-radius: 10px; text-shadow: none; }
    .kw-serif { background: rgba(255,255,255,.18); color: #fff; padding: 0 14px; border-radius: 10px;
      font: italic 400 62px "Playfair Display", serif; border: 2px solid rgba(255,255,255,.45); }
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
${html}  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
${js}    window.__timelines["captions"] = tl;
  </script>
</template>
`;
fs.writeFileSync(proj + "/compositions/captions.html", out);
console.log(`ok: ${chunks.length} baris caption`);
