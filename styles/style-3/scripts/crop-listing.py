#!/usr/bin/env python3
"""Potong screenshot listing TikTok Shop (dari telefon) → gambar produk sahaja (buang bar hitam, status bar, butang bawah).
Guna: python3 -I styles/style-3/scripts/crop-listing.py <screenshot.jpg> <keluar.jpg> [<screenshot2> <keluar2> ...]
Cara: baris yang bukan hitam pekat (max > 12) dikumpul jadi blok; blok yang tingginya paling hampir dengan lebar
skrin (gambar listing biasanya segi empat sama, lebar penuh) dipilih."""
import sys
from PIL import Image


def find(src):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    g = im.convert("L").load()
    content = [max(g[x, y] for x in range(0, w, 2)) > 12 for y in range(h)]
    runs, start, gap = [], None, 0
    for y, c in enumerate(content + [False] * 8):
        if c:
            start = y if start is None else start
            gap = 0
        elif start is not None:
            gap += 1
            if gap > 6:
                runs.append((start, y - gap + 1))
                start, gap = None, 0
    # gambar gelap ada baris hitam pekat di dalam → gabung blok berturutan selagi tinggi <= lebar
    best = None
    for i in range(len(runs)):
        a = runs[i][0]
        for j in range(i, len(runs)):
            b = runs[j][1]
            if b - a > w * 1.02:
                break
            if best is None or abs((b - a) - w) < abs((best[1] - best[0]) - w):
                best = (a, b)
    if best is None or best[1] - best[0] < 0.4 * w:
        sys.exit(f"{src}: tiada blok gambar dijumpai")
    return im, best


args = sys.argv[1:]
if not args or len(args) % 2:
    sys.exit(__doc__)
found = [(args[i], args[i + 1], *find(args[i])) for i in range(0, len(args), 2)]
# screenshot dari viewer yang sama letak gambar di tempat yang sama → guna kedudukan gambar yang tepat segi empat
exact = {im.size: a for _, _, im, (a, b) in found if abs((b - a) - im.size[0]) <= 4}
for src, dst, im, (a, b) in found:
    w, h = im.size
    if abs((b - a) - w) > 4:
        if im.size in exact:
            a = exact[im.size]
        else:  # tiada rujukan: kembangkan sama rata hingga segi empat
            a = max(0, a - (w - (b - a)) // 2)
        b = min(h, a + w)
    im.crop((0, a, w, b)).save(dst, quality=95)
    print(f"{src}: y {a}–{b} ({w}×{b - a}) -> {dst}")
