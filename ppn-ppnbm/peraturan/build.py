"""Daftar ringkas 10 file peraturan untuk re-test. python3 build.py -> link-peraturan.html"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ringkas import FILES, PETA
e = html.escape
rows = "".join(
  f'<tr><td class="f">{e(n)}.pdf</td><td>{e(isi)}<div class="g">{e(cari)}</div>{f"<div class=c>{e(cat)}</div>" if cat else ""}</td>'
  f'<td><a href="{e(u)}">unduh / buka</a></td><td class="cb">☐</td></tr>' for n, isi, u, cari, cat in FILES)
peta = "".join(f"<tr><td>{e(t)}</td><td class='f'>{e(f)}</td><td>{e(p)}</td></tr>" for t, f, p in PETA)
page = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Link Unduh Peraturan PPN</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap">
<style>
@page {{ size: A4; margin: 13mm 13mm 14mm; }}
body {{ font-family: "IBM Plex Sans", Arial, sans-serif; font-size: 10pt; line-height: 1.4; color: #111; margin: 0; }}
h1 {{ font-size: 16pt; margin: 0 0 1mm; }} h2 {{ font-size: 12pt; margin: 6mm 0 2mm; border-bottom: 1.2pt solid #111; padding-bottom: .8mm; }}
p {{ margin: 0 0 2mm; }} ol {{ margin: 0; padding-left: 5mm; }}
table {{ width: 100%; border-collapse: collapse; }}
th {{ text-align: left; font-size: 8.8pt; border-bottom: 1pt solid #111; padding: 1mm 1.8mm; }}
td {{ vertical-align: top; padding: 1.6mm 1.8mm; border-bottom: .5pt solid #C9CED3; }}
tr {{ break-inside: avoid; }}
td.f {{ font-weight: 700; white-space: nowrap; }} td.cb {{ font-size: 13pt; width: 6mm; }}
.g {{ color: #444; font-size: 8.8pt; }} .c {{ font-size: 8.4pt; color: #8A2D1C; word-break: break-all; }}
a {{ color: #0B4F9C; font-weight: 700; white-space: nowrap; }}
.box {{ border: .9pt solid #111; padding: 2.4mm 3.4mm; margin: 2mm 0 0; }}
</style></head><body>
<h1>File peraturan untuk re-test PPN</h1>
<p>Cukup unduh 11 file ini (UU PPN dipecah jadi 01a dan 01b karena naskah gabungannya hanya tersedia di situs berbayar/login). Simpan dengan <b>nama persis seperti kolom kiri</b> (01, 02, …) dalam satu folder <b>PERATURAN PPN</b>, supaya urut saat ujian. Peraturan lain yang disebut di cheatsheet cukup <b>dikutip</b> sebagai dasar hukum, tidak perlu dibuka.</p>
<table><thead><tr><th>Nama file</th><th>Isi · yang dicari dengan Ctrl+F</th><th>Tautan</th><th>✓</th></tr></thead><tbody>{rows}</tbody></table>
<p class="g" style="margin-top:1.5mm"><b>Aturan UU PPN:</b> cari pasal di <b>01a</b> (perubahan terbaru) dulu. Kalau pasal itu tidak ada di 01a, artinya tidak diubah, jadi buka <b>01b</b>. Kolom "File 01" pada tabel di bawah berarti 01a/01b.</p>
<div class="box"><b>Malam ini:</b> unduh semua → ganti nama file → matikan Wi-Fi → buka tiap file sekali dan coba Ctrl+F. Kalau tautan gagal, ketik nomor peraturan di <b>jdih.kemenkeu.go.id</b>.</div>
<h2>Saat ujian: soal tentang apa → buka file mana</h2>
<table><thead><tr><th>Soal tentang</th><th>File</th><th>Cari (Ctrl+F)</th></tr></thead><tbody>{peta}</tbody></table>
</body></html>'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "link-peraturan.html"), "w").write(page)
print("ok", len(FILES))
