// Copies lessons from the Google Drive copy (the source of truth) into this repo.
// Run it by hand after you edit a lesson in Drive: npm run sync
// Set LESSONS_SOURCE to point at another copy of the lessons folder.
import { copyFileSync, existsSync, mkdirSync, readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT } from './lessons.mjs';

const SOURCE = process.env.LESSONS_SOURCE ?? '/Users/winnie.nguyen/Library/CloudStorage/GoogleDrive-nguyenphuctuongvan@gmail.com/My Drive/03_Mentoring/programs/ai-design-workflow/lessons';
const DEST = join(ROOT, 'lessons');

if (!existsSync(SOURCE)) {
	console.error(`sync: source not found, nothing copied: ${SOURCE}`);
	process.exit(1);
}

// copy every file in a folder tree, skipping _archive
function copyTree(src, dst) {
	for (const name of readdirSync(src)) {
		if (name === '_archive' || name.startsWith('.')) continue;
		const from = join(src, name);
		const to = join(dst, name);
		if (statSync(from).isDirectory()) {
			mkdirSync(to, { recursive: true });
			copyTree(from, to);
		} else {
			copyFileSync(from, to);
			console.log(`copied ${join(from.replace(SOURCE, 'lessons'))}`);
		}
	}
}

for (const name of readdirSync(SOURCE)) {
	if (!/^\d+-/.test(name)) continue;
	const src = join(SOURCE, name);
	if (!statSync(src).isDirectory()) continue;
	// the lesson's materials and assets; slides/ holds built decks and is left to the repo
	for (const sub of ['materials', 'assets']) {
		if (!existsSync(join(src, sub))) continue;
		const dst = join(DEST, name, sub);
		mkdirSync(dst, { recursive: true });
		copyTree(join(src, sub), dst);
	}
}
