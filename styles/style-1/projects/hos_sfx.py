"""SFX khas video hos sahaja: ganti whoosh dengan bunyi titisan air ("bloop").
Guna selepas build.py:  python3 -I styles/style-1/projects/hos_sfx.py work/v1/hf/assets/sfx/whoosh.wav
(Style 1 asal tidak diubah.)"""
import sys, wave
import numpy as np

SR = 44100
D = 0.38                                   # sama panjang dengan whoosh asal (data-duration tak berubah)

def drop(t0, f0, f1, k):
    t = np.arange(int(SR * D)) / SR - t0
    on = t >= 0
    tt = np.where(on, t, 0)
    f = f0 * (f1 / f0) ** np.minimum(tt / 0.07, 1)      # pic naik cepat = bunyi titisan
    ph = 2 * np.pi * np.cumsum(f * on) / SR
    env = np.minimum(1, tt / 0.003) * np.exp(-tt * k) * on
    return np.sin(ph) * env

x = drop(0.0, 420, 1500, 32) + 0.35 * drop(0.11, 700, 1900, 45)   # titisan + percikan kecil
x = x / np.max(np.abs(x)) * 0.6
st = (np.stack([x, x], 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
print("->", sys.argv[1])
