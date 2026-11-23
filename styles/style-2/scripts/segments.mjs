// Jana tag <video> untuk setiap segmen selepas potongan (punch-in berselang-seli)
// dan peta masa sumber -> masa edit.
// Guna: node segments.mjs <tamat_sumber_s> '<[[a,b],[a,b],...]>' [--voice] [masa_sumber ...]
// --voice: video dibisukan + <audio src="voice.m4a"> (suara bersih dari clean-voice.sh) dipotong sama.
const end = +process.argv[2];
const cuts = JSON.parse(process.argv[3]).sort((x, y) => x[0] - y[0]);
const VOICE = process.argv.includes("--voice");
const times = process.argv.slice(4).filter(a => a !== "--voice");
const keep = []; let t = 0;
for (const [a, b] of cuts) { if (a > t) keep.push([t, a]); t = Math.max(t, b); }
if (t < end) keep.push([t, end]);
const map = s => { let off = 0; for (const [a, b] of cuts) { if (s >= b) off += b - a; else if (s > a) return +(a - off).toFixed(3); } return +(s - off).toFixed(3); };
let at = 0;
keep.forEach(([a, b], i) => {
  const d = +(b - a).toFixed(2);
  const st = +at.toFixed(2), ms = +a.toFixed(2);
  const snd = VOICE ? `muted` : `data-has-audio="true" data-volume="1"`;
  console.log(`<video id="seg${i + 1}" class="clip seg${i % 2 ? " punch" : ""}" src="src.mp4" playsinline ${snd}\n  data-start="${st}" data-media-start="${ms}" data-duration="${d}" data-track-index="0"></video>`);
  if (VOICE) console.log(`<audio id="vo${i + 1}" src="voice.m4a" data-start="${st}" data-media-start="${ms}" data-duration="${d}" data-volume="1" data-fade-in="0.015" data-fade-out="${i === keep.length - 1 ? 0.4 : 0.015}" data-track-index="1"></audio>`);
  at += d;
});
console.log(`\n<!-- jumlah tempoh: ${at.toFixed(2)} s (root data-duration) -->`);
for (const s of times) console.log(`sumber ${s} -> edit ${map(+s)}`);
