"""Style 1 – cover photo TikTok (1080×1920 PNG) dari video mentah + COVER dalam config projek.

Guna (dari root repo):
  python3 -I styles/style-1/tools/cover.py <raw.mp4> <projects/nama.py> <out_dir>
    -> <out_dir>/cover.png (cover pertama), cover2.png, cover3.png …

Config projek:
  COVERS = [dict(
      at=4.2,                                  # saat dalam video ASAL (pilih frame muka + produk jelas)
      kicker="sabun pencuci pinggan,",         # teks kecil atas
      title="senang",                          # tajuk besar + titik merah
      stickers=["cepat berbuih", "minyak hilang terus ✓"],   # 0–3 sticker putih condong (dari apa yang DISEBUT)
      pill="tip 1-3 · cara cuci senang",       # label monospace gelap (pilihan; nombor biru); None = tiada
      shift=330,                               # gambar diturunkan (px) supaya tajuk tak tutup muka
  ), ...]
Reka letak: atas putih (gradient Style 1) + kicker + tajuk; sticker kiri y≈1060; pil y≈1600.
Frame suram (YAVG < 130) dicerahkan automatik (atau beri brighten="eq=…" sendiri).
"""
import html, os, re, runpy, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
RAW, PROJ, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
C = runpy.run_path(PROJ)
covers = C.get("COVERS") or ([C["COVER"]] if "COVER" in C else [])
if not covers:
    sys.exit("Tiada COVERS dalam config projek.")
os.makedirs(OUT, exist_ok=True)
esc = html.escape

CSS = """
@font-face{font-family:I;font-weight:500;src:url(Inter-Medium.otf)}
@font-face{font-family:I;font-weight:600;src:url(Inter-SemiBold.otf)}
@font-face{font-family:D;font-weight:700;src:url(InterDisplay-Bold.otf)}
@font-face{font-family:M;font-weight:500;src:url(JetBrainsMono-Medium.ttf)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;position:relative;background:#f6f7fa}
#bg{position:absolute;left:0;width:1080px;height:1920px;background:url(bg.jpg) center/cover}
#grad{position:absolute;left:0;top:0;width:1080px;height:860px;background:linear-gradient(180deg,rgba(246,247,250,1) 0%,rgba(246,247,250,1) 38%,rgba(246,247,250,.5) 66%,rgba(246,247,250,0) 100%)}
.kick{position:absolute;top:150px;width:1080px;text-align:center;font:500 46px I;color:#16161a}
.big{position:absolute;top:205px;width:1080px;display:flex;justify-content:center}
.big span{position:relative;font:700 FSpx/1 D;letter-spacing:-3px;color:#16161a;left:-18px;white-space:nowrap}
.big b{position:absolute;right:-46px;bottom:.13em;width:38px;height:38px;background:#e5484d}
.stk{position:absolute;height:84px;padding:0 26px;border-radius:10px;background:#fff;display:flex;align-items:center;font:600 48px I;color:#16161a;white-space:nowrap;box-shadow:0 6px 18px rgba(0,0,0,.35)}
.pill{position:absolute;left:60px;top:1600px;height:62px;padding:0 18px;border-radius:9px;background:rgba(24,24,28,.92);font:500 36px/62px M;color:#fff;white-space:pre}
.pill em{font-style:normal;color:#6e7bff}
"""
STK_POS = [(40, 1060, -2.0), (60, 1165, 1.5), (80, 1270, -1.5)]


def luma(img):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", img, "-vf", "scale=270:-1,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-",
                          "-f", "null", "-"], capture_output=True, text=True).stdout
    v = [float(l.split("=")[1]) for l in out.splitlines() if "YAVG=" in l]
    return v[0] if v else 128.0


for n, cv in enumerate(covers, 1):
    tmp = tempfile.mkdtemp()
    for f in os.listdir(FONTS):
        shutil.copyfile(os.path.join(FONTS, f), os.path.join(tmp, f))
    raw_png = os.path.join(tmp, "raw.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(cv["at"]), "-i", RAW, "-frames:v", "1", "-vf", "scale=1080:1920", raw_png], check=True)
    eq = cv.get("brighten") or ("eq=brightness=0.06:gamma=1.25:saturation=1.1" if luma(raw_png) < 130 else "null")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw_png, "-vf", eq, "-q:v", "2", os.path.join(tmp, "bg.jpg")], check=True)
    title = cv["title"]
    fs = min(230, int(820 / (0.56 * max(1, len(title)))))   # tajuk panjang -> font kecil
    body = [f'<div id="bg" style="top:{cv.get("shift", 330)}px"></div><div id="grad"></div>',
            f'<div class="kick">{esc(cv.get("kicker", ""))}</div>',
            f'<div class="big"><span>{esc(title)}<b></b></span></div>']
    for (x, y, a), s in zip(STK_POS, cv.get("stickers", [])):
        body.append(f'<div class="stk" style="left:{x}px;top:{y}px;transform:rotate({a}deg)">{esc(s)}</div>')
    if cv.get("pill"):
        pill = re.sub(r"(\d+)", r"<em>\1</em>", esc(cv["pill"]))
        body.append(f'<div class="pill">{pill}</div>')
    page = os.path.join(tmp, "cover.html")
    open(page, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS.replace("FS", str(fs))}</style></head>'
                          f'<body>{"".join(body)}</body></html>')
    out = os.path.join(os.path.abspath(OUT), "cover.png" if n == 1 else f"cover{n}.png")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          "const p=await b.newPage({viewport:{width:1080,height:1920}});"
          f"await p.goto('file://{page}');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);"
          f"await p.screenshot({{path:'{out}'}});await b.close()}})()")
    subprocess.run(["node", "-e", js], check=True, cwd=tmp)
    shutil.rmtree(tmp, ignore_errors=True)
    print("->", out)
