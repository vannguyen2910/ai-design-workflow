// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	site: 'https://vannguyen2910.github.io',
	base: '/ai-design-workflow',
	integrations: [
		starlight({
			title: 'AI Design Workflow',
			customCss: ['./src/styles/custom.css'],
			sidebar: [
				{ label: 'Giới thiệu chương trình', slug: 'index' },
				{ label: 'Landing Page', slug: 'landing' },
				{
					label: 'Lessons',
					items: [
						{ label: 'Lesson 1', slug: 'lessons/design-process-with-ai/overview' },
						{ label: 'Lesson 2', slug: 'lessons/discover-the-problem/overview' },
						{ label: 'Lesson 3', slug: 'lessons/research-you-can-trust/overview' },
						{ label: 'Lesson 5', slug: 'lessons/ai-prototyping/overview' },
					],
				},
			],
		}),
	],
});
