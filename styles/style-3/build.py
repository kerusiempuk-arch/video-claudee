"""Style 3 (HyperFrames) – "tajuk atas": label kecil + tajuk besar bertitik di atas kepala, pil, nombor besar,
kad gambar produk (latar blur), butang kuning "Beli di beg kuning". TIADA subtitle bawah (arahan owner).

Guna (dari root repo):
  python3 -I styles/style-3/build.py <raw.mp4> <projects/nama.py> <work_dir>            # bina projek
  python3 -I styles/style-3/build.py <raw.mp4> <projects/nama.py> <work_dir> --plan     # cetak potongan + END sahaja
  python3 -I styles/style-3/build.py <raw.mp4> <projects/nama.py> <work_dir> --cut-audio <out.wav>
                                                     # suara bersih selepas dipotong (untuk transkripsi / masa)
Lepas itu, dalam <work_dir>:  hyperframes check  /  snapshot --at …  /  render -q draft|high -o …

Automatik:
  1. Potongan: senyap > MIN_SILENCE + REMOVE (aaa/okay/ulangan/gagap) + SRC_END. Satu <video> setiap segmen;
     segmen selang-seli punch-in PUNCH (origin atas). Masa overlay = masa SELEPAS potong.
  2. Suara utama sahaja: highpass + RNNoise (arnndn) + lowpass, −14 LUFS. Video dibisukan.
  3. Video gelap (YAVG < DARK_Y) dicerahkan melalui `hyperframes media-treatment`.
  4. Overlay Style 3: gradien gelap di atas, HEADS (label + tajuk / nombor besar + pil), IMAGES (kad gambar
     produk, latar blur + gelap), CTA (pil kuning + anak panah), sound effect.
Teks tajuk: "Lain warna." — titik di hujung ditulis sendiri dalam config.
"""
import html, json, math, os, runpy, shutil, subprocess, sys, wave, array

HERE = os.path.dirname(os.path.abspath(__file__))
CLI = os.path.expanduser("~/.claude/skills/hyperframes/scripts/plugin-cli.mjs")
RNN_URL = "https://raw.githubusercontent.com/GregorR/rnnoise-models/master/conjoined-burgers-2018-08-28/cb.rnnn"
RNN = os.path.expanduser("~/.cache/style1/cb.rnnn")

RAW, PROJ, W = sys.argv[1], sys.argv[2], sys.argv[3]
PROJ_DIR = os.path.dirname(os.path.abspath(PROJ))
C = runpy.run_path(PROJ)

REMOVE = C.get("REMOVE", [])
SILENCE_DB = C.get("SILENCE_DB", -38)
MIN_SIL = C.get("MIN_SILENCE", 0.30)
PAD = C.get("PAD", 0.06)
PUNCH = C.get("PUNCH", 1.07)
TAIL = C.get("TAIL", 0.0)
POSITION = C.get("POSITION", "top")   # "top" (biasa) / "bottom" (bila kepala di atas frame → tajuk, CTA, gradien di bawah)
HEAD_Y = C.get("HEAD_Y", 1240 if POSITION == "bottom" else 190)   # atas label kecil (px, kanvas 1080×1920)
CTA_Y = 1300 if POSITION == "bottom" else 200                       # default CTA["y"]
IMG_TOP = C.get("IMG_TOP", 190 if POSITION == "bottom" else 470)   # atas kad gambar produk (bottom: atas tajuk y 1240)
IMG_W = C.get("IMG_W", 1000)         # lebar kad gambar produk
DENOISE = C.get("DENOISE", True)
DARK_Y = C.get("DARK_Y", 105)
BRIGHTEN = C.get("BRIGHTEN", "auto")
esc = html.escape


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def duration(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


# ------------------------------------------------------------------ 1. potongan (sama dengan Style 1/2)
def plan_cuts():
    src_end = C.get("SRC_END", duration(RAW))
    tmp = os.path.join(W, ".tmp")
    os.makedirs(tmp, exist_ok=True)
    wav = os.path.join(tmp, "a16k.wav")
    sh(["ffmpeg", "-v", "error", "-y", "-i", RAW, "-ac", "1", "-ar", "16000", wav])
    w = wave.open(wav)
    pcm = array.array("h", w.readframes(w.getnframes()))
    hop = 320
    db = []
    for i in range(0, len(pcm), hop):
        blk = pcm[i:i + hop]
        rms = math.sqrt(sum(v * v for v in blk) / max(1, len(blk))) / 32768
        db.append(20 * math.log10(rms + 1e-9))
    sm = [sorted(db[max(0, i - 2):i + 3])[len(db[max(0, i - 2):i + 3]) // 2] for i in range(len(db))]
    step = hop / 16000
    sil, start = [], None
    for i, v in enumerate(sm + [0]):
        t = i * step
        if v < SILENCE_DB and start is None:
            start = t
        elif v >= SILENCE_DB and start is not None:
            if t - start >= MIN_SIL:
                sil.append((start + PAD, t - PAD))
            start = None
    sil = [(a, min(b, src_end - TAIL)) for a, b in sil if a < src_end - TAIL]
    cuts = sorted([(a, b) for a, b in sil if b > a] + [tuple(r) for r in REMOVE] + [(src_end, 1e9)])
    merged = []
    for a, b in cuts:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    keep, cur = [], 0.0
    for a, b in merged:
        if a - cur > 0.12:
            keep.append((round(cur, 3), round(a, 3)))
        cur = max(cur, b)
    return keep


# ------------------------------------------------------------------ 2. suara utama sahaja
def clean_voice(out):
    chain = "highpass=f=80,lowpass=f=12000"
    if DENOISE:
        if not os.path.exists(RNN):
            os.makedirs(os.path.dirname(RNN), exist_ok=True)
            sh(["curl", "-sSL", "-o", RNN, RNN_URL])
        chain = f"highpass=f=80,arnndn=m={RNN},lowpass=f=12000"
    sh(["ffmpeg", "-v", "error", "-y", "-i", RAW, "-vn", "-af", chain + ",loudnorm=I=-14:TP=-2",
        "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k", out])


def cut_audio(src_audio, keep, out):
    parts = [f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,"
             f"afade=t=out:st={max(0, b - a - 0.015):.3f}:d=0.015[a{i}]" for i, (a, b) in enumerate(keep)]
    fc = ";".join(parts) + ";" + "".join(f"[a{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1[a]"
    sh(["ffmpeg", "-v", "error", "-y", "-i", src_audio, "-filter_complex", fc, "-map", "[a]", "-ar", "16000", "-ac", "1", out])


# ------------------------------------------------------------------ 3. kecerahan
def mean_luma():
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", RAW, "-vf",
                          "fps=1,scale=270:-1,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-",
                          "-f", "null", "-"], capture_output=True, text=True).stdout
    vals = [float(l.split("=")[1]) for l in out.splitlines() if "YAVG=" in l]
    return sum(vals) / len(vals) if vals else 128.0


def brighten_patch(y):
    if BRIGHTEN is None:
        return None
    if isinstance(BRIGHTEN, dict):
        return {"adjust": BRIGHTEN}
    if y >= DARK_Y:
        return None
    return {"adjust": {"exposure": round(max(0.15, min(0.8, (118 - y) / 85)), 2), "shadows": 0.25, "blacks": 0.08}}


# ------------------------------------------------------------------ 4. HTML
def f2(x):
    return f"{x:.3f}"


FONT = 'font-family: "S3 Jakarta", sans-serif;'
FONT_CSS = """
    @font-face { font-family: "S3 Jakarta"; font-weight: 200 800; src: url("assets/fonts/PlusJakartaSans.ttf"); }"""
SFX = []  # (t, name, vol)


def scene(cid, css, body, js):
    return f"""<template>
  <style>{FONT_CSS}
    #root {{ position: absolute; inset: 0; {FONT} }}
{css}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="1080" data-height="1920">
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


def build_shade(end):
    """Gradien gelap di atas (atau di bawah bila POSITION="bottom") sepanjang video supaya tajuk putih jelas."""
    body = f'    <div id="sh" class="clip" data-start="0" data-duration="{f2(end)}"></div>'
    if POSITION == "bottom":
        css = """
    #sh { position: absolute; left: 0; top: 1000px; width: 1080px; height: 920px;
      background: linear-gradient(0deg, rgba(18,20,26,.80) 0%, rgba(18,20,26,.55) 45%, rgba(18,20,26,0) 100%); }"""
    else:
        css = """
    #sh { position: absolute; left: 0; top: 0; width: 1080px; height: 820px;
      background: linear-gradient(180deg, rgba(18,20,26,.78) 0%, rgba(18,20,26,.50) 38%, rgba(18,20,26,0) 100%); }"""
    return scene("shade", css, body, "")


HEAD_CSS = """
    .hd { position: absolute; left: 40px; width: 1000px; display: flex; flex-direction: column; align-items: center; }
    .kick { font-weight: 600; font-size: 28px; letter-spacing: 9px; color: rgba(255,255,255,.82); text-transform: uppercase;
      text-shadow: 0 2px 10px rgba(0,0,0,.35); }
    .ttl { margin-top: 10px; font-weight: 800; font-size: 96px; line-height: 1.05; letter-spacing: -2px; color: #fff; text-align: center;
      white-space: nowrap; text-shadow: 0 4px 22px rgba(0,0,0,.40); }
    .pills { margin-top: 26px; display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; max-width: 980px; }
    .pill { height: 58px; padding: 0 26px; border-radius: 29px; background: #fff; color: #15171C; display: flex; align-items: center;
      font-weight: 700; font-size: 29px; white-space: nowrap; box-shadow: 0 8px 22px rgba(0,0,0,.25); opacity: 0; }
    .bigv { position: relative; margin-top: 2px; height: 230px; width: 1000px; }
    .bv { position: absolute; left: 0; top: 0; width: 1000px; text-align: center; font-weight: 800; font-size: 210px; line-height: 230px;
      letter-spacing: -6px; color: #fff; text-shadow: 0 6px 28px rgba(0,0,0,.40); opacity: 0; }
    .sub { margin-top: 4px; font-weight: 600; font-size: 40px; color: #fff; text-shadow: 0 2px 12px rgba(0,0,0,.45); }
    .uline { margin-top: 14px; height: 6px; width: 380px; border-radius: 3px; background: #22C55E; transform-origin: 50% 50%; }"""


def build_head(cid, h):
    """Satu 'tajuk': label kecil + tajuk besar (atau nombor besar bertukar) + pil yang muncul ikut suara.
    Masuk: blur → tajam; keluar: tajam → blur."""
    s, e = h["start"], h["end"]
    d = e - s
    big = h.get("big")
    if big:
        vals = "".join(f'<div class="bv" id="{cid}-v{j}">{esc(v)}</div>' for j, (at, v) in enumerate(big))
        main = f'      <div class="bigv">{vals}</div>\n'
        if h.get("sub"):
            main += f'      <div class="sub" id="{cid}-sub">{esc(h["sub"])}</div>\n'
        if h.get("line"):
            main += f'      <div class="uline" id="{cid}-ul"></div>\n'
    else:
        main = f'      <div class="ttl" id="{cid}-t">{esc(h["title"])}</div>\n'
    pills = h.get("pills", [])
    if pills:
        main += '      <div class="pills">' + "".join(
            f'<div class="pill" id="{cid}-p{j}">{esc(t)}</div>' for j, (at, t) in enumerate(pills)) + '</div>\n'
    body = (f'    <div id="{cid}-w" class="clip hd" data-start="0" data-duration="{f2(d)}" style="top:{HEAD_Y}px" '
            f'data-layout-allow-overflow>\n'
            f'      <div class="kick" id="{cid}-k">{esc(h.get("kicker", ""))}</div>\n{main}    </div>')
    js = f'    tl.fromTo("#{cid}-k", {{ opacity: 0, y: -8 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power2.out" }}, 0);\n'
    if big:
        for j, (at, v) in enumerate(big):
            t = max(0.0, at - s)
            js += (f'    tl.fromTo("#{cid}-v{j}", {{ opacity: 0, scale: 0.6, filter: "blur(14px)" }}, '
                   f'{{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.4, ease: "back.out(2)" }}, {f2(t)});\n')
            if j > 0:
                js += (f'    tl.to("#{cid}-v{j - 1}", {{ opacity: 0, scale: 1.25, filter: "blur(14px)", duration: 0.25, '
                       f'ease: "power2.in" }}, {f2(t)});\n')
            SFX.append((s + t, "click" if j else "whoosh-short", 0.4 if j else 0.3))
        if h.get("sub"):
            js += f'    tl.fromTo("#{cid}-sub", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, 0.25);\n'
        if h.get("line"):
            js += f'    tl.fromTo("#{cid}-ul", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: "power3.out" }}, 0.4);\n'
        out_ids = f'["#{cid}-v{len(big) - 1}", "#{cid}-k"' + (f', "#{cid}-sub"' if h.get("sub") else "") + \
                  (f', "#{cid}-ul"' if h.get("line") else "") + "]"
    else:
        js += (f'    tl.fromTo("#{cid}-t", {{ opacity: 0, y: 14, filter: "blur(16px)" }}, '
               f'{{ opacity: 1, y: 0, filter: "blur(0px)", duration: 0.45, ease: "power3.out" }}, 0.05);\n')
        SFX.append((s + 0.05, "whoosh-short", 0.3))
        out_ids = f'["#{cid}-t", "#{cid}-k"]'
    for j, (at, t) in enumerate(pills):
        tt = max(0.15, at - s)
        js += (f'    tl.fromTo("#{cid}-p{j}", {{ opacity: 0, y: 10, scale: 0.8 }}, '
               f'{{ opacity: 1, y: 0, scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {f2(tt)});\n')
        SFX.append((s + tt, "pop", 0.3))
    if pills:
        out_ids = out_ids[:-1] + ", " + ", ".join(f'"#{cid}-p{j}"' for j in range(len(pills))) + "]"
    if not h.get("hold"):
        js += f'    tl.to({out_ids}, {{ opacity: 0, filter: "blur(14px)", duration: 0.28, ease: "power2.in" }}, {f2(d - 0.3)});\n'
    return scene(cid, HEAD_CSS, body, js)


def build_image(cid, im, fname):
    """Kad gambar produk di tengah; footage di belakang di-blur + digelapkan."""
    s, e = im["start"], im["end"]
    d = e - s
    body = (f'    <div id="{cid}-bg" class="clip" data-start="0" data-duration="{f2(d)}"></div>\n'
            f'    <div id="{cid}-w" class="clip" data-start="0" data-duration="{f2(d)}" '
            f'style="position:absolute;left:{(1080 - IMG_W) // 2}px;top:{IMG_TOP}px;width:{IMG_W}px">\n'
            f'      <img id="{cid}-i" src="assets/img/{fname}" alt="">\n    </div>')
    css = f"""
    #{cid}-bg {{ position: absolute; inset: 0; background: rgba(16,18,24,.38); backdrop-filter: blur(26px); -webkit-backdrop-filter: blur(26px); opacity: 0; }}
    #{cid}-i {{ display: block; width: {IMG_W}px; height: auto; border-radius: 34px; box-shadow: 0 24px 60px rgba(0,0,0,.45); opacity: 0; }}"""
    js = (f'    tl.fromTo("#{cid}-bg", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power2.out" }}, 0);\n'
          f'    tl.fromTo("#{cid}-i", {{ opacity: 0, y: 60, scale: 0.9 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "power3.out" }}, 0.05);\n'
          f'    tl.to("#{cid}-i", {{ opacity: 0, y: 30, scale: 0.96, duration: 0.3, ease: "power2.in" }}, {f2(d - 0.32)});\n'
          f'    tl.to("#{cid}-bg", {{ opacity: 0, duration: 0.3, ease: "power2.in" }}, {f2(d - 0.3)});\n')
    SFX.append((s + 0.05, "sparkle", 0.3))
    return scene(cid, css, body, js)


def build_cta(c, end):
    s = c["start"]
    d = end - s
    body = (f'    <div id="ct" class="clip" data-start="0" data-duration="{f2(d)}" style="top:{c.get("y", CTA_Y)}px">\n'
            f'      <div id="ct-btn">{esc(c.get("text", "Beli di beg kuning"))}</div>\n'
            '      <div id="ct-arr"><svg viewBox="0 0 48 48" fill="none" stroke="#FFD21F" stroke-width="6" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M12 10l12 11 12-11"/><path d="M12 26l12 11 12-11"/></svg></div>\n    </div>')
    css = """
    #ct { position: absolute; left: 0; width: 1080px; display: flex; flex-direction: column; align-items: center; }
    #ct-btn { height: 112px; padding: 0 58px; border-radius: 56px; background: #FFD21F; color: #15171C; display: flex; align-items: center;
      font-weight: 800; font-size: 50px; white-space: nowrap; box-shadow: 0 14px 40px rgba(255,210,31,.45); opacity: 0; }
    #ct-arr { margin-top: 26px; width: 74px; height: 74px; opacity: 0; }
    #ct-arr svg { width: 74px; height: 74px; }"""
    js = ('    tl.fromTo("#ct-btn", { opacity: 0, y: -20, scale: 0.85 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.8)" }, 0.05);\n'
          '    tl.fromTo("#ct-arr", { opacity: 0 }, { opacity: 1, duration: 0.25 }, 0.4);\n'
          f'    tl.fromTo("#ct-arr", {{ y: 0 }}, {{ y: 16, duration: 0.38, ease: "sine.inOut", yoyo: true, repeat: {max(1, int((d - 0.5) / 0.38) - 1)} }}, 0.45);\n')
    SFX.append((s + 0.05, "ping", 0.4))
    return scene("cta", css, body, js)


def build_index(keep, end, hosts, sfx_dur):
    segs, auds, at = [], [], 0.0
    for i, (a, b) in enumerate(keep):
        d = round(b - a, 3)
        cls = "clip seg punch" if i % 2 == 1 and PUNCH != 1.0 else "clip seg"
        segs.append(f'      <video id="seg{i}" class="{cls}" src="src.mp4" muted playsinline data-start="{f2(at)}" '
                    f'data-media-start="{a}" data-duration="{d}" data-track-index="0"></video>')
        auds.append(f'      <audio id="vo{i}" src="voice.m4a" data-start="{f2(at)}" data-media-start="{a}" data-duration="{d}" data-volume="1" '
                    f'data-fade-in="0.015" data-fade-out="{0.4 if i == len(keep) - 1 else 0.015}" data-track-index="1"></audio>')
        at += d
    sfx, lanes = [], []
    for k, (t, name, vol) in enumerate(sorted(e for e in SFX + [tuple(x) for x in C.get("EXTRA_SFX", [])] if e[0] < end)):
        dur = sfx_dur[name]
        lane = next((j for j, e in enumerate(lanes) if e <= t), None)
        if lane is None:
            lanes.append(0)
            lane = len(lanes) - 1
        lanes[lane] = t + dur
        sfx.append(f'      <audio id="sfx{k}-{name}" src="assets/sfx/{name}.mp3" data-start="{f2(t)}" '
                   f'data-duration="{min(dur, end - t):.3f}" data-volume="{vol}" data-track-index="{8 + lane}"></audio>')
    host_html = "\n".join(
        f'      <div id="{h}" data-composition-id="{h}" data-composition-src="compositions/{h}.html" data-start="{f2(s)}" '
        f'data-duration="{f2(d)}" data-track-index="{ti}" data-track-kind="graphics" '
        f'data-width="1080" data-height="1920" style="z-index:{z}"></div>' for h, s, d, ti, z in hosts)
    return f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      .seg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; }}
      .seg.punch {{ transform: scale({PUNCH}); transform-origin: 50% 4%; }}
    </style>
  </head>
  <body>
    <!-- Style 3 (HyperFrames) – dijana oleh styles/style-3/build.py. Jangan edit tangan; ubah config projek dan bina semula. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{f2(end)}" data-width="1080" data-height="1920">
{chr(10).join(segs)}
{host_html}
      <!-- suara utama sahaja (bunyi latar dibuang, −14 LUFS) -->
{chr(10).join(auds)}
      <!-- sound effect -->
{chr(10).join(sfx)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""


def main():
    os.makedirs(W, exist_ok=True)
    keep = plan_cuts()
    end = round(sum(b - a for a, b in keep), 3)
    print(f"# {len(keep)} segmen, END = {end:.2f}s")
    for a, b in keep:
        print(f"   keep {a:6.2f} - {b:6.2f}")
    if C.get("END") and abs(C["END"] - end) > 0.05:
        print(f"! END dalam config ({C['END']}) lain daripada potongan ({end:.2f}) – kemas kini config.")
    if "--plan" in sys.argv:
        return
    voice = os.path.join(W, "voice.m4a")
    clean_voice(voice)
    if "--cut-audio" in sys.argv:
        out = sys.argv[sys.argv.index("--cut-audio") + 1]
        cut_audio(voice, keep, out)
        print("->", out)
        return
    shutil.copyfile(RAW, os.path.join(W, "src.mp4"))
    for d in ("sfx", "fonts", "img"):
        os.makedirs(os.path.join(W, "assets", d), exist_ok=True)
    sfx_dur = {}
    for f in os.listdir(os.path.join(HERE, "sfx")):
        shutil.copyfile(os.path.join(HERE, "sfx", f), os.path.join(W, "assets", "sfx", f))
        sfx_dur[os.path.splitext(f)[0]] = duration(os.path.join(HERE, "sfx", f))
    shutil.copyfile(os.path.join(HERE, "fonts", "PlusJakartaSans.ttf"), os.path.join(W, "assets", "fonts", "PlusJakartaSans.ttf"))
    y = mean_luma()
    patch = brighten_patch(y)
    print(f"# kecerahan purata YAVG={y:.0f}" + (f" → dicerahkan {json.dumps(patch)}" if patch else " (ok)"))
    comp = os.path.join(W, "compositions")
    if os.path.isdir(comp):
        shutil.rmtree(comp)
    os.makedirs(comp)
    files, hosts = {}, []
    files["shade"] = build_shade(end)
    hosts.append(("shade", 0, end, 2, 3))
    for i, im in enumerate(C.get("IMAGES", [])):
        cid = f"img{i + 1}"
        src = im["src"] if os.path.isabs(im["src"]) else os.path.join(os.getcwd(), im["src"])
        if not os.path.exists(src):
            src = os.path.join(PROJ_DIR, im["src"])
        fname = f"{cid}{os.path.splitext(src)[1].lower()}"
        shutil.copyfile(src, os.path.join(W, "assets", "img", fname))
        files[cid] = build_image(cid, im, fname)
        hosts.append((cid, im["start"], im["end"] - im["start"], 3, 4))
    for i, h in enumerate(C.get("HEADS", [])):
        cid = f"head{i + 1}"
        files[cid] = build_head(cid, h)
        hosts.append((cid, h["start"], h["end"] - h["start"], 4 + i % 2, 6))
    if C.get("CTA"):
        files["cta"] = build_cta(C["CTA"], end)
        hosts.append(("cta", C["CTA"]["start"], end - C["CTA"]["start"], 6, 7))
    for k, v in files.items():
        open(os.path.join(comp, k + ".html"), "w").write(v)
    open(os.path.join(W, "index.html"), "w").write(build_index(keep, end, hosts, sfx_dur))
    name = os.path.splitext(os.path.basename(PROJ))[0]
    json.dump({"name": f"style3-{name}", "private": True, "type": "module"}, open(os.path.join(W, "package.json"), "w"))
    json.dump({"id": f"style3-{name}", "name": name}, open(os.path.join(W, "meta.json"), "w"))
    if patch:
        sh(["node", CLI, "media-treatment", "--project", W, "--selector", ".seg", "--grading", json.dumps(patch),
            "--apply", "--json"], stdout=subprocess.DEVNULL)
    print("->", W, "(seterusnya: hyperframes check / snapshot / render dalam folder ini)")


main()
