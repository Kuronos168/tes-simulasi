"""Bangun kunci-jawaban.html dari data.py. Jalankan: python3 build.py"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import SOAL

assert len(SOAL) == 40 and [s["n"] for s in SOAL] == list(range(1, 41))

def grid():
    cells = "".join(
        f'<div class="g"><span class="gn">{s["n"]}</span><span class="ga">{s["a"]}</span></div>' for s in SOAL)
    return f'<div class="grid">{cells}</div>'

def item(s):
    calc = "".join(f"<li>{c}</li>" for c in s["calc"])
    x = f'<p class="x"><span class="lbl">Pengecoh</span>{s["x"]}</p>' if s.get("x") else ""
    return f'''
<section class="soal">
  <div class="hd"><span class="no">Soal {s["n"]}</span><span class="ans">{s["a"]}</span><span class="val">{s["v"]}</span></div>
  <div class="tp">{s["topik"]}</div>
  <p><span class="lbl">Penjelasan</span>{s["jel"]}</p>
  <div class="calc"><span class="lbl">Perhitungan</span><ul>{calc}</ul></div>
  <p class="dh"><span class="lbl">Dasar hukum</span>{s["dh"]}</p>
  {x}
</section>'''

dist = {k: sum(1 for s in SOAL if s["a"] == k) for k in "ABCD"}

page = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<title>Kunci Jawaban UTS PPN &amp; PPnBM</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<style>
@page {{ size: A4; margin: 14mm 15mm 15mm; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; background: #fff; color: #000; }}
body {{ font-family: "IBM Plex Sans", Arial, sans-serif; font-size: 9.6pt; line-height: 1.42; }}
h1 {{ font-size: 18pt; margin: 0 0 1mm; }}
.sub {{ font-size: 9.5pt; color: #333; margin: 0 0 5mm; }}
h2 {{ font-size: 11.5pt; margin: 6mm 0 2mm; border-bottom: 1pt solid #000; padding-bottom: 1mm; }}
.grid {{ display: grid; grid-template-columns: repeat(10, 1fr); border-top: 0.6pt solid #000; border-left: 0.6pt solid #000; margin-bottom: 2mm; }}
.g {{ display: flex; justify-content: space-between; align-items: baseline; padding: 1.6mm 2.2mm; border-right: 0.6pt solid #000; border-bottom: 0.6pt solid #000; }}
.gn {{ font-size: 8.5pt; color: #444; }}
.ga {{ font-size: 13pt; font-weight: 700; }}
.note {{ font-size: 8.8pt; color: #333; margin: 0 0 1.5mm; }}
.tpl {{ border: 0.8pt solid #000; padding: 3mm 4mm; margin: 2mm 0 0; }}
.tpl ol {{ margin: 1mm 0 2mm; padding-left: 5mm; }}
.tpl li {{ margin-bottom: 0.8mm; }}
.tpl .eg {{ border-top: 0.5pt dashed #666; padding-top: 2mm; font-size: 9.2pt; }}
.soal {{ break-inside: avoid; border-top: 0.8pt solid #000; padding: 2.6mm 0 3mm; }}
.hd {{ display: flex; align-items: baseline; gap: 3mm; }}
.no {{ font-weight: 700; font-size: 11pt; }}
.ans {{ font-weight: 700; font-size: 11pt; border: 1pt solid #000; padding: 0 2mm; }}
.val {{ font-weight: 600; }}
.tp {{ font-size: 8.6pt; color: #444; margin: 0.6mm 0 1.6mm; text-transform: uppercase; letter-spacing: 0.04em; }}
p {{ margin: 0 0 1.4mm; }}
.lbl {{ display: inline-block; min-width: 23mm; font-weight: 700; font-size: 8.6pt; }}
.calc {{ display: flex; margin: 0 0 1.4mm; }}
.calc ul {{ margin: 0; padding: 0; list-style: none; }}
.calc li {{ margin: 0 0 0.4mm; font-variant-numeric: tabular-nums; }}
.dh {{ }}
.x {{ font-size: 8.8pt; color: #333; }}
b {{ font-weight: 700; }}
</style></head><body>

<h1>Kunci Jawaban UTS PPN &amp; PPnBM</h1>
<p class="sub">40 soal pilihan ganda dari scan soal UTS (halaman 2–11). Aturan per Oktober 2026 mengikuti PPT dosen: tarif 12%, DPP nonmewah 11/12, besaran tertentu PMK 11/2025 s.t.d.d. PMK 53/2025.</p>

<h2>Ringkasan jawaban</h2>
{grid()}
<p class="note">Sebaran jawaban: A {dist["A"]} · B {dist["B"]} · C {dist["C"]} · D {dist["D"]}. Singkatan: PK = Pajak Keluaran, PM = Pajak Masukan, FP = Faktur Pajak, DPP = Dasar Pengenaan Pajak, jt = juta.</p>

<h2>Format menulis jawaban di kertas (re-test)</h2>
<div class="tpl">
  <p>Ketentuan re-test: setiap jawaban <b>wajib</b> disertai penjelasan, perhitungan, dan dasar hukum. Tulis empat baris ini untuk setiap soal (± 3 menit per soal):</p>
  <ol>
    <li><b>Jawaban</b>: huruf dan angka/pernyataan.</li>
    <li><b>Dasar hukum</b>: pasal + peraturan (mis. UU PPN Pasal 16D; PMK 131/2024 Pasal 3).</li>
    <li><b>Penjelasan</b>: 1–2 kalimat: aturan apa yang dipakai dan mengapa fakta soal memenuhinya.</li>
    <li><b>Perhitungan</b>: rumus → angka → hasil. Untuk soal teori tulis "tidak ada perhitungan".</li>
  </ol>
  <div class="eg"><b>Contoh (Soal 1):</b> Jawaban B, Rp64.350.000. Dasar hukum: UU PPN Pasal 1 angka 18, Pasal 7 ayat (1) huruf b; PMK 131/2024 Pasal 3. Penjelasan: Harga Jual mencakup ongkos kirim yang ditagih penjual, dikurangi potongan yang dicantumkan di FP; barang nonmewah sehingga DPP 11/12. Perhitungan: HJ = 600 − 30 + 15 = 585 jt; DPP = 11/12 × 585 jt = 536,25 jt; PPN = 12% × 536,25 jt = Rp64.350.000.</div>
</div>

<h2>Pembahasan per soal</h2>
{"".join(item(s) for s in SOAL)}
</body></html>'''

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kunci-jawaban.html")
open(out, "w").write(page)
print("ok", out, dist)
