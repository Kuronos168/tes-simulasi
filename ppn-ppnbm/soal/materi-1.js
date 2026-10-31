// Materi 1 · Pengantar PPN & PPnBM
// t = nomor materi, d = "e" (Easy) / "h" (Hard), c = id konsep di concepts.js
// o = [teks opsi, catatan kenapa benar/salah], a = indeks opsi benar, x = pembahasan ("§Judul", "`rumus", paragraf).
// Urutan opsi diacak saat ujian. Tambahkan soal baru di AKHIR file supaya id soal lama tetap cocok.
(window.QUESTIONS = window.QUESTIONS || []).push(

/* ============ EASY ============ */
{t:1,d:"e",c:["kredit"],
q:"Fitur yang paling membedakan PPN dari pajak penjualan (sales tax) yang dipungut hanya di satu tahap adalah…",
o:[["Tarif tunggal untuk semua barang","Sales tax juga bisa bertarif tunggal. Tarif bukan pembeda utamanya."],
["Adanya pengkreditan atas Pajak Masukan","Tepat. Kredit Pajak Masukan membuat setiap tahap hanya menyetor PPN atas nilai tambahnya."],
["Pajaknya hanya dibayar oleh konsumen","Sales tax juga pada akhirnya ditanggung konsumen. Ini bukan pembeda."],
["Tidak memerlukan faktur sama sekali","Justru PPN sangat bergantung pada Faktur Pajak (credit-invoice method)."]],
a:1,x:"§Konsep\nPPN dipungut di banyak tahap (pabrik, distributor, pengecer). Supaya tidak terjadi pajak berganda, setiap penjual boleh mengurangkan PPN yang ia bayar saat membeli (Pajak Masukan) dari PPN yang ia pungut saat menjual (Pajak Keluaran).\n`Setor = Pajak Keluaran − Pajak Masukan\nSales tax konvensional biasanya dipungut di satu titik saja (pabrik, pedagang besar, atau eceran) dan tidak mengenal kredit pajak masukan.\n§Kunci ingat\nPertanyaan “apa pembeda PPN dari sales tax” hampir selalu dijawab: KREDIT PAJAK MASUKAN. Ini jawaban kunci latihan dosen di slide Bagian 1."},

{t:1,d:"e",c:["karakteristik"],
q:"PPN disebut pajak tidak langsung karena…",
o:[["Objek dan subjek pajaknya selalu pihak yang sama persis","Kebalikannya: pihak yang menanggung dan yang menyetor justru berbeda."],
["Penanggung beban dan penyetor pajaknya bisa pihak berbeda","Tepat. Konsumen menanggung beban, PKP penjual yang memungut, menyetor, dan melapor."],
["Pajaknya dipungut dan dikelola oleh pemerintah daerah","PPN adalah pajak pusat, dipungut melalui DJP. Ini tidak terkait istilah ‘tidak langsung’."],
["Pajaknya dihitung dari besarnya penghasilan pembeli","Itu ciri PPh. PPN dihitung dari nilai transaksi, bukan penghasilan."]],
a:1,x:"§Konsep\nPajak tidak langsung = beban pajaknya bisa dialihkan ke pihak lain.\n• Pemikul beban: pembeli/konsumen akhir (membayar harga + PPN).\n• Penanggung jawab penyetoran: PKP penjual (memungut, menyetor, melapor).\n§Konsekuensi\nKalau penjual tidak memungut PPN dari pembeli, itu tanggung jawab penjual, bukan pembeli (kecuali keadaan tanggung jawab renteng).\n§Kunci ingat\nTidak langsung = “yang menanggung ≠ yang menyetor”."},

{t:1,d:"e",c:["kredit"],
q:"PT Andalas mencatat Pajak Keluaran Rp25.000.000 dan Pajak Masukan yang dapat dikreditkan Rp18.000.000 untuk satu Masa Pajak. Berapa PPN yang harus disetor?",
o:[["Rp7.000.000","Tepat. 25 juta − 18 juta = 7 juta (kurang bayar)."],
["Rp18.000.000","Ini Pajak Masukan, bukan jumlah yang disetor."],
["Rp25.000.000","Kalau menyetor seluruh PK, Pajak Masukan tidak dikreditkan sama sekali."],
["Rp43.000.000","PK dan PM tidak dijumlahkan. PM justru mengurangi PK."]],
a:0,x:"§Rumus\n`PPN kurang bayar = Pajak Keluaran − Pajak Masukan yang dapat dikreditkan\n`= Rp25.000.000 − Rp18.000.000 = Rp7.000.000\n§Istilah\n• Pajak Keluaran (PK): PPN yang dipungut dari pembeli saat kita menjual.\n• Pajak Masukan (PM): PPN yang kita bayar ke supplier saat membeli.\nKalau PK > PM → kurang bayar (setor). Kalau PM > PK → lebih bayar (kompensasi ke masa berikutnya atau restitusi)."},

{t:1,d:"e",c:["karakteristik"],
q:"Tuan A berpenghasilan Rp10 juta per bulan dan Tuan B Rp100 juta per bulan. Keduanya membeli televisi yang sama di toko yang sama dan membayar PPN dengan jumlah yang sama. Karakteristik PPN yang paling tepat menggambarkan keadaan ini adalah…",
o:[["Pajak subjektif","Pajak subjektif justru memperhatikan keadaan pribadi wajib pajak (misalnya PPh). PPN tidak."],
["Pajak objektif","Tepat. PPN melihat objek/transaksinya, bukan kondisi atau penghasilan pembelinya."],
["Pajak langsung","PPN adalah pajak tidak langsung."],
["Pajak progresif","Progresif berarti tarif naik bila dasar naik. PPN bertarif sama untuk siapa pun."]],
a:1,x:"§Konsep\nPajak objektif menempatkan OBJEK (barang/jasa yang dikonsumsi) sebagai faktor dominan timbulnya pajak. Siapa pembelinya, kaya atau miskin, tidak relevan.\n§Akibatnya\n• PPN tidak memperhatikan asas keadilan berdasarkan kemampuan bayar.\n• PPN bersifat regresif: bagi Tuan A, PPN yang sama memakan porsi penghasilan yang lebih besar dibanding Tuan B.\n§Kunci ingat\nObjektif = “lihat barangnya”. Subjektif = “lihat orangnya” (contoh PPh dengan PTKP)."},

{t:1,d:"e",c:["karakteristik"],
q:"PPN menganut prinsip tujuan (destination principle). Akibat yang paling tepat dari prinsip ini adalah…",
o:[["Ekspor tidak membawa beban PPN, impor dikenai PPN","Tepat. Pajak dikenakan di tempat barang dikonsumsi: impor dipajaki, ekspor tidak membawa beban PPN Indonesia."],
["Ekspor dikenai PPN penuh dan impor dibebaskan","Kebalikannya. Ini prinsip asal (origin), bukan tujuan."],
["PPN dipungut di tempat barang diproduksi","Itu prinsip asal (origin principle)."],
["PPN hanya dikenakan atas barang buatan dalam negeri","Barang impor yang dikonsumsi di Indonesia juga dikenai PPN."]],
a:0,x:"§Konsep\nDestination principle: pajak konsumsi dikenakan di NEGARA TUJUAN, tempat barang/jasa dikonsumsi.\n• Konsumsi di Indonesia (termasuk barang impor dan jasa dari luar negeri yang dimanfaatkan di Indonesia) → kena PPN Indonesia.\n• Barang/jasa yang dikonsumsi di luar negeri (ekspor) → tarif 0%, sehingga PPN Indonesia tidak ikut ‘diekspor’.\n§Tujuannya\nPerlakuan netral antara barang dalam negeri dan barang impor yang sama-sama dikonsumsi di Indonesia."},

{t:1,d:"e",c:["sejarah"],
q:"Undang-undang yang pertama kali membentuk kerangka PPN dan PPnBM di Indonesia adalah…",
o:[["UU Nomor 42 Tahun 2009","UU 42/2009 adalah perubahan ketiga, bukan UU pertama."],
["UU Nomor 8 Tahun 1983","Tepat. UU 8/1983 adalah UU PPN induk; semua UU sesudahnya mengubahnya."],
["UU Nomor 7 Tahun 2021","UU 7/2021 adalah UU HPP yang mengubah UU PPN, bukan UU pertama."],
["UU Nomor 11 Tahun 1994","UU 11/1994 adalah perubahan pertama."]],
a:1,x:"§Urutan sejarah UU PPN\n`UU 8/1983  (induk) → UU 11/1994 (perubahan 1) → UU 18/2000 (perubahan 2) → UU 42/2009 (perubahan 3)\n`→ UU 11/2020 Cipta Kerja → UU 7/2021 HPP → Perppu 2/2022 → UU 6/2023\n§Status 2026\nRujukan resminya ditulis: UU 8/1983 sebagaimana terakhir diubah dengan UU 6/2023. Jadi UU 8/1983 tetap menjadi ‘induk’, sedangkan UU lain adalah perubahannya.\n§Kunci ingat\n“8/83” = delapan tiga, yang pertama."},

{t:1,d:"e",c:["ppnbm"],
q:"Pernyataan yang benar tentang PPnBM adalah…",
o:[["PPnBM dipungut di setiap tahap penyerahan, sama seperti PPN","PPnBM bukan multi-tahap. Ia dipungut satu kali saja."],
["PPnBM dipungut satu kali dan tidak dapat dikreditkan","Tepat. Dipungut di pabrikan atau saat impor, dan PPnBM yang dibayar tidak bisa dikreditkan."],
["PPnBM dapat dikreditkan seperti Pajak Masukan PPN","PPnBM bukan Pajak Masukan, sehingga tidak bisa dikreditkan."],
["PPnBM dikenakan pada semua barang yang harganya di atas Rp1 miliar","‘Mewah’ adalah kategori hukum menurut klasifikasi, bukan sekadar harga mahal."]],
a:1,x:"§PPN vs PPnBM\n`PPN  : banyak tahap, PM dapat dikreditkan, tarif 12% (0% ekspor)\n`PPnBM: SATU tahap (pabrikan atau impor), TIDAK dapat dikreditkan, tarif 10%–200%\n§Siapa yang memungut PPnBM\nHanya pengusaha yang MENGHASILKAN barang mewah (pabrikan) saat menyerahkannya, atau saat barang mewah DIIMPOR. Distributor dan pengecer tidak memungut PPnBM lagi, tetapi tetap memungut PPN.\n§Mahal belum tentu mewah\nKlasifikasi barang mewah ditetapkan peraturan (PMK). Mulai dari jenis barang dan aturannya, bukan dari harganya."},

/* ============ HARD ============ */
{t:1,d:"h",c:["kredit"],
q:"Dengan tarif ilustrasi 10%, sebuah barang melewati rantai: bahan dijual Rp100, pabrik menjual Rp180, distributor menjual Rp250, dan peritel menjual ke konsumen Rp300. Semua Pajak Masukan memenuhi syarat kredit. Berapa setoran PPN di tahap DISTRIBUTOR dan berapa total penerimaan negara dari seluruh rantai?",
o:[["Distributor Rp7; total Rp30","Tepat. Distributor: PK 25 − PM 18 = 7. Total 10 + 8 + 7 + 5 = 30 = 10% × 300."],
["Distributor Rp25; total Rp83","Rp25 adalah PK distributor tanpa dikurangi PM. Menjumlahkan semua PK menghasilkan pajak berganda (kumulatif)."],
["Distributor Rp7; total Rp73","Total yang benar dihitung dari setoran tiap tahap (10 + 8 + 7 + 5), bukan PK ditambah sebagian setoran."],
["Distributor Rp5; total Rp30","Rp5 adalah setoran peritel (30 − 25), bukan distributor."]],
a:0,x:"§Langkah\nHitung PK tiap tahap = 10% × harga jual. PM = PK tahap sebelumnya.\n`Bahan      : PK 10%×100 = 10; PM 0  → setor 10\n`Pabrik     : PK 10%×180 = 18; PM 10 → setor 8\n`Distributor: PK 10%×250 = 25; PM 18 → setor 7\n`Peritel    : PK 10%×300 = 30; PM 25 → setor 5\n`Total = 10 + 8 + 7 + 5 = 30\n§Makna\nTotal setoran (30) sama dengan 10% × harga ke konsumen (300). Ini bukti PPN tidak kumulatif walau dipungut di banyak tahap.\nKalau tidak ada kredit (seperti sales tax berantai), negara memungut 10 + 18 + 25 + 30 = 83, artinya pajak ditumpuk (cascading).\n§Catatan\nTarif 10% di sini hanya ilustrasi mekanisme dari slide dosen, bukan tarif transaksi 2026."},

{t:1,d:"h",c:["ppnbm","hitung"],
q:"PT Lux mengimpor BKP yang menurut PMK tergolong barang mewah. DPP Rp800.000.000, tarif PPN 12%, tarif PPnBM diasumsikan 20%. Barang lalu dijual ke peritel. Berapa total PPN dan PPnBM saat impor, dan bagaimana perlakuan PPnBM pada tahap peritel?",
o:[["Rp256.000.000; peritel tidak memungut ulang PPnBM dan tidak mengkreditkannya","Tepat. PPN 96 jt + PPnBM 160 jt = 256 jt. PPnBM hanya sekali (saat impor) dan tidak bisa dikreditkan."],
["Rp256.000.000; peritel memungut lagi PPnBM 20% atas harga jualnya","PPnBM tidak dipungut ulang di tahap distributor/peritel."],
["Rp275.200.000; peritel tidak memungut ulang PPnBM","Rp275,2 jt muncul bila PPnBM dihitung dari (DPP + PPN). Salah: PPN dan PPnBM dihitung terpisah dari DPP yang sama."],
["Rp256.000.000; peritel boleh mengkreditkan PPnBM sebagai Pajak Masukan","PPnBM tidak dapat dikreditkan, baik terhadap PPN maupun PPnBM."]],
a:0,x:"§Langkah hitung\n`PPN   = 12% × Rp800.000.000 = Rp96.000.000\n`PPnBM = 20% × Rp800.000.000 = Rp160.000.000\n`Total pajak impor = Rp256.000.000\nBarang mewah memakai DPP penuh (bukan 11/12), jadi PPN-nya benar-benar 12%.\n§Tahap berikutnya\n• Peritel tetap memungut PPN atas penjualannya.\n• Peritel TIDAK memungut PPnBM lagi (PPnBM satu tahap).\n• PPnBM yang sudah dibayar importir tidak bisa dikreditkan; secara ekonomi ikut masuk harga/biaya.\n§Jebakan\nPPnBM tidak dihitung dari harga + PPN. Keduanya dikalikan dari DPP yang sama.\nTarif PPnBM 20% hanya asumsi soal. Dalam praktik, cek dulu kelompok barang dan tarifnya di PMK."},

{t:1,d:"h",c:["hierarki"],
q:"Pasangkan pertanyaan berikut dengan lapis aturan yang paling tepat: (a) norma tarif PPN, (b) penerapan umum PPN dan PPnBM, (c) penetapan DPP nilai lain, (d) format dan teknis pelaporan Faktur Pajak.",
o:[["(a) PP, (b) UU, (c) PER, (d) PMK","Lapisnya tertukar. Tarif adalah norma pokok sehingga ada di UU."],
["(a) UU, (b) PP, (c) PMK, (d) PER","Tepat. Norma pokok di UU, penerapan umum di PP, detail kebijakan di PMK, teknis administrasi di PER."],
["(a) UU, (b) PMK, (c) PP, (d) PER","Penerapan umum diatur PP (PP 44/2022), sedangkan DPP nilai lain diatur PMK (PMK 11/2025)."],
["(a) UU, (b) PP, (c) PER, (d) PMK","DPP nilai lain ada di PMK; teknis format faktur ada di PER (PER-11/PJ/2025)."]],
a:1,x:"§Empat lapis aturan pajak\n`UU  → norma pokok: objek, subjek, tarif, hak, kewajiban (UU PPN)\n`PP  → penerapan umum (PP 44/2022 Penerapan PPN & PPnBM)\n`PMK → detail kebijakan: DPP, nilai lain, fasilitas (PMK 131/2024, PMK 11/2025)\n`PER → teknis administrasi & pelaporan DJP (PER-11/PJ/2025)\n§Prinsip\nAturan lebih rendah harus punya dasar delegasi dan tidak boleh mengubah norma aturan di atasnya.\n§Kunci ingat\nU-P-P-P: Undang-undang → Pemerintah (PP) → Pak Menteri (PMK) → Pak Dirjen (PER)."},

{t:1,d:"h",c:["sejarah","hierarki"],
q:"Sebuah transaksi terjadi pada November 2021. Seorang staf menganalisisnya cukup dengan membaca teks UU 42/2009. Penilaian yang paling tepat atas langkah staf tersebut adalah…",
o:[["Sudah tepat, karena UU 42/2009 adalah perubahan UU PPN terakhir sebelum 2022 sehingga cukup dibaca sendiri","Tidak tepat. UU 11/2020 (Cipta Kerja) dan UU 7/2021 (HPP) juga mengubah UU PPN dan harus dicek tanggal berlakunya."],
["Kurang tepat; baca UU 8/1983 dengan semua perubahan yang sudah berlaku per tanggal transaksi, lalu aturan pelaksananya","Tepat. Tanggal transaksi menentukan versi hukum yang berlaku; perubahan yang sudah efektif harus digabungkan."],
["Kurang tepat; harus memakai UU 6/2023 karena itulah UU PPN terbaru yang selalu menggantikan versi lama","UU 6/2023 belum ada pada November 2021. Aturan dipilih berdasarkan tanggal transaksi, bukan aturan paling baru."],
["Kurang tepat; cukup membaca PMK terbaru karena PMK adalah aturan yang paling teknis dan paling rinci","PMK tidak bisa berdiri sendiri tanpa UU induk; dan PMK terbaru belum tentu berlaku pada tanggal transaksi."]],
a:1,x:"§Langkah penelusuran hukum (dari slide dosen)\n1) Identifikasi tanggal dan jenis transaksi.\n2) Buka UU PPN induk (UU 8/1983) beserta perubahan yang SUDAH BERLAKU pada tanggal itu.\n3) Telusuri PP, PMK, PER yang didelegasikan dan masih aktif.\n4) Periksa ketentuan peralihan, pencabutan, dan tanggal efektif.\n§Kenapa UU 42/2009 saja tidak cukup\nSebelum November 2021 sudah ada UU 11/2020 (Cipta Kerja) yang mengubah ketentuan PPN, dan UU 7/2021 (HPP) diundangkan Oktober 2021 dengan tanggal berlaku bertahap. Semua harus diuji tanggal berlakunya.\n§Kunci ingat\nAturan dibaca “per tanggal transaksi”, bukan “aturan terbaru”."},

{t:1,d:"h",c:["kredit","karakteristik"],
q:"Sebuah negara memungut pajak 10% di setiap tahap penjualan (pabrik → pedagang besar → pengecer) TANPA mekanisme kredit pajak masukan. Masalah utama yang muncul dibanding PPN adalah…",
o:[["Pajak hanya dipungut sekali sehingga penerimaan negara jauh lebih kecil","Justru pajak dipungut berkali-kali, bukan sekali."],
["Cascading: pajak tahap sebelumnya masuk harga lalu dipajaki lagi","Tepat. Tanpa kredit, pajak menumpuk (kumulatif) sehingga beban akhir lebih besar dari tarif × harga konsumen."],
["Konsumen akhir sama sekali tidak menanggung beban pajaknya","Konsumen tetap menanggung, bahkan menanggung beban yang lebih besar karena pajak bertumpuk."],
["Pajak berubah sifat dari tidak langsung menjadi pajak langsung","Pajak penjualan berantai tetap pajak tidak langsung. Masalahnya ada pada penumpukan pajak."]],
a:1,x:"§Konsep cascading (kumulatif)\nTanpa kredit pajak masukan, pajak yang dibayar di tahap 1 menjadi bagian harga tahap 2, lalu dikenai pajak lagi. Pajak dikenai pajak.\n§Ilustrasi dari materi (kolom kiri slide ‘Non Cumulative’)\nTanpa kredit: pajak 100.000 + 140.000 + 170.000 menumpuk dan harga akhir naik. Dengan kredit (PPN): 100.000 + 30.000 + 20.000 = 150.000 = tarif × harga akhir.\n§Kunci\nPPN = multi-stage levy tetapi NON-cumulative, karena ada kredit Pajak Masukan."}

);
