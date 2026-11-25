"""Sound effect sintetik (tiada isu hak cipta). python3 sfx.py <out_dir>"""
import sys, os, wave
import numpy as np

SR = 44100

def save(path, x, gain=0.8):
    x = x / (np.max(np.abs(x)) + 1e-9) * gain
    st = np.stack([x, x], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())

def t_(d):
    return np.arange(int(SR * d)) / SR

def lowpass(x, cutoff):
    """one-pole lowpass, cutoff boleh array (sweep)."""
    cutoff = np.broadcast_to(cutoff, x.shape)
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.zeros_like(x); prev = 0.0
    for i in range(len(x)):
        prev = (1 - a[i]) * x[i] + a[i] * prev
        y[i] = prev
    return y

def pop():  # sticker muncul
    t = t_(0.09)
    f = 950 * np.exp(-t * 28) + 260
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 45)

def click():  # pilihan kad bertukar
    t = t_(0.035)
    rng = np.random.default_rng(1)
    return (0.6 * np.sin(2 * np.pi * 2600 * t) + 0.4 * rng.standard_normal(len(t))) * np.exp(-t * 160)

def whoosh(d=0.38):  # tukar seksyen / tajuk masuk
    t = t_(d)
    rng = np.random.default_rng(2)
    n = rng.standard_normal(len(t))
    sweep = 400 + 5000 * np.sin(np.pi * t / d) ** 2
    hp = n - lowpass(n, 150)
    y = lowpass(hp, sweep)
    env = np.sin(np.pi * (t / d) ** 0.7) ** 2
    return y * env

def ding():  # CTA
    t = t_(1.1)
    y = sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * k)
            for f, a, k in [(1568, 1.0, 4.0), (3136, 0.35, 6.0), (4704, 0.15, 9.0), (2093, 0.4, 5.0)])
    att = np.minimum(1, t / 0.004)
    return y * att

def drop(d=0.38):  # pilihan ganti whoosh (SFX_WHOOSH = "drop"): titisan air + percikan kecil
    def one(t0, f0, f1, k):
        t = t_(d) - t0
        on = t >= 0
        tt = np.where(on, t, 0)
        f = f0 * (f1 / f0) ** np.minimum(tt / 0.07, 1)   # pic naik cepat = bunyi titisan
        ph = 2 * np.pi * np.cumsum(f * on) / SR
        return np.sin(ph) * np.minimum(1, tt / 0.003) * np.exp(-tt * k) * on
    return one(0.0, 420, 1500, 32) + 0.35 * one(0.11, 700, 1900, 45)

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    save(os.path.join(out, "pop.wav"), pop(), 0.7)
    save(os.path.join(out, "click.wav"), click(), 0.5)
    save(os.path.join(out, "whoosh.wav"), whoosh(), 0.6)
    save(os.path.join(out, "ding.wav"), ding(), 0.55)
    save(os.path.join(out, "drop.wav"), drop(), 0.6)
    print("ok", out)
