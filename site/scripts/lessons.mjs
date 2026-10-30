// Finds every lesson folder under lessons/ (NN-slug/materials/*). Shared by the Astro sidebar and the overview generator.
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
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
