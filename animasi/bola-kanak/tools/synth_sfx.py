"""Sintesis SFX fizikal (tiada akses Openverse dalam sesi ini). Deterministik (seed tetap)."""
import numpy as np, wave, os
SR = 44100
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "sfx")
rng = np.random.default_rng(7)

def save(name, x, peak=0.89):
    x = np.asarray(x, dtype=np.float64)
    x = x / (np.max(np.abs(x)) + 1e-9) * peak
    s = (x * 32767).astype(np.int16)
    st = np.stack([s, s], axis=1)
    with wave.open(os.path.join(OUT, name + ".wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())

def t(d): return np.arange(int(SR * d)) / SR
def env(d, a, r): tt = t(d); return np.minimum(tt / a, 1) * np.exp(-tt / r)
def lp(x, a):  # one-pole low-pass, a in (0,1): smaller = darker
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x): acc += a * (v - acc); y[i] = acc
    return y
def hp(x, a): return x - lp(x, a)
noise = lambda d: rng.standard_normal(int(SR * d))

# sepakan: thump rendah + klik kulit bola
d = 0.35; tt = t(d)
f = 140 * np.exp(-tt * 18) + 55
thump = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(d, 0.002, 0.07)
slap = hp(noise(d), 0.5) * env(d, 0.0005, 0.012)
save("kick", thump * 1.0 + slap * 0.6)

# lantunan bola: thump lebih ringan
d = 0.25; tt = t(d); f = 200 * np.exp(-tt * 25) + 90
save("bounce", np.sin(2 * np.pi * np.cumsum(f) / SR) * env(d, 0.002, 0.045) + hp(noise(d), 0.4) * env(d, 0.0005, 0.006) * 0.4)

# jatuh terduduk: thud
d = 0.4; tt = t(d); f = 90 * np.exp(-tt * 10) + 40
save("thud", np.sin(2 * np.pi * np.cumsum(f) / SR) * env(d, 0.003, 0.09) + lp(noise(d), 0.08) * env(d, 0.001, 0.05) * 2)

# daun berdesir (bola masuk pokok)
d = 0.9; x = hp(lp(noise(d), 0.5), 0.15)
am = 0.6 + 0.4 * np.sin(2 * np.pi * 13 * t(d)) * np.sin(2 * np.pi * 3 * t(d))
save("rustle", x * am * env(d, 0.01, 0.3))

# tiang gol "tuing": logam bergetar (separa harmonik) + vibrato
d = 1.4; tt = t(d)
vib = 1 + 0.02 * np.sin(2 * np.pi * 7 * tt) * np.exp(-tt * 2)
m = sum(a * np.sin(2 * np.pi * fr * np.cumsum(vib) / SR) * np.exp(-tt * dec) for fr, a, dec in [(520, 1, 3), (1410, .5, 5), (2730, .25, 8)])
save("tiang", m * np.minimum(tt / 0.001, 1) + hp(noise(d), 0.6) * env(d, 0.0003, 0.004) * 0.8)

# percikan lumpur/air
d = 0.7; tt = t(d)
spl = lp(noise(d), 0.35) * env(d, 0.004, 0.12)
bub = sum(np.sin(2 * np.pi * (300 + 900 * k) * (1 + 2 * tt) * tt) * np.exp(-((tt - 0.03 * k - 0.02) / 0.015) ** 2) for k in range(1, 6)) * 0.3
save("splash", spl + bub)

# guruh: hingar sangat rendah, bergulung
d = 3.5; tt = t(d)
x = lp(lp(noise(d), 0.02), 0.05)
roll = np.exp(-tt / 1.2) * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 1.3 * tt))) * np.minimum(tt / 0.02, 1)
crack = hp(noise(d), 0.3) * env(d, 0.001, 0.05) * 0.03
save("thunder", x * roll + crack, peak=0.95)

# hujan (bed 9 s): hingar tinggi + titisan rawak
d = 9.0; tt = t(d)
bed = hp(lp(noise(d), 0.45), 0.08) * 0.35
drops = np.zeros(len(tt))
for pos in rng.integers(0, len(tt) - 2000, 900):
    n = 600; drops[pos:pos + n] += hp(rng.standard_normal(n), 0.5) * np.exp(-np.arange(n) / 90) * rng.uniform(0.2, 1)
x = bed + drops * 0.5
fade = np.minimum(np.minimum(tt / 0.8, 1), np.minimum((d - tt) / 0.8, 1))
save("rain", x * fade, peak=0.7)

# wisel pengadil: dua tiupan, nada ~2.8 kHz dengan getaran bola kecil
def whistle(d):
    tt = t(d); fr = 2800 + 120 * np.sign(np.sin(2 * np.pi * 32 * tt))
    s = np.sin(2 * np.pi * np.cumsum(fr) / SR) + 0.15 * hp(noise(d), 0.6)
    return s * np.minimum(np.minimum(tt / 0.02, 1), np.minimum((d - tt) / 0.03, 1))
save("whistle", np.concatenate([whistle(0.22), np.zeros(int(SR * .08)), whistle(0.7)]), peak=0.6)

# sorakan budak: hingar jalur suara dengan modulasi suku kata, naik turun
d = 3.2; tt = t(d)
voices = np.zeros(len(tt))
for k in range(9):
    f0 = rng.uniform(280, 480); ph = rng.uniform(0, 1)
    fr = f0 * (1 + 0.25 * np.sin(2 * np.pi * rng.uniform(1.5, 3) * tt + ph))
    tone = sum(np.sin(2 * np.pi * h * np.cumsum(fr) / SR) / h for h in range(1, 5))
    syl = 0.5 + 0.5 * np.sin(2 * np.pi * rng.uniform(3, 5) * tt + ph * 6)
    voices += tone * syl
crowd = voices * 0.12 + hp(lp(noise(d), 0.4), 0.05) * 0.5
shape = np.minimum(tt / 0.15, 1) * np.exp(-np.maximum(tt - 1.6, 0) / 0.8)
save("cheer", crowd * shape, peak=0.75)
print("ok")
