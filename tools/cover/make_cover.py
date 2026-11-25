"""Cover photo TikTok (1080×1920) – frame yang nampak produk + nama produk, dalam FONT & GAYA style video itu.

Guna (dari root repo):
  python3 -I tools/cover/make_cover.py <video> <masa_s> <output.png> --style 1|2|3 --title "<Nama produk>" \
      [--kicker "..."] [--pills "a,b,c"] [--pos bottom|top] [--y PX] [--bright 0.06]

Gaya (sama dengan grafik dalam video):
  --style 1  Product Explainer: kicker Inter 500 hitam + tajuk besar Inter Display Bold hitam dengan TITIK MERAH segi empat,
             kad gelap macOS (titik merah/kuning/hijau) dengan nama produk, tag monospace "a · b · c" (maks 3),
             butang kuning "Tekan beg kuning ↓". Latar putih lembut di belakang tajuk supaya teks hitam jelas.
             --title = 1 perkataan untuk tajuk besar (titik ditambah auto); --name = nama produk dalam kad (default --title).
  --style 2  Review: kad putih bucu bulat, kicker JetBrains Mono biru #2F6BFF, tajuk Inter 700 hitam dengan *satu perkataan*
             serif italik biru (Playfair Display), chip kelabu (--pills), pil hook putih "✳ review **produk**" di atas kad.
  --style 3  Tajuk atas/bawah: label kecil berjarak + tajuk besar Plus Jakarta Sans 800 bertitik, pil (pertama kuning),
             gradien gelap.
- Pilih frame: produk jelas & penuh, muka pandang kamera, tak kabur (bandingkan beberapa masa berdekatan dulu).
- --pos bottom (default) = blok teks di bawah produk; top = di atas. --y = atas blok (kekal dalam 240–1680 px, cover dipotong 3:4).
- JANGAN reka fakta: hanya yang disebut dalam video / disahkan owner.
"""
import argparse, html, os, re, shutil, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
a = argparse.ArgumentParser()
a.add_argument("video"); a.add_argument("t", type=float); a.add_argument("out")
a.add_argument("--style", required=True, choices=["1", "2", "3"])
a.add_argument("--title", required=True); a.add_argument("--name", default="")
a.add_argument("--kicker", default=""); a.add_argument("--pills", default="")
a.add_argument("--pos", default="bottom", choices=["bottom", "top"]); a.add_argument("--y", type=int)
a.add_argument("--bright", type=float, default=0.06)
o = a.parse_args()
e = html.escape
pills = [p.strip() for p in o.pills.split(",") if p.strip()]
bottom = o.pos == "bottom"

FONTS = """
@font-face{font-family:J;font-weight:200 800;src:url(fonts/PlusJakartaSans.ttf)}
@font-face{font-family:"S1 Inter";font-weight:500;src:url(fonts/Inter-Medium.otf)}
@font-face{font-family:"S1 Inter";font-weight:700;src:url(fonts/Inter-Bold.otf)}
@font-face{font-family:"S1 Display";font-weight:700;src:url(fonts/InterDisplay-Bold.otf)}
@font-face{font-family:"S1 Mono";font-weight:500;src:url(fonts/JetBrainsMono-Medium.ttf)}
@font-face{font-family:"Playfair";font-style:italic;font-weight:400 900;src:url(fonts/PlayfairDisplay-Italic.ttf)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:#000}
.bg{position:absolute;inset:0;background:url(f.png) center/cover}
.sh{position:absolute;left:0;width:1080px;height:840px}
"""


def grad(rgb, a1, a2):
    d = "0deg" if bottom else "180deg"
    return (f'top:{1080 if bottom else 0}px;background:linear-gradient({d},rgba({rgb},{a1}) 0%,rgba({rgb},{a2}) 50%,rgba({rgb},0) 100%)')


def style3():
    y = o.y if o.y is not None else (1330 if bottom else 260)
    fs = 138 if len(o.title) <= 15 else max(84, int(138 * 15 / len(o.title)))
    css = f"""
.sh{{{grad("18,20,26", .92, .75)}}}
.box{{position:absolute;left:0;top:{y}px;width:1080px;display:flex;flex-direction:column;align-items:center;font-family:J,sans-serif}}
.k{{font-weight:700;font-size:32px;letter-spacing:10px;color:rgba(255,255,255,.9);text-transform:uppercase}}
.t{{margin-top:8px;font-weight:800;font-size:{fs}px;line-height:1;letter-spacing:-4px;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.5);white-space:nowrap}}
.r{{margin-top:30px;display:flex;flex-wrap:wrap;justify-content:center;gap:16px;max-width:1000px}}
.p{{height:76px;padding:0 34px;border-radius:38px;background:#fff;color:#15171C;display:flex;align-items:center;font-weight:800;font-size:38px;box-shadow:0 10px 26px rgba(0,0,0,.3)}}
.p:first-child{{background:#FFD21F}}"""
    body = ('<div class="box">' + (f'<div class="k">{e(o.kicker)}</div>' if o.kicker else "") + f'<div class="t">{e(o.title)}</div>'
            + (('<div class="r">' + "".join(f'<div class="p">{e(p)}</div>' for p in pills) + "</div>") if pills else "") + "</div>")
    return css, body


def style1():
    y = o.y if o.y is not None else (1250 if bottom else 200)
    word = o.title.rstrip(".")
    name = o.name or o.title.rstrip(".")
    tags = " · ".join(pills[:3])
    fs = 150 if len(word) <= 8 else max(84, int(150 * 8 / len(word)))
    nm = max(30, min(46, int(560 / (0.53 * max(1, len(name))))))
    css = f"""
.sh{{{grad("255,255,255", .88, .62)}}}
.box{{position:absolute;left:0;top:{y}px;width:1080px}}
.k{{width:1080px;text-align:center;font:500 36px "S1 Inter";color:rgb(22,22,26)}}
.big{{margin-top:6px;width:1080px;display:flex;justify-content:center}}
.big span{{position:relative;left:-14px;font:700 {fs}px/1 "S1 Display";letter-spacing:-1px;color:rgb(22,22,26);white-space:nowrap}}
.big b{{position:absolute;right:-{int(fs * .2)}px;bottom:.13em;width:{int(fs * .155)}px;height:{int(fs * .155)}px;background:rgb(229,72,77)}}
.win{{position:relative;margin:24px auto 0;width:700px;height:270px;border-radius:20px;background:rgba(24,24,28,.94);box-shadow:0 18px 50px rgba(0,0,0,.35)}}
.dots{{position:absolute;left:26px;top:26px;display:flex;gap:11px}}
.dots i{{display:block;width:14px;height:14px;border-radius:7px}}
.wl{{position:absolute;left:110px;top:16px;height:36px;line-height:36px;font:500 26px "S1 Inter";color:rgb(220,220,228)}}
.nm{{position:absolute;left:34px;top:66px;font:700 {nm + 6}px/56px "S1 Display";color:#fff;white-space:nowrap}}
.tg{{position:absolute;left:34px;top:126px;font:500 26px/32px "S1 Mono";color:rgb(160,160,170);white-space:nowrap}}
.btn{{position:absolute;left:24px;top:178px;width:652px;height:72px;border-radius:36px;background:rgb(255,212,59);display:flex;
 align-items:center;justify-content:center;font:700 38px "S1 Inter";color:rgb(22,22,26)}}"""
    body = f"""<div class="box">{f'<div class="k">{e(o.kicker)}</div>' if o.kicker else ''}
<div class="big"><span>{e(word)}<b></b></span></div>
<div class="win"><div class="dots"><i style="background:#FF5F57"></i><i style="background:#FEBC2E"></i><i style="background:#28C840"></i></div>
<div class="wl">TikTok Shop</div><div class="nm">{e(name)}</div><div class="tg">{e(tags)}</div><div class="btn">Tekan beg kuning ↓</div></div></div>"""
    return css, body


def style2():
    y = o.y if o.y is not None else (1300 if bottom else 300)
    t = e(o.title)
    t = re.sub(r"\*(.+?)\*", r'<span class="acc">\1</span>', t)
    name = o.name or re.sub(r"\*", "", o.title)
    css = f"""
.sh{{{grad("14,22,52", .55, .25)}}}
.box{{position:absolute;left:90px;top:{y}px;width:900px}}
.hk{{display:inline-flex;height:80px;padding:0 34px;border-radius:40px;background:#fff;align-items:center;gap:16px;
 box-shadow:0 10px 30px rgba(0,0,0,.25);font:500 34px "S1 Inter";color:#444;white-space:nowrap}}
.hk b{{font-weight:700;color:#111}} .hk svg{{width:36px;height:36px}}
.card{{margin-top:22px;border-radius:30px;background:#fff;box-shadow:0 18px 50px rgba(0,0,0,.30);padding:34px 42px 38px}}
.kick{{font:500 30px "S1 Mono";color:#2F6BFF;letter-spacing:2px}}
.ttl{{margin-top:8px;font:700 70px/1.1 "S1 Inter";color:#111}}
.acc{{font:italic 400 80px/1 "Playfair",serif;color:#2F6BFF}}
.row{{margin-top:22px;display:flex;flex-wrap:wrap;gap:14px}}
.chip{{height:60px;padding:0 22px;border-radius:16px;border:2px solid #D5DAE3;background:#F6F7FA;display:flex;align-items:center;
 font:700 32px "S1 Inter";color:#222}}"""
    star = ('<svg viewBox="0 0 24 24" fill="#D97757"><path d="M12 1.5l1.6 7 6.3-3.6-4.2 5.9 6.8 1.2-6.8 1.2 4.2 5.9-6.3-3.6-1.6 7-1.6-7-6.3 '
            '3.6 4.2-5.9-6.8-1.2 6.8-1.2-4.2-5.9 6.3 3.6z"/></svg>')
    body = (f'<div class="box"><div class="hk">{star}<span>review <b>{e(name)}</b></span></div><div class="card">'
            + (f'<div class="kick">{e(o.kicker.upper())}</div>' if o.kicker else "") + f'<div class="ttl">{t}</div>'
            + (('<div class="row">' + "".join(f'<div class="chip">{e(p)}</div>' for p in pills) + "</div>") if pills else "")
            + "</div></div>")
    return css, body


css, body = {"1": style1, "2": style2, "3": style3}[o.style]()
tmp = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(o.t), "-i", o.video, "-frames:v", "1", "-vf",
                f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,eq=brightness={o.bright}:saturation=1.1",
                os.path.join(tmp, "f.png")], check=True)
shutil.copytree(os.path.join(HERE, "fonts"), os.path.join(tmp, "fonts"))
open(os.path.join(tmp, "c.html"), "w").write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}{css}</style></head>'
    f'<body><div class="bg"></div><div class="sh"></div>{body}</body></html>')
js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
      "const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.argv[1]);"
      "await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);"
      "await p.screenshot({path:process.argv[2]});await b.close()})()")
subprocess.run(["node", "-e", js, os.path.join(tmp, "c.html"), os.path.abspath(o.out)], check=True)
shutil.rmtree(tmp)
print("->", o.out)
