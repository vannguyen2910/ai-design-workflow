// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	integrations: [
		starlight({
			title: 'AI Design Workflow',
			customCss: ['./src/styles/custom.css'],
			sidebar: [
				{ label: 'Giới thiệu', slug: 'index' },
				{
					label: 'Lessons',
					items: [
						{ label: 'Lesson 1: Your Design Process, with AI', slug: 'lessons/design-process-with-ai/lesson' },
						{ label: 'Practice 1: Case Folder and Hub', slug: 'lessons/design-process-with-ai/practice' },
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
