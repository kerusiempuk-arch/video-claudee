"""Style 1 – kaburkan plate nombor kenderaan dalam video mentah (ikut gerakan kamera), SEBELUM build.py.

Guna (dari root repo, venv .venv-style1 ada opencv):
  .venv-style1/bin/python -I styles/style-1/tools/blur_plate.py <raw.mp4> <out.mp4> --ref 9.5 --box 500,1312,265,68 \
        [--anchor 34.5:384,1406,320,76 ...] [--window 4.6] [--check <check.jpg>]

  --ref T --box x,y,w,h   frame (saat, video ASAL) di mana plate jelas + kotak HURUF plate (piksel penuh 1080×1920).
                          Jadi templat: setiap frame dicari (multi-skala); padanan ≥ 0.8 = kedudukan terus.
  --anchor T:x,y,w,h      kedudukan manual tambahan untuk plate separuh di tepi frame (templat tak jumpa).
  --window S              frame tanpa padanan ikut gerakan kamera (phase correlation) dari anchor terdekat
                          dalam S saat (default 4.6). Lebih jauh → tak dikaburkan.
  --check out.jpg         helaian semakan (setiap 0.5 s, kotak merah) – LIHAT, terutama bila plate masuk/keluar frame.

Kotak kabur = huruf ×1.7 lebar, ×3.0 tinggi (turun sikit), pixelate + blur, tepi lembut. Audio disalin.
Lepas itu guna <out.mp4> sebagai RAW untuk build.py dan cover.py. Rujukan: projects/bar_ratchet.py.
"""
import argparse, json, subprocess
import cv2, numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("raw"); ap.add_argument("out")
ap.add_argument("--ref", type=float, required=True)
ap.add_argument("--box", required=True)
ap.add_argument("--anchor", action="append", default=[])
ap.add_argument("--window", type=float, default=4.6)
ap.add_argument("--min-score", type=float, default=0.8)
ap.add_argument("--check")
a = ap.parse_args()

probe = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                   "stream=r_frame_rate", "-of", "json", a.raw], capture_output=True, text=True).stdout)
n_, d_ = probe["streams"][0]["r_frame_rate"].split("/")
FPS = float(n_) / float(d_)
# saiz selepas auto-rotate ffmpeg
f0 = subprocess.run(["ffmpeg", "-v", "error", "-i", a.raw, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                    capture_output=True).stdout
H, W = cv2.imdecode(np.frombuffer(f0, np.uint8), cv2.IMREAD_COLOR).shape[:2]


def frames():
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.raw, "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            return
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)


# 1) imbasan separuh resolusi
small = np.array([cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), (W // 2, H // 2)) for f in frames()])
N = len(small)
bx, by, bw, bh = [int(v) // 2 for v in a.box.split(",")]
T = small[int(round(a.ref * FPS))][by:by + bh, bx:bx + bw]
anchors = {}
for i, g in enumerate(small):
    best = (-1, None)
    for sc in (0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.35):
        t = cv2.resize(T, None, fx=sc, fy=sc)
        _, m, _, loc = cv2.minMaxLoc(cv2.matchTemplate(g, t, cv2.TM_CCOEFF_NORMED))
        if m > best[0]:
            best = (m, (loc[0] + t.shape[1] / 2, loc[1] + t.shape[0] / 2, t.shape[1], t.shape[0]))
    if best[0] >= a.min_score:
        anchors[i] = best[1]
for s in a.anchor:
    t, box = s.split(":")
    x, y, w, h = [float(v) / 2 for v in box.split(",")]
    anchors[int(round(float(t) * FPS))] = (x + w / 2, y + h / 2, w, h)
print(f"# {len(anchors)}/{N} frame ada plate (templat/anchor)")

# 2) gerakan kamera (bahagian bawah frame)
lo = small[:, H // 4:].astype(np.float32)
win = cv2.createHanningWindow((lo.shape[2], lo.shape[1]), cv2.CV_32F)
shift = [(0.0, 0.0)] + [cv2.phaseCorrelate(lo[i - 1], lo[i], win)[0] for i in range(1, N)]
C = np.cumsum(np.array(shift), 0)
ak = np.array(sorted(anchors)) if anchors else np.array([], int)
pos = [None] * N
for i in range(N):
    if not len(ak):
        break
    j = ak[np.argmin(abs(ak - i))]
    if abs(j - i) > a.window * FPS:
        continue
    cx, cy, w, h = anchors[j]
    d = C[i] - C[j]
    pos[i] = (cx + d[0], cy + d[1], w, h)


def rect(pp, s=1):
    cx, cy, w, h = [v * s for v in pp]
    bw_, bh_ = w * 1.7, h * 3.0
    cy += 0.2 * h
    return int(cx - bw_ / 2), int(cy - bh_ / 2), int(cx + bw_ / 2), int(cy + bh_ / 2)


if a.check:
    tiles = []
    for i in range(0, N, int(FPS / 2)):
        g = cv2.cvtColor(small[i], cv2.COLOR_GRAY2BGR)
        if pos[i]:
            x0, y0, x1, y1 = rect(pos[i])
            cv2.rectangle(g, (x0, y0), (x1, y1), (0, 0, 255), 3)
        cv2.putText(g, f"{i / FPS:.1f}", (10, 40), 0, 1.2, (0, 255, 255), 3)
        tiles.append(cv2.resize(g, (180, int(180 * H / W))))
    while len(tiles) % 12:
        tiles.append(np.zeros_like(tiles[0]))
    cv2.imwrite(a.check, np.vstack([np.hstack(tiles[k:k + 12]) for k in range(0, len(tiles), 12)]))
    print("-> semak", a.check)

# 3) kabur + encode
q = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", f"{FPS}",
                      "-i", "-", "-i", a.raw, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "14", "-preset", "medium",
                      "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", a.out], stdin=subprocess.PIPE)
for i, f in enumerate(frames()):
    f = f.copy()
    if i < N and pos[i]:
        x0, y0, x1, y1 = rect(pos[i], 2)
        x0, y0, x1, y1 = max(0, x0), max(0, y0), min(W, x1), min(H, y1)
        if x1 - x0 > 20 and y1 - y0 > 20:
            r = f[y0:y1, x0:x1]
            sm = cv2.resize(r, (max(1, (x1 - x0) // 28), max(1, (y1 - y0) // 28)), interpolation=cv2.INTER_AREA)
            pix = cv2.GaussianBlur(cv2.resize(sm, (x1 - x0, y1 - y0)), (0, 0), 12)
            m = np.zeros((y1 - y0, x1 - x0), np.float32)
            m[10:-10, 10:-10] = 1
            m = cv2.GaussianBlur(m, (0, 0), 5)[..., None]
            f[y0:y1, x0:x1] = (pix * m + r * (1 - m)).astype(np.uint8)
    q.stdin.write(f.tobytes())
q.stdin.close()
q.wait()
print("->", a.out)
