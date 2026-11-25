# Kasut kanvas (Drive 1vVldCKRS0CmhCzJnDXRWEHKJFB5QPPqA)
# Bina: python3 -I styles/style-2/build.py <raw.mp4> <fail ini> <work_dir>   (--plan / --cut-audio <wav>)
REMOVE = [
    (17.05, 20.35),   # "Okey, aa pakai buat pergi jalan-jalan" (ulangan pertama)
    (23.95, 27.50),   # "Okey, berminat dengan aa kasut" (ulangan pertama)
]
SRC_END = 30.6
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 20.94
CAPTION_Y = 655
CARD_TOP = 1500   # turun sikit supaya kad tak tutup kasut

CAPTIONS = [
    (1.32, [("Kasut", 0.02, ""), ("yang", 0.51, ""), ("ringan", 0.80, "box")]),        # "yarin kas" – SAHKAN "yang ringan"
    (3.00, [("dan", 1.32, ""), ("senang", 1.76, ""), ("dipakai.", 2.25, "serif")]),
    (4.49, [("Ini", 3.00, ""), ("dia", 3.41, ""), ("ada", 3.69, ""), ("warna", 3.90, "")]),
    (5.13, [("hitam,", 4.49, "box")]),
    (6.00, [("ada", 5.13, ""), ("warna", 5.33, ""), ("biru.", 5.73, "box")]),
    (8.00, [("Saiz", 6.00, ""), ("ada", 6.44, ""), ("pelbagai.", 6.80, "serif")]),
    (9.03, [("Dia", 8.00, ""), ("punya", 8.40, ""), ("design", 8.69, "box")]),
    (10.00, [("sangat", 9.03, ""), ("menarik.", 9.46, "serif")]),
    (11.00, [("Paling", 10.00, ""), ("penting,", 10.40, "")]),
    (12.31, [("tapak", 11.00, ""), ("dia", 11.41, ""), ("anti-slip.", 11.69, "box")]),
    (13.00, [("Bahagian", 12.31, ""), ("dalam,", 12.76, "")]),
    (14.00, [("dia", 13.00, ""), ("ada", 13.40, ""), ("span.", 13.46, "box")]),
    (15.21, [("Pakai", 14.00, ""), ("untuk", 14.44, ""), ("pergi", 14.76, "")]),
    (16.18, [("jalan-jalan,", 15.21, "serif")]),
    (17.00, [("naik", 16.18, ""), ("motor,", 16.73, "box")]),
    (18.00, [("sangat", 17.00, ""), ("sesuai.", 17.41, "serif")]),
    (19.31, [("Berminat", 18.00, ""), ("dengan", 18.69, ""), ("kasut", 18.97, "box")]),
    (20.15, [("ini,", 19.31, ""), ("dapatkan", 19.50, ""), ("di", 20.02, "")]),
    (20.94, [("beg kuning", 20.15, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **kasut ringan**", x=350, y=860)

CARDS = [
    dict(kind="check", start=3.00, end=8.00, kicker="PILIHAN", title="Warna & *saiz*",
         items=[("Warna hitam", 4.49), ("Warna biru", 5.73), ("Saiz pelbagai", 6.80)]),   # biru – SAHKAN
    dict(kind="icon", start=8.00, end=10.00, kicker="01 · DESIGN", title="Sangat *menarik*", icon="star"),
    dict(kind="icon", start=10.00, end=12.31, kicker="02 · TAPAK", title="Tapak *anti-slip*", icon="shield"),
    dict(kind="icon", start=12.31, end=14.00, kicker="03 · BAHAGIAN DALAM", title="Ada *span*", icon="heart"),
    dict(kind="check", start=14.00, end=18.00, kicker="04 · SESUAI", title="Sesuai *dipakai*",
         items=[("Jalan-jalan", 15.21), ("Naik motor", 16.73)]),
]
RAIL = dict(start=8.00, end=18.00, steps=[(8.00, "Design"), (10.00, "Anti-slip"), (12.31, "Span"), (14.00, "Sesuai")])
CTA = dict(start=18.00, button_at=19.50, button="Tekan *beg kuning*",
           items=["Ringan & senang dipakai", "Tapak anti-slip", "Ada span di dalam", "Warna hitam & biru"])
