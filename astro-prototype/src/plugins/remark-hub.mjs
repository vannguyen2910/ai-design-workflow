// Remark plugin: keeps Markdown links between hub files working, drops (or folds) "AI draft" sections.
import path from 'node:path';
import fs from 'node:fs';
import { visit } from 'unist-util-visit';
import { toString } from 'mdast-util-to-string';
import { scan, assetUrl, isPrivate, CASE } from '../lib/hubindex.mjs';

const DRAFT = /\bAI draft\b/i;

export function remarkHub(options = {}) {
  const team = !!options.team;
  return (tree, file) => {
    // 1. AI-draft sections: removed by default, folded in team mode
    const out = [];
    let skipping = false;
    for (let i = 0; i < tree.children.length; i++) {
      const node = tree.children[i];
      if (node.type === 'heading' && node.depth <= 2) {
        const isDraft = node.depth === 2 && DRAFT.test(toString(node));
        if (skipping && !isDraft) skipping = false;
        if (isDraft) {
          if (!team) { skipping = true; continue; }
          out.push({ type: 'html', value: `<details class="draft"><summary>Bản nháp AI, chưa kiểm tra: ${toString(node).replace(/</g, '&lt;')}</summary>` });
          // include following nodes until the next H2 or higher
          let j = i + 1;
          while (j < tree.children.length && !(tree.children[j].type === 'heading' && tree.children[j].depth <= 2)) { out.push(tree.children[j]); j++; }
          out.push({ type: 'html', value: '</details>' });
          i = j - 1;
          continue;
        }
      }
      if (!skipping) out.push(node);
    }
    tree.children = out;

    // 2. links and images that point to files inside the case
    const from = file?.path ? path.dirname(file.path) : null;
    if (!from) return;
    const { routes } = scan();
    visit(tree, (node, index, parent) => {
      if ((node.type !== 'link' && node.type !== 'image') || !node.url || /^(https?:|mailto:|#|\/)/.test(node.url)) return;
      const [rel, hash] = node.url.split('#');
      const abs = path.resolve(from, decodeURIComponent(rel));
      if (node.type === 'link') {
        if (routes.has(abs)) { node.url = routes.get(abs) + (hash ? '#' + hash : ''); return; }
        if (fs.existsSync(abs) && fs.statSync(abs).isFile() && !isPrivate(abs) && !abs.toLowerCase().endsWith('.md') && abs.startsWith(CASE)) {
          node.url = assetUrl(abs); return;
        }
        // not published: keep the text, drop the link
        if (parent && typeof index === 'number') parent.children.splice(index, 1, ...node.children);
        return;
      }
      if (fs.existsSync(abs) && !isPrivate(abs) && abs.startsWith(CASE)) node.url = assetUrl(abs);
    });
  };
}
