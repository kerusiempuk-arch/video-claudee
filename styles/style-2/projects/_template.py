# <Nama produk> (Drive <ID>) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-2/projects/boxer.py
# Bina: python3 -I styles/style-2/build.py <raw.mp4> <fail ini> <work_dir>   (--plan / --cut-audio <wav>)

# --- potongan (build.py), masa ikut video ASAL. Senyap > 0.3 s dipotong automatik.
REMOVE = [
    # (mula, tamat),  # "aaa" / "emm" / "okay" / ulangan pertama / gagap / ayat tak habis
]
SRC_END = 99.0        # potong selepas ni (orang keluar frame / kamera jatuh). Biar ~0.6 s selepas perkataan terakhir
                      # supaya CTA kekal >= 2 s di skrin (TAIL sahaja tak panjangkan END) – semak hyperframes check (line_unread)
TAIL = 0.7            # hujung tak dipotong senyap — masa baca CTA
# PUNCH = 1.07        # punch-in pada segmen selang-seli (origin atas, kepala tak terpotong)
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

# --- overlay (build.py), masa ikut video SELEPAS dipotong (transkripsi cut.wav dari --cut-audio)
END = 0.0             # dari --plan
CAPTION_Y = 600       # dada, bawah dagu (ubah ikut kedudukan muka; boxer guna 545)
# CARD_TOP = 1360     # jalur kad di bawah (atas kaki); jangan tutup muka/produk

CAPTIONS = [  # (tamat_kumpulan, [(perkataan, mula, gaya)]) — gaya "" / "box" (kotak putih) / "serif" (serif italik). Max ~4 perkataan
    # (1.64, [("Zaman", 0.03, ""), ("sekarang", 0.26, "")]),
]
HOOK = dict(start=0.15, end=3.0, text="review **<produk>**", x=350, y=760)
CARDS = [
    # dict(kind="vs", start=, end=, kicker="ZAMAN SEKARANG", old="<lama>", new="<produk>", new_at=<bila nama produk disebut>),
    #      old/new pendek (1–2 perkataan, cth "Nipis" → "Tebal") supaya tak jadi dua baris
    # dict(kind="icon", start=, end=, kicker="01 · <KELEBIHAN>", title="Lebih *<kata>*", icon="heart"),  # heart wind star shield bolt tag
    # dict(kind="check", start=, end=, kicker="02 · ...", title="...", items=[("<teks>", <bila ✓>), ...]),
    # dict(kind="chips", start=, end=, kicker="03 · PILIHAN", title="Pelbagai saiz & warna",
    #      chips=[...], chips_at=, colors=["#hex", ...], colors_at=),   # JANGAN reka saiz/warna – sahkan dengan user
]
RAIL = dict(start=0, end=0, steps=[])   # steps=[(bila, "Label"), ...] — label langkah sebelah kepala
CTA = dict(start=0, button_at=0,   # button_at dihadkan auto ke END - 2.2 s
           button="Tekan *beg kuning*", items=["...", "..."])
# EXTRA_SFX = [(masa, "pop"|"whoosh-short"|"click"|"sparkle"|"ping", volume), ...]
