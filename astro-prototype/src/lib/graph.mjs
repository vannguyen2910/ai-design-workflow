// Same rules as tools/export-hub.py: relations are stored one way, the other direction is derived.
import { scan, refs, ART_STATUS } from './hubindex.mjs';

const MSG = {
  noNeed: 'Decision này chưa nối được về nhu cầu nào của người dùng',
  strain: (p) => `Decision này đi ngược nguyên tắc ${p}: cân nhắc sửa, hoặc ghi lại vì sao chấp nhận`,
  unserved: 'Nhu cầu này chưa có design decision nào phục vụ',
  untested: 'Hypothesis này chưa có test',
  noMetric: 'Hypothesis này chưa có metric để biết đúng hay sai',
  planned: 'Test này mới ở dạng kế hoạch, chưa chạy',
  simulated: 'Test này dùng người mô phỏng, không phải người dùng thật: chưa tính là bằng chứng',
  noReal: 'Hypothesis này chưa có bằng chứng từ người dùng thật',
  principle: 'Principle chưa có câu hỏi có/không để kiểm tra',
  orphan: 'Tài liệu này chưa nối với item nào (property supports đang trống)',
};

export function graph() {
  const idx = scan();
  const byId = Object.fromEntries(idx.items.map((i) => [i.id, i]));
  const of = (L) => idx.items.filter((i) => i.letter === L).map((i) => i.id);
  const O = of('O'), H = of('H'), M = of('M'), D = of('D'), T = of('T');
  O.sort((a, b) => (Number(byId[a].meta.rank) || 999) - (Number(byId[b].meta.rank) || 999));
  const rel = (id, key) => refs(byId[id].meta[key]).filter((x) => byId[x]);
  const serves = Object.fromEntries(H.map((h) => [h, rel(h, 'serves')]));
  const metric = Object.fromEntries(H.map((h) => [h, rel(h, 'metric')]));
  const tests = Object.fromEntries([...D, ...T].map((x) => [x, rel(x, 'tests')]));
  const measures = Object.fromEntries(T.map((t) => [t, rel(t, 'measures')]));
  const follows = Object.fromEntries(D.map((d) => [d, refs(byId[d].meta.follows)]));
  const strains = Object.fromEntries(D.map((d) => [d, refs(byId[d].meta.pulls_against)]));
  const REL = ['serves', 'metric', 'tests', 'measures', 'follows', 'pulls_against'];
  const back = {};
  for (const i of idx.items) for (const k of REL) for (const t of refs(i.meta[k])) {
    if (byId[t] && t !== i.id) (back[t] ||= []).push({ from: i.id, label: k });
  }
  const hypsOf = (o) => H.filter((h) => serves[h].includes(o));
  const decisionsOf = (h) => D.filter((d) => tests[d].includes(h));
  const testsOf = (h) => T.filter((t) => tests[t].includes(h));

  const warnings = [];
  const warn = {};
  const flag = (kind, ids, text) => { warnings.push({ kind, ids, text }); ids.forEach((i) => (warn[i] ||= []).push(text)); };
  for (const d of D) if (!tests[d].length || tests[d].every((h) => !serves[h]?.length)) flag('noNeed', [d], MSG.noNeed);
  for (const d of D) for (const p of strains[d]) flag('strain', [d], MSG.strain(p));
  for (const o of O) { const hs = hypsOf(o); if (!hs.length || !hs.some((h) => decisionsOf(h).length)) flag('unserved', [o], MSG.unserved); }
  for (const h of H) { if (!testsOf(h).length) flag('untested', [h], MSG.untested); if (!metric[h].length) flag('noMetric', [h], MSG.noMetric); }
  const kind = (t) => {
    const m = byId[t].meta;
    if (String(m.status || '').toLowerCase() === 'planned') return 'planned';
    if (String(m.participants_type || '').toLowerCase() === 'simulated') return 'simulated';
    return 'real';
  };
  for (const t of T) { const k = kind(t); if (k === 'planned') flag('planned', [t], MSG.planned); else if (k === 'simulated') flag('simulated', [t], MSG.simulated); }
  for (const h of H) { const ts = testsOf(h); if (ts.length && !ts.some((t) => kind(t) === 'real')) flag('noReal', [h], MSG.noReal); }
  const emptyP = Object.entries(idx.principles).filter(([, v]) => !v.check.trim() && !v.name.startsWith('(')).map(([k]) => k);
  if (emptyP.length) warnings.push({ kind: 'principle', ids: emptyP, text: MSG.principle });
  for (const a of idx.artifacts) if (!a.supports.length) flag('orphan', [a.id], MSG.orphan);

  const artFor = {};
  for (const a of idx.artifacts) for (const s of a.supports) if (byId[s]) (artFor[s] ||= []).push(a.id);

  /** chains from an opportunity down to id */
  const paths = (id) => {
    const it = byId[id];
    if (!it) return [];
    if (it.letter === 'O') return [[id]];
    let parents = [];
    if (it.letter === 'H') parents = serves[id];
    else if (it.letter === 'D' || it.letter === 'T') parents = tests[id];
    else if (it.letter === 'M') parents = H.filter((h) => metric[h].includes(id));
    return parents.flatMap((p) => paths(p).map((c) => [...c, id]));
  };
  return { idx, byId, O, H, M, D, T, serves, metric, tests, measures, follows, strains, back, warnings, warn, artFor, hypsOf, decisionsOf, testsOf, paths };
}
