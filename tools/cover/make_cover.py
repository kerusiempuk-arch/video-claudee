"""Cover photo TikTok (1080×1920) – frame yang nampak produk + nama produk. Untuk SEMUA style.

Guna (dari root repo):
  python3 -I tools/cover/make_cover.py <video> <masa_s> <output.png> --title "Extension Wire." \
      [--kicker "Surge protector · SIRIM"] [--pills "5 Soket,3 Pin,Wire panjang"] [--pos bottom|top] [--y 1330] [--bright 0.06]

- Pilih frame: produk jelas & penuh, muka pandang kamera, tak kabur (bandingkan beberapa masa berdekatan dulu).
- --pos bottom (default): teks di bawah produk; --pos top: teks di atas (bila produk/muka di bawah).
  --y = atas blok teks (default 1330 bottom / 260 top). Kekal dalam 240–1680 px (cover dipotong 3:4 di grid profil).
- Pil pertama kuning, lain putih. JANGAN reka fakta: hanya yang disebut dalam video / disahkan owner.
"""
import argparse, html, os, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
a = argparse.ArgumentParser()
a.add_argument("video"); a.add_argument("t", type=float); a.add_argument("out")
a.add_argument("--title", required=True); a.add_argument("--kicker", default=""); a.add_argument("--pills", default="")
a.add_argument("--pos", default="bottom", choices=["bottom", "top"]); a.add_argument("--y", type=int)
a.add_argument("--bright", type=float, default=0.06)
o = a.parse_args()
y = o.y if o.y is not None else (1330 if o.pos == "bottom" else 260)
tmp = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(o.t), "-i", o.video, "-frames:v", "1", "-vf",
                f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,eq=brightness={o.bright}:saturation=1.1",
                os.path.join(tmp, "f.png")], check=True)
shutil.copyfile(os.path.join(HERE, "PlusJakartaSans.ttf"), os.path.join(tmp, "J.ttf"))
e = html.escape
pills = [p.strip() for p in o.pills.split(",") if p.strip()]
grad = ("top:1080px;height:840px;background:linear-gradient(0deg,rgba(18,20,26,.92) 0%,rgba(18,20,26,.75) 50%,rgba(18,20,26,0) 100%)"
        if o.pos == "bottom" else
        "top:0;height:840px;background:linear-gradient(180deg,rgba(18,20,26,.92) 0%,rgba(18,20,26,.75) 50%,rgba(18,20,26,0) 100%)")
fs = 138 if len(o.title) <= 15 else max(84, int(138 * 15 / len(o.title)))
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:J;font-weight:200 800;src:url(J.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#000;font-family:J,sans-serif}}
.bg{{position:absolute;inset:0;background:url(f.png) center/cover}}
.sh{{position:absolute;left:0;width:1080px;{grad}}}
.box{{position:absolute;left:0;top:{y}px;width:1080px;display:flex;flex-direction:column;align-items:center}}
.k{{font-weight:700;font-size:32px;letter-spacing:10px;color:rgba(255,255,255,.9);text-transform:uppercase}}
.t{{margin-top:8px;font-weight:800;font-size:{fs}px;line-height:1;letter-spacing:-4px;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.5);white-space:nowrap}}
.r{{margin-top:30px;display:flex;flex-wrap:wrap;justify-content:center;gap:16px;max-width:1000px}}
.p{{height:76px;padding:0 34px;border-radius:38px;background:#fff;color:#15171C;display:flex;align-items:center;font-weight:800;font-size:38px;box-shadow:0 10px 26px rgba(0,0,0,.3)}}
.p:first-child{{background:#FFD21F}}
</style></head><body><div class="bg"></div><div class="sh"></div><div class="box">
{f'<div class="k">{e(o.kicker)}</div>' if o.kicker else ''}<div class="t">{e(o.title)}</div>
{('<div class="r">' + ''.join(f'<div class="p">{e(p)}</div>' for p in pills) + '</div>') if pills else ''}
</div></body></html>"""
open(os.path.join(tmp, "c.html"), "w").write(page)
js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
      "const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.argv[1]);"
      "await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);"
      "await p.screenshot({path:process.argv[2]});await b.close()})()")
subprocess.run(["node", "-e", js, os.path.join(tmp, "c.html"), os.path.abspath(o.out)], check=True)
shutil.rmtree(tmp)
print("->", o.out)
