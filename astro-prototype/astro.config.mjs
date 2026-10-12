// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { remarkHub } from './src/plugins/remark-hub.mjs';
import { scan, TYPES, STAGES, ART_TYPES } from './src/lib/hubindex.mjs';

const idx = scan();
const team = process.env.HUB_TEAM === '1';

// Sidebar is generated from the hub folder, so adding a file adds a menu entry.
const sidebar = [
  { label: 'Overview', link: '/' },
  { label: 'Journey', items: idx.pages.filter((p) => p.kind === 'week').map((p) => ({ label: p.label, link: `/pages/${p.id}/` })) },
  {
    label: 'Documents',
    collapsed: false,
    items: [
      { label: 'All documents', link: '/docs/' },
      ...STAGES.flatMap((s) => {
        const group = idx.artifacts.filter((a) => a.stage === s);
        return group.length ? [{ label: s, collapsed: true, items: group.map((a) => ({ label: a.title, link: `/docs/${a.id}/` })) }] : [];
      }),
    ],
  },
  {
    label: 'Insights',
    items: [
      { label: 'Insights', link: '/trace/' },
      ...TYPES.map((t) => ({
        label: t.many, collapsed: true,
        items: idx.items.filter((i) => i.letter === t.letter).map((i) => ({ label: `${i.id}: ${i.title}`, link: `/items/${i.id}/` })),
      })),
    ],
  },
  { label: 'Reference', items: idx.pages.filter((p) => p.kind === 'ref').map((p) => ({ label: p.label, link: `/pages/${p.id}/` })) },
  { label: 'Về trang này', link: '/about-this-site/' },
];

export default defineConfig({
  site: process.env.HUB_SITE || undefined,
  base: process.env.HUB_BASE || '/',
  // Codespaces serves the dev site on a *.app.github.dev host.
  vite: { server: { allowedHosts: true } },
  markdown: { remarkPlugins: [[remarkHub, { team }]] },
  integrations: [
    starlight({
      title: idx.caseName,
      description: 'Knowledge Hub của dự án',
      defaultLocale: 'root',
      locales: { root: { label: 'Tiếng Việt', lang: 'vi' } },
      sidebar,
      customCss: ['./src/styles/custom.css'],
      components: {
        ThemeProvider: './src/components/ThemeProvider.astro',
        ThemeSelect: './src/components/ThemeSelect.astro',
      },
      credits: false,
    }),
  ],
});
