import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import path from 'node:path';

// The hub is read straight from the case folder: nothing is copied into this project.
const CASE = path.resolve(process.env.HUB_CASE_DIR || path.resolve(process.cwd(), '../workspace/demo-case'));
const HUB = path.join(CASE, 'hub');
const stem = (entry: string) => path.basename(entry).replace(/\.md$/, '');

// wikilink values such as "[[H1]]" or "[[principle-checks|P8]]" are stored as written; ids are resolved in src/lib
const links = z.union([z.string(), z.array(z.string())]).optional();

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),

  // O, H, M, D, T items. A wrong `type` or a missing `title` fails the build instead of showing up later.
  items: defineCollection({
    loader: glob({
      pattern: '[OHMDT][0-9]*.md',
      base: HUB,
      generateId: ({ entry }) => stem(entry),
    }),
    schema: z.object({
      type: z.enum(['opportunity', 'hypothesis', 'metric', 'decision', 'test']),
      title: z.string(),
      rank: z.number().optional(),
      evidence: z.string().optional(),
      serves: links, metric: links, tests: links, measures: links, follows: links, pulls_against: links,
      status: z.string().optional(), baseline: z.string().optional(), measured_by: z.string().optional(),
      participants: z.number().optional(), participants_type: z.enum(['real', 'simulated']).optional(),
      result: z.string().optional(),
    }),
  }),

  // Documents (artifacts): a single .md, or a folder with index.md plus dropped files.
  artifacts: defineCollection({
    loader: glob({
      pattern: ['artifacts/**/*.md', '!artifacts/_templates/**', '!artifacts/README.md'],
      base: HUB,
      generateId: ({ entry }) => {
        const parts = entry.split('/'); // artifacts/<slug>.md or artifacts/<slug>/index.md
        return parts.length > 2 ? parts[1] : stem(entry);
      },
    }),
    schema: z.object({
      type: z.string().default('generic'),
      title: z.string(),
      stage: z.enum(['Setup', 'Discover', 'Define', 'Develop', 'Deliver']).optional(),
      status: z.enum(['verified', 'draft', 'simulated', 'planned']).optional(),
      summary: z.string().optional(),
      takeaways: z.array(z.string()).optional(),
      supports: links, source: z.string().optional(),
      media: z.array(z.string()).optional(), links: z.array(z.string()).optional(),
      embed: z.boolean().optional(), embed_url: z.string().optional(),
    }),
  }),

  // Stage pages, gates, case log, principle checks
  pages: defineCollection({
    loader: glob({
      pattern: ['hub/0*.md', 'hub/gates.md', 'case-log.md', 'learnings/context-principle-checks.md'],
      base: CASE,
      generateId: ({ entry }) => (entry.endsWith('context-principle-checks.md') ? 'principles' : stem(entry)),
    }),
    schema: z.object({ title: z.string().optional() }).passthrough(),
  }),

  // Working files and original documents that artifacts take their content from (`source:`).
  sources: defineCollection({
    loader: glob({
      pattern: [
        'learnings/**/*.md',
        '!**/_raw-private/**', '!**/prototype/**',
      ],
      base: CASE,
      generateId: ({ entry }) => entry.replace(/\.md$/, ''),
    }),
    schema: z.object({}).passthrough(),
  }),
};
