"""Cetak aras bunyi (dBFS) setiap 30 ms untuk cari titik potong tepat.
Guna: python3 -I energy.py <a16k.wav> <dari_s> <hingga_s>"""
import sys, wave, struct, math
w = wave.open(sys.argv[1]); sr = w.getframerate(); n = w.getnframes()
d = struct.unpack('<%dh' % n, w.readframes(n))
lo, hi = float(sys.argv[2]), float(sys.argv[3])
def rms(a, b):
    s = d[int(a * sr):int(b * sr)] or [0]
    return 20 * math.log10(max(1, math.sqrt(sum(x * x for x in s) / len(s))) / 32768)
t = lo
out = []
while t < hi:
    out.append(f"{t:.2f}:{rms(t, t + 0.03):.0f}"); t += 0.03
print(" ".join(out))
