"""Daftar tautan unduh peraturan untuk re-test (open peraturan, offline). python3 build.py -> link-peraturan.html"""
import html
J = "https://jdih.kemenkeu.go.id"
# (nama, dipakai untuk, [(label, url)], catatan)
WAJIB = [
 ("UU PPN (UU 8/1983 dan perubahannya)", "hampir semua soal; pasal 1, 1A, 2, 3A, 4, 4A, 5A, 7, 8A, 9, 9A, 11–16D",
  [("Naskah gabungan (DDTC), paling praktis", "https://perpajakan.ddtc.co.id/sumber-hukum/peraturan-pusat/undang-undang-konsolidasi-ppn-setelah-uu-hpp"),
   ("UU 8/1983 asli (PDF, BPK)", "https://peraturan.bpk.go.id/Download/35808/UU%20Nomor%208%20Tahun%201983.pdf"),
   ("UU 42/2009 perubahan ketiga (PDF)", J+"/api/download/7ba0c9a6-d0dd-4d7f-a8a8-b4099b3c321c/42TAHUN2009UU.pdf"),
   ("UU 7/2021 HPP + penjelasan (PDF)", "https://peraturan.go.id/files/uu7-2021pjl.pdf"),
   ("UU 7/2021 HPP (halaman BPK)", "https://peraturan.bpk.go.id/Details/185162/uu-no-7-tahun-2021")],
  "Naskah gabungan = semua perubahan sudah digabung. Kalau DDTC minta login, pakai UU 42/2009 + UU HPP (Bab IV HPP berisi perubahan PPN)."),
 ("UU KUP", "Pasal 3 (SPT), Pasal 14 ayat (4) (sanksi faktur)",
  [("Naskah gabungan (DDTC)", "https://perpajakan.ddtc.co.id/sumber-hukum/peraturan-pusat/undang-undang-konsolidasi-kup-setelah-uu-hpp"),
   ("UU 6/1983 asli (halaman BPK)", "https://peraturan.bpk.go.id/Details/46986/uu-no-6-tahun-1983")], ""),
 ("PP 44/2022", "penyerahan, saat & tempat terutang, konsinyasi, jasa luar negeri, kurs",
  [("Halaman BPK (ada tombol download)", "https://peraturan.bpk.go.id/Details/232656/pp-no-44-tahun-2022"),
   ("Halaman JDIH Kemenkeu", J+"/dok/pp-44-tahun-2022")], ""),
 ("PP 49/2022", "fasilitas dibebaskan / tidak dipungut (beras, jasa kesehatan medis)",
  [("Unduh PDF (BPK)", "https://peraturan.bpk.go.id/Download/280043/PP%20Nomor%2049%20Tahun%202022.pdf"),
   ("Lampiran daftar barang (PDF)", "https://www.pajak.go.id/sites/default/files/Lampiran%20PP49TAHUN2022.pdf"),
   ("Halaman BPK", "https://peraturan.bpk.go.id/Details/232943/pp-no-49-tahun-2022")], ""),
 ("PMK 131/2024", "tarif 12%, DPP 11/12, barang mewah",
  [("Unduh PDF", J+"/api/download/ad276b82-94bd-4197-b409-af33e2842cd6/2024pmkeuangan131.pdf"),
   ("Halaman JDIH (link dari PPT dosen)", J+"/dok/pmk-131-tahun-2024")], ""),
 ("PMK 11/2025", "DPP nilai lain & besaran tertentu (payung)",
  [("Unduh PDF", J+"/api/download/52955502-8733-4fdd-98ce-bb03c31cda0b/2025pmkeuangan11.pdf"),
   ("Halaman JDIH (link dari PPT dosen)", J+"/dok/pmk-11-tahun-2025")], ""),
 ("PMK 53/2025", "perubahan PMK 11/2025 (KMS 2,2%, asuransi, kripto)",
  [("Unduh PDF", J+"/api/download/0a0b88a1-d37c-41b8-88b3-532c6f74250e/53%20Tahun%202025.pdf"),
   ("Halaman JDIH", J+"/dok/pmk-53-tahun-2025/summary"),
   ("Halaman BPK", "https://peraturan.bpk.go.id/Details/326338/pmk-no-53-tahun-2025")], ""),
 ("PMK 81/2024", "Coretax: tenggat, retur, BUMN, asuransi, KMS, PMSE, ekspor jasa",
  [("Unduh PDF", J+"/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf"),
   ("Halaman JDIH (link dari PPT dosen)", J+"/dok/pmk-81-tahun-2024")], "File besar (ratusan halaman). Pakai Ctrl+F: \"Pasal 294\", \"Pasal 323\", dst."),
 ("PMK 1/2026", "perubahan keempat PMK 81/2024",
  [("Unduh PDF", J+"/api/download/b5f99bff-f689-4e4f-ae3a-7c6a9a4cfe8a/2026pmkeuangan001.pdf"),
   ("Halaman JDIH", J+"/dok/pmk-1-tahun-2026")], ""),
 ("PMK 71/PMK.03/2022", "paket, biro wisata, freight forwarding, umrah + wisata, voucer",
  [("Unduh PDF", J+"/download/ac789c8c-ca29-4efc-9987-cc1d89979ba6/71_PMK.03_2022.pdf"),
   ("Halaman JDIH", J+"/dok/71-pmk-03-2022/view")], ""),
 ("PMK 48/2023", "emas perhiasan",
  [("Unduh PDF", J+"/api/download/a0aa02e4-837d-4236-baba-7095e2ace61a/2023pmkeuangan048.pdf.pdf"),
   ("Halaman JDIH", J+"/dok/pmk-48-tahun-2023/summary")], "Sudah diubah, terakhir PMK 52/2025. Besaran PPN terbaru juga ada di PMK 11/2025 Pasal 19."),
 ("PMK 231/PMK.03/2019 jo. PMK 59/PMK.03/2022", "pemungut instansi pemerintah (Pasal 16–19)",
  [("PMK 59/2022, unduh PDF", J+"/api/download/82d6ff76-02e8-460e-b603-7bfb24f8a855/59~PMK.03~2022Per.pdf"),
   ("PMK 59/2022, halaman JDIH (link dari PPT dosen)", J+"/dok/59-pmk-03-2022"),
   ("PMK 231/2019, halaman JDIH", J+"/dok/231-pmk-03-2019")], "Pasal 18 ayat (1) huruf a–h (pengecualian) ada di PMK 59/2022."),
 ("PMK 58/PMK.03/2022", "Pihak Lain dalam Sistem Informasi Pengadaan",
  [("Unduh PDF", J+"/api/download/990e3756-d744-4e15-8df2-961e62eb9d3e/58~PMK.03~2022Per.pdf"),
   ("Halaman JDIH", J+"/dok/58-pmk-03-2022")], ""),
 ("PER-11/PJ/2025", "Faktur Pajak & SPT Masa PPN (Pasal 29A, 36, 44, 48–55, Lampiran D)",
  [("Unduh PDF (pajak.go.id)", "https://www.pajak.go.id/sites/default/files/lampiran/PER-11_PJ_2025_0.pdf"),
   ("Halaman JDIH (link dari PPT dosen)", J+"/dok/per-11pj2025")], ""),
 ("PER-12/PJ/2026", "perubahan PER-11/PJ/2025 (urutan SPT, pembetulan)",
  [("Halaman pajak.go.id (ada lampiran PDF)", "https://www.pajak.go.id/index.php/en/node/120655")], ""),
 ("PER-12/PJ/2025", "PMSE: bukti pungut dipersamakan Faktur Pajak (Pasal 9–14)",
  [("Halaman pajak.go.id", "https://www.pajak.go.id/en/node/116429"),
   ("Lampiran (PDF)", "https://www.pajak.go.id/sites/default/files/lampiran/Lampiran%20PER%2012%20Tahun%202025.pdf"),
   ("Halaman dari PPT dosen", "https://stats.pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran")], ""),
]
TAMBAHAN = [
 ("PMK 32/PMK.010/2019", "daftar ekspor JKP 0%",
  [("Unduh PDF", J+"/api/download/fulltext/2019/32~PMK.010~2019Per.pdf"), ("Halaman JDIH", J+"/dok/32-pmk-010-2019")],
  "JDIH menandainya dicabut oleh PMK 81/2024 (isinya dipindah ke PMK 81/2024). Dosen masih memakainya di PPT."),
 ("PMK 92/PMK.03/2020", "jasa keagamaan (umrah/haji)",
  [("Unduh PDF", J+"/api/download/2073a4a9-acdb-4ae5-ad6b-1469c7a857a4/92~PMK.03~2020Per.pdf"), ("Halaman JDIH", J+"/dok/92-pmk-03-2020")], ""),
 ("PMK 75/PMK.03/2010", "nilai lain: pemakaian sendiri, cuma-cuma, pembubaran",
  [("Naskah (halaman web)", J+"/fulltext/2010/75~PMK.03~2010Per.HTM")], "Berupa halaman web: simpan dengan Ctrl+P → Save as PDF. Rumus terbarunya ada di PMK 11/2025 Pasal 4."),
 ("PMK 41/2023", "agunan yang dijual kreditur",
  [("Unduh PDF", J+"/api/download/7d475fef-cce0-4b81-959a-d8604ecb8e85/2023pmkeuangan041.pdf"), ("Halaman JDIH (link dari PPT dosen)", J+"/dok/pmk-41-tahun-2023")], ""),
 ("PMK 64/PMK.03/2022", "hasil pertanian tertentu",
  [("Unduh PDF", J+"/api/download/4fc869f4-0174-4aca-b095-e431b8925f93/64~PMK.03~2022Per.pdf"), ("Halaman JDIH (link dari PPT dosen)", J+"/dok/64-pmk-03-2022")], ""),
 ("PMK 62/PMK.03/2022", "LPG tertentu",
  [("Unduh PDF", J+"/api/download/97b78893-f296-4735-9712-8ef7cdb37c6c/62~PMK.03~2022Per.pdf")], ""),
 ("PMK 79/2024", "KSO",
  [("Halaman JDIH (ada tombol download)", J+"/dok/pmk-79-tahun-2024")], ""),
 ("PMK 164/2023", "batas pengusaha kecil Rp4,8 M, lapor akhir tahun buku",
  [("Halaman JDIH", J+"/dok/pmk-164-tahun-2023/summary")], "Mencabut aturan batas pengusaha kecil yang lama (PMK 68/2010 dan PMK 197/2013), jadi PMK 197/2013 tidak perlu diunduh."),
 ("PMK 50/2025", "aset kripto",
  [("Unduh PDF", J+"/api/download/66a7633b-9e1b-4a54-9046-5320aa96c7e1/2025pmkeuangan050.pdf"), ("Halaman JDIH", J+"/dok/pmk-50-tahun-2025")], ""),
 ("PER-11/PJ/2020", "pemusatan tempat PPN terutang",
  [("Halaman JDIH", J+"/dok/per-11-pj-2020"), ("Halaman pajak.go.id", "https://pajak.go.id/id/peraturan-direktur-jenderal-pajak-nomor-11pj2020")], ""),
]

def rows(items, start):
    out = []
    for i, (nama, guna, links, cat) in enumerate(items, start):
        ls = "".join(f'<li><a href="{html.escape(u)}">{html.escape(l)}</a><span class="u">{html.escape(u)}</span></li>' for l, u in links)
        c = f'<div class="c">{html.escape(cat)}</div>' if cat else ""
        out.append(f'<tr><td class="n">{i}</td><td class="cb">☐</td><td class="p"><b>{html.escape(nama)}</b><div class="g">{html.escape(guna)}</div>{c}</td><td><ul>{ls}</ul></td></tr>')
    return "".join(out)

page = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Link Unduh Peraturan PPN</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap">
<style>
@page {{ size: A4; margin: 12mm 12mm 14mm; }}
body {{ font-family: "IBM Plex Sans", Arial, sans-serif; font-size: 9.4pt; line-height: 1.4; color: #111; margin: 0; }}
h1 {{ font-size: 16pt; margin: 0 0 1mm; }} h2 {{ font-size: 11.5pt; margin: 5mm 0 1.5mm; border-bottom: 1.2pt solid #111; padding-bottom: .8mm; }}
p {{ margin: 0 0 1.6mm; }} ol {{ margin: 0 0 2mm; padding-left: 5mm; }}
table {{ width: 100%; border-collapse: collapse; }}
td {{ vertical-align: top; padding: 1.4mm 1.6mm; border-bottom: .5pt solid #C9CED3; }}
tr {{ break-inside: avoid; }}
td.n {{ width: 5mm; font-weight: 700; }} td.cb {{ width: 5mm; }} td.p {{ width: 38%; }}
.g {{ color: #444; font-size: 8.6pt; }} .c {{ font-size: 8.4pt; color: #8A2D1C; margin-top: .6mm; }}
ul {{ margin: 0; padding: 0; list-style: none; }} li {{ margin: 0 0 1.2mm; }}
a {{ color: #0B4F9C; font-weight: 600; }}
.u {{ display: block; font-size: 7pt; color: #666; word-break: break-all; }}
.box {{ border: .9pt solid #111; padding: 2.4mm 3.2mm; margin: 2mm 0; }}
</style></head><body>
<h1>Link unduh peraturan untuk re-test PPN</h1>
<p>Klik tautan biru untuk membuka atau mengunduh. Tautan yang bertanda <b>“link dari PPT dosen”</b> diambil langsung dari PPT materi 7. Tautan lainnya ditemukan lewat pencarian di situs resmi (jdih.kemenkeu.go.id, peraturan.bpk.go.id, pajak.go.id, peraturan.go.id). Pengecualiannya naskah gabungan UU dari DDTC, situs swasta yang paling praktis.</p>
<div class="box"><b>Cara menyimpan (malam ini)</b><ol>
<li>Buat folder <b>PERATURAN PPN</b> di laptop.</li>
<li>Klik "Unduh PDF". Kalau yang terbuka halaman JDIH/BPK, cari tombol <b>Download/Unduh</b> di halaman itu.</li>
<li>Ganti nama file menjadi nomor + topik, misalnya <i>PMK 71-2022 paket wisata freight.pdf</i>.</li>
<li>Matikan Wi-Fi, lalu buka setiap file sekali untuk memastikan bisa dibaca offline dan Ctrl+F berfungsi.</li>
<li>Kalau satu tautan gagal, ketik nomor peraturannya di kolom cari <b>jdih.kemenkeu.go.id</b> atau <b>peraturan.bpk.go.id</b>.</li>
</ol>Label "Dicabut/diubah" di JDIH: tetap unduh, karena dosen masih mengutipnya. Perubahannya sudah dicatat di kolom kiri.</div>
<h2>A · Wajib diunduh (dipakai di soal UTS)</h2>
<table>{rows(WAJIB, 1)}</table>
<h2>B · Tambahan (topik yang jarang muncul)</h2>
<table>{rows(TAMBAHAN, len(WAJIB)+1)}</table>
<p style="margin-top:3mm" class="g">Jangan lupa folder 7 PPT dosen dan PDF kunci jawaban UTS.</p>
</body></html>'''
open("link-peraturan.html", "w").write(page)
print("ok", len(WAJIB), len(TAMBAHAN))
