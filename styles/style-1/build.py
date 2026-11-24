"""Style 1 (HyperFrames) – jana projek HyperFrames dari video mentah + config projek.

Guna (dari root repo):
  python3 -I styles/style-1/build.py <raw.mp4> <projects/nama.py> <work_dir>            # bina projek
  python3 -I styles/style-1/build.py <raw.mp4> <projects/nama.py> <work_dir> --plan     # cetak potongan + END sahaja
  python3 -I styles/style-1/build.py <raw.mp4> <projects/nama.py> <work_dir> --cut-audio <out.wav>
                                                                    # audio bersih selepas dipotong (untuk transkripsi)
Lepas itu, dalam <work_dir>:  hyperframes check  /  snapshot --at …  /  render -q draft|high -o …

Apa yang build.py buat (automatik):
  1. Potongan: senyap > MIN_SILENCE + REMOVE + SRC_END (logik sama dengan cut.py lama). Setiap segmen
     <video> sendiri; segmen selang-seli punch-in PUNCH (fokus PUNCH_Y). Masa overlay = masa SELEPAS potong.
  2. Bunyi: hanya suara utama – highpass + RNNoise (arnndn) + lowpass, kemudian loudnorm −14 LUFS.
     Video dibisukan; suara bersih main sebagai <audio> yang dipotong sama.
  3. Kecerahan: ukur purata luma (YAVG). Kalau < DARK_Y (105) → exposure/shadows dinaikkan melalui
     `hyperframes media-treatment` (atau ikut BRIGHTEN dalam config).
  4. Overlay Style 1: gradient putih atas, zoom perlahan, hook (kicker + tajuk besar + titik merah + kad
     macOS dengan pilihan 01/02), progress bar + label "kelebihan n / N", sticker putih condong,
     bulatan biru, kapsyen bawah ikut perkataan, CTA (tajuk + kad + butang), sound effect.
"""
import html, json, math, os, runpy, shutil, subprocess, sys, wave, array

HERE = os.path.dirname(os.path.abspath(__file__))
CLI = os.path.expanduser("~/.claude/skills/hyperframes/scripts/plugin-cli.mjs")
RNN_URL = "https://raw.githubusercontent.com/GregorR/rnnoise-models/master/conjoined-burgers-2018-08-28/cb.rnnn"
RNN = os.path.expanduser("~/.cache/style1/cb.rnnn")

RAW, PROJ, W = sys.argv[1], sys.argv[2], sys.argv[3]
C = runpy.run_path(PROJ)

# ------------------------------------------------------------------ config (default sama dengan engine.py lama)
REMOVE = C.get("REMOVE", [])
SILENCE_DB = C.get("SILENCE_DB", -38)
MIN_SIL = C.get("MIN_SILENCE", 0.30)
PAD = C.get("PAD", 0.06)
PUNCH = C.get("PUNCH", 1.08)
TAIL = C.get("TAIL", 0.0)
PUNCH_Y = C.get("PUNCH_Y", 0.35)
CAPTION_Y = C.get("CAPTION_Y", 1780)
CARD_Y = C.get("CARD_Y", 1110)
ZOOM = C.get("ZOOM", 0.05)
DENOISE = C.get("DENOISE", True)
DARK_Y = C.get("DARK_Y", 105)
BRIGHTEN = C.get("BRIGHTEN", "auto")      # "auto" | None | {"exposure":..,"shadows":..,"blacks":..}

def rgb(c, a=None):
    al = (c[3] / 255 if len(c) > 3 else 1) if a is None else a
    return f"rgba({c[0]},{c[1]},{c[2]},{al:.3f})"

INK = (22, 22, 26)
ACCENT = (110, 123, 255)
BLUE = (66, 99, 235)
RED = (229, 72, 77)
CAPTION_ACCENT = tuple(C.get("CAPTION_ACCENT", ACCENT))[:3]


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def duration(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


# ------------------------------------------------------------------ 1. potongan (port cut.py)
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


# ------------------------------------------------------------------ 2. suara bersih
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
    parts = []
    for i, (a, b) in enumerate(keep):
        d = b - a
        parts.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,"
                     f"afade=t=out:st={max(0, d - 0.015):.3f}:d=0.015[a{i}]")
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
    e = max(0.15, min(0.8, (118 - y) / 85))
    return {"adjust": {"exposure": round(e, 2), "shadows": 0.25, "blacks": 0.08}}


# ------------------------------------------------------------------ 4. HTML
FONT_CSS = """
    @font-face { font-family: "S1 Inter"; font-weight: 500; src: url("assets/fonts/Inter-Medium.otf"); }
    @font-face { font-family: "S1 Inter"; font-weight: 600; src: url("assets/fonts/Inter-SemiBold.otf"); }
    @font-face { font-family: "S1 Inter"; font-weight: 700; src: url("assets/fonts/Inter-Bold.otf"); }
    @font-face { font-family: "S1 Display"; font-weight: 700; src: url("assets/fonts/InterDisplay-Bold.otf"); }
    @font-face { font-family: "S1 Mono"; font-weight: 500; src: url("assets/fonts/JetBrainsMono-Medium.ttf"); }"""

esc = html.escape


def scene(cid, css, body, js):
    return f"""<template>
  <style>{FONT_CSS}
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


def f2(x):
    return f"{x:.3f}"


def fade_js(sel, a0, a1, fin, fout, extra_from="", extra_to=""):
    """Masuk di a0 (fin s), keluar sebelum a1 (fout s) – opacity pada anak .clip."""
    js = f'    tl.fromTo("{sel}", {{ opacity: 0{extra_from} }}, {{ opacity: 1{extra_to}, duration: {fin}, ease: "power3.out" }}, {f2(a0)});\n'
    if fout:
        js += f'    tl.to("{sel}", {{ opacity: 0, duration: {fout}, ease: "power2.in" }}, {f2(max(a0 + fin, a1 - fout))});\n'
    return js


def window_card_html(pre, label, height, inner):
    return f"""      <div class="win" style="height:{height}px">
        <div class="dots"><i style="background:#FF5F57"></i><i style="background:#FEBC2E"></i><i style="background:#28C840"></i></div>
        <div class="wlabel">{esc(label)}</div>
{inner}
      </div>"""


WIN_CSS = """
    .win { position: absolute; left: 0; top: 0; width: 620px; border-radius: 18px; background: rgba(24,24,28,.92); }
    .dots { position: absolute; left: 24px; top: 24px; display: flex; gap: 10px; }
    .dots i { display: block; width: 12px; height: 12px; border-radius: 6px; }
    .wlabel { position: absolute; left: 100px; top: 14px; height: 32px; line-height: 32px; font: 500 24px "S1 Inter"; color: rgb(220,220,228); }"""

TITLE_CSS = """
    .big { position: absolute; left: 0; width: 1080px; height: 220px; display: flex; justify-content: center; align-items: center; }
    .big span { position: relative; font-family: "S1 Display"; font-weight: 700; color: rgb(22,22,26); line-height: 1; letter-spacing: -1px; left: -14px; }
    .big b { position: absolute; right: -34px; bottom: 0.13em; width: 26px; height: 26px; background: rgb(229,72,77); }"""


def big_title_html(id_, word, y, size):
    return f'<div class="big" style="top:{y - 110}px"><span id="{id_}" style="font-size:{size}px">{esc(word)}<b></b></span></div>'


def build_hook(H, end):
    body, js = [], ""
    y = H.get("y", 112)
    body.append(f'    <div id="hk" class="clip" data-start="0" data-duration="{f2(end)}">')
    body.append(f'      <div id="hk-in">')
    body.append(f'        <div class="kick" style="top:{y - 25}px">{esc(H["kicker"])}</div>')
    body.append("        " + big_title_html("hk-title", H["title"], y + 103, 150))
    body.append("      </div>")
    opts = ""
    for i, (txt, num) in enumerate(H["options"]):
        oy = 60 + i * 62
        opts += (f'        <div class="opt" style="top:{oy}px"><div class="sel" id="hk-sel{i}"></div>'
                 f'<span class="ot" id="hk-ot{i}">{esc(txt)}</span><span class="on">{esc(num)}</span></div>\n')
    body.append(f'      <div id="hk-card" style="position:absolute;left:230px;top:{CARD_Y}px;width:620px;height:190px">')
    body.append(window_card_html("hk", C["CTA"]["card_label"], 190, opts.rstrip()))
    body.append("      </div>")
    body.append("    </div>")
    css = WIN_CSS + TITLE_CSS + """
    .kick { position: absolute; left: 0; width: 1080px; height: 50px; line-height: 50px; text-align: center; font: 500 34px "S1 Inter"; color: rgb(22,22,26); }
    .opt { position: absolute; left: 14px; width: 592px; height: 54px; }
    .sel { position: absolute; inset: 0; border-radius: 10px; background: rgb(66,99,235); opacity: 0; }
    .ot { position: absolute; left: 20px; top: 0; height: 54px; line-height: 54px; font: 500 32px "S1 Inter"; color: rgb(200,200,208); }
    .on { position: absolute; right: 20px; top: 0; height: 54px; line-height: 54px; font: 500 22px "S1 Mono"; color: rgb(170,170,180); }"""
    js += f'    tl.fromTo("#hk-in", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.25, ease: "power2.in" }}, {f2(end - 0.25)});\n'
    js += f'    tl.fromTo("#hk-card", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out" }}, 0.25);\n'
    js += f'    tl.to("#hk-card", {{ opacity: 0, duration: 0.25, ease: "power2.in" }}, {f2(end - 0.25)});\n'
    sel_at = list(H["select_at"]) + [1e9]
    for i in range(len(H["options"])):
        a, b = sel_at[i], sel_at[i + 1]
        if a >= end:
            continue
        js += f'    tl.fromTo("#hk-sel{i}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.06, ease: "none" }}, {f2(a)});\n'
        js += f'    tl.fromTo("#hk-ot{i}", {{ color: "rgb(200,200,208)" }}, {{ color: "rgb(255,255,255)", duration: 0.06, ease: "none" }}, {f2(a)});\n'
        if b < end:
            js += f'    tl.to("#hk-sel{i}", {{ opacity: 0, duration: 0.06, ease: "none" }}, {f2(b)});\n'
            js += f'    tl.to("#hk-ot{i}", {{ color: "rgb(200,200,208)", duration: 0.06, ease: "none" }}, {f2(b)});\n'
    return scene("hook", css, "\n".join(body), js)


def build_sections(hook_end, end, sections):
    dur = end - hook_end
    body = [f'    <div id="sc-bar" class="clip" data-start="0" data-duration="{f2(dur)}" data-layout-ignore>',
            '      <div id="sc-bar-in"><div class="track"></div><div class="fill" id="sc-fill"></div></div>',
            "    </div>"]
    css = """
    #sc-bar-in { position: absolute; left: 60px; top: 118px; width: 960px; height: 4px; }
    .track { position: absolute; inset: 0; background: rgba(120,120,130,.55); }
    .fill { position: absolute; inset: 0; background: rgb(66,99,235); transform-origin: 0 50%; }
    .lab { position: absolute; left: 60px; top: 140px; height: 52px; display: flex; align-items: center; gap: 18px; }
    .pill { height: 52px; padding: 0 14px; border-radius: 8px; background: rgba(24,24,28,.92); display: flex; align-items: center;
      font: 500 30px "S1 Mono"; color: #fff; white-space: pre; }
    .pill em { font-style: normal; color: rgb(110,123,255); }
    .sub { font: 500 32px "S1 Inter"; color: rgb(22,22,26); white-space: nowrap; }"""
    js = '    tl.fromTo("#sc-bar-in", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power3.out" }, 0);\n'
    js += f'    tl.fromTo("#sc-fill", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {f2(dur)}, ease: "none" }}, 0);\n'
    for i, (a0, a1, label, num, sub) in enumerate(sections):
        n1, n2 = [s.strip() for s in num.split("/")]
        s, d = a0 - hook_end, a1 - a0
        body.append(f'    <div id="sc{i}" class="clip" data-start="{f2(max(0, s))}" data-duration="{f2(d)}">')
        body.append(f'      <div class="lab" id="sc{i}-in"><div class="pill">{esc(label)} <em>{esc(n1)}</em> / {esc(n2)}</div>'
                    f'<div class="sub">{esc(sub)}</div></div>')
        body.append("    </div>")
        last = i == len(sections) - 1
        js += fade_js(f"#sc{i}-in", max(0, s), max(0, s) + d, 0.2, 0.2 if last else 0)
    return scene("sections", css, "\n".join(body), js)


def sticker_html(id_, text, x, y, ang):
    return (f'<div class="stk" style="left:{x}px;top:{y}px;transform:rotate({-ang}deg)">'
            f'<div class="stk-in" id="{id_}">{esc(text)}</div></div>')


def build_stickers(stickers, circles):
    body, js = [], ""
    css = """
    .stk { position: absolute; transform-origin: 50% 50%; }
    .stk-in { height: 60px; padding: 0 18px; border-radius: 8px; background: #fff; display: flex; align-items: center;
      font: 600 34px "S1 Inter"; color: rgb(22,22,26); white-space: nowrap; box-shadow: 0 4px 14px rgba(0,0,0,.35); }
    .ring { position: absolute; border: 6px solid rgb(66,99,235); border-radius: 50%; box-sizing: border-box; }"""
    for i, (a0, a1, text, x, y, ang) in enumerate(stickers):
        body.append(f'    <div id="st{i}" class="clip" data-start="{f2(a0)}" data-duration="{f2(a1 - a0)}">'
                    + sticker_html(f"st{i}-in", text, x, y, ang) + "</div>")
        js += fade_js(f"#st{i}-in", a0, a1, 0.12, 0.15, ", scale: 0.8", ", scale: 1")
    for i, (a0, a1, cx, cy, r, label, lx, ly) in enumerate(circles):
        body.append(f'    <div id="ci{i}" class="clip" data-start="{f2(a0)}" data-duration="{f2(a1 - a0)}">'
                    f'<div class="ring" id="ci{i}-r" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px"></div>'
                    + sticker_html(f"ci{i}-l", label, lx, ly, 3) + "</div>")
        js += fade_js(f"#ci{i}-r", a0, a1, 0.25, 0.2, ", scale: 0.7", ", scale: 1")
        js += fade_js(f"#ci{i}-l", a0, a1, 0.12, 0.2, ", scale: 0.8", ", scale: 1")
    if not body:
        body.append('    <div id="st-none" class="clip" data-start="0" data-duration="0.1"></div>')
    return scene("stickers", css, "\n".join(body), js)


def build_captions(caps):
    body, js = [], ""
    css = f"""
    .cap {{ position: absolute; left: 0; top: {CAPTION_Y - 50}px; width: 1080px; height: 100px; display: flex; justify-content: center;
      align-items: center; gap: 0.25em; font: 700 60px "S1 Inter"; white-space: nowrap; }}
    .cw {{ display: inline-block; color: #fff; -webkit-text-stroke: 4px rgba(20,20,30,.67); paint-order: stroke fill;
      text-shadow: 0 3px 7px rgba(0,0,0,.86); }}
    .cw.hi {{ color: {rgb(CAPTION_ACCENT)}; }}"""
    for i, (g_end, words) in enumerate(caps):
        g0 = words[0][1]
        nxt = caps[i + 1][1][0][1] if i + 1 < len(caps) else 1e9
        g1 = min(g_end, nxt)
        spans = " ".join(f'<span class="cw{" hi" if hi else ""}" id="cp{i}w{j}">{esc(w)}</span>'
                         for j, (w, ws, hi) in enumerate(words))
        body.append(f'    <div id="cp{i}" class="clip cap" data-start="{f2(g0)}" data-duration="{f2(g1 - g0)}">{spans}</div>')
        for j, (w, ws, hi) in enumerate(words):
            js += (f'    tl.fromTo("#cp{i}w{j}", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.15, ease: "power3.out" }}, '
                   f'{f2(max(g0, ws))});\n')
    return scene("captions", css, "\n".join(body), js)


def build_cta(cta, end):
    body, js = [], ""
    t0, c0 = cta["title_at"], cta["card_at"]
    bc = cta.get("button_color", RED)
    tc = cta.get("button_text_color", (255, 255, 255))
    nm_px = max(30, min(46, int(560 / (0.53 * max(1, len(cta["name"]))))))  # nama panjang -> font kecil, muat dalam kad
    css = WIN_CSS + TITLE_CSS + f"""
    .nm {{ position: absolute; left: 30px; top: 57px; height: 50px; line-height: 50px; font: 700 {nm_px}px "S1 Display"; color: #fff; white-space: nowrap; }}
    .tg {{ position: absolute; left: 30px; top: 110px; height: 28px; line-height: 28px; font: 500 22px "S1 Mono"; color: rgb(160,160,170); white-space: nowrap; }}
    .btn {{ position: absolute; left: 20px; top: 160px; width: 580px; height: 70px; border-radius: 35px; background: {rgb(bc)};
      display: flex; align-items: center; justify-content: center; font: 700 36px "S1 Inter"; color: {rgb(tc)}; }}"""
    body.append(f'    <div id="ct-t" class="clip" data-start="{f2(t0)}" data-duration="{f2(end - t0)}">'
                + big_title_html("ct-title", cta["title"], cta.get("title_y", 250), 170) + "</div>")
    inner = (f'        <div class="nm">{esc(cta["name"])}</div>\n        <div class="tg">{esc(cta["tags"])}</div>\n'
             f'        <div class="btn">{esc(cta["button"])}</div>')
    body.append(f'    <div id="ct-c" class="clip" data-start="{f2(c0)}" data-duration="{f2(end - c0)}">'
                f'<div id="ct-card" style="position:absolute;left:230px;top:{cta.get("card_y", 1090)}px;width:620px;height:250px">\n'
                + window_card_html("ct", cta["card_label"], 250, inner) + "\n    </div></div>")
    js += '    tl.fromTo("#ct-title", { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "power3.out" }, ' + f2(t0) + ");\n"
    js += '    tl.fromTo("#ct-card", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, ' + f2(c0) + ");\n"
    return scene("cta", css, "\n".join(body), js)


def sfx_events(end):
    if not C.get("SFX", True):
        return []
    H, S_, ST, CI, CTA = C["HOOK"], C["SECTIONS"], C["STICKERS"], C["CIRCLES"], C["CTA"]
    ev = [(0.0, "whoosh", 0.5)]
    ev += [(ts, "click", 0.6) for ts in H["select_at"]]
    ev += [(a0, "whoosh", 0.45) for a0, *_ in S_]
    ev += [(a0, "pop", 0.55) for a0, *_ in ST]
    ev += [(c[0], "pop", 0.55) for c in CI]
    ev += [(CTA["title_at"], "whoosh", 0.5), (CTA["card_at"], "ding", 0.5)]
    ev += [tuple(e) for e in C.get("EXTRA_SFX", [])]
    return sorted((max(0.0, t), n, v) for t, n, v in ev if t < end)


SFX_DUR = {}


def build_index(keep, end, patch):
    segs, auds, at = [], [], 0.0
    for i, (a, b) in enumerate(keep):
        d = round(b - a, 3)
        punch = i % 2 == 1 and PUNCH != 1.0
        style = f' style="transform:scale({PUNCH});transform-origin:50% {PUNCH_Y * 100:.0f}%"' if punch else ""
        segs.append(f'        <video id="seg{i}" class="clip seg" src="src.mp4" muted playsinline data-start="{f2(at)}" '
                    f'data-media-start="{a}" data-duration="{d}" data-track-index="0"{style}></video>')
        last = i == len(keep) - 1
        auds.append(f'      <audio id="vo{i}" src="voice.m4a" data-start="{f2(at)}" data-media-start="{a}" data-duration="{d}" '
                    f'data-volume="1" data-fade-in="0.015" data-fade-out="{0.4 if last else 0.015}" data-track-index="1"></audio>')
        at += d
    sfx, lanes = [], []
    for k, (t, name, vol) in enumerate(sfx_events(end)):
        dur = SFX_DUR[name]
        lane = next((j for j, e in enumerate(lanes) if e <= t), None)
        if lane is None:
            lanes.append(0)
            lane = len(lanes) - 1
        lanes[lane] = t + dur
        sfx.append(f'      <audio id="sfx{k}-{name}" src="assets/sfx/{name}.wav" data-start="{f2(t)}" '
                   f'data-duration="{min(dur, end - t):.3f}" data-volume="{vol}" data-track-index="{6 + lane}"></audio>')
    hosts = [("hook", 0, C["HOOK"]["end"], 2), ("sections", C["HOOK"]["end"], end - C["HOOK"]["end"], 3),
             ("stickers", 0, end, 4), ("cta", 0, end, 4), ("captions", 0, end, 5)]
    host_html = "\n".join(
        f'      <div id="{h}" data-composition-id="{h}" data-composition-src="compositions/{h}.html" data-start="{f2(s)}" '
        f'data-duration="{f2(d)}" data-track-index="{ti}" data-track-kind="{"captions" if h == "captions" else "graphics"}" '
        f'data-width="1080" data-height="1920" style="z-index:{10 + n}"></div>'
        for n, (h, s, d, ti) in enumerate(hosts))
    grad = ("linear-gradient(180deg, rgba(246,247,250,.96) 0%, rgba(246,247,250,.66) 25%, "
            "rgba(246,247,250,.39) 50%, rgba(246,247,250,.16) 75%, rgba(246,247,250,0) 100%)")
    return f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      #bg {{ position: absolute; inset: 0; z-index: 1; overflow: hidden; }}
      .seg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
      #grad {{ position: absolute; left: 0; top: 0; width: 1080px; height: 560px; z-index: 5; background: {grad}; }}
    </style>
  </head>
  <body>
    <!-- Style 1 (HyperFrames) – dijana oleh styles/style-1/build.py. Jangan edit tangan; ubah config projek dan bina semula. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{f2(end)}" data-width="1080" data-height="1920">
      <div id="bg">
{chr(10).join(segs)}
      </div>
      <div id="grad"></div>
{host_html}
      <!-- suara utama sahaja (bunyi latar dibuang, −14 LUFS) -->
{chr(10).join(auds)}
      <!-- sound effect -->
{chr(10).join(sfx)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      tl.fromTo("#bg", {{ scale: 1 }}, {{ scale: {1 + ZOOM}, duration: {f2(end)}, ease: "none" }}, 0);
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
    if abs(C.get("END", end) - end) > 0.05 and C.get("END"):
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
    for d in ("fonts", "sfx"):
        os.makedirs(os.path.join(W, "assets", d), exist_ok=True)
    for f in os.listdir(os.path.join(HERE, "fonts")):
        if f.endswith((".otf", ".ttf")):
            shutil.copyfile(os.path.join(HERE, "fonts", f), os.path.join(W, "assets", "fonts", f))
    for f in os.listdir(os.path.join(HERE, "sfx")):
        shutil.copyfile(os.path.join(HERE, "sfx", f), os.path.join(W, "assets", "sfx", f))
        SFX_DUR[f[:-4]] = duration(os.path.join(HERE, "sfx", f))
    y = mean_luma()
    patch = brighten_patch(y)
    print(f"# kecerahan purata YAVG={y:.0f}" + (f" → dicerahkan {json.dumps(patch)}" if patch else " (ok)"))
    comp = os.path.join(W, "compositions")
    os.makedirs(comp, exist_ok=True)
    files = {
        "hook": build_hook(C["HOOK"], C["HOOK"]["end"]),
        "sections": build_sections(C["HOOK"]["end"], end, C["SECTIONS"]),
        "stickers": build_stickers(C["STICKERS"], C["CIRCLES"]),
        "captions": build_captions(C["CAPTIONS"]),
        "cta": build_cta(C["CTA"], end),
    }
    for k, v in files.items():
        open(os.path.join(comp, k + ".html"), "w").write(v)
    open(os.path.join(W, "index.html"), "w").write(build_index(keep, end, patch))
    name = os.path.splitext(os.path.basename(PROJ))[0]
    json.dump({"name": f"style1-{name}", "private": True, "type": "module"}, open(os.path.join(W, "package.json"), "w"))
    json.dump({"id": f"style1-{name}", "name": name}, open(os.path.join(W, "meta.json"), "w"))
    if patch:
        sh(["node", CLI, "media-treatment", "--project", W, "--selector", ".seg", "--grading", json.dumps(patch),
            "--apply", "--json"], stdout=subprocess.DEVNULL)
    print("->", W, "(seterusnya: hyperframes check / snapshot / render dalam folder ini)")


main()
