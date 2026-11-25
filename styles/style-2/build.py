"""Style 2 (HyperFrames) – jana projek HyperFrames dari video mentah + config projek.

Guna (dari root repo):
  python3 -I styles/style-2/build.py <raw.mp4> <projects/nama.py> <work_dir>            # bina projek
  python3 -I styles/style-2/build.py <raw.mp4> <projects/nama.py> <work_dir> --plan     # cetak potongan + END sahaja
  python3 -I styles/style-2/build.py <raw.mp4> <projects/nama.py> <work_dir> --cut-audio <out.wav>
                                                     # suara bersih selepas dipotong (untuk transkripsi caption)
Lepas itu, dalam <work_dir>:  hyperframes check  /  snapshot --at …  /  render -q draft|high -o …

Automatik:
  1. Potongan: senyap > MIN_SILENCE + REMOVE (aaa/okay/ulangan/gagap) + SRC_END. Satu <video> setiap segmen;
     segmen selang-seli punch-in PUNCH (origin atas, kepala tak terpotong). Masa overlay = masa SELEPAS potong.
  2. Suara utama sahaja: highpass + RNNoise (arnndn) + lowpass, −14 LUFS. Video dibisukan.
  3. Video gelap (YAVG < DARK_Y) dicerahkan melalui `hyperframes media-treatment`.
  4. Overlay Style 2: pil hook, kad VS, kad kelebihan (ikon / senarai ✓ / saiz & warna), garis progress biru
     dengan label langkah, caption karaoke di dada, CTA (ringkasan ✓ + butang kuning), sound effect.
Teks: *perkataan* = serif italik biru (dalam kad) ; **perkataan** = tebal (dalam pil hook).
"""
import html, json, math, os, re, runpy, shutil, subprocess, sys, wave, array

HERE = os.path.dirname(os.path.abspath(__file__))
CLI = os.path.expanduser("~/.claude/skills/hyperframes/scripts/plugin-cli.mjs")
RNN_URL = "https://raw.githubusercontent.com/GregorR/rnnoise-models/master/conjoined-burgers-2018-08-28/cb.rnnn"
RNN = os.path.expanduser("~/.cache/style1/cb.rnnn")

RAW, PROJ, W = sys.argv[1], sys.argv[2], sys.argv[3]
C = runpy.run_path(PROJ)

REMOVE = C.get("REMOVE", [])
SILENCE_DB = C.get("SILENCE_DB", -38)
MIN_SIL = C.get("MIN_SILENCE", 0.30)
PAD = C.get("PAD", 0.06)
PUNCH = C.get("PUNCH", 1.07)
TAIL = C.get("TAIL", 0.0)
CAPTION_Y = C.get("CAPTION_Y", 655)
CARD_TOP = C.get("CARD_TOP", 1500)
DENOISE = C.get("DENOISE", True)
DARK_Y = C.get("DARK_Y", 105)
BRIGHTEN = C.get("BRIGHTEN", "auto")
esc = html.escape


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def duration(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


# ------------------------------------------------------------------ 1. potongan (sama dengan Style 1)
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


def rich(text):
    """*x* -> serif italik biru ; **x** -> tebal."""
    t = esc(text).replace("\n", "<br>")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*(.+?)\*", r'<span class="acc">\1</span>', t)


def scene(cid, css, body, js):
    return f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
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


CARD_CSS = """
    .cw { position: absolute; left: 120px; width: 760px; z-index: 1; }
    .card { position: absolute; inset: 0; border-radius: 30px; background: #fff; opacity: 0;
      box-shadow: 0 18px 50px rgba(0,0,0,.30); padding: 28px 36px; }
    .kick { font: 700 28px "JetBrains Mono", monospace; color: #2F6BFF; letter-spacing: 2px; }
    .ttl { margin-top: 6px; font: 700 48px/1.15 "Inter", sans-serif; color: #111; }
    .acc { font: italic 400 54px/1.1 "Playfair Display", serif; color: #2F6BFF; }"""

CHECK_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" '
             'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')
ICONS = {
    "heart": '<svg viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54s-20-11-20-26a11 11 0 0 1 20-6 11 11 0 0 1 20 6c0 15-20 26-20 26z" fill="#DCE6FF"/></svg>',
    "wind": '<svg viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="4.5" stroke-linecap="round"><path d="M8 22h32a7 7 0 1 0-7-7"/><path d="M8 34h44a7 7 0 1 1-7 7"/><path d="M8 46h22"/></svg>',
    "star": '<svg viewBox="0 0 64 64" fill="#DCE6FF" stroke="#2F6BFF" stroke-width="4" stroke-linejoin="round"><path d="M32 8l7 15 16 2-12 11 3 16-14-8-14 8 3-16L9 25l16-2z"/></svg>',
    "shield": '<svg viewBox="0 0 64 64" fill="#DCE6FF" stroke="#2F6BFF" stroke-width="4" stroke-linejoin="round"><path d="M32 6l22 8v16c0 14-10 24-22 28C20 54 10 44 10 30V14z"/></svg>',
    "bolt": '<svg viewBox="0 0 64 64" fill="#DCE6FF" stroke="#2F6BFF" stroke-width="4" stroke-linejoin="round"><path d="M36 6L14 36h16l-4 22 24-32H34z"/></svg>',
    "tag": '<svg viewBox="0 0 64 64" fill="#DCE6FF" stroke="#2F6BFF" stroke-width="4" stroke-linejoin="round"><path d="M8 32V10h22l26 26-22 22z"/><circle cx="20" cy="22" r="4" fill="#2F6BFF"/></svg>',
}
SFX = []  # (t, name, vol)


def card_frame(cid, i, top, height, inner, extra_css, js_inner, start, end):
    """Kad putih: masuk 0.45 s, keluar 0.3 s sebelum tamat."""
    d = end - start
    body = (f'    <div id="{cid}-w" class="clip cw" data-start="0.1" data-duration="{f2(d - 0.1)}" '
            f'style="top:{top}px;height:{height}px">\n      <div class="card" id="{cid}-c">\n{inner}\n      </div>\n    </div>')
    js = (f'    tl.fromTo("#{cid}-c", {{ opacity: 0, y: 40, scale: 0.94 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "power3.out" }}, 0.1);\n'
          + js_inner
          + f'    tl.to("#{cid}-c", {{ opacity: 0, y: 20, duration: 0.3, ease: "power2.in" }}, {f2(d - 0.35)});\n')
    SFX.append((start + 0.08, "whoosh-short", 0.35))
    return scene(cid, CARD_CSS + extra_css, body, js)


def card_vs(cid, k):
    s, e = k["start"], k["end"]
    na = k.get("new_at", s + 1.1) - s
    inner = f"""        <div class="kick">{esc(k["kicker"])}</div>
        <div class="vrow">
          <div class="vside" id="{cid}-o"><div class="vico" style="background:#E7E9EE"><svg viewBox="0 0 24 24" fill="none" stroke="#9097A3" stroke-width="3.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></div><span class="old">{esc(k["old"])}</span></div>
          <div class="varr" id="{cid}-a">→</div>
          <div class="vside" id="{cid}-n"><div class="vico" style="background:#2F6BFF">{CHECK_SVG}</div><span class="new">{esc(k["new"])}</span></div>
        </div>"""
    css = """
    .vrow { margin-top: 22px; display: flex; align-items: center; justify-content: space-between; }
    .vside { display: flex; align-items: center; gap: 16px; font: 700 40px "Inter", sans-serif; }
    .old { color: #9097A3; text-decoration: line-through; text-decoration-thickness: 4px; }
    .new { font: italic 400 52px "Playfair Display", serif; color: #2F6BFF; }
    .vico { width: 52px; height: 52px; border-radius: 26px; display: flex; align-items: center; justify-content: center; flex: none; }
    .vico svg { width: 30px; height: 30px; }
    .varr { font: 700 44px "Inter", sans-serif; color: #2F6BFF; }"""
    js = (f'    tl.fromTo("#{cid}-o", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }}, 0.35);\n'
          f'    tl.fromTo("#{cid}-a", {{ opacity: 0, x: -14 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }}, {f2(max(0.6, na - 0.2))});\n'
          f'    tl.fromTo("#{cid}-n", {{ opacity: 0, scale: 0.7 }}, {{ opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }}, {f2(na)});\n')
    SFX.append((s + 0.4, "click", 0.35))
    SFX.append((s + na, "sparkle", 0.3))
    return card_frame(cid, 0, CARD_TOP + 30, 250, inner, css, js, s, e)


def card_icon(cid, k):
    s, e = k["start"], k["end"]
    inner = f"""        <div class="irow"><div><div class="kick">{esc(k["kicker"])}</div><div class="ttl">{rich(k["title"])}</div></div>
          <div class="ico" id="{cid}-i">{ICONS.get(k.get("icon", "star"), ICONS["star"])}</div></div>"""
    css = """
    .card { display: flex; align-items: center; }
    .irow { width: 100%; display: flex; justify-content: space-between; align-items: center; }
    .ico { width: 150px; height: 150px; border-radius: 28px; background: #EEF3FF; display: flex; align-items: center; justify-content: center; flex: none; }
    .ico svg { width: 96px; height: 96px; }"""
    js = f'    tl.fromTo("#{cid}-i", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2.2)" }}, 0.4);\n'
    SFX.append((s + 0.4, "pop", 0.35))
    return card_frame(cid, 0, CARD_TOP + 30, 250, inner, css, js, s, e)


def card_check(cid, k):
    s, e = k["start"], k["end"]
    rows = "\n".join(
        f'        <div class="crow" id="{cid}-r{j}"><div class="cbox"><div class="cfill" id="{cid}-k{j}">{CHECK_SVG}</div></div>{esc(t)}</div>'
        for j, (t, at) in enumerate(k["items"]))
    inner = f'        <div class="kick">{esc(k["kicker"])}</div>\n        <div class="ttl">{rich(k["title"])}</div>\n{rows}'
    css = """
    .ttl { font-size: 46px; }
    .crow { margin-top: 16px; display: flex; align-items: center; gap: 20px; font: 400 34px "Inter", sans-serif; color: #222; }
    .cbox { position: relative; width: 44px; height: 44px; border-radius: 12px; border: 3px solid #C9CDD6; flex: none; }
    .cfill { position: absolute; inset: -3px; border-radius: 12px; background: #2F6BFF; display: flex; align-items: center; justify-content: center; opacity: 0; }
    .cfill svg { width: 28px; height: 28px; }"""
    ids = ", ".join(f'"#{cid}-r{j}"' for j in range(len(k["items"])))
    js = f'    tl.fromTo([{ids}], {{ opacity: 0, x: -16 }}, {{ opacity: 1, x: 0, duration: 0.3, stagger: 0.15, ease: "power2.out" }}, 0.5);\n'
    for j, (t, at) in enumerate(k["items"]):
        js += f'    tl.fromTo("#{cid}-k{j}", {{ opacity: 0, scale: 0.3 }}, {{ opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2.5)" }}, {f2(at - s)});\n'
        SFX.append((at, "click", 0.4))
    h = 150 + 60 * len(k["items"])
    return card_frame(cid, 0, CARD_TOP + 250 - h + 30, h, inner, css, js, s, e)


def card_chips(cid, k):
    s, e = k["start"], k["end"]
    chips = "".join(f'<div class="chip" id="{cid}-s{j}">{esc(c)}</div>' for j, c in enumerate(k.get("chips", [])))
    dots = "".join(f'<div class="dot" id="{cid}-d{j}" style="background:{c}"></div>' for j, c in enumerate(k.get("colors", [])))
    inner = (f'        <div class="kick">{esc(k["kicker"])}</div>\n        <div class="ttl">{rich(k["title"])}</div>\n'
             + (f'        <div class="row">{chips}</div>\n' if chips else "") + (f'        <div class="row">{dots}</div>' if dots else ""))
    css = """
    .ttl { font-size: 46px; }
    .row { margin-top: 16px; display: flex; align-items: center; gap: 12px; }
    .chip { min-width: 74px; height: 50px; padding: 0 14px; border-radius: 14px; border: 2px solid #D5DAE3; background: #F6F7FA;
      display: flex; align-items: center; justify-content: center; font: 700 28px "Inter", sans-serif; color: #222; }
    .dot { width: 50px; height: 50px; border-radius: 25px; border: 4px solid #fff; box-shadow: 0 0 0 2px #D5DAE3; }"""
    js = ""
    if chips:
        ids = ", ".join(f'"#{cid}-s{j}"' for j in range(len(k["chips"])))
        at = k.get("chips_at", s + 0.4)
        js += f'    tl.fromTo([{ids}], {{ opacity: 0, y: 12, scale: 0.8 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.25, stagger: 0.1, ease: "back.out(2)" }}, {f2(at - s)});\n'
        SFX.append((at, "pop", 0.3))
    if dots:
        ids = ", ".join(f'"#{cid}-d{j}"' for j in range(len(k["colors"])))
        at = k.get("colors_at", s + 1.2)
        js += f'    tl.fromTo([{ids}], {{ opacity: 0, scale: 0.3 }}, {{ opacity: 1, scale: 1, duration: 0.25, stagger: 0.09, ease: "back.out(2.5)" }}, {f2(at - s)});\n'
        SFX.append((at, "pop", 0.3))
    h = 150 + (66 if chips else 0) + (66 if dots else 0)
    return card_frame(cid, 0, CARD_TOP + 250 - h + 30, h, inner, css, js, s, e)


def build_hook(h):
    s, e = h.get("start", 0.15), h["end"]
    x, y = h.get("x", 350), h.get("y", 860)
    body = (f'    <div id="hk" class="clip" data-start="{f2(s)}" data-duration="{f2(e - s)}" style="position:absolute;left:{x}px;top:{y}px;height:72px">\n'
            f'      <div id="hk-in"><svg viewBox="0 0 24 24" fill="#D97757"><path d="M12 1.5l1.6 7 6.3-3.6-4.2 5.9 6.8 1.2-6.8 1.2 4.2 5.9-6.3-3.6-1.6 7-1.6-7-6.3 3.6 4.2-5.9-6.8-1.2 6.8-1.2-4.2-5.9 6.3 3.6z"/></svg>'
            f'<span>{rich(h["text"])}</span></div>\n    </div>')
    css = """
    #hk-in { height: 72px; padding: 0 30px; border-radius: 36px; background: #fff; opacity: 0; display: flex; align-items: center; gap: 14px;
      box-shadow: 0 10px 30px rgba(0,0,0,.25); font: 400 30px "Inter", sans-serif; color: #444; white-space: nowrap; }
    #hk-in b { font-weight: 700; color: #111; }
    #hk-in svg { width: 32px; height: 32px; }"""
    js = (f'    tl.fromTo("#hk-in", {{ opacity: 0, y: 18, scale: 0.9 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.6)" }}, {f2(s)});\n'
          f'    tl.to("#hk-in", {{ opacity: 0, y: -10, duration: 0.3, ease: "power2.in" }}, {f2(e - 0.35)});\n')
    SFX.append((s, "pop", 0.35))
    return scene("hook", css, body, js)


def build_rail(r):
    s, e, steps = r["start"], r["end"], r["steps"]
    Y = [318 + 62 * i for i in range(len(steps))]
    pills = "\n".join(f'        <div class="rp" id="rl-p{i}"><span data-layout-ignore>{i + 1:02d}</span>{esc(t)}</div>'
                      for i, (at, t) in enumerate(steps))
    body = (f'    <div id="rl" class="clip" data-start="0" data-duration="{f2(e - s)}" data-layout-allow-overflow data-layout-allow-overlap>\n'
            f'      <div id="rl-track"></div><div id="rl-fill"></div><div id="rl-node"></div>\n      <div id="rl-label">\n{pills}\n      </div>\n    </div>')
    css = """
    #rl { position: absolute; left: 0; top: 0; width: 460px; height: 1920px; }
    #rl-track { position: absolute; left: 58px; top: 0; width: 5px; height: 1920px; background: rgba(255,255,255,.6); }
    #rl-fill { position: absolute; left: 58px; top: 0; width: 5px; height: 1920px; background: #2F6BFF; transform-origin: 50% 0%; }
    #rl-node { position: absolute; left: 41px; top: 0; width: 40px; height: 40px; border-radius: 20px; background: #2F6BFF; border: 6px solid #fff; box-shadow: 0 4px 14px rgba(0,0,0,.35); }
    #rl-label { position: absolute; left: 124px; top: 0; height: 50px; }
    .rp { position: absolute; left: 0; top: 0; height: 50px; padding: 0 22px 0 10px; border-radius: 25px; opacity: 0; background: #2F6BFF; color: #fff;
      display: flex; align-items: center; gap: 12px; white-space: nowrap; font: 700 28px "Inter", sans-serif; box-shadow: 0 6px 18px rgba(47,107,255,.4); }
    .rp span { width: 34px; height: 34px; border-radius: 17px; background: rgba(255,255,255,.25); display: flex; align-items: center; justify-content: center; font: 700 18px "JetBrains Mono", monospace; }"""
    js = ('    tl.fromTo("#rl", { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.4, ease: "power2.out" }, 0);\n'
          f'    tl.fromTo("#rl-fill", {{ scaleY: {Y[0] / 1920:.4f} }}, {{ scaleY: {Y[0] / 1920:.4f}, duration: 0.01 }}, 0);\n'
          f'    tl.fromTo("#rl-node", {{ y: {Y[0] - 20} }}, {{ y: {Y[0] - 20}, duration: 0.01 }}, 0);\n'
          f'    tl.fromTo("#rl-label", {{ y: {Y[0] - 25} }}, {{ y: {Y[0] - 25}, duration: 0.01 }}, 0);\n'
          '    tl.fromTo("#rl-p0", { opacity: 0, x: -12 }, { opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }, 0.25);\n')
    for i in range(1, len(steps)):
        t = steps[i][0] - s
        js += (f'    tl.to("#rl-fill", {{ scaleY: {Y[i] / 1920:.4f}, duration: 0.45, ease: "power2.inOut" }}, {f2(t)});\n'
               f'    tl.to("#rl-node", {{ y: {Y[i] - 20}, duration: 0.45, ease: "power2.inOut" }}, {f2(t)});\n'
               f'    tl.to("#rl-label", {{ y: {Y[i] - 25}, duration: 0.45, ease: "power2.inOut" }}, {f2(t)});\n'
               f'    tl.to("#rl-p{i - 1}", {{ opacity: 0, duration: 0.2 }}, {f2(t)});\n'
               f'    tl.fromTo("#rl-p{i}", {{ opacity: 0, x: -12 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }}, {f2(t + 0.3)});\n')
    js += f'    tl.to("#rl", {{ opacity: 0, x: -40, duration: 0.3, ease: "power2.in" }}, {f2(e - s - 0.35)});\n'
    return scene("rail", css, body, js)


def build_cta(c, end):
    s = c["start"]
    rows = "\n".join(f'      <div class="ctr" id="ct-r{i}"><div class="ctd">{CHECK_SVG}</div>{esc(t)}</div>' for i, t in enumerate(c["items"]))
    # butang "Tekan beg kuning" mesti di skrin >= 2.2 s (hyperframes check line_unread)
    bat = min(c.get("button_at", s + 0.45), end - 2.2) - s
    body = (f'    <div id="ct-tint" class="clip" data-start="0" data-duration="{f2(end - s)}"></div>\n'
            f'    <div id="ct-box" class="clip" data-start="0.15" data-duration="{f2(end - s - 0.15)}">\n      <div id="ct-line" style="height:{78 * (len(c["items"]) - 1)}px"></div>\n{rows}\n'
            f'      <div id="ct-btn" style="top:{78 * len(c["items"]) + 78}px"><svg viewBox="0 0 64 64" fill="none" stroke="#1A1A1A" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">'
            '<path d="M8 22h48l-6 30H14z" fill="#1A1A1A" fill-opacity=".08"/><path d="M22 22l8-14M42 22l-8-14"/><path d="M24 32v12M32 32v12M40 32v12"/></svg>'
            f'<span>{rich(c["button"])}</span></div>\n    </div>')
    css = """
    #ct-tint { position: absolute; inset: 0; z-index: 0; background: rgba(14,22,52,.62); opacity: 0; }
    #ct-box { position: absolute; left: 150px; top: 760px; width: 760px; height: 640px; z-index: 1; }
    .ctr { position: relative; z-index: 1; display: flex; align-items: center; gap: 24px; height: 78px; font: 700 38px "Inter", sans-serif; color: #fff; opacity: 0; }
    .ctd { width: 44px; height: 44px; border-radius: 22px; background: #2F6BFF; flex: none; display: flex; align-items: center; justify-content: center; }
    .ctd svg { width: 26px; height: 26px; }
    #ct-line { position: absolute; left: 20px; top: 40px; width: 4px; background: rgba(255,255,255,.35); z-index: 0; }
    #ct-btn { position: absolute; left: 0; height: 110px; width: 640px; border-radius: 55px; opacity: 0; background: #FFC93C; display: flex;
      align-items: center; justify-content: center; gap: 20px; font: 900 42px "Inter", sans-serif; color: #1A1A1A; box-shadow: 0 14px 40px rgba(255,201,60,.45); }
    #ct-btn svg { width: 58px; height: 58px; }
    #ct-btn .acc { font: italic 400 46px "Playfair Display", serif; color: #1A1A1A; }"""
    ids = ", ".join(f'"#ct-r{i}"' for i in range(len(c["items"])))
    js = ('    tl.fromTo("#ct-tint", { opacity: 0 }, { opacity: 1, duration: 0.45, ease: "power2.inOut" }, 0);\n'
          f'    tl.fromTo([{ids}], {{ opacity: 0, x: -24 }}, {{ opacity: 1, x: 0, duration: 0.28, stagger: 0.1, ease: "power2.out" }}, 0.2);\n'
          f'    tl.fromTo("#ct-btn", {{ opacity: 0, y: 30, scale: 0.85 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.8)" }}, {f2(bat)});\n'
          f'    tl.fromTo("#ct-btn svg", {{ rotation: 0 }}, {{ rotation: -12, duration: 0.12, ease: "sine.inOut", yoyo: true, repeat: 5 }}, {f2(bat + 0.45)});\n')
    SFX.append((s, "whoosh-short", 0.35))
    SFX.append((s + bat, "ping", 0.4))
    return scene("cta", css, body, js)


def build_captions(caps):
    body, js = [], ""
    css = f"""
    .cap {{ position: absolute; left: 120px; top: {CAPTION_Y}px; width: 840px; height: 110px; z-index: 1; display: flex; align-items: center; justify-content: center; }}
    .cl {{ font: 700 56px "Inter", sans-serif; color: #fff; text-align: center; white-space: nowrap; padding: 6px 22px; border-radius: 18px;
      background: rgba(10,14,28,.42); text-shadow: 0 2px 10px rgba(0,0,0,.5); }}
    .w {{ display: inline-block; }}
    .box {{ background: #fff; color: #111; padding: 0 14px; border-radius: 10px; text-shadow: none; }}
    .serif {{ background: rgba(255,255,255,.18); color: #fff; padding: 0 14px; border-radius: 10px; font: italic 400 62px "Playfair Display", serif;
      border: 2px solid rgba(255,255,255,.45); }}"""
    for i, (g_end, words) in enumerate(caps):
        g0 = max(0, words[0][1] - 0.05)
        nxt = caps[i + 1][1][0][1] - 0.05 if i + 1 < len(caps) else 1e9
        g1 = min(g_end, nxt)
        spans = " ".join(f'<span class="w {st or ""}" id="cp{i}w{j}">{esc(w)}</span>' for j, (w, ws, st) in enumerate(words))
        body.append(f'    <div id="cp{i}" class="clip cap" data-start="{f2(g0)}" data-duration="{f2(g1 - g0)}"><div class="cl">{spans}</div></div>')
        for j, (w, ws, st) in enumerate(words):
            js += f'    tl.fromTo("#cp{i}w{j}", {{ opacity: 0.3 }}, {{ opacity: 1, duration: 0.1, ease: "none" }}, {f2(max(g0, ws - 0.03))});\n'
    return scene("captions", css, "\n".join(body), js)


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
                   f'data-duration="{min(dur, end - t):.3f}" data-volume="{vol}" data-track-index="{6 + lane}"></audio>')
    host_html = "\n".join(
        f'      <div id="{h}" data-composition-id="{h}" data-composition-src="compositions/{h}.html" data-start="{f2(s)}" '
        f'data-duration="{f2(d)}" data-track-index="{ti}" data-track-kind="{"captions" if h == "captions" else "graphics"}" '
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
      body {{ font-family: "Inter", sans-serif; }}
      .seg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; }}
      .seg.punch {{ transform: scale({PUNCH}); transform-origin: 50% 4%; }}
    </style>
  </head>
  <body>
    <!-- Style 2 (HyperFrames) – dijana oleh styles/style-2/build.py. Jangan edit tangan; ubah config projek dan bina semula. -->
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
    os.makedirs(os.path.join(W, "assets", "sfx"), exist_ok=True)
    sfx_dur = {}
    for f in os.listdir(os.path.join(HERE, "sfx")):
        shutil.copyfile(os.path.join(HERE, "sfx", f), os.path.join(W, "assets", "sfx", f))
        sfx_dur[os.path.splitext(f)[0]] = duration(os.path.join(HERE, "sfx", f))
    y = mean_luma()
    patch = brighten_patch(y)
    print(f"# kecerahan purata YAVG={y:.0f}" + (f" → dicerahkan {json.dumps(patch)}" if patch else " (ok)"))
    comp = os.path.join(W, "compositions")
    if os.path.isdir(comp):
        shutil.rmtree(comp)
    os.makedirs(comp)
    files, hosts = {}, []
    if C.get("HOOK"):
        files["hook"] = build_hook(C["HOOK"])
        hosts.append(("hook", 0, C["HOOK"]["end"], 2, 5))
    kinds = {"vs": card_vs, "icon": card_icon, "check": card_check, "chips": card_chips}
    for i, k in enumerate(C.get("CARDS", [])):
        cid = f"card{i + 1}"
        files[cid] = kinds[k["kind"]](cid, k)
        hosts.append((cid, k["start"], k["end"] - k["start"], 2, 5))
    if C.get("RAIL"):
        r = C["RAIL"]
        files["rail"] = build_rail(r)
        hosts.append(("rail", r["start"], r["end"] - r["start"], 3, 6))
    if C.get("CTA"):
        files["cta"] = build_cta(C["CTA"], end)
        hosts.append(("cta", C["CTA"]["start"], end - C["CTA"]["start"], 2, 5))
    files["captions"] = build_captions(C["CAPTIONS"])
    hosts.append(("captions", 0, end, 4, 7))
    for k, v in files.items():
        open(os.path.join(comp, k + ".html"), "w").write(v)
    open(os.path.join(W, "index.html"), "w").write(build_index(keep, end, hosts, sfx_dur))
    name = os.path.splitext(os.path.basename(PROJ))[0]
    json.dump({"name": f"style2-{name}", "private": True, "type": "module"}, open(os.path.join(W, "package.json"), "w"))
    json.dump({"id": f"style2-{name}", "name": name}, open(os.path.join(W, "meta.json"), "w"))
    if patch:
        sh(["node", CLI, "media-treatment", "--project", W, "--selector", ".seg", "--grading", json.dumps(patch),
            "--apply", "--json"], stdout=subprocess.DEVNULL)
    print("->", W, "(seterusnya: hyperframes check / snapshot / render dalam folder ini)")


main()
