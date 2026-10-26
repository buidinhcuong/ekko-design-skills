# Components

Specs were measured from the Figma components. Token names are the Figma variable names (CSS: `var(--<name>)`,
Tailwind: same class name). The full list of component sets with every variant property and its Figma
key is in `component-inventory.md` (generated).

**Library contents:** Avatar · Avatar stack · Alert · Button · Social button · Text link · Button group ·
Badge · Chip · Breadcrumb · Charts (Column, Bar, Line, Donut, Pie + legend/tooltip/axes) · Checkbox ·
Radio · Divider · File uploader · File progress · Input · Input addon · Helper text · Text area ·
Message input · Menu item · Shortcut · Sidebar item · Top bar · Counter · Pagination · Date picker ·
Scrollbar · Slider · Status dot · Loader · Table cell · Underlined tabs · Squared tabs · Toast · Toggle ·
Tooltip · Ekko logo · Cursors · Page template (Head, Content, Footer, Sidebar, Topbar, Title).

There is **no Modal/Dialog, Card, Select or Bottom sheet component**. Compose them from the
foundations: `bg-primary`, `radius-24`, `shadow-xl` (modal) or `border-secondary` (card), 24 padding,
`display-xs/SemiBold` title, and buttons right-aligned (primary last).

## Universal state model

Every interactive component has **Default · Hover · Focus · Disable**, and selectable ones add
**Selected** (plus Indeterminate for checkboxes; Error/Filled/Typing for inputs).

| State | Treatment |
|---|---|
| Hover | One step darker/stronger fill (`bg-brand-500` → `bg-brand-600`; white → `bg-secondary`; clear → `bg-tertiary`; list item → `bg-grey-200`) |
| Focus | `focus-ring-brand` (Clear buttons use `focus-ring-secondary`). Show it on keyboard focus (`:focus-visible`) |
| Disable | Brand fill → `bg-brand-200` + `text-white-disable`; neutral → text `text-tertiary`. No shadow, `cursor: not-allowed` |
| Selected | Brand fill or `bg-grey-200` + SemiBold label (nav/menus), brand underline (tabs) |
| Error | `text-error` border on inputs, error helper text with icon, `focus-ring-error` |

## Button

Types: **Brand** (primary) · **Secondary** (outlined) · **Clear** (ghost) · **Success** · **Alert** (destructive red).
Options: icon left/right, icon-only (`Text=Off`), dropdown chevron.

| Size | Height | Padding (v/h) | Radius | Label | Icon-only |
|---|---|---|---|---|---|
| sm | 32 | 4 / 12 | 12 | `text-sm/Regular` | 32×32, pad 4 |
| md | 40 | 8 / 16 | 14 | `text-sm/Regular` | 40×40, pad 8 |
| lg | 48 | 12 / 20 | 18 | `text-md/Regular` | 48×48, pad 12 |
| xl | 56 | 14 / 20 | 18 | `text-lg/Regular` | 56×56, pad 16 |

Icon ↔ label gap 8, icons 20px (sm/md) or 24px (lg/xl).

| Type | Default | Hover | Disabled | Text |
|---|---|---|---|---|
| Brand | `bg-brand-500` | `bg-brand-600` | `bg-brand-200` | `text-white` (disabled `text-white-disable`) |
| Secondary | `bg-primary` + 1px `border-primary` | `bg-secondary` | same, text `grey-400` | `text-primary` |
| Clear | transparent | `bg-tertiary` | transparent | `text-primary` (disabled `text-tertiary`) |
| Success | `success-500` | `success-600` | `success-200` | white |
| Alert | `error-500` | `error-600` | `error-200` | white |

Rules: one Brand button per view/section. Secondary for the alternative action, Clear for low-emphasis
actions (Cancel, toolbar). Alert only for destructive confirmations. Labels are sentence case and verb-first
("Rút lương", "Save changes").

**Text link:** no padding, radius 4, `text-brand-500` (Secondary type uses `text-secondary`). Sizes md/lg/xl use
`text-sm/md/lg`. Underline on hover.

**Social button:** md is 40h, pad 10/16, r14, `bg-primary` + `border-primary`, `text-sm`, brand logo icon left (Apple / Google).

**Button group / Group button:** joined segmented buttons (2–6), `border-primary` dividers, sizes sm/md/lg,
optional checkbox per item.

## Input

Structure: **Label** (`text-sm/Medium` `text-primary`, red `*` in `text-error` when required) → gap 8 →
**Field** → gap 8 → **Helper text** (`text-sm` `text-secondary`, or `text-error` + icon for errors).

| Size | Field height |
|---|---|
| sm | 36 |
| md | 44 |
| lg | 48 |

Field: `bg-primary`, 1px `border-primary`, **radius 16**, horizontal padding 16, content `text-md`
(placeholder `text-tertiary`), optional icon left/right (24px, `icon-secondary`), optional **Input addon**
(left prefix such as country code/currency with chevron, or right suffix) separated by a 1px `border-primary` divider,
addon text `text-secondary`.

States: Default · Hover · Focus (`focus-ring-brand`) · Typing · Filled (value in `text-primary`) ·
Error (border in the `text-error` color + error helper) · Disable · Tag (chips inside). Hover and Disable keep
`bg-primary` + `border-primary`. In code, use `border-tertiary` on hover, and on disable dim the content to
`text-tertiary` with `cursor: not-allowed`.

**Text area:** min 120h, pad 12/16, r16, same states. **Message input:** chat composer with attach + send.

## Selection controls

- **Checkbox** 16×16, r6. Selected/Indeterminate are `bg-brand-500` with a white glyph. Unselected has a 1px `border-primary` on `bg-primary`. Disabled uses a `bg-tertiary` fill.
- **Radio** 16×16 circle. Selected has a `bg-brand-500` ring with a white dot.
- **With label:** label `text-sm` or `text-md` `text-primary`, gap 8, `Text side` Left/Right.
- **Toggle** 52×24 track, r32, pad 2. Off = `grey-300`, On = `payday-blue-500`. White knob 20.
  Toggle with label follows the same pattern.

## Badge and chip

**Badge** (status label, non-interactive):

| Size | Height | Padding | Radius | Text |
|---|---|---|---|---|
| sm | 22 | 2 / 6 | 10 | `text-xs` |
| md | 28 | 4 / 6 | 12 | `text-sm` |
| lg | 36 | 8 / 8 | 14 | `text-sm` |

Colors (tinted fill + colored text): Brand `bg-brand-50`/`text-brand-500` · Green `bg-success-50`/`text-success` ·
Yellow `bg-warning-50`/`text-warning` · Red `bg-error-50`/`text-error` · Grey `bg-grey-50`/`text-primary`.
Options: leading dot, icon, Outline (adds a 1px border of the matching `border-*`).

**Chip** (interactive/filter, with close ×): sm 22h (2/6, r10), md 24h (2/6, r12), lg 32h (6/8, r14), same colors,
Hover darkens the tint.

## Feedback

**Alert** (inline, persistent): pad 12, gap 12, **r24**, tinted fill + 1px border
(`bg-brand-50`+`border-brand`, `bg-grey-50`+`border-primary`, `bg-success-50`+`border-success`,
`bg-warning-50`+`border-warning`, `bg-error-50`+`border-error`). Title `text-md/SemiBold` `text-primary`,
description `text-sm` `text-secondary`, leading status icon in the matching color, optional 1–2 buttons + close.

**Toast** (transient): ~452w, pad 12, gap 16, **r24**, `bg-primary` + `border-secondary` + `shadow-lg`,
colored status icon (Brand/Green/Yellow/Red), title `text-sm/Medium`, description `text-sm` `text-secondary`,
optional action. Stack bottom-right (web) or top (mobile).

**Tooltip**: pad 6/12, r12, `text-sm`. Colors: White (`bg-primary` + `border-primary`), Grey, Payday Blue
(white text), Fluorescent/Lime (dark text). Optional chevron left/center/right.

**Loader**: spinner in Payday Blue. **File progress**: In progress / Uploaded / Error.

**Status dot**: xs 8 · sm 10 · md 12 · lg 14 · xl 16. Online `success-500`, Busy `error-500`,
Away `warning-500`, Offline `grey-400`. Optional white outline ring (on avatars).

## Navigation

- **Top bar**: 64h, pad 16/32, `bg-primary`. Logo left + menu items (`text-sm/Medium`), right side icon
  button (32, full radius, `border-primary`), user avatar + name, chevron. States: Logged in / Guest.
- **Sidebar item**: 40h (300w container), pad 8/16, r12, icon 20 + label `text-sm`. Selected = `bg-grey-200` +
  `text-sm/SemiBold` + icon in `text-brand-500`. Types: Item / Toggle (expandable) / Label (section header).
  Optional **Counter** (24×24, r8, `bg-tertiary` `text-secondary`; selected `bg-brand-500` white).
- **Underlined tabs**: item 56h, pad 16/8, `text-sm`. Selected = `text-brand-600` + 2px Payday Blue underline;
  Hover = brand text. Optional counter badge.
- **Squared tabs** (segmented control): track `bg-secondary`, r16, pad 2. Items 40h, pad 8/16, r12,
  `text-sm`. Selected item = `bg-primary` (r14), `text-primary`.
- **Breadcrumb**: Chevron or Slash separators, items `text-sm` `text-secondary`, current item `text-primary`.
- **Pagination**: number items 32×32, `text-sm` `text-secondary` (current page `text-primary`), hover state,
  First/Prev/Next/Last buttons, optional "Add on" (rows-per-page / go-to). Container type White or Clear.
- **Menu item** (dropdown/context menu): 48h, pad 8/16, `text-sm` + optional description `text-sm`
  `text-secondary`, shortcut `text-xs`. Hover = `bg-grey-200`, Selected = SemiBold. Types: Icon, Avatar,
  Checkbox, Status dot, Social, Label. Panel: `bg-primary`, r24, `shadow-md`, pad 8.

## Data display

- **Table cell**: 48h, pad 12/16, gap 8, `text-sm/Regular` `text-primary`. Row background White (`bg-primary`) or
  Grey (`bg-secondary`) for zebra striping. Header cells use `Type=Label` (`text-xs/Medium` `text-secondary`,
  optional help icon). Cells can contain checkbox, avatar (+name/description), avatar stack, badge(s),
  button, icons.
- **Avatar**: xs 24 · sm 32 · md 40 · lg 48 · xl 56. Image or initials (`grey-100` fill, text `grey-500`
  Medium). Rounded (full) or Squared. Optional status dot. **Avatar stack**: 2–6 overlapping with a white
  ring + "+N" counter.
- **Charts**: card with **Chart title** (title + dropdown + button), plot, legend. See the chart palette in
  `color-usage.md`.
- **Divider**: 1px, Light (`border-secondary`) / Heavy (`border-primary`), horizontal or vertical.

## Inputs (advanced)

- **Date picker**: panel 328w, pad 16, gap 24, **r32**, `bg-primary` + `shadow-lg`. Day cells: selected
  `bg-brand-500` white text, range `bg-brand-50`, today outlined. Types: Date, Range, Month, Year.
- **Slider**: track `bg-tertiary`, fill `bg-brand-500`, white knob with `shadow-sm`, optional ticks/labels.
- **File uploader**: dropzone pad 48, **r32**, `bg-primary` + `border-primary` (dashed on hover/drag),
  upload icon, `text-sm` + `text-sm/Light` `text-secondary` hint. States: Default/Hover/Focus/Error/Disable.

## Composition recipes

**Card**: `bg-primary`, 1px `border-secondary` (or `shadow-sm`), r24, pad 24 (mobile 16–20), gap 16.
**Page (web app)**: canvas `bg-secondary`. Top bar 64 + sidebar 300 on `bg-primary`. Content padding 32,
card grid gap 24.
**Mobile app screen**: canvas `bg-secondary` or `bg-primary`, 20 side margin, screen title `display-xs/SemiBold`,
cards r24, primary CTA = full-width **lg** Brand button (48h) pinned above the safe area.
**Money amounts (VN)**: `12.000.000đ` or `12.000.000 ₫`, with a dot as the thousands separator. Use tabular figures
(`font-variant-numeric: tabular-nums`) in tables.
**Empty state**: icon (Duotone Brand style, 48–64), `text-lg/SemiBold` title, `text-sm` `text-secondary` description,
one Brand button. A Newsreader italic word is allowed here.

## Working inside Figma

When creating designs in the Figma file (Figma MCP / figma-console / plugin API):
1. Search and **instantiate library components**. Don't redraw buttons or inputs. Set variant
   properties (`Size`, `Type`, `State`), toggle booleans and swap icon instances.
2. **Bind variables** for every fill, stroke, spacing, padding, radius and gap
   (`setBoundVariable` / `setBoundVariableForPaint`). Apply **text styles** (`textStyleId`) rather than
   raw font settings, and effect styles for shadows.
3. Use auto layout with token spacing, and frames named semantically.
4. For dark mode, set the frame's variable mode for the `1. Color modes` collection to **Dark mode**. Don't
   repaint.
5. Screenshot and verify (alignment, spacing, contrast) before finishing.
