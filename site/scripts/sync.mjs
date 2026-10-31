// Two-way sync of the lessons between Google Drive and this repo, so either side can be edited.
//   npm run sync
// For each file, a hash from the last sync tells which side changed:
//   one side changed        -> copy it to the other side
//   both sides changed      -> conflict: nothing is overwritten, the file is listed and the run exits with code 2
//   missing on one side     -> never deleted or re-created, only reported
// Synced: lessons/NN-*/materials and assets (with _archive), and learning/lesson-*-details.md.
// Generated overview pages are skipped. Set DRIVE_PROGRAM to point at another copy of the program folder.
import { createHash } from 'node:crypto';
import { copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { ROOT } from './lessons.mjs';

const DRIVE =
	process.env.DRIVE_PROGRAM ??
	'/Users/winnie.nguyen/Library/CloudStorage/GoogleDrive-nguyenphuctuongvan@gmail.com/My Drive/03_Mentoring/programs/ai-design-workflow';
const STATE = join(ROOT, 'site', '.sync-state.json');

if (!existsSync(DRIVE)) {
	console.error(`sync: Drive folder not found, nothing done: ${DRIVE}`);
	process.exit(1);
}

const skip = (name) => name === '.DS_Store' || name.endsWith('-overview.mdx');

function walk(base, rel, out) {
	const dir = join(base, rel);
	if (!existsSync(dir)) return;
	for (const name of readdirSync(dir)) {
		if (skip(name)) continue;
		const r = `${rel}/${name}`;
		if (statSync(join(base, r)).isDirectory()) walk(base, r, out);
		else out.add(r);
	}
}

// the relative paths that exist under `base` and belong to the sync
function list(base) {
	const out = new Set();
	const lessons = join(base, 'lessons');
	if (existsSync(lessons)) {
		for (const d of readdirSync(lessons)) {
			if (!/^\d+-/.test(d)) continue;
			for (const sub of ['materials', 'assets']) walk(base, `lessons/${d}/${sub}`, out);
		}
	}
	const learning = join(base, 'learning');
	if (existsSync(learning)) {
		for (const f of readdirSync(learning)) if (/^lesson-.+-details\.md$/.test(f)) out.add(`learning/${f}`);
	}
	return out;
}

const hash = (p) => (existsSync(p) ? createHash('sha1').update(readFileSync(p)).digest('hex') : null);
const state = existsSync(STATE) ? JSON.parse(readFileSync(STATE, 'utf8')) : {};

function copy(from, to, rel) {
	mkdirSync(dirname(join(to, rel)), { recursive: true });
	copyFileSync(join(from, rel), join(to, rel));
}

const toRepo = [], toDrive = [], conflicts = [], missing = [];
const all = new Set([...list(DRIVE), ...list(ROOT)]);
for (const rel of Object.keys(state)) if (!all.has(rel)) delete state[rel]; // gone on both sides
for (const rel of all) {
	const d = hash(join(DRIVE, rel));
	const r = hash(join(ROOT, rel));
	const s = state[rel];
	if (d && r) {
		if (d === r) state[rel] = d;
		else if (s === r) { copy(DRIVE, ROOT, rel); toRepo.push(rel); state[rel] = d; }
		else if (s === d) { copy(ROOT, DRIVE, rel); toDrive.push(rel); state[rel] = r; }
		else conflicts.push(rel);
	} else if (d && !r) {
		if (s === undefined) { copy(DRIVE, ROOT, rel); toRepo.push(rel); state[rel] = d; }
		else missing.push(`${rel} (deleted in the repo, still in Drive)`);
	} else if (r && !d) {
		if (s === undefined) { copy(ROOT, DRIVE, rel); toDrive.push(rel); state[rel] = r; }
		else missing.push(`${rel} (deleted in Drive, still in the repo)`);
	}
}
writeFileSync(STATE, JSON.stringify(state, null, 1) + '\n');

const show = (title, items) => items.length && console.log(`${title} (${items.length}):\n${items.map((i) => `  ${i}`).join('\n')}`);
show('Drive -> repo', toRepo);
show('repo -> Drive', toDrive);
show('Left alone, missing on one side', missing);
show('CONFLICT: changed on both sides, nothing overwritten. Keep one version, then run sync again', conflicts);
if (!toRepo.length && !toDrive.length && !conflicts.length && !missing.length) console.log('sync: Drive and the repo are in step.');
process.exit(conflicts.length ? 2 : 0);
