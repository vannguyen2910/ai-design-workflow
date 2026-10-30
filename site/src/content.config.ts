import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { docsSchema } from '@astrojs/starlight/schema';

// Reads the program's own markdown (repo root is one level up); nothing is copied.
const id = ({ entry }: { entry: string }) =>
	entry === 'introduction.md'
		? 'index'
		: entry === 'landing/landing-page.md'
		? 'landing'
		: entry.replace(/^lessons\/\d+-([^/]+)\/materials\/.*-(lesson|practice|overview)\.mdx?$/, 'lessons/$1/$2');

export const collections = {
	docs: defineCollection({
		loader: glob({
			base: '..',
			pattern: ['introduction.md', 'landing/landing-page.md', 'lessons/*/materials/*-lesson.md', 'lessons/*/materials/*-practice.md', 'lessons/*/materials/*-overview.mdx'],
			generateId: id,
		}),
		// lessons use `draft: true` to mean work in progress; the site still publishes them
		schema: (ctx) => z.preprocess((d) => ({ ...(d as object), draft: false }), docsSchema()(ctx)),
	}),
};
