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
			const referenceFile = join(materials, `${slug}-reference.md`);
			if (!existsSync(lessonFile)) return null;
			return {
				num,
				slug,
				materials,
				lesson: frontmatter(lessonFile),
				practice: existsSync(practiceFile) ? frontmatter(practiceFile) : null,
				reference: existsSync(referenceFile),
			};
		})
		.filter(Boolean)
		.sort((a, b) => a.num - b.num);
}

// A YouTube link in any common form -> its embed URL. Anything else (Drive, Vimeo) returns null and is shown as a plain link.
export function youtubeEmbed(url = '') {
	const m = url.match(/(?:youtu\.be\/|[?&]v=|\/embed\/|\/live\/|\/shorts\/)([\w-]{11})(?![\w-])/);
	return m ? `https://www.youtube-nocookie.com/embed/${m[1]}` : null;
}

// mentees.md: one `- [Name](https://link)` line per mentee. Only http(s) links count, because they end up in an iframe.
export function parseMentees(text) {
	const seen = {};
	return [...text.matchAll(/^\s*[-*]\s*\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/gm)].map((m) => {
		const name = m[1].trim();
		// "Nguyễn Đức" -> nguyen-duc; a repeated name gets -2, -3 so every mentee has its own page
		const base = name.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/gi, 'd').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'mentee';
		seen[base] = (seen[base] || 0) + 1;
		return { name, url: m[2], slug: seen[base] > 1 ? `${base}-${seen[base]}` : base };
	});
}

// classes/<batch>/ holds mentees.md and playback/NN-<lesson-slug>.md (one per taught lesson)
export function listBatches() {
	const CLASSES = join(ROOT, 'classes');
	if (!existsSync(CLASSES)) return [];
	return readdirSync(CLASSES, { withFileTypes: true })
		.filter((d) => d.isDirectory())
		.map((d) => {
			const dir = join(CLASSES, d.name);
			const menteesFile = join(dir, 'mentees.md');
			const playbackDir = join(dir, 'playback');
			return {
				slug: d.name,
				label: d.name.replace(/-/g, ' ').replace(/^./, (c) => c.toUpperCase()), // batch-1 -> Batch 1
				dir,
				mentees: existsSync(menteesFile) ? parseMentees(readFileSync(menteesFile, 'utf8').replace(/<!--[\s\S]*?-->/g, '')) : [],
				playbacks: (existsSync(playbackDir) ? readdirSync(playbackDir) : [])
					.filter((f) => /^\d+-.+\.md$/.test(f))
					.sort()
					.map((f) => ({ num: Number(f.match(/^\d+/)[0]), slug: f.replace(/^\d+-|\.md$/g, ''), meta: frontmatter(join(playbackDir, f)) })),
			};
		})
		.sort((a, b) => b.slug.localeCompare(a.slug, undefined, { numeric: true })); // newest batch first
}
