# Simulasi UTS Digital Leadership

Latihan soal pilihan ganda (A–D) bergaya LMS untuk UTS mata kuliah Digital Leadership.

- `index.html`: aplikasi (timer, navigasi soal, tandai ragu-ragu, kunci jawaban per soal + pembahasan, nilai & rekap per materi, ulangi soal yang salah, riwayat percobaan).
- `questions.js`: bank soal, mode Easy dan Hard, 7 materi (03 Sep – 15 Okt).
- `tools/check-questions.js`: validasi bank soal, termasuk cek supaya jawaban benar tidak cenderung jadi opsi terpanjang. Jalankan `node tools/check-questions.js`.

Buka `index.html` di browser (file `questions.js` harus berada di folder yang sama).

## Simulasi lain

- [`ppn-ppnbm/`](ppn-ppnbm/): Simulasi UTS PPN & PPnBM (Easy/Hard, 7 materi, aturan per Oktober 2026).
