# Simulasi UTS Statistika Bisnis

Latihan soal pilihan ganda (A–D) bergaya LMS untuk UTS Statistika Bisnis (format UTS: 25 soal, 150 menit, kalkulator sains + tabel statistik).

- `index.html`: aplikasi (timer, navigasi soal, tandai ragu-ragu, kunci jawaban per soal + pembahasan langkah hitung, salin soal untuk AI lain, nilai & rekap per materi, ulangi soal yang salah, riwayat percobaan).
- `questions.js`: bank soal Easy (40) dan Hard (41), 7 materi sesuai Quiz 1–7 Lentera. Tiap soal punya pembahasan langkah demi langkah, rumus Excel (format Indonesia), dan ketikan kalkulator.
- `concepts.js`: konsep dasar (binomial, Poisson, normal, interval kepercayaan, dll.) yang tampil di bawah pembahasan dan di halaman Ringkasan konsep, plus glosarium Indonesia–Inggris. Aplikasi menambahkan istilah Inggris dalam kurung pada kemunculan pertama tiap istilah.
- `tools/check-questions.js`: validasi bank soal, termasuk cek supaya jawaban benar tidak cenderung jadi opsi terpanjang dan format angkanya (jumlah desimal) tidak beda sendiri. Jalankan `node statistika-bisnis/tools/check-questions.js`.

Buka `index.html` di browser (file `questions.js` harus berada di folder yang sama).
