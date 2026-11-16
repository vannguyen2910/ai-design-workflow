// @ts-nocheck
// Lesson pages (overview, lesson, practice) share one lesson: keep the sidebar and the tab title consistent with the page title.
import { defineRouteMiddleware } from '@astrojs/starlight/route-data';
import { listLessons } from '../scripts/lessons.mjs';

const CARD = { lesson: 'Lý thuyết', practice: 'Thực hành', reference: 'Tài liệu tham khảo' };

// mark the "Lesson N" sidebar link as current while on any page of that lesson
function markCurrent(entries, href) {
	for (const e of entries) {
		if (e.type === 'group') markCurrent(e.entries, href);
		else if (e.href.endsWith(href)) e.isCurrent = true;
	}
}

export const onRequest = defineRouteMiddleware((context) => {
	const route = context.locals.starlightRoute;
	// a mentee page or a lesson's playback page lights up its batch in the sidebar
	const c = route.id.match(/^classes\/([^/]+)\/(playback|mentees)\//);
	if (c) return markCurrent(route.sidebar, `/classes/${c[1]}/`);
	const m = route.id.match(/^lessons\/([^/]+)\/(lesson|practice|reference|overview)$/);
	const lesson = m && listLessons().find((l) => l.slug === m[1]);
	if (!lesson) return;

	markCurrent(route.sidebar, `/lessons/${lesson.slug}/overview/`);
	const title =
		m[2] === 'overview' ? `Lesson ${lesson.num}: ${lesson.lesson.title}` : `${CARD[m[2]]} · Lesson ${lesson.num}`;
	route.entry.data.title = title;
	// the head is built before this runs, so update the tab title and share title there too
	for (const h of route.head) {
		if (h.tag === 'title') h.content = `${title} | ${route.siteTitle}`;
		else if (h.tag === 'meta' && h.attrs?.property === 'og:title') h.attrs.content = title;
	}
});
