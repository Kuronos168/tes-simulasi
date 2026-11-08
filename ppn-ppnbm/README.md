# Simulasi UTS PPN & PPnBM

Latihan soal pilihan ganda (A–D) bergaya LMS untuk UTS Pajak Pertambahan Nilai dan Pajak Penjualan atas Barang Mewah. Isi soal mengikuti materi dan latihan dosen (aturan per Oktober 2026: tarif 12%, DPP nilai lain 11/12, PMK 11/2025 jo. PMK 53/2025, PMK 81/2024, PER-11/PJ/2025).

- `index.html`: aplikasi (timer, navigasi soal, tandai ragu-ragu, kunci jawaban per soal + pembahasan langkah demi langkah, ringkasan konsep, salin soal untuk AI lain, nilai & rekap per materi, ulangi soal yang salah, riwayat percobaan).
- `soal/materi-1.js` … `materi-7.js`: bank soal per materi, mode Easy dan Hard. Tambahkan soal baru di akhir file materinya supaya id soal lama tetap cocok.
- `concepts.js`: kartu konsep dasar yang tampil di bawah pembahasan dan di halaman Ringkasan konsep.
- `tools/check-questions.js`: validasi bank soal (struktur, id konsep, bias panjang jawaban, format angka). Jalankan `node ppn-ppnbm/tools/check-questions.js`.
- `tools/longest.js`: bantu penulis soal melihat soal yang jawaban benarnya paling panjang.

Buka `index.html` di browser (folder `soal/` dan `concepts.js` harus ikut).

Materi: 1 Pengantar PPN & PPnBM · 2 Pengusaha Kena Pajak · 3 Objek PPN & penyerahan · 4 Saat & tempat terutang, KSO, pemusatan · 5 Faktur Pajak · 6 DPP, tarif & DPP nilai lain · 7 Besaran tertentu, KMS, aktiva Pasal 16D, objek spesifik & pemungut.

## Cheatsheet

- `cheatsheet/Cheatsheet-Retest-PPN-PPnBM.pdf`: edisi re-test (9 Nov 2026, open PPT & peraturan). 8 halaman A4: format jawaban 4 baris, peta soal UTS, checklist peraturan untuk disimpan offline, lalu tabel kata kunci → aturan → dasar hukum per topik. Sumber: `cheatsheet/cheatsheet-retest.html`.

- `cheatsheet/Cheatsheet-UTS-PPN-PPnBM.pdf`: 8 halaman A4 (4 lembar bolak-balik), satu bab per halaman, huruf ±9,5 pt. Isinya sudah dicocokkan dengan ke-126 soal simulasi. Sumber: `cheatsheet/cheatsheet.html`.
- `cheatsheet/Cheatsheet-UTS-PPN-PPnBM-ringkas-2hal.pdf`: versi ringkas 2 halaman (1 lembar), huruf ±7 pt. Sumber: `cheatsheet/cheatsheet-2hal.html`.
- Setelah mengedit HTML, buat ulang PDF dengan Chrome/Chromium (Print → Save as PDF, ukuran A4, margin None, background graphics aktif).

## Kunci jawaban UTS

- `kunci-uts/Kunci-Jawaban-UTS-PPN-PPnBM.pdf`: kunci 40 soal UTS: teks soal lengkap (diketik ulang dari scan, `kunci-uts/soal.py`) diikuti jawaban, yang berisi penjelasan, perhitungan, dasar hukum, dan alasan opsi lain salah. Isi ada di `kunci-uts/data.py`; bangun ulang dengan `python3 kunci-uts/build.py`, lalu cetak HTML-nya ke PDF.
