// Reads a case folder (the same Markdown the Python exporter reads) and builds an in-memory index.
// Used at config time (sidebar), by the remark plugin (link map) and by pages (relations).
import fs from 'node:fs';
import path from 'node:path';
import YAML from 'yaml';

// Project sites on GitHub Pages live under /<repo>/, so every internal URL goes through withBase().
const BASE = (process.env.HUB_BASE || '/').replace(/\/+$/, '');
export const withBase = (p) => BASE + p;
export const CASE = path.resolve(process.env.HUB_CASE_DIR || path.resolve(process.cwd(), '../workspace/demo-case'));
export const HUB = path.join(CASE, 'hub');
const read = (p) => fs.readFileSync(p, 'utf8');
const exists = (p) => fs.existsSync(p);

export const TYPES = [
  { letter: 'O', folder: 'opportunities', one: 'Opportunity', en: 'Opportunity', many: 'Opportunities' },
  { letter: 'H', folder: 'hypotheses', one: 'Hypothesis', en: 'Hypothesis', many: 'Hypotheses' },
  { letter: 'M', folder: 'metrics', one: 'Metric', en: 'Metric', many: 'Metrics' },
  { letter: 'D', folder: 'decisions', one: 'Decision', en: 'Decision', many: 'Decisions' },
  { letter: 'T', folder: 'tests', one: 'Test', en: 'Test', many: 'Tests' },
];
export const STAGES = ['Setup', 'Discover', 'Define', 'Develop', 'Deliver'];
export const ART_TYPES = {
  'competitor-analysis': 'Phân tích đối thủ', persona: 'Persona', 'survey-results': 'Kết quả khảo sát',
  'interview-synthesis': 'Tổng hợp phỏng vấn', 'user-flow': 'User flow', 'ia-sitemap': 'Information architecture',
  prototype: 'Prototype', 'test-plan': 'Kế hoạch test', 'test-report': 'Báo cáo test',
  requirements: 'Yêu cầu (PRD)', 'solution-pool': 'Solution pool', generic: 'Tài liệu',
};
export const ART_STATUS = { verified: 'Đã kiểm tra', draft: 'Bản nháp', simulated: 'Mô phỏng', planned: 'Kế hoạch' };
const PRIVATE = ['_raw-private', '_personal', '/.git/', '_templates'];
export const isPrivate = (p) => PRIVATE.some((x) => p.replace(/\\/g, '/').includes(x)) || path.basename(p) === 'AGENTS.md';

export function front(md) {
  const m = md.match(/^---\s*\n([\s\S]*?)\n---\s*\n?/);
  if (!m) return { data: {}, body: md };
  let data = {};
  try { data = YAML.parse(m[1]) || {}; } catch { data = {}; }
  return { data, body: md.slice(m[0].length) };
}
export const wikiId = (s) => String(s ?? '').replace(/\[\[(?:[^\]|]+\|)?([^\]]+)\]\]/g, '$1').trim();
export const refs = (v) => (Array.isArray(v) ? v : v ? [v] : []).map(wikiId).filter(Boolean);
const natkey = (s) => s.replace(/\d+/g, (n) => n.padStart(6, '0'));
const natSort = (a, b) => natkey(a).localeCompare(natkey(b));
const h1 = (body) => (body.match(/^#\s+(.+)$/m) || [])[1]?.trim();

let cache;
export function scan() {
  if (cache) return cache;
  const items = [];
  // Items are files named by their ID (O1.md, H1.md, D1.md...) directly in hub/; the first letter is the type.
  for (const f of exists(HUB) ? fs.readdirSync(HUB).sort(natSort) : []) {
    const m = f.match(/^([OHMDT])\d+\.md$/);
    const t = m && TYPES.find((x) => x.letter === m[1]);
    if (!t) continue;
    const abs = path.join(HUB, f);
    const { data, body } = front(read(abs));
    const id = f.replace(/\.md$/, '');
    items.push({ id, letter: t.letter, type: t, abs, meta: data, body, title: String(data.title || h1(body) || id) });
  }
  const artifacts = [];
  const adir = path.join(HUB, 'artifacts');
  if (exists(adir)) {
    for (const f of fs.readdirSync(adir).sort(natSort)) {
      if (f.startsWith('_') || f.startsWith('.') || f.toLowerCase() === 'readme.md') continue;
      const full = path.join(adir, f);
      let md = null, folder = null, id = f;
      if (fs.statSync(full).isFile() && f.endsWith('.md')) { md = full; id = f.replace(/\.md$/, ''); }
      else if (fs.statSync(full).isDirectory()) {
        for (const c of ['index.md', 'README.md', `${f}.md`]) if (exists(path.join(full, c))) { md = path.join(full, c); folder = full; break; }
      }
      if (!md) continue;
      const { data, body } = front(read(md));
      const links = (Array.isArray(data.links) ? data.links : data.links ? [data.links] : []).map(String);
      artifacts.push({
        id, abs: md, folder, body, meta: data,
        title: String(data.title || h1(body) || id), type: String(data.type || 'generic').toLowerCase(),
        stage: String(data.stage || ''), status: String(data.status || '').toLowerCase(), summary: String(data.summary || ''),
        takeaways: (Array.isArray(data.takeaways) ? data.takeaways : data.takeaways ? [data.takeaways] : []).map(String).filter(Boolean),
        supports: refs(data.supports), source: data.source ? String(data.source) : '',
        media: (Array.isArray(data.media) ? data.media : data.media ? [data.media] : []).map(String),
        links, embed: String(data.embed) === 'true', embedUrl: data.embed_url ? String(data.embed_url) : '',
      });
    }
  }
  const pages = [];
  const addPage = (abs, id, kind, label) => {
    if (!exists(abs)) return;
    const { data, body } = front(read(abs));
    pages.push({ id, abs, kind, title: String(data.title || h1(body) || label || id), label: label || h1(body) || id });
  };
  addPage(path.join(HUB, 'README.md'), 'overview-source', 'overview');
  for (const f of fs.readdirSync(HUB).sort(natSort)) {
    if (/^\d\d-.*\.md$/.test(f)) addPage(path.join(HUB, f), f.replace(/\.md$/, ''), 'week');
  }
  addPage(path.join(HUB, 'gates.md'), 'gates', 'ref', 'Gates');
  addPage(path.join(CASE, 'learnings', 'context-principle-checks.md'), 'principles', 'ref', 'Principle checks');
  addPage(path.join(CASE, 'case-log.md'), 'case-log', 'ref', 'Case log');

  const overviewMd = exists(path.join(HUB, 'README.md')) ? read(path.join(HUB, 'README.md')) : '';
  const caseName = ((overviewMd.match(/^\|\s*Tên case\s*\|\s*(.+?)\s*\|\s*$/m) || [])[1] || path.basename(CASE)).replace(/[*`]/g, '');
  const agreement = ((overviewMd.match(/^\|\s*Agreement status\s*\|\s*(.+?)\s*\|\s*$/m) || [])[1] || '').replace(/\*.*?\*|[*`]/g, '').trim();
  const gates = parseGates(pages.find((p) => p.id === 'gates'));
  const principles = parsePrinciples(pages.find((p) => p.id === 'principles'));

  // route map: absolute path -> route, so links between Markdown files keep working
  const routes = new Map();
  for (const i of items) routes.set(path.resolve(i.abs), withBase(`/items/${i.id}/`));
  for (const a of artifacts) {
    routes.set(path.resolve(a.abs), withBase(`/docs/${a.id}/`));
    if (a.source) routes.set(path.resolve(path.dirname(a.abs), a.source), withBase(`/docs/${a.id}/`));
  }
  for (const p of pages) routes.set(path.resolve(p.abs), p.id === 'overview-source' ? withBase('/') : withBase(`/pages/${p.id}/`));

  cache = { items, artifacts, pages, caseName, agreement, gates, principles, routes };
  return cache;
}

function parseGates(page) {
  if (!page) return [];
  const out = []; let cur = null;
  for (const line of read(page.abs).split('\n')) {
    const h = line.match(/^##\s+Gate\s+\d+:\s*(.+)/);
    if (h) { cur = { name: h[1].trim(), checks: [] }; out.push(cur); continue; }
    if (cur && line.trim().startsWith('|')) {
      const c = line.trim().replace(/^\||\|$/g, '').split('|').map((x) => x.trim());
      if (c.length >= 3 && /^\d[a-z]$/.test(c[0])) cur.checks.push({ id: c[0], text: c[1], status: c[2].toLowerCase() });
    }
  }
  for (const g of out) {
    const st = g.checks.map((c) => c.status);
    g.passed = st.filter((s) => s === 'passed').length; g.total = st.length;
    g.status = st.includes('failed') ? 'failed' : st.length && st.every((s) => s === 'passed') ? 'passed' : 'open';
  }
  return out;
}
function parsePrinciples(page) {
  const out = {};
  if (!page) return out;
  for (const line of read(page.abs).split('\n')) {
    if (!line.trim().startsWith('|')) continue;
    const c = line.trim().replace(/^\||\|$/g, '').split('|').map((x) => x.trim());
    if (c.length >= 3 && /^P\d+$/.test(c[0])) out[c[0]] = { name: c[1], check: c[2] };
  }
  return out;
}

/** URL of a file that scripts/prepare-assets.mjs copied into public/hub-assets */
export function assetUrl(abs) {
  return withBase('/hub-assets/') + path.relative(CASE, abs).split(path.sep).map(encodeURIComponent).join('/');
}
export function mediaKind(p) {
  const e = path.extname(p).toLowerCase();
  if (['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'].includes(e)) return 'image';
  if (['.mp4', '.webm', '.mov'].includes(e)) return 'video';
  if (e === '.pdf') return 'pdf';
  if (['.html', '.htm'].includes(e)) return 'html';
  if (e === '.md') return 'doc';
  return 'file';
}
export function mediaOf(a) {
  const seen = new Set(); const out = [];
  for (const m of a.media) {
    const abs = path.resolve(path.dirname(a.abs), m);
    if (exists(abs) && !isPrivate(abs) && !seen.has(abs)) { seen.add(abs); out.push({ kind: mediaKind(abs), abs, name: path.basename(abs) }); }
  }
  if (a.folder) {
    for (const f of fs.readdirSync(a.folder).sort(natSort)) {
      const abs = path.join(a.folder, f);
      if (fs.statSync(abs).isFile() && abs !== a.abs && !f.startsWith('.') && !seen.has(abs) && !isPrivate(abs)) {
        seen.add(abs); out.push({ kind: mediaKind(abs), abs, name: f });
      }
    }
  }
  const order = { image: 0, html: 1, video: 2, pdf: 3, doc: 5, file: 6 };
  return out.sort((x, y) => (order[x.kind] ?? 9) - (order[y.kind] ?? 9));
}
