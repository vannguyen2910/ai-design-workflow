// Finds every lesson folder under lessons/ (NN-slug/materials/*). Shared by the Astro sidebar and the overview generator.
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

// The repo root holds both lessons/ and site/. Walk up from the working directory, because Astro bundles this
// file into site/dist/, where a path relative to the file would be wrong.
function findRoot() {
	for (let d = process.cwd(), i = 0; i < 4; i++, d = join(d, '..')) {
		if (existsSync(join(d, 'lessons')) && existsSync(join(d, 'site'))) return d;
	}
	return join(dirname(fileURLToPath(import.meta.url)), '..', '..');
}
export const ROOT = findRoot();
const LESSONS = join(ROOT, 'lessons');

// frontmatter: flat `key: value` pairs, quotes stripped
export function frontmatter(file) {
	const text = readFileSync(file, 'utf8');
	const m = text.match(/^---\n([\s\S]*?)\n---/);
	const meta = {};
	for (const line of m ? m[1].split('\n') : []) {
		const kv = line.match(/^(\w[\w-]*):\s*(.*)$/);
		if (kv) meta[kv[1]] = kv[2].replace(/^"(.*)"$/, '$1');
	}
	return meta;
}

export function listLessons() {
	return readdirSync(LESSONS, { withFileTypes: true })
		.filter((d) => d.isDirectory() && /^\d+-/.test(d.name))
		.map((d) => {
			const num = Number(d.name.match(/^\d+/)[0]);
			const slug = d.name.replace(/^\d+-/, '');
			const materials = join(LESSONS, d.name, 'materials');
			const lessonFile = join(materials, `${slug}-lesson.md`);
			const practiceFile = join(materials, `${slug}-practice.md`);
			if (!existsSync(lessonFile)) return null;
			return {
				num,
				slug,
				materials,
				lesson: frontmatter(lessonFile),
				practice: existsSync(practiceFile) ? frontmatter(practiceFile) : null,
			};
		})
		.filter(Boolean)
		.sort((a, b) => a.num - b.num);
}
