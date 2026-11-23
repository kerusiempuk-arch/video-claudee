"""TikTok edit: perancah lipat. Usage:
  python3 render.py <input.mp4> <output.mp4> [--preview]
Preview = 540x960 + PREVIEW watermark, final = 1080x1920.
"""
import subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC, OUT = sys.argv[1], sys.argv[2]
PREVIEW = "--preview" in sys.argv
W, H = (540, 960) if PREVIEW else (1080, 1920)
S = W / 1080  # design coordinates are 1080x1920
FPS = 30
END = 21.3

INTER = "/usr/share/fonts/opentype/inter/"
F_BOLD = INTER + "Inter-Bold.otf"
F_XBOLD = INTER + "InterDisplay-Bold.otf"
F_SEMI = INTER + "Inter-SemiBold.otf"
F_MED = INTER + "Inter-Medium.otf"
F_MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Medium.ttf"

INK = (22, 22, 26, 255)
WHITE = (255, 255, 255, 255)
ACCENT = (110, 123, 255, 255)   # biru-ungu kata kunci
BLUE = (66, 99, 235, 255)        # progress / selection
RED = (229, 72, 77, 255)
CARD = (24, 24, 28, 235)
GREY = (70, 70, 78, 255)

_fc = {}
def font(path, size):
    k = (path, round(size * S))
    if k not in _fc:
        _fc[k] = ImageFont.truetype(path, max(1, round(size * S)))
    return _fc[k]

def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3

def fade(t, a, b, fin=0.15, fout=0.15):
    if t < a or t > b:
        return 0.0
    return min(ease((t - a) / fin), ease((b - t) / fout) if fout else 1.0)

# ------------------------------------------------------------------ timeline
# Kapsyen ikut suara (dari transkripsi). (start, end, [(word, highlight)])
CAPTIONS = [
    (0.00, 1.00, [("Nanti-nanti", False)]),
    (1.00, 2.40, [("saya", False), ("nak", False), ("naik", False), ("atas", True)]),
    (8.30, 9.40, [("Nanti", False), ("dulu", True)]),
]
HOOK_END = 3.0
SECTIONS = [  # (start, end, label, num, subtitle)
    (3.0, 9.2, "kelebihan", "1 / 3", "naik senang"),
    (9.2, 14.4, "kelebihan", "2 / 3", "kukuh & stabil"),
    (14.4, 18.4, "kelebihan", "3 / 3", "berdiri pun boleh"),
]
STICKERS = [  # (start, end, text, x, y, angle) – disusun bertindan macam reference
    (3.5, 9.0, "duduk pun selesa", 70, 300, 2.0),
    (5.4, 9.0, "sampai tingkap atas", 110, 370, -1.5),
    (9.6, 14.2, "besi tebal", 70, 300, 2.0),
    (10.8, 14.2, "tak goyang", 110, 370, -1.5),
    (12.2, 14.2, "tahan berat", 150, 440, 1.5),
    (14.8, 18.3, "platform lebar", 70, 300, -2.0),
    (16.0, 18.3, "selamat buat kerja cat", 110, 370, 1.5),
]
CIRCLES = [  # (start, end, cx, cy, r, label, label_x, label_y)
    (6.0, 7.8, 650, 225, 85, "tinggi", 760, 250),
    (10.6, 12.4, 860, 735, 80, "besi kukuh", 560, 800),
]
CTA_TITLE = (18.4, END, "kukuh")
CTA_CARD_START = 19.3

# ------------------------------------------------------------------ helpers
def shadow_text(base, xy, text, f, fill, alpha, blur=6, shadow_a=150, anchor="mm"):
    if alpha <= 0:
        return
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((xy[0], xy[1] + 3 * S), text, font=f, fill=(0, 0, 0, int(shadow_a * alpha)), anchor=anchor)
    sh = sh.filter(ImageFilter.GaussianBlur(blur * S))
    base.alpha_composite(sh)
    lay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    c = fill[:3] + (int(fill[3] * alpha),)
    ImageDraw.Draw(lay).text(xy, text, font=f, fill=c, anchor=anchor)
    base.alpha_composite(lay)

def rrect(d, box, r, fill):
    d.rounded_rectangle([v * S for v in box], radius=r * S, fill=fill)

def with_alpha(c, a):
    return c[:3] + (int(c[3] * a),)

# top gradient (macam langit terang dalam reference) supaya teks gelap nampak jelas
def make_gradient():
    g = Image.new("L", (1, 256))
    for y in range(256):
        g.putpixel((0, y), int(245 * (1 - y / 255) ** 1.3))
    g = g.resize((W, int(560 * S)))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    white = Image.new("RGBA", g.size, (246, 247, 250, 255))
    white.putalpha(g)
    lay.alpha_composite(white, (0, 0))
    return lay
GRAD = make_gradient()

# ------------------------------------------------------------------ elements
def draw_progress(img, t):
    if t < HOOK_END:
        return
    a = ease((t - HOOK_END) / 0.3)
    d = ImageDraw.Draw(img)
    x0, x1, y = 60, 1020, 118
    d.rectangle([x0 * S, y * S, x1 * S, (y + 4) * S], fill=(120, 120, 130, int(140 * a)))
    p = (t - HOOK_END) / (END - HOOK_END)
    d.rectangle([x0 * S, y * S, (x0 + (x1 - x0) * p) * S, (y + 4) * S], fill=with_alpha(BLUE, a))

def draw_section(img, t):
    for a0, a1, label, num, sub in SECTIONS:
        a = fade(t, a0, a1, 0.2, 0.0 if a1 < 18 else 0.2)
        if a <= 0:
            continue
        d = ImageDraw.Draw(img)
        fm = font(F_MONO, 30)
        n1, n2 = num.split(" / ")
        parts = [(label + " ", WHITE), (n1, ACCENT), (" / " + n2, WHITE)]
        tw = sum(d.textlength(p, font=fm) for p, _ in parts) / S
        x, y = 60, 140
        rrect(d, (x, y, x + tw + 28, y + 52), 8, with_alpha(CARD, a))
        cx = (x + 14) * S
        for p, c in parts:
            d.text((cx, (y + 26) * S), p, font=fm, fill=with_alpha(c, a), anchor="lm")
            cx += d.textlength(p, font=fm)
        d.text(((x + tw + 46) * S, (y + 26) * S), sub, font=font(F_MED, 32), fill=with_alpha(INK, a), anchor="lm")

def draw_caption(img, t):
    for a0, a1, words in CAPTIONS:
        if not (a0 <= t <= a1):
            continue
        f = font(F_BOLD, 58)
        d = ImageDraw.Draw(img)
        widths = [d.textlength(w, font=f) for w, _ in words]
        gap = d.textlength(" ", font=f)
        total = sum(widths) + gap * (len(words) - 1)
        x = W / 2 - total / 2
        n = len(words)
        for i, ((w, hi), ww) in enumerate(zip(words, widths)):
            ws = a0 + (a1 - a0 - 0.3) * i / max(1, n)   # perkataan muncul satu-satu
            a = fade(t, ws, a1, 0.12, 0.12)
            pop = 1 - 0.0 * a
            y = 1010 * S + (1 - ease((t - ws) / 0.15)) * 14 * S
            shadow_text(img, (x + ww / 2, y), w, f, ACCENT if hi else WHITE, a)
            x += ww + gap

def sticker(img, text, x, y, angle, a, t_in):
    if a <= 0:
        return
    f = font(F_SEMI, 34)
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    tw = tmp.textlength(text, font=f)
    pw, ph = int(tw + 36 * S), int(60 * S)
    pad = int(20 * S)
    s = Image.new("RGBA", (pw + 2 * pad, ph + 2 * pad), (0, 0, 0, 0))
    sh = Image.new("RGBA", s.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([pad, pad + 4 * S, pad + pw, pad + ph + 4 * S], radius=8 * S, fill=(0, 0, 0, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(7 * S))
    s.alpha_composite(sh)
    d = ImageDraw.Draw(s)
    d.rounded_rectangle([pad, pad, pad + pw, pad + ph], radius=8 * S, fill=(255, 255, 255, 255))
    d.text((pad + pw / 2, pad + ph / 2), text, font=f, fill=INK, anchor="mm")
    # pop-in: scale 0.8 -> 1
    k = 0.8 + 0.2 * ease((t_in) / 0.18)
    s = s.resize((max(1, int(s.width * k)), max(1, int(s.height * k))), Image.LANCZOS)
    s = s.rotate(angle, resample=Image.BICUBIC, expand=True)
    if a < 1:
        al = s.getchannel("A").point(lambda v: int(v * a))
        s.putalpha(al)
    img.alpha_composite(s, (int(x * S - pad), int(y * S - pad)))

def draw_stickers(img, t):
    for a0, a1, text, x, y, ang in STICKERS:
        a = fade(t, a0, a1, 0.12, 0.15)
        sticker(img, text, x, y, ang, a, t - a0)

def draw_circles(img, t):
    for a0, a1, cx, cy, r, label, lx, ly in CIRCLES:
        a = fade(t, a0, a1, 0.2, 0.2)
        if a <= 0:
            continue
        k = 0.7 + 0.3 * ease((t - a0) / 0.25)
        rr = r * k
        d = ImageDraw.Draw(img)
        d.ellipse([(cx - rr) * S, (cy - rr) * S, (cx + rr) * S, (cy + rr) * S], outline=with_alpha(BLUE, a), width=max(2, int(6 * S)))
        sticker(img, label, lx, ly, 3, a, t - a0)

def draw_hook(img, t):
    a = fade(t, 0.0, HOOK_END, 0.01, 0.25)
    if a <= 0:
        return
    d = ImageDraw.Draw(img)
    d.text((W / 2, 112 * S), "perancah lipat paling", font=font(F_MED, 34), fill=with_alpha(GREY, a), anchor="mm")
    big_title(img, "kukuh", 215, a, t)
    # kad pilihan gaya tetingkap
    ca = fade(t, 0.25, HOOK_END, 0.25, 0.25)
    if ca <= 0:
        return
    sel = None if t < 1.0 else (0 if t < 2.0 else 1)
    card(img, ca, 1110, options=[("Ringan nak angkat", "01"), ("Kukuh nak panjat", "02")], sel=sel)

def big_title(img, word, y, a, t, size=150):
    f = font(F_XBOLD, size)
    d = ImageDraw.Draw(img)
    tw = d.textlength(word, font=f)
    x = W / 2 - tw / 2 - 14 * S
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.text((x, y * S), word, font=f, fill=with_alpha(INK, a), anchor="lm")
    dot = 26
    ld.rectangle([x + tw + 8 * S, (y + 38) * S, x + tw + (8 + dot) * S, (y + 38 + dot) * S], fill=with_alpha(RED, a))
    img.alpha_composite(lay)

def window_card(img, a, top, height, width=620):
    d = ImageDraw.Draw(img)
    x0 = 540 - width / 2
    rrect(d, (x0, top, x0 + width, top + height), 18, with_alpha(CARD, a))
    for i, c in enumerate([(255, 95, 87, 255), (254, 188, 46, 255), (40, 200, 64, 255)]):
        cx = x0 + 30 + i * 22
        d.ellipse([(cx - 6) * S, (top + 30 - 6) * S, (cx + 6) * S, (top + 30 + 6) * S], fill=with_alpha(c, a))
    d.text(((x0 + 100) * S, (top + 30) * S), "Perancah Lipat", font=font(F_MED, 24), fill=with_alpha((220, 220, 228, 255), a), anchor="lm")
    return d, x0

def card(img, a, top, options, sel):
    d, x0 = window_card(img, a, top, 190)
    for i, (txt, num) in enumerate(options):
        y = top + 60 + i * 62
        if sel == i:
            rrect(d, (x0 + 14, y, x0 + 606, y + 54), 10, with_alpha(BLUE, a))
        col = WHITE if sel == i else (200, 200, 208, 255)
        d.text(((x0 + 34) * S, (y + 27) * S), txt, font=font(F_MED, 32), fill=with_alpha(col, a), anchor="lm")
        d.text(((x0 + 586) * S, (y + 27) * S), num, font=font(F_MONO, 22), fill=with_alpha((170, 170, 180, 255), a), anchor="rm")

def draw_cta(img, t):
    a0, a1, word = CTA_TITLE
    a = fade(t, a0, a1, 0.2, 0.01)
    if a > 0:
        big_title(img, word + "", 250, a, t, size=170)
    ca = fade(t, CTA_CARD_START, END, 0.25, 0.01)
    if ca <= 0:
        return
    top = 1090 + (1 - ease((t - CTA_CARD_START) / 0.3)) * 40
    d, x0 = window_card(img, ca, top, 250)
    d.text(((x0 + 30) * S, (top + 82) * S), "Perancah Lipat", font=font(F_XBOLD, 46), fill=with_alpha(WHITE, ca), anchor="lm")
    d.text(((x0 + 30) * S, (top + 124) * S), "ringan · kukuh · boleh lipat", font=font(F_MONO, 22), fill=with_alpha((160, 160, 170, 255), ca), anchor="lm")
    rrect(d, (x0 + 20, top + 160, x0 + 600, top + 230), 35, with_alpha(RED, ca))
    d.text((540 * S, (top + 195) * S), "Link dekat bawah ↓", font=font(F_BOLD, 36), fill=with_alpha(WHITE, ca), anchor="mm")

def draw_watermark(img):
    if not PREVIEW:
        return
    d = ImageDraw.Draw(img)
    d.text((W / 2, 1780 * S), "PREVIEW", font=font(F_BOLD, 40), fill=(255, 255, 255, 110), anchor="mm")

def frame(t):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ga = 1.0
    img.alpha_composite(GRAD)
    draw_progress(img, t)
    draw_section(img, t)
    draw_hook(img, t)
    draw_stickers(img, t)
    draw_circles(img, t)
    draw_caption(img, t)
    draw_cta(img, t)
    draw_watermark(img)
    return img

# ------------------------------------------------------------------ render
if __name__ == "__main__":
    if "--still" in sys.argv:  # debug: python3 render.py in out.png --preview --still 5.0
        t = float(sys.argv[-1])
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", SRC, "-frames:v", "1",
                        "-vf", f"scale={W}:{H}", "/tmp/_bg.png"], check=True)
        bg = Image.open("/tmp/_bg.png").convert("RGBA")
        bg.alpha_composite(frame(t))
        bg.convert("RGB").save(OUT)
        sys.exit()
    n = int(END * FPS)
    # latar: zoom perlahan 1.00 -> 1.05, potong hujung yang kamera jatuh
    vf = (f"[0:v]trim=0:{END},setpts=PTS-STARTPTS,"
          f"scale=w='trunc({W}*(1+0.05*t/{END})/2)*2':h=-2:eval=frame,crop={W}:{H},fps={FPS},format=rgba[bg];"
          f"[bg][1:v]overlay=0:0:format=auto,format=yuv420p[v];"
          f"[0:a]atrim=0:{END},asetpts=PTS-STARTPTS,afade=t=out:st={END-0.4}:d=0.4,loudnorm=I=-14:TP=-1.5[a]")
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", SRC,
           "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-filter_complex", vf, "-map", "[v]", "-map", "[a]",
           "-c:v", "libx264", "-preset", "veryfast" if PREVIEW else "slow",
           "-crf", "26" if PREVIEW else "17", "-c:a", "aac", "-b:a", "192k",
           "-movflags", "+faststart", "-t", str(END), OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close()
    sys.exit(p.wait())
