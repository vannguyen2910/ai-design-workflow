import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { docsSchema } from '@astrojs/starlight/schema';

// Reads the program's own markdown (repo root is one level up); nothing is copied.
const id = ({ entry }: { entry: string }) =>
	entry === 'introduction.md'
		? 'index'
		: entry.replace(/^lessons\/\d+-([^/]+)\/materials\/.*-(lesson|practice)\.md$/, 'lessons/$1/$2');

export const collections = {
	docs: defineCollection({
		loader: glob({
			base: '..',
			pattern: ['introduction.md', 'lessons/*/materials/*-lesson.md', 'lessons/*/materials/*-practice.md'],
			generateId: id,
		}),
		// lessons use `draft: true` to mean work in progress; the site still publishes them
		schema: (ctx) => z.preprocess((d) => ({ ...(d as object), draft: false }), docsSchema()(ctx)),
	}),
};
