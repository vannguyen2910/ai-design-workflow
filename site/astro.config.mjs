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
						{ label: 'Lesson 2: Discover the Problem', slug: 'lessons/discover-the-problem/lesson' },
						{ label: 'Practice 2: Break the Brief', slug: 'lessons/discover-the-problem/practice' },
						{ label: 'Lesson 3: Insights You Can Trust', slug: 'lessons/research-you-can-trust/lesson' },
						{ label: 'Practice 3: Run the Four Steps', slug: 'lessons/research-you-can-trust/practice' },
					],
				},
			],
		}),
	],
});
