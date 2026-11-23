"""Langkah 1: potong senyap + bahagian berulang/gagap, tambah punch-in pada setiap jump cut.
Usage: python3 cut.py <raw.mp4> <cut.mp4> <project.py>

Config project (pilihan):
  REMOVE = [(start, end), ...]   # bahagian sumber yang dibuang (ulangan, gagap, salah cakap)
  SRC_END = 21.3                 # buang semua selepas masa ni
  SILENCE_DB = -38               # bawah paras ni dikira senyap
  MIN_SILENCE = 0.30             # senyap lebih panjang dari ni dipotong
  PAD = 0.06                     # ruang nafas yang ditinggal di tepi setiap potongan
  PUNCH = 1.08                   # zoom untuk segmen selang-seli (1.0 = tiada)
"""
import subprocess, sys, runpy, wave, array, math, os, tempfile

RAW, OUT, PROJ = sys.argv[1], sys.argv[2], sys.argv[3]
C = runpy.run_path(PROJ)
REMOVE = C.get("REMOVE", [])
SILENCE_DB = C.get("SILENCE_DB", -38)
MIN_SIL = C.get("MIN_SILENCE", 0.30)
PAD = C.get("PAD", 0.06)
PUNCH = C.get("PUNCH", 1.08)
TAIL = C.get("TAIL", 0.0)       # saat hujung yang tak dipotong senyap (masa untuk baca CTA)
PUNCH_Y = C.get("PUNCH_Y", 0.35)  # 0 = zoom ke atas, 0.5 = tengah (muka biasanya di atas)

def duration(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())

src_end = C.get("SRC_END", duration(RAW))

# --- tenaga audio setiap 20ms
tmp = tempfile.mkdtemp()
wav = os.path.join(tmp, "a.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", RAW, "-ac", "1", "-ar", "16000", wav], check=True)
w = wave.open(wav)
pcm = array.array("h", w.readframes(w.getnframes()))
HOP = 320
db = []
for i in range(0, len(pcm), HOP):
    blk = pcm[i:i + HOP]
    rms = math.sqrt(sum(v * v for v in blk) / max(1, len(blk))) / 32768
    db.append(20 * math.log10(rms + 1e-9))
# smooth (median of 5) supaya bunyi konsonan pendek tak pecahkan segmen
sm = [sorted(db[max(0, i - 2):i + 3])[len(db[max(0, i - 2):i + 3]) // 2] for i in range(len(db))]
step = HOP / 16000

# --- cari senyap panjang
silences, start = [], None
for i, v in enumerate(sm + [0]):
    t = i * step
    if v < SILENCE_DB and start is None:
        start = t
    elif v >= SILENCE_DB and start is not None:
        if t - start >= MIN_SIL:
            silences.append((start + PAD, t - PAD))
        start = None

silences = [(a, min(b, src_end - TAIL)) for a, b in silences if a < src_end - TAIL]
cuts = sorted([(a, b) for a, b in silences if b > a] + list(REMOVE) + [(src_end, 1e9)])
# --- gabung & terbalikkan jadi KEEP
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

# segmen yang bersambung rapat (senyap pendek) dikira satu "shot" untuk punch-in
total = sum(b - a for a, b in keep)
print(f"# {len(keep)} segmen, {total:.2f}s (asal {src_end:.2f}s)")
for a, b in keep:
    print(f"   keep {a:6.2f} - {b:6.2f}")

# --- render: setiap segmen trim, segmen selang-seli punch-in, audio fade 15ms supaya tiada klik
probe = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                 "stream=width,height:stream_side_data=rotation", "-of", "default=nw=1", RAW]).decode()
info = dict(l.split("=") for l in probe.split() if "=" in l)
w0, h0 = int(info["width"]), int(info["height"])
if abs(int(float(info.get("rotation", 0)))) == 90:
    w0, h0 = h0, w0
parts, labels = [], []
for i, (a, b) in enumerate(keep):
    z = PUNCH if i % 2 == 1 else 1.0
    zw, zh = int(w0 * z) // 2 * 2, int(h0 * z) // 2 * 2
    v = (f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,scale={zw}:{zh},"
         f"crop={w0}:{h0}:(iw-{w0})/2:(ih-{h0})*{PUNCH_Y},setsar=1[v{i}]")
    d = b - a
    au = (f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,"
          f"afade=t=out:st={max(0, d - 0.015):.3f}:d=0.015[a{i}]")
    parts += [v, au]
    labels.append(f"[v{i}][a{i}]")
fc = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(keep)}:v=1:a=1[v][a]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", RAW, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "14", "-r", "30", "-c:a", "aac", "-b:a", "256k", OUT],
               check=True)
print("->", OUT, f"{duration(OUT):.2f}s")
