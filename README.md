# Simulasi UTS

Latihan soal pilihan ganda (A–D) bergaya LMS. Buka `index.html` di browser; file `questions.js` harus berada di folder yang sama.

## Digital Leadership (folder root)

- `index.html`: aplikasi (timer, navigasi soal, tandai ragu-ragu, kunci jawaban per soal + pembahasan, nilai & rekap per materi, ulangi soal yang salah, riwayat percobaan).
- `questions.js`: bank soal, mode Easy dan Hard, 7 materi (03 Sep – 15 Okt).

## Manajemen Keuangan Lanjutan (folder `mkl/`)

- `mkl/index.html`: aplikasi mode latihan. Jawaban langsung dicek begitu dipilih, dengan alasan tiap opsi dan pembahasan langkah demi langkah (termasuk rumus Excel). Timer 120 menit, navigasi soal, ragu-ragu, nilai & rekap per materi, ulangi soal yang salah, riwayat.
- `mkl/questions.js`: 80 soal. Easy 40 dan Hard 40, masing-masing Corporate Governance 10, Capital Budgeting 15, Cost of Capital 15. Soal dikelompokkan per materi, urutan dan opsi diacak tiap sesi.

## Validasi bank soal

`tools/check-questions.js` mengecek struktur soal, jumlah soal per materi, dan memastikan jawaban benar tidak cenderung menjadi opsi terpanjang.

```
node tools/check-questions.js        # Digital Leadership
node tools/check-questions.js mkl    # Manajemen Keuangan Lanjutan
```
