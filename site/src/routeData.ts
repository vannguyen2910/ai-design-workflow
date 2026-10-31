// @ts-nocheck
// Lesson pages (overview, lesson, practice) share one lesson: keep the sidebar and the tab title consistent with the page title.
import { defineRouteMiddleware } from '@astrojs/starlight/route-data';
import { listLessons } from '../scripts/lessons.mjs';

const CARD = { lesson: 'Lý thuyết', practice: 'Thực hành' };

// mark the "Lesson N" sidebar link as current while on any page of that lesson
function markCurrent(entries, slug) {
	for (const e of entries) {
		if (e.type === 'group') markCurrent(e.entries, slug);
		else if (e.href.includes(`/lessons/${slug}/overview/`)) e.isCurrent = true;
	}
}

export const onRequest = defineRouteMiddleware((context) => {
	const route = context.locals.starlightRoute;
	const m = route.id.match(/^lessons\/([^/]+)\/(lesson|practice|overview)$/);
	const lesson = m && listLessons().find((l) => l.slug === m[1]);
	if (!lesson) return;

	markCurrent(route.sidebar, lesson.slug);
	const title =
		m[2] === 'overview' ? `Lesson ${lesson.num}: ${lesson.lesson.title}` : `${CARD[m[2]]} · Lesson ${lesson.num}`;
	route.entry.data.title = title;
	// the head is built before this runs, so update the tab title and share title there too
	for (const h of route.head) {
		if (h.tag === 'title') h.content = `${title} | ${route.siteTitle}`;
		else if (h.tag === 'meta' && h.attrs?.property === 'og:title') h.attrs.content = title;
	}
});
