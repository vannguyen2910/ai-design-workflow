// Rewrites .md links in lesson and program pages so they work on the site.
// Lesson and practice files become the site pages. Any other repo file links to its copy on GitHub,
// because the site publishes only lesson and practice pages.
import { existsSync } from 'node:fs';
import { dirname, relative, resolve, sep } from 'node:path';
import { ROOT } from './lessons.mjs';

const REPO = 'https://github.com/vannguyen2910/ai-design-workflow/blob/main/';
const LESSON_PAGE = /^lessons\/\d+-([^/]+)\/materials\/.+-(lesson|practice)\.md$/;
const PAGE_ID = { 'introduction.md': '', 'landing/landing-page.md': 'landing' };

// id of the page a file becomes: lessons/<slug>/<kind>, or '' for the home page
function pageId(repoPath) {
	if (repoPath in PAGE_ID) return PAGE_ID[repoPath];
	const m = repoPath.match(LESSON_PAGE);
	return m ? `lessons/${m[1]}/${m[2]}` : null;
}

// relative URL from one page to another, e.g. lessons/a/overview -> lessons/a/lesson = ../lesson/
function relativeUrl(fromId, toId) {
	const from = fromId ? fromId.split('/') : [];
	const to = toId ? toId.split('/') : [];
	let k = 0;
	while (k < from.length && k < to.length && from[k] === to[k]) k++;
	const ups = '../'.repeat(from.length - k) || './';
	return ups + to.slice(k).join('/') + (to.length > k ? '/' : '');
}

function rewrite(url, fromRepoPath) {
	if (/^(https?:|mailto:|#|\/)/.test(url) || !/\.md(#.*)?$/.test(url)) return url;
	const [pathPart, hash = ''] = url.split('#');
	const target = relative(ROOT, resolve(dirname(resolve(ROOT, fromRepoPath)), pathPart)).split(sep).join('/');
	const id = pageId(target);
	if (id !== null) return relativeUrl(pageId(fromRepoPath) ?? '', id) + (hash ? `#${hash}` : '');
	if (existsSync(resolve(ROOT, target))) return REPO + target + (hash ? `#${hash}` : '');
	return url;
}

function walk(node, fn) {
	if (node.type === 'link') fn(node);
	for (const child of node.children ?? []) walk(child, fn);
}

export default function remarkLinks() {
	return (tree, file) => {
		const repoPath = relative(ROOT, file.path).split(sep).join('/');
		walk(tree, (link) => {
			link.url = rewrite(link.url, repoPath);
		});
	};
}
