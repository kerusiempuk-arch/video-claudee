"""Transkripsi dengan masa setiap perkataan + tanda filler & ulangan.
Usage: .venv-style1/bin/python styles/style-1/tools/transcribe.py <video.mp4> [--json out.json]

- Prompt "Aaa, okay." + suppress_tokens=[] supaya Whisper TAK sorok filler.
- [FILLER]  = aaa/aa/eh/emm/hmm/okay/ok  -> masukkan dalam REMOVE
- [ULANG?]  = frasa sama disebut dua kali -> semak; kalau memang ulangan, simpan sebutan yang LENGKAP
- [PANJANG] = perkataan >0.9s, biasanya Whisper gabung ulangan -> lihat transkripsi semula tingkap
Nota: filler pendek kadang-kadang tak ditulis langsung. Semak juga bunyi pendek
(0.1–0.3s) yang terpencil antara ayat dengan tenaga audio (cut.py cetak segmen).
"""
import sys, json, subprocess, tempfile, os, wave, re
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")  # proxy hanya benarkan muat turun biasa
import numpy as np
from faster_whisper import WhisperModel
src = sys.argv[1]
tmp = tempfile.mkdtemp()
wav = os.path.join(tmp, "a.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ac", "1", "-ar", "16000", wav], check=True)
w = wave.open(wav)
a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768

m = WhisperModel("medium", device="cpu", compute_type="int8")
segs, _ = m.transcribe(a, language="ms", word_timestamps=True, suppress_tokens=[],
                       initial_prompt="Aaa, okay. Emm.", condition_on_previous_text=False)
words = [dict(w=x.word.strip(), s=round(x.start, 2), e=round(x.end, 2), p=round(x.probability, 2))
         for s in segs for x in s.words]

FILL = re.compile(r"^(a+|aa+h?|e+h|e*m+|hm+|okay|ok|okey)[.,!?]*$", re.I)
norm = lambda t: re.sub(r"[^a-z0-9]", "", t.lower())
for x in words:
    x["flag"] = "FILLER" if FILL.match(x["w"]) else ""
# ulangan: n-gram (1..6) diulang terus, atau dengan <=2 perkataan di tengah (ayat tak habis)
toks = [norm(x["w"]) for x in words]
for n in range(6, 1, -1):
    for i in range(len(toks) - n):
        for gap in range(0, 3):
            j = i + n + gap
            if toks[i:i + n] == toks[j:j + n] and all(toks[i:i + n]):
                for k in range(i, i + n):
                    words[k]["flag"] = words[k]["flag"] or f"ULANG? – sama dgn {words[j]['s']:.2f}s; kalau ulangan, simpan yg LENGKAP"
for i in range(len(toks) - 1):
    if toks[i] and toks[i] == toks[i + 1]:
        words[i]["flag"] = words[i]["flag"] or "GAGAP/ULANG"
# perkataan terlalu panjang = Whisper mungkin gabung ulangan -> transkripsi semula tingkap kecil
for x in words:
    if x["e"] - x["s"] > 0.9 and len(x["w"]) < 12:
        s0, s1 = max(0, x["s"] - 1.6), x["e"] + 0.3
        pad = np.zeros(8000, np.float32)
        seg = np.concatenate([pad, a[int(s0 * 16000):int(s1 * 16000)], pad])
        sub, _ = m.transcribe(seg, language="ms", word_timestamps=True, suppress_tokens=[],
                              initial_prompt="Aaa, okay.", condition_on_previous_text=False)
        txt = " ".join(f"{y.word.strip()}@{s0 + y.start - 0.5:.2f}" for t in sub for y in t.words)
        x["flag"] = x["flag"] or f"PANJANG {x['e'] - x['s']:.1f}s – semak: {txt}"

for x in words:
    f = f"   <-- [{x['flag']}]" if x["flag"] else ""
    low = "  (?)" if x["p"] < 0.5 else ""
    print(f"{x['s']:6.2f}-{x['e']:6.2f}  {x['w']}{low}{f}")
if "--json" in sys.argv:
    json.dump(words, open(sys.argv[sys.argv.index("--json") + 1], "w"), ensure_ascii=False, indent=1)
