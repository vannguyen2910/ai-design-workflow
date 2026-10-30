// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { listLessons } from './scripts/lessons.mjs';
import remarkLinks from './scripts/remark-links.mjs';

// one sidebar entry per lesson folder: lessons/NN-slug/ -> "Lesson N" -> its overview page
const lessons = listLessons().map((l) => ({ label: `Lesson ${l.num}`, slug: `lessons/${l.slug}/overview` }));

export default defineConfig({
	site: 'https://vannguyen2910.github.io',
	base: '/ai-design-workflow',
	markdown: { remarkPlugins: [remarkLinks] },
	integrations: [
		starlight({
			title: 'AI Design Workflow',
			customCss: ['./src/styles/custom.css'],
				components: { PageTitle: './src/components/PageTitle.astro' },
				routeMiddleware: './src/routeData.ts',
			sidebar: [
				{ label: 'Giới thiệu chương trình', slug: 'index' },
				{ label: 'Landing Page', slug: 'landing' },
				{ label: 'Lessons', items: lessons },
			],
		}),
	],
});
