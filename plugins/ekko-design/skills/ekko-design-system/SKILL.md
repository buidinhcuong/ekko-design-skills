---
name: ekko-design-system
description: Ekko's design system (Ekko UI DS + Brand Guideline v2, from the "[Ekko UI] - Design System" Figma file). It holds the real design tokens (colors, typography, spacing, radius, shadows, light/dark), the 60+ component specs, the icon set, logos, the K-Wave element and the slide master. Use it whenever you design, build, style or review anything for Ekko. That covers product UI (mobile app screens, web apps, dashboards, landing pages, HTML/React/Tailwind/Flutter code, Figma frames) and brand communications (slides, pitch decks, presentations, one-pagers, social posts, posters, banners, reports, emails). It also applies to Vietnamese requests such as "thiết kế", "giao diện", "màn hình app", "slide", "pitch deck", "bài thuyết trình" or "banner" for Ekko. Use it even if the user never says "design system": any mention of Ekko colors, Payday Blue, Lime, Bricolage Grotesque, Ekko buttons/inputs/cards or "make it look like Ekko" should trigger it.
---

# Ekko Design System

Ekko is a Vietnamese fintech that offers Earned Wage Access ("Make every day, pay").
This skill is the coded form of the Figma file **[Ekko UI] - Design System**
(`https://www.figma.com/design/mEy0ESGWDUPfX6AKSo15xu`). Everything you make for Ekko,
whether it is an app screen or a pitch deck, uses the same tokens. If a value isn't a token, it isn't Ekko.

## Step 1: Work out what you're making, then load the right reference

| You are making… | Read (in `references/`) |
|---|---|
| App / web UI, dashboard, component, HTML/React/Tailwind/Flutter code | `color-usage.md`, `typography.md`, `layout-and-effects.md`, `components.md` |
| Slides, pitch deck, presentation, one-pager, poster, social post | `brand-and-slides.md`, `color-usage.md`, `typography.md` |
| Anything that needs an icon | `icons.md` |
| You need an exact value that isn't in the cheat sheet below | `tokens.md` (generated, has every token) |
| Building in Figma itself | `components.md` → "Working inside Figma", plus `component-inventory.md` for variant names and keys |

Read only what the task needs. The cheat sheet below covers most small tasks on its own.

## Step 2: Follow the non-negotiables

1. **Use tokens only.** Every color, font size, spacing, radius and shadow must come from
   the DS. Never invent a hex value, never use an "almost" value (15px, #3D57F0). If you
   need something that doesn't exist, use the nearest token and say so.
2. **In UI, use semantic tokens instead of primitives.** Write `bg-primary`, `text-secondary` and
   `border-primary`, not `#FFFFFF` or `grey-600`. Semantic tokens flip automatically for
   dark mode. Primitives are for brand/marketing artwork and for charts.
3. **Use one typeface family.** **Bricolage Grotesque** is used for everything (UI + headlines + body).
   **Newsreader Italic** is only for emphasis on a few words ("make *everyday* count"),
   usually colored Payday Blue (or Lime on dark). Never set whole paragraphs in Newsreader.
4. **Payday Blue `#3E58F1` is the brand/action color.** It is used for primary buttons, links, selected
   states and focus rings. **Lime `#B3F42C`** is the highlight color: it is the accent on dark surfaces
   and replaces Payday Blue as the "highlight" in dark mode. Never put Lime text on white.
   **Midnight `#00034F`** is the deep brand background. **Jade `#AEDFDA`** is the soft supporting color.
5. **Status colors are only for status.** Success green, Warning yellow and Error red are for
   feedback (alerts, badges, validation). They are never decoration.
6. **Use the scales.** Spacing comes from the 2/4/6/8/10/12/14/16/18/20/24/32/40/48/56/64/80/96… scale.
   Radius comes from the 2–64 + full scale. Text uses the 12 → 72 type scale. Grids are 12 / 6 / 4 columns.
7. **Support light and dark.** Product UI must work in both modes. Using semantic tokens
   gives you dark mode for free. Check contrast in both.
8. **Use the logo exactly as supplied.** Use the SVGs in `assets/logos/`. Only the 4 official colors
   are allowed (Payday Blue, Midnight, Lime, Jade). Never recolor, outline, rotate, add effects to,
   or re-typeset the logo.

## Cheat sheet (most-used tokens)

**Brand colors:** Payday Blue `#3E58F1` · Midnight `#00034F` · Lime `#B3F42C` · Jade `#AEDFDA` ·
Black `#1B1C1D` (Base/Black, used instead of pure #000) · White `#FFFFFF`

**Semantic colors (light → dark):**

| Token | Light | Dark | Use for |
|---|---|---|---|
| `bg-primary` | `#FFFFFF` | `#232323` | Cards, surfaces, inputs |
| `bg-secondary` | `#F5F5F5` | `#141414` | Page/app background behind cards |
| `bg-brand-500` | `#3E58F1` | `#3E58F1` | Primary button |
| `bg-brand-600` | `#3247C2` | `#6076EE` | Primary button hover |
| `bg-brand-50` | `#EDF0FE` | `#131B4D` | Brand tint (badges, selected rows) |
| `bg-brand-highlight` | `#3E58F1` | `#B3F42C` | Highlight surface (blue → lime in dark) |
| `text-primary` | `#141414` | `#FBFBFB` | Headings, body |
| `text-secondary` | `#5E5E5E` | `#DBDBDB` | Supporting text, labels |
| `text-tertiary` | `#A5A5A5` | `#5E5E5E` | Placeholder, disabled, meta |
| `text-brand-500` | `#3E58F1` | `#6076EE` | Links, brand text |
| `text-highlight` / `text-on-highlight` | `#3E58F1` / `#FFF` | `#B3F42C` / `#141414` | Text on/for highlight |
| `border-primary` | `#DBDBDB` | `#5E5E5E` | Input & button borders |
| `border-secondary` | `#ECECEC` | `#5E5E5E` | Card/divider borders |
| `text-success` / `-warning` / `-error` | `#629C28` / `#CAA102` / `#D5394A` | `#98D05B` / `#FDD435` / `#F3797D` | Status text |

**Typography (desktop; mobile shrinks display sizes):**
`display-2xl` 72/80 · `display-xl` 60/68 · `display-lg` 48/56 · `display-md` 36/44 ·
`display-sm` 30/38 · `display-xs` 24/32 · `text-xl` 20/30 · `text-lg` 18/28 · `text-md` 16/24 ·
`text-sm` 14/20 · `text-xs` 12/18. Weights: Light 300, Regular 400, Medium 500, SemiBold 600.
UI defaults: body `text-md/Regular`, controls `text-sm/Regular`, labels and nav `text-sm/Medium` or
`SemiBold`, headings `display-*/Medium` or `SemiBold`.

**Radius:** small controls 10–12 · buttons md/inputs 14–16 · large buttons 18 · cards, toasts and alerts 24 ·
slide cards 48 · pills/avatars `full`.

**Shadows:** `shadow-xs` → `shadow-xl` (soft, layered). The focus ring is `focus-ring-brand` = 1px white + 2px Payday Blue.

**Button sizes:** sm 32h (pad 4/12, r12, text-sm) · md 40h (8/16, r14, text-sm) ·
lg 48h (12/20, r18, text-md) · xl 56h (14/20, r18, text-lg).

## Step 3: Pick the right implementation route

- **HTML / CSS:** link `assets/tokens/ekko-tokens.css`. It loads Google Fonts and defines every
  token as a CSS variable with light + dark (`data-theme="dark"` or the OS setting). Write
  `var(--bg-primary)`, `var(--font-size-text-md)`, `var(--radius-14)`, `var(--shadow-md)`.
  Start from `assets/templates/ui-starter.html`.
- **Tailwind v4:** `@import "tailwindcss"; @import "./tailwind-theme.css";`. Classes map 1:1
  to Figma names: `bg-primary text-secondary border-primary bg-brand-500 hover:bg-brand-600
  text-display-lg text-md rounded-14 shadow-md focus-ring-brand font-primary`.
  Primitives: `bg-payday-blue-500 text-lime-500 bg-jade-200`. Spacing: Tailwind's 4px scale
  already matches (spacing-16 = `p-4`, spacing-18 = `p-4.5`, spacing-6 = `p-1.5`).
- **Tailwind v3:** `presets: [require('./tailwind.preset.cjs')]` + import `ekko-tokens.css`.
- **React Native / Flutter / Swift / Compose:** read raw values from
  `assets/tokens/tokens.json`, or from the tables in `references/tokens.md`, and create a theme object that
  keeps the Figma token names.
- **Slides (HTML deck, PPTX, Google Slides, Keynote, Canva):** follow `references/brand-and-slides.md`.
  For HTML decks start from `assets/templates/slide-template.html` (1920×1080 master).
- **Figma:** use the published library components and bind variables. Never detach or paint raw hex.
  See `components.md`.

Copy the asset files you need into the user's project or output folder. Don't link to this
skill's path from deliverables.

## Step 4: Check before you deliver

- [ ] No raw hex/px values outside the token set (search your output for `#` and `px`)
- [ ] Bricolage Grotesque loads, and Newsreader appears only on short italic emphasis
- [ ] Primary action = Payday Blue, with at most one primary button per view/section
- [ ] Text contrast ≥ 4.5:1 (body) in light **and** dark. No Lime or Jade text on white
- [ ] Spacing, radius and type all come from the scales; components match the specs in `components.md`
- [ ] Every interactive element has hover, focus (`focus-ring-brand`) and disabled states
- [ ] Logo is an official SVG in an official color, with clear space around it
- [ ] Copy follows the voice: optimistic, visionary, ambitious, charismatic (see `brand-and-slides.md`)

## File map

```
SKILL.md                      ← you are here
references/
  color-usage.md              color roles, semantic mapping, dark mode, chart palette
  typography.md               type scale, weights, hierarchy recipes, Vietnamese text
  layout-and-effects.md       spacing, radius, grids, shadows, focus rings, gradients
  components.md               every component: variants, sizes, states, specs
  icons.md                    icon set (4,500+), styles, finding & using icons
  brand-and-slides.md         logo, K-Wave, voice & tone, slide master & deck recipes
  tokens.md                   GENERATED: every token value
  component-inventory.md      GENERATED: every Figma component set, its variants and key
assets/
  tokens/tokens.json          source of truth (exported from Figma)
  tokens/ekko-tokens.css      CSS variables (light/dark)
  tokens/tailwind-theme.css   Tailwind v4 theme
  tokens/tailwind.preset.cjs  Tailwind v3 preset
  tokens/icons.tsv            icon index: name, category, styles, keywords
  tokens/icons.json           raw icon export (source for icons.tsv)
  icons/*.svg                 common UI icons (Stroke, currentColor) + _sprite.svg
  logos/*.svg                 primary / secondary / symbol × 4 colors + wordmark with K-Wave tail
  k-wave/*.svg                K-Wave shapes for brand layouts
  templates/ui-starter.html   product UI starter using the tokens
  templates/slide-template.html  1920×1080 deck master
scripts/
  export-figma.js             re-export tokens from Figma
  build_tokens.py             regenerate CSS/Tailwind/tokens.md from tokens.json
```
