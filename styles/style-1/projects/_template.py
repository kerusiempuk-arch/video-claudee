# <Nama produk> (Drive <ID>) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    # (mula, tamat),  # "aaa" / "okay" / ulangan pertama / ayat tak habis
]
SRC_END = 99.0        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 0.0             # tempoh selepas potongan (build.py --plan)
CAPTION_Y = 680       # atas, paras dada (pilihan user); kena muka -> 700–760 (duduk: 760); muka rendah dalam frame -> 900
CARD_Y = 1420       # kad hook rendah supaya produk tak tertutup
ZOOM = 0.04
# CAPTION_ACCENT = (255, 212, 59, 255)   # paksa warna; default auto: baju/latar biru → kuning
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# SFX_WHOOSH = "drop"  # ganti whoosh dengan titisan air (produk air / dapur / mesin basuh)
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)]) — 1–3 perkataan; [] = tiada kapsyen
    # (1.36, [("Zaman", 0.00, False), ("sekarang", 0.64, False)]),
]
HOOK = dict(end=3.0, y=100,  # end = hujung ayat pembuka (boleh ~8s supaya 2 pilihan sempat disebut); select_at = bila setiap pilihan DISEBUT
            kicker="<produk> paling", title="<katakunci>",
            options=[("<pilihan A>", "01"), ("<pilihan B>", "02")], select_at=[1.0, 2.0])  # boleh 3 pilihan ("03")
SECTIONS = [  # (mula, tamat, "kelebihan" atau "tip", "1 / 3", subtajuk)
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut) — x 50/80/110, y 250/320/390; senarai 3 benda -> y 260/340/420, sudut 2/-1.5/1.5 bertindan
]
CIRCLES = []  # (mula, tamat, cx, cy, r, label, label_x, label_y)
COVERS = [  # cover photo (tools/cover.py) – at = masa video ASAL; 2 pilihan (produk+muka, hasil)
    # dict(at=4.2, kicker="<produk>,", title="<katakunci>", stickers=["<kelebihan 1>", "<kelebihan 2> ✓"], pill="kelebihan 1-3 · <subtajuk>"),  # label pil ikut SECTIONS ("kelebihan" / "tip")
]
BIG_WORDS = []  # (mula, tamat, perkataan, titik_merah) – perkataan besar sekejap di tengah video, cth. (11.1, 12.4, "berbuih", True)
CTA = dict(title="<katakunci>",  # utamakan perkataan yang disebut di hujung (cth. "murah"), kalau tiada ulang tajuk hook
           title_at=0.0, title_y=230, card_at=0.0, card_y=1180,
           card_label="<Produk>", name="<Produk>", tags="a · b · c",  # maks 3 tag pendek (1–2 perkataan)
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
