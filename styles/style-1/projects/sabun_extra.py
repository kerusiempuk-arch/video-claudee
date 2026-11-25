"""Tambahan khas video sabun (ikut video rujukan rak besi) – TIDAK mengubah Style 1.
Jalankan selepas build.py:  python3 -I styles/style-1/projects/sabun_extra.py styles/style-1/projects/sabun.py work/sabun/hf

1. Kad hook muat 3 pilihan (build.py asal: tinggi 190px untuk 2 pilihan).
2. BIG_WORDS: perkataan besar hitam + titik merah muncul sekejap di tengah video.
"""
import html, os, re, runpy, sys

C = runpy.run_path(sys.argv[1])
W = sys.argv[2]
comp = os.path.join(W, "compositions")

# 1. kad hook 3 pilihan
n = len(C["HOOK"]["options"])
if n > 2:
    h = 60 + n * 62 + 10
    p = os.path.join(comp, "hook.html")
    s = open(p).read()
    s = s.replace("height:190px", f"height:{h}px").replace('class="win" style="height:190px"', f'class="win" style="height:{h}px"')
    s = s.replace('<div class="win" style="height:190px">', f'<div class="win" style="height:{h}px">')
    open(p, "w").write(s)

# 2. perkataan besar
words = C.get("BIG_WORDS", [])
if words:
    p = os.path.join(comp, "stickers.html")
    s = open(p).read()
    css = """
    .bw { position: absolute; left: 0; top: 230px; width: 1080px; height: 220px; display: flex; justify-content: center; align-items: center; }
    .bw span { position: relative; font-family: "S1 Display"; font-weight: 700; font-size: 170px; color: rgb(22,22,26); line-height: 1;
      letter-spacing: -1px; text-shadow: 0 0 30px rgba(255,255,255,.55); }
    .bw b { position: absolute; right: -36px; bottom: 0.13em; width: 28px; height: 28px; background: rgb(229,72,77); }"""
    body, js = "", ""
    for i, (a0, a1, w, dot) in enumerate(words):
        body += (f'    <div id="bw{i}" class="clip" data-start="{a0:.3f}" data-duration="{a1 - a0:.3f}">'
                 f'<div class="bw"><span id="bw{i}-in">{html.escape(w)}{"<b></b>" if dot else ""}</span></div></div>\n')
        js += (f'    tl.fromTo("#bw{i}-in", {{ opacity: 0, scale: 1.25 }}, {{ opacity: 1, scale: 1, duration: 0.18, ease: "power3.out" }}, {a0:.3f});\n'
               f'    tl.to("#bw{i}-in", {{ opacity: 0, duration: 0.15, ease: "power2.in" }}, {a1 - 0.15:.3f});\n')
    s = s.replace("  </style>", css + "\n  </style>", 1)
    s = s.replace("  </div>\n  <script>", body + "  </div>\n  <script>", 1)
    s = re.sub(r'(    window\.__timelines\["stickers"\])', js + r"\1", s, count=1)
    open(p, "w").write(s)
print("sabun_extra: siap")
