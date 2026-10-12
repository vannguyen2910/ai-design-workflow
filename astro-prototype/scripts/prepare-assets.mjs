// Copies the media that the hub links to into public/hub-assets (never raw data, personal notes or Markdown).
import fs from 'node:fs';
import path from 'node:path';
import { CASE, isPrivate } from '../src/lib/hubindex.mjs';

const OUT = path.resolve('public/hub-assets');
fs.rmSync(OUT, { recursive: true, force: true });
const roots = ['hub/artifacts', 'learnings'];
const ok = /\.(png|jpe?g|gif|webp|svg|html?|pdf|mp4|webm|mov|csv)$/i;
let n = 0;
const walk = (dir) => {
  if (!fs.existsSync(dir)) return;
  for (const f of fs.readdirSync(dir)) {
    const abs = path.join(dir, f);
    if (isPrivate(abs) || f.startsWith('.')) continue;
    if (fs.statSync(abs).isDirectory()) { walk(abs); continue; }
    if (!ok.test(f)) continue;
    const dest = path.join(OUT, path.relative(CASE, abs));
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(abs, dest); n++;
  }
};
roots.forEach((r) => walk(path.join(CASE, r)));
console.log(`prepare-assets: ${n} files -> public/hub-assets`);
