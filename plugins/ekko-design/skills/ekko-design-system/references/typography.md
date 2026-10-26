# Typography

## Typefaces

| Role | Family | Weights in DS | Source |
|---|---|---|---|
| **Primary**: everything (UI, headlines, body, buttons) | **Bricolage Grotesque** | Light 300, Regular 400, Medium 500, SemiBold 600 | Google Fonts (free, supports Vietnamese) |
| **Secondary**: special/emphasis text only | **Newsreader** (italic) | Light Italic, Italic, Medium Italic, SemiBold Italic | Google Fonts (free, supports Vietnamese) |

Load both: `https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Newsreader:ital,opsz,wght@1,6..72,300..600&display=swap`
(already included in `ekko-tokens.css`).

Fallbacks: `system-ui, -apple-system, 'Segoe UI', sans-serif` / `Georgia, serif`.
In tools that lack the fonts (PowerPoint on a machine without them, email), install the fonts or
embed them. If you can't, fall back to Arial/Helvetica and say so. Don't swap in a lookalike silently.

Bricolage Grotesque has optical sizes. Browsers pick them automatically with `font-optical-sizing: auto`
(the default), so large display text gets the tighter display cut.

## Type scale (Figma variables `2. Typography`)

| Token | Desktop size/line | Mobile size/line | Typical use |
|---|---|---|---|
| `display-2xl` | 72 / 80 | 48 / 56 | Hero headline (web), slide statement |
| `display-xl` | 60 / 68 | 40 / 48 | Landing hero, slide section title |
| `display-lg` | 48 / 56 | 32 / 40 | Page hero, big numbers |
| `display-md` | 36 / 44 | 28 / 36 | Page title |
| `display-sm` | 30 / 38 | 24 / 32 | Section title |
| `display-xs` | 24 / 32 | 22 / 30 | Card/dialog title, mobile screen title |
| `text-xl` | 20 / 30 | 20 / 30 | Lead paragraph, large card title |
| `text-lg` | 18 / 28 | 18 / 28 | Subheading, xl button |
| `text-md` | 16 / 24 | 16 / 24 | **Body default**, lg button, input text |
| `text-sm` | 14 / 20 | 14 / 20 | **Controls default**: buttons md/sm, tabs, badges, table cells, labels |
| `text-xs` | 12 / 18 | 12 / 18 | Captions, helper meta, chart axes, sm badges |

Letter-spacing is 0 for every style. Don't add tracking, except optional uppercase meta labels (see slides).

Figma text style names: `<token>/<weight>`, for example `text-sm/Medium`, `display-lg/SemiBold`,
`text-md/Italic` (Newsreader). In CSS use `.ekko-<token>` + `.ekko-<weight>`, or Tailwind
`text-<token>` (`text-md`, `text-display-lg`) + `font-medium`.

## Weight usage

| Weight | UI | Brand / slides |
|---|---|---|
| **Light 300** | Rare (large numbers) | **Body copy on brand materials**, slide meta labels |
| **Regular 400** | **Body, buttons, inputs, table text** | Large statements (cover titles, 128px), body on slides |
| **Medium 500** | Labels, nav items, emphasized text, titles | **Headlines** (brand guideline rule: "Headlines: Bricolage Grotesque Medium") |
| **SemiBold 600** | Headings, card titles, alert titles, selected nav | Strong subheads, key numbers |

Bricolage Grotesque Bold exists but isn't part of the DS. Avoid it.

## Hierarchy recipes

**App screen (mobile):** screen title `display-xs/SemiBold` · section title `text-lg/SemiBold` ·
body `text-md/Regular` `text-primary` · secondary info `text-sm/Regular` `text-secondary` ·
caption `text-xs` `text-tertiary`.

**Web app / dashboard:** page title `display-sm/SemiBold` (or `display-md/Medium`) · card title
`text-lg/SemiBold` · KPI number `display-md/SemiBold` · KPI label `text-sm/Medium` `text-secondary` ·
table `text-sm/Regular`, header `text-xs/Medium` `text-secondary`.

**Landing page:** hero `display-2xl/Medium` (mobile auto-shrinks to 48) with one Newsreader italic
phrase in `text-brand-500` · sub `text-xl/Light` or `Regular` `text-secondary` · section titles
`display-md/Medium` · body `text-lg/Light` or `text-md/Regular`.

**Slides (1920×1080):** see `brand-and-slides.md`. Sizes there go beyond the UI scale
(statement 128px), which is intentional for projection.

## Newsreader emphasis (the Ekko signature)

The brand's typographic signature is a sans headline with **one short phrase in Newsreader Italic**:

> Ekko exists to *make everyday* count.
> Our business is to *make pay-day history.*
> Early Access to Your *Pay.*

Rules:
- Use 1–4 words, once per headline. Never set whole sentences or body text in it.
- Match the size of the surrounding sans text. Newsreader looks smaller, so it can go
  ~5–10% larger if needed.
- Color: Payday Blue on light backgrounds; Lime, Jade or white on dark. It can also stay the same
  color as the headline when the layout is already busy.
- Weight: `Italic` (Regular) or `Light Italic` for big statements, `Medium Italic` for small sizes.
- In UI, use it for marketing moments only (onboarding, empty states, hero banners), not in
  functional UI like forms or tables.

## Vietnamese text

Both fonts include Vietnamese diacritics. Vietnamese wraps longer than English. Leave
10–20% more room, keep line-height at the token value (don't tighten), and check that stacked
diacritics (ệ, ở, ữ) aren't clipped in fixed-height containers.
