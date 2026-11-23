# Panduan Gaya Video (rujukan: video "editing with Claude")

Dikaji dari video rujukan (Google Drive `1dwMtteYsa9ZirF828ME6Gvdj2ESqN9Xc`).

## Spesifikasi teknikal
- Menegak **9:16**, 576×1024 (eksport kita: 1080×1920), **30 fps**, ~2 min 17 s
- Audio AAC stereo 44.1 kHz, ~-20 LUFS keseluruhan; tiada senyap panjang (ada bed bunyi/muzik perlahan di bawah suara)

## Struktur (4 shot sahaja — satu take panjang talking head)
| Masa | Bahagian | Apa berlaku |
|---|---|---|
| 0:00–0:08 | **Hook** | Wajah jelas, tajam, tiada blur. Pil kecil "✳ editing with **Claude**" di atas kepala. |
| 0:08–1:49 | **Badan / tutorial** | Latar (footage sendiri) di-**blur kuat + digelapkan**; kad UI animasi di tengah skrin menerangkan setiap langkah. |
| 1:49–1:57 | **Contoh / payoff** | Blur hilang, footage tajam semula; demo teks besar "THE HOOK" dengan kotak pemilih (gaya editor). |
| 1:57–2:13 | **Rumusan + CTA** | Blur semula dengan tint biru tua, senarai semak semua langkah (✓), kotak komen "EDITOR", butang "Following". |
| 2:13–2:17 | **Outro** | Skrin gelap, logo TikTok + bar carian @username. |

## Elemen visual tetap
1. **Caption satu baris di atas** (~y 13% skrin), putih, sans-serif sederhana tebal (Inter/SF style), saiz sederhana.
   - Ditaip **perkataan demi perkataan**: perkataan seterusnya kelihatan pudar/lut sinar sebelum disebut (karaoke reveal).
   - **Kata kunci** (Claude, HyperFrames, FFmpeg, yt-dlp, reference, prompt, music, footage) dalam **kotak sorotan** — kotak putih + teks hitam, atau kotak kelabu + teks **serif italik**.
2. **Garis progress menegak** di kiri (x ~4%): garis biru yang memanjang ke bawah, dengan bulatan nod; label pil biru kecil di sebelahnya menamakan langkah semasa ("Desktop app", "One folder", "Local chat", "Five tools", "One prompt", "Your style", "The key line", "Stand out", "Film & drop", "Claude edits", "Feedback"). Muncul hanya semasa bahagian tutorial.
3. **Kad UI putih** (bucu bulat ~16px, bayang lembut, lebar ~78% skrin) di tengah: tetingkap app, folder biru, toggle Cloud/Local, carta orbit "5 tools" dengan ikon berkembang satu-satu, senarai semak, editor prompt bernombor baris, timeline/footage bertindan 3D, polaroid link.
   - Tajuk: sans-serif hitam tebal; aksen **serif italik** (cth "→ *finished reel*"); label kecil huruf monospace biru.
   - Warna aksen: **biru #2F6BFF**, oren Claude **#D97757**, putih, hitam.
4. **Latar ketika kad muncul**: footage sendiri, Gaussian blur besar + gelap ~30–40% supaya kad menonjol.
5. **Watermark TikTok + @username** (tak perlu ditiru — TikTok tambah sendiri).

## Gerakan & rentak
- Tiada jump cut kerap: rentak datang dari **animasi kad yang berubah setiap 2–4 saat** mengikut ayat.
- Kad masuk dengan **scale/fade + sedikit naik**, elemen dalam kad muncul berperingkat (stagger), bar progress mengisi (cth 3% → 94%).
- Peralihan bahagian: blur masuk/keluar lembut (~0.3–0.5 s), bukan potongan keras.
- Payoff: footage tajam semula + teks besar dengan "selection box" seolah-olah sedang diedit.

## Peraturan wajib (arahan pemilik)
- **Sentiasa potong** bahagian senyap (jeda > ~0.3 s dipendekkan ke ~0.1 s), **perkataan/ayat berulang** (kekalkan sebutan yang terakhir/terbaik) dan **gagap** sebelum menambah grafik.
- Silih setiap jump cut dengan punch-in kecil (scale ~1.07, origin di atas supaya kepala tak terpotong).
- Masukkan **sound effect** pada setiap aksi visual: whoosh (kad masuk/tukar), pop (pil/chip/ikon muncul), click (tanda ✓), sparkle (pendedahan produk), ping (butang CTA). Volume ~0.3–0.4, di bawah suara.
- Hantar gambar frame draf dulu sebelum render.

## Resipi untuk edit video baru (HyperFrames)
1. Transkrip footage → timestamp perkataan (`hyperframes transcribe`, perlu whisper-cpp).
2. Caption karaoke satu baris di atas + kotak sorotan untuk kata kunci.
3. Bahagikan skrip kepada hook / langkah-langkah / payoff / CTA.
4. Hook: footage tajam + pil "editing with ___".
5. Setiap langkah: blur latar, garis progress kiri + label langkah, satu kad UI yang menggambarkan langkah itu.
6. Payoff tajam, rumusan senarai semak, outro.
