// Validasi bank soal: struktur + bias panjang jawaban.
// Jalankan: node tools/check-questions.js
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const src = fs.readFileSync(path.join(__dirname, "..", "questions.js"), "utf8");
const ctx = { window: {} };
vm.runInNewContext(src, ctx);
const Q = ctx.window.QUESTIONS;

let errors = 0, longest = 0, shortest = 0, ratioSum = 0;
const flagged = [];
const counts = {};
Q.forEach((q, i) => {
  const tag = `#${i} (t${q.t}${q.d})`;
  const bad = (m) => { errors++; console.log("ERROR", tag, m); };
  if (![1, 2, 3, 4, 5, 6, 7].includes(q.t)) bad("t tidak valid");
  if (!["e", "h"].includes(q.d)) bad("d tidak valid");
  if (!q.q || !q.x) bad("q/x kosong");
  if (!Array.isArray(q.o) || q.o.length !== 4) bad("opsi harus 4");
  else q.o.forEach((o, j) => { if (!o[0] || !o[1]) bad(`opsi ${j} tanpa teks/catatan`); });
  if (!(q.a >= 0 && q.a <= 3)) bad("a tidak valid");
  const texts = q.o.map((o) => o[0]);
  if (new Set(texts).size !== 4) bad("opsi duplikat");
  const len = texts.map((t) => t.length);
  const c = len[q.a];
  const others = len.filter((_, j) => j !== q.a);
  const avg = others.reduce((s, v) => s + v, 0) / others.length;
  if (c > Math.max(...others)) longest++;
  if (c < Math.min(...others)) shortest++;
  ratioSum += c / avg;
  if (c > Math.max(...others) * 1.12 && c - Math.max(...others) > 4) flagged.push(`${tag} benar=${c} max lain=${Math.max(...others)} :: ${q.q.slice(0, 60)}`);
  const k = `${q.d}${q.t}`; counts[k] = (counts[k] || 0) + 1;
});

const n = Q.length;
console.log(`Total soal: ${n}`);
console.log("Per mode/materi:", JSON.stringify(counts));
console.log(`Jawaban benar = opsi TERPANJANG : ${longest}/${n} (${(100 * longest / n).toFixed(1)}%)  [acak murni ≈ 25%]`);
console.log(`Jawaban benar = opsi TERPENDEK  : ${shortest}/${n} (${(100 * shortest / n).toFixed(1)}%)`);
console.log(`Rata-rata rasio panjang benar / rata-rata pengecoh: ${(ratioSum / n).toFixed(3)}`);
if (flagged.length) { console.log("\nJawaban benar jauh lebih panjang dari semua pengecoh:"); flagged.forEach((f) => console.log("  " + f)); }
if (errors || longest / n > 0.3 || flagged.length) process.exitCode = 1;
