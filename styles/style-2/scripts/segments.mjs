// Jana tag <video> untuk setiap segmen selepas potongan (punch-in berselang-seli)
// dan peta masa sumber -> masa edit.
// Guna: node segments.mjs <tamat_sumber_s> '<[[a,b],[a,b],...]>' [masa_sumber ...]
const end = +process.argv[2];
const cuts = JSON.parse(process.argv[3]).sort((x, y) => x[0] - y[0]);
const keep = []; let t = 0;
for (const [a, b] of cuts) { if (a > t) keep.push([t, a]); t = Math.max(t, b); }
if (t < end) keep.push([t, end]);
const map = s => { let off = 0; for (const [a, b] of cuts) { if (s >= b) off += b - a; else if (s > a) return +(a - off).toFixed(3); } return +(s - off).toFixed(3); };
let at = 0;
keep.forEach(([a, b], i) => {
  const d = +(b - a).toFixed(2);
  console.log(`<video id="seg${i + 1}" class="clip seg${i % 2 ? " punch" : ""}" src="src.mp4" playsinline data-has-audio="true" data-volume="1"\n  data-start="${+at.toFixed(2)}" data-media-start="${+a.toFixed(2)}" data-duration="${d}" data-track-index="0"></video>`);
  at += d;
});
console.log(`\n<!-- jumlah tempoh: ${at.toFixed(2)} s (root data-duration) -->`);
for (const s of process.argv.slice(4)) console.log(`sumber ${s} -> edit ${map(+s)}`);
