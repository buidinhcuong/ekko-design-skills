# Notes for AI agents working on this repo

This repo is a Claude Code plugin marketplace of **Ekko design skills**.

- Skills live in `plugins/ekko-design/skills/<skill>/SKILL.md` (+ `references/`, `assets/`, `scripts/`).
- `ekko-design-system` is the foundation. Other design skills reference it for tokens instead of copying values.
- The token source of truth is `plugins/ekko-design/skills/ekko-design-system/assets/tokens/tokens.json`, exported
  from Figma by `scripts/export-figma.js` (run it through the figma-console MCP `figma_execute` tool). After
  updating it, run `python3 plugins/ekko-design/skills/ekko-design-system/scripts/build_tokens.py`.
- Never hand-edit the generated files: `ekko-tokens.css`, `tailwind-theme.css`, `tailwind.preset.cjs`,
  `icons.tsv`, `references/tokens.md`, `references/component-inventory.md`.
- When the Figma components change, re-measure the affected specs and update `references/components.md` by hand.
- Bump `version` in both `.claude-plugin/marketplace.json` and `plugins/ekko-design/.claude-plugin/plugin.json`,
  and add a `CHANGELOG.md` entry for every release. See `docs/CONTRIBUTING.md`.
- To use these skills while designing for Ekko (not maintaining the repo), read
  `plugins/ekko-design/skills/ekko-design-system/SKILL.md` first.
