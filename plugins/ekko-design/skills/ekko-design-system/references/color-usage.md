# Color usage

Exact values for every token are in `tokens.md`. This file explains **which** token to
use and **when**.

## Architecture

```
Primitives (raw palette)  →  1. Color modes (semantic, Light/Dark)  →  components
grey-900, payday-blue-500     text-primary, bg-brand-500, border-primary
```

- **Product UI uses semantic tokens.** They are named for their role
  (`text-*`, `bg-*`, `icon-*`, `border-*`, `alpha-*`) and swap values in dark mode.
- **Primitives** are 10-step ramps (50 → 900) for Grey, Payday Blue, Lime, Jade, Success,
  Warning and Error, plus Base, Ekko brand and Secondary colors. Reach for them only in
  marketing artwork, illustrations and data viz, or when no semantic token fits (then say so).

## The four brand colors

| Color | Hex | Role | Pairs well with |
|---|---|---|---|
| **Payday Blue** | `#3E58F1` | The brand. Primary actions, links, selection, focus, key brand moments | White, Midnight, Jade |
| **Midnight** | `#00034F` | Deep brand background for statements, dark slides and heroes. Midnight text on Jade | White text, Lime highlight |
| **Lime** ("Fluorescent") | `#B3F42C` | Energy and highlights. The highlight color in dark mode, accent on dark backgrounds | Black `#1B1C1D`, Midnight |
| **Jade** ("Amicable Jade") | `#AEDFDA` | Calm supporting background for K-Wave panels, soft sections | Midnight text, Payday Blue large text |

Support neutrals: **Base/Black `#1B1C1D`** (use instead of `#000`), **White**, and the Grey ramp.

### Ratio guidance
- **Product UI** is roughly 80% neutrals (white/grey surfaces, grey text), 15% Payday Blue, and 5% status and other colors.
- **Brand/marketing** pieces are bolder. A whole slide can be Payday Blue, Midnight, Jade or Black.
  Keep to one dominant brand color per layout plus one accent (Lime on Midnight/Black,
  Payday Blue on White/Jade).

## Semantic token guide

### Backgrounds
| Token | Use |
|---|---|
| `bg-primary` | Default surface: cards, modals, inputs, top bar, sidebar |
| `bg-secondary` | App/page canvas behind cards; segmented-control track |
| `bg-tertiary` | Strong neutral fill: counters, toggle-off track |
| `bg-grey-50` / `bg-grey-200` | Subtle neutral fills: grey alert, selected sidebar item (`bg-grey-200`), table header |
| `bg-grey-500` / `bg-grey-600` | Neutral solid fills (rare) |
| `bg-brand-50` | Brand tint: brand badge, info alert, selected row |
| `bg-brand-200` | Disabled primary button |
| `bg-brand-500` | Primary button, checked checkbox/toggle, active indicator |
| `bg-brand-600` | Primary button hover/pressed |
| `bg-brand-highlight` | Highlight surface: Payday Blue in light, **Lime in dark** |
| `bg-success-*`, `bg-warning-*`, `bg-error-*` | 50 = tinted container, 200 = stronger tint, 500 = solid, 600 = solid hover |

### Text and icons
| Token | Use |
|---|---|
| `text-primary` / `icon-primary` | Headings, body, primary icons |
| `text-secondary` / `icon-secondary` | Labels, helper text, secondary icons, input addons |
| `text-tertiary` | Placeholders, disabled text, timestamps. Not for essential info (2.5:1) |
| `text-white` | Text on brand/solid fills |
| `text-white-disable` | Text on disabled brand button |
| `text-brand-500` / `text-brand-600` | Links, brand-colored text (600 = hover) |
| `text-highlight` / `icon-highlight` | Highlighted text/icon (blue → lime in dark) |
| `text-on-highlight` / `icon-on-highlight` | Content on `bg-brand-highlight` (white → near-black in dark) |
| `text-success` / `text-warning` / `text-error` | Status messages, validation, deltas |

### Borders
| Token | Use |
|---|---|
| `border-primary` | Inputs, secondary buttons, tooltips, dividers that need presence |
| `border-secondary` | Card outlines, toasts, light dividers |
| `border-tertiary` | Stronger neutral outline (hover) |
| `border-brand` / `-success` / `-warning` / `-error` | Colored containers (alerts), error input |
| `border-white` | Avatar ring, overlap separators |
| `border-gradient-1/2/3` (Figma: `graident-*`) | Stops for gradient borders on skeuomorphic surfaces |
| `border-component` (`#8A38F5`) | **Figma-internal** (component-set outline). Never use in designs |

### Alpha
`alpha-10 … alpha-90` are white at N% in light mode and Base/Black at N% in dark mode. Use them for overlays on
imagery, glass effects and scrims. (`Black/alpha-*` primitives are always dark, for modal scrims, e.g. `black-alpha-50`.)

## Dark mode

Dark mode is defined in Figma, not improvised. Its key behaviours:
- Surfaces: `bg-primary` → Grey/800 `#232323`, `bg-secondary` → Grey/900 `#141414`.
- Text inverts (`text-primary` → Grey/50).
- **Highlight switches from Payday Blue to Lime** (`bg-brand-highlight`, `text-highlight`,
  `icon-highlight`). Content on highlight becomes near-black.
- Status text uses the 400 step (lighter) and tinted containers use the 900 step.
- `bg-brand-500` stays Payday Blue, so primary buttons keep their color.

In CSS this is automatic with `ekko-tokens.css` (OS setting or `data-theme="dark"`).

## Contrast: known limits (WCAG, measured)

| Pair | Ratio | Rule |
|---|---|---|
| White on Payday Blue / Payday Blue on White | 5.4:1 | OK for all text |
| Midnight on White, White on Midnight | 18.7:1 | OK |
| Midnight on Jade | 12.8:1 | OK. **Preferred text color on Jade** |
| Lime on Black / Midnight | 12.9 / 14.1:1 | OK. Lime is a dark-background color |
| Payday Blue on Jade | 3.7:1 | Large text only (≥ 24px, or ≥ 18.5px SemiBold) |
| Payday Blue on Black / Midnight | 3.2 / 3.4:1 | Large text only. On dark, prefer Lime or `payday-blue-400`/`300` |
| White on Jade | 1.5:1 | **Never** |
| Lime on White | 1.3:1 | **Never** |
| `text-tertiary` on White | 2.5:1 | Placeholder/disabled only |
| `text-warning` on White | 2.4:1 | Pair with an icon and don't rely on color alone. Use `text-primary` for the message body inside warning containers |
| `text-success` on White | 3.3:1 | Same as warning for small text |
| White on Success/500 button | 2.1:1 | Known DS limit. Prefer `md`+ size, and don't use for long labels |
| White on Error/500 button | 3.4:1 | Large/medium labels only |

## Data visualisation palette

**Product UI charts** (what the Figma Charts components use): the *Secondary colors*, in this order:

1. Secondary Blue `#1283EB`
2. Secondary Yellow `#FFE459`
3. Secondary Purple `#C000BD`
4. Secondary Teal `#0F9E9A`
5. Secondary Violet `#7B61FF`
6. Secondary Green `#2BBF5D`

Chart chrome: grid lines `grey-300`/`grey-200`, axis labels `grey-400` `text-xs`, legend text
`icon-secondary`, values `text-primary`, plot card `bg-primary` + `border-primary`.

**Brand charts** (slides, pitch decks, reports where the brand should lead):
Payday Blue `#3E58F1` → Lime `#B3F42C` (on dark backgrounds; use `lime-600 #8FC323` on white) →
Jade-500 `#4A8D8B` → Midnight `#00034F` → `grey-300` for "other".

- Sequential: use one ramp (e.g. `payday-blue-100 → 900`).
- Positive/negative: `success-500` / `error-500`.

## Gradients (Figma paint styles)

| Name | Value | Use |
|---|---|---|
| `gradient-brand` | `#D8DDFB → #90A3F4` | Soft brand panels, illustrations |
| `gradient-brand-2` | `#3E58F1 → #00034F` | Hero/cover backgrounds, premium cards |
| `gradient-brand-3` | `#B3F42C → #AEDFDA` | Fresh accent (Lime → Jade), marketing only |
| `gradient-neon` | `#B3F42C → #F5F5F5` | Accent fades |
| `gradient-green/red/yellow/grey` | 100 → 300 of each ramp | Status illustration fills |
| `gradient-border` / `-border-2` | grey ↔ white | Skeuomorphic border sheen |

Use gradients sparingly. Never put them behind body text in UI.
