# Simulasi UTS

Latihan soal pilihan ganda (A–D) bergaya LMS. Buka `index.html` di browser lalu pilih mata kuliah.

| Folder | Mata kuliah | Isi |
| --- | --- | --- |
| `sikbb/` | Sistem Informasi dan Kecerdasan Bisnis | 3 bab (Pertemuan 5–7), 40 soal Easy + 40 soal Hard |
| `digital-leadership/` | Digital Leadership | 7 materi (03 Sep – 15 Okt), mode Easy dan Hard |

Setiap folder berisi:

- `index.html`: aplikasi (timer, navigasi soal, tandai ragu-ragu, kunci jawaban per soal + pembahasan tiap opsi, nilai & rekap per bab/materi, ulangi soal yang salah, riwayat percobaan).
- `questions.js`: bank soal. File ini harus berada di folder yang sama dengan `index.html`.

Validasi bank soal (struktur + cek supaya jawaban benar tidak cenderung jadi opsi terpanjang):

```bash
node tools/check-questions.js sikbb
node tools/check-questions.js digital-leadership
```
