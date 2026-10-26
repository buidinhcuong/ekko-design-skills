# Layout, spacing, radius and effects

## Spacing scale (Figma `3. Spacing`)

`0 · 2 · 4 · 6 · 8 · 10 · 12 · 14 · 16 · 18 · 20 · 24 · 32 · 40 · 48 · 56 · 64 · 80 · 96 · 128 · 160 · 192 · 224 · 256 · 320 · 384 · 480 · 560 · 640 · 720 · 768 · 960 · 1024 · 1280 · 1440 · 1600 · 1920`

Token names are `spacing-<px>` (`--spacing-16`). The large values (320+) are widths for
containers/breakpoints. Tailwind's default 4px scale expresses every value: px ÷ 4, so
16 → `4`, 18 → `4.5`, 6 → `1.5`, 10 → `2.5`, 14 → `3.5`.

Rhythm used by the components:
- **Inside controls:** 2–8 (icon ↔ label gap 8, badge padding 4/6)
- **Control padding:** 8/16 (md button, tabs), 12/20 (lg button), 0/16 (input horizontal)
- **Component internal:** 12 (alerts, toasts padding; gaps 12–16)
- **Between related elements:** 8–16 (label → input 8, form fields 16–20)
- **Between groups/cards:** 24–32
- **Section spacing:** 48–96 (web), 56 (slide margin)

## Radius scale (Figma `4. Radius`)

`0 · 2 · 4 · 6 · 8 · 10 · 12 · 14 · 16 · 18 · 20 · 22 · 24 · 32 · 56 · 64 · full(9999)`
(primitives also include 40 and 48. Slide cards use 48.)

| Element | Radius |
|---|---|
| Checkbox | 6 |
| Counter chip | 8 |
| sm badge | 10 |
| sm button, md badge, tooltip, tab item, sidebar item, input addon | 12 |
| md button, lg badge, selected squared tab | 14 |
| Input field | 16 |
| lg / xl button | 18 |
| Cards, alerts, toasts, modals, dropdown panels | 24 |
| Toggle track | 32 |
| Large media/brand cards (slides, marketing) | 48 |
| Avatars, icon buttons, pills, status dots | full |

The DS is distinctly **soft and rounded**. Square corners (0–4) are only for tables, dividers and
full-bleed imagery.

## Grids (Figma grid styles)

| Breakpoint | Columns | Gutter | Margin |
|---|---|---|---|
| Desktop (≥1280) | 12 | 32 | 32 |
| Tablet (768–1279) | 6 | 32 | 32 |
| Mobile (<768) | 4 | 20 | 20 |

- Max content width on web: 1280 (`spacing-1280`); text column ≤ 720.
- Mobile app: 375–393pt frames, 20 side margin, top bar 64, tab bar per platform.
- Desktop app shell (Figma Page template): **Top bar 64h** (padding 16/32) and **Sidebar 300w**
  (items 40h, padding 8/16, r12) on `bg-primary`. Content area on `bg-secondary` holds `bg-primary` cards.
- Slides: 1920×1080, 56 margin (see `brand-and-slides.md`).

## Elevation (Effect styles: Shadows)

Layered, very soft shadows. Values are in CSS form (also in `ekko-tokens.css`):

| Token | Use |
|---|---|
| `shadow-xs` | Buttons (secondary), inputs on grey backgrounds |
| `shadow-sm` | Cards at rest |
| `shadow-md` | Dropdowns, popovers, hover-raised cards |
| `shadow-lg` | Toasts, floating panels |
| `shadow-xl` | Modals, dialogs |

Prefer **borders (`border-secondary`) over shadows** for flat cards on white. Use shadow when the
element floats above content.

## Focus rings

`focus-ring-<color>` is a 1px white gap plus a 2px colored ring (`brand`, `secondary` grey, `tertiary`
dark grey, `success`, `warning`, `error`). The `-shadow-sm` variants add a small shadow.

- Every focusable element gets `focus-ring-brand` on `:focus-visible`.
- Use the semantic color for its context (an error input gets `focus-ring-error`).

```css
.btn:focus-visible { outline: none; box-shadow: var(--focus-ring-brand); }
```

## Skeuomorphic

`skeuomorphic-sm` / `skeuomorphic-md` = shadow-xs/sm plus a top inner highlight (white 40%) and a bottom
inner shade (black 40%). They're used for tactile buttons and app-icon/glass elements. Use them
sparingly, never on large surfaces.

## Glass icon

The brand guideline includes "glass" 3D icons (frosted, translucent, using brand colors). They're for
marketing/illustration only, not functional UI icons.
