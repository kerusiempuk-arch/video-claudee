"""Bunyi kucing untuk video vitamin kucing SAHAJA (tidak ubah Style 1).
Jana meow sintetik (bebas hak cipta) dan tukar SFX dalam projek HyperFrames yang dah dibina.
  python3 -I styles/style-1/projects/vitamin_kucing_sfx.py work/v1/hf
Pemetaan: whoosh (tajuk/seksyen) -> meow, pop (sticker) -> mew, click (pilihan kad) -> mrrp, ding (kad CTA) -> meow panjang.
"""
import os, re, sys, wave
import numpy as np

SR = 44100


def save(path, x, gain=0.8):
    x = x / (np.max(np.abs(x)) + 1e-9) * gain
    st = np.stack([x, x], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())


def resonator(x, f, bw):
    """penapis formant 2-kutub, frekuensi boleh berubah (array)."""
    y = np.zeros_like(x); y1 = y2 = 0.0
    r = np.exp(-np.pi * bw / SR)
    for i in range(len(x)):
        c = 2 * r * np.cos(2 * np.pi * f[i] / SR)
        yi = x[i] + c * y1 - r * r * y2
        y[i] = yi; y2, y1 = y1, yi
    return y * (1 - r)


def env(pts, n):
    """kontur linear daripada [(pecahan_masa, nilai), ...]."""
    xs, vs = zip(*pts)
    return np.interp(np.linspace(0, 1, n), xs, vs)


def meow(d=0.55, f0=(560, 820, 760, 480), seed=0):
    n = int(SR * d)
    rng = np.random.default_rng(seed)
    pitch = env([(0, f0[0]), (0.3, f0[1]), (0.6, f0[2]), (1, f0[3])], n)
    pitch *= 1 + 0.012 * np.sin(2 * np.pi * 6 * np.arange(n) / SR)       # vibrato sikit
    ph = 2 * np.pi * np.cumsum(pitch) / SR
    src = sum(np.sin(k * ph) / k ** 1.1 for k in range(1, 14))             # sumber suara (harmonik)
    src += 0.04 * rng.standard_normal(n)                                    # nafas
    # m -> i -> a -> o -> w
    F1 = env([(0, 350), (0.15, 450), (0.4, 950), (0.75, 700), (1, 450)], n)
    F2 = env([(0, 1500), (0.15, 2300), (0.4, 1700), (0.75, 1100), (1, 900)], n)
    F3 = env([(0, 2800), (0.4, 3000), (1, 2600)], n)
    y = resonator(src, F1, 160) * 1.0 + resonator(src, F2, 220) * 0.7 + resonator(src, F3, 300) * 0.3
    a = env([(0, 0), (0.08, 0.5), (0.25, 1), (0.7, 0.85), (1, 0)], n)
    return y * a


def mrrp(d=0.16):
    n = int(SR * d)
    t = np.arange(n) / SR
    am = 0.6 + 0.4 * np.sin(2 * np.pi * 38 * t)                              # getar "rrr"
    return meow(d, f0=(420, 620, 640, 600), seed=3) * am


def make(out):
    os.makedirs(out, exist_ok=True)
    sounds = {
        "cat_meow": meow(0.55),
        "cat_mew": meow(0.26, f0=(820, 1050, 1000, 760), seed=1),
        "cat_mrrp": mrrp(),
        "cat_meow_long": meow(0.85, f0=(520, 760, 720, 420), seed=2),
    }
    dur = {}
    for k, x in sounds.items():
        save(os.path.join(out, k + ".wav"), x)
        dur[k] = len(x) / SR
    return dur


MAP = {"whoosh": ("cat_meow", 0.55), "drop": ("cat_meow", 0.55), "pop": ("cat_mew", 0.5),
       "click": ("cat_mrrp", 0.5), "ding": ("cat_meow_long", 0.6)}

if __name__ == "__main__":
    hf = sys.argv[1]
    dur = make(os.path.join(hf, "assets", "sfx"))
    p = os.path.join(hf, "index.html")
    html = open(p).read()
    pat = re.compile(r'      <audio id="sfx(\d+)-(\w+)" src="assets/sfx/\w+\.wav" data-start="([\d.]+)" '
                     r'data-duration="([\d.]+)" data-volume="([\d.]+)" data-track-index="(\d+)"></audio>')
    ms = list(pat.finditer(html))
    assert ms, "tiada SFX dijumpai dalam index.html"
    end = max(float(m.group(4)) + float(m.group(3)) for m in ms)
    lanes, new = [], []
    for m in ms:
        k, name, t = m.group(1), m.group(2), float(m.group(3))
        cat, vol = MAP.get(name, (name, float(m.group(5))))
        d = dur.get(cat, float(m.group(4)))
        d = min(d, max(0.05, end - t))
        lane = next((j for j, e in enumerate(lanes) if e <= t), None)
        if lane is None:
            lanes.append(0); lane = len(lanes) - 1
        lanes[lane] = t + d
        new.append(f'      <audio id="sfx{k}-{cat}" src="assets/sfx/{cat}.wav" data-start="{t:.2f}" '
                   f'data-duration="{d:.3f}" data-volume="{vol}" data-track-index="{6 + lane}"></audio>')
    s, e = ms[0].start(), ms[-1].end()
    html = html[:s] + "\n".join(new) + html[e:]
    open(p, "w").write(html)
    print(f"{len(new)} SFX ditukar ke bunyi kucing, {len(lanes)} lorong")
