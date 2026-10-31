// Bantu penulis soal: tampilkan soal yang jawaban benarnya paling panjang. node ppn-ppnbm/tools/longest.js [materi]
const fs = require("fs"), path = require("path"), vm = require("vm");
const ctx = { window: {} }, only = process.argv[2];
for (let i = 1; i <= 7; i++) { const f = path.join(__dirname, "..", "soal", `materi-${i}.js`); if (fs.existsSync(f)) vm.runInNewContext(fs.readFileSync(f, "utf8"), ctx); }
ctx.window.QUESTIONS.forEach((q, i) => {
  if (only && String(q.t) !== only) return;
  const len = q.o.map((o) => o[0].length), c = len[q.a], others = len.filter((_, j) => j !== q.a);
  if (c > Math.max(...others)) console.log(`#${i} t${q.t}${q.d} benar=${c} lain=${others.join("/")} :: ${q.o[q.a][0]}`);
});
