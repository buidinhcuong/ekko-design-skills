# Icons

The Figma library ships **4,500+ icon component sets** across 60 categories (Arrows, Business,
Communications, Editing, Users, Security, Crypto, AI, Weather…). Names and styles match
**Hugeicons** 1:1 (e.g. `chevron-down-01`, `search-02`, `user-add-01`, `ai-beautify`).

## Styles

Each icon has 6 variants (`Style=` property):

| Style | Look | Use |
|---|---|---|
| **Stroke** | 1.5px outline, rounded | **Default for UI**: nav, buttons, inputs, lists |
| Solid | filled | Selected/active nav item, small sizes where outline gets weak |
| Bulk | filled with a lighter secondary layer | Feature tiles, larger decorative icons |
| Duotone | outline + tinted fill | Illustrative spots, empty states |
| Twotone | outline with a second-tone stroke | Rare. Marketing/illustration |
| **Duotone Brand** | duotone in Payday Blue tones | Brand moments: onboarding, empty states, feature highlights |

The **Color Icon** category (60 sets, `Color=Blue/Jade/Lime`) holds multi-color illustrative icons (QR Code,
Lucky draw, Wallet-like "Bag", Chart, Calendar…) for marketing and promo surfaces.

Don't mix Stroke and Solid in the same group except for the selected/unselected pair.

## Size and color

- Grid 24×24 (Figma default). Use **20** inside sm/md buttons, inputs and sidebar items, **24** for standalone
  and lg/xl buttons, **16** in badges/chips and dense tables, and **32–64** for feature/empty-state icons.
- Color with tokens only: `icon-primary` (default), `icon-secondary` (supporting, input icons),
  `icon-highlight` (active/brand, which becomes Lime in dark mode), `icon-on-highlight` (on brand fills), white on
  brand buttons, and status colors for status icons.
- Icon-only buttons need an accessible label (`aria-label`) and a tooltip on desktop.

## Finding an icon

Search `assets/tokens/icons.tsv` (columns: name, category, styles, keywords):

```bash
grep -i "wallet" assets/tokens/icons.tsv | cut -f1,2
grep -iP "\tSecurity\t" assets/tokens/icons.tsv | cut -f1 | head
```

Keywords are in English. Translate Vietnamese concepts first (lương → salary/money, rút tiền → withdraw,
thông báo → notification).

Common picks for Ekko (verify that they exist with grep):
home-01 · wallet-01 · money-send-01 · money-receive-01 · credit-card · bank · calendar-03 ·
notification-01 · user · user-group · settings-01 · search-01 · shield-01 · lock · qr-code ·
chart-line-data-01 · invoice-01 · customer-support · arrow-right-02 · chevron-down-01 · cancel-01 ·
tick-02 · plus-sign · information-circle · alert-02.

## Using icons in code

- **Hugeicons packages** (recommended): `@hugeicons/react` + `@hugeicons/core-free-icons` gives the
  Stroke (rounded) style for free. Solid/Bulk/Duotone/Twotone need Hugeicons Pro.
  ```jsx
  import { HugeiconsIcon } from '@hugeicons/react';
  import { Wallet01Icon } from '@hugeicons/core-free-icons';
  <HugeiconsIcon icon={Wallet01Icon} size={24} color="currentColor" strokeWidth={1.5} />
  ```
  Package names are PascalCase + `Icon` (`chevron-down-01` → `ChevronDown01Icon`).
- **Ready-made SVGs:** `assets/icons/` has 14 common Stroke icons (home-01, wallet-01, user-group,
  settings-01, notification-01, search-01, plus-sign, chevron-down-01, arrow-right-02, money-send-01,
  chart-line-data-01, information-circle, tick-02, cancel-01) using `currentColor`, plus `_sprite.svg` with
  `<symbol id="i-<name>">` for inline `<use href="#i-home-01"/>`.
- **No package available** (static HTML, slides): export the SVG from Figma (the component
  `<name>` → `Style=Stroke`). In HTML set `stroke="currentColor"` so the token color applies.
- Never substitute a different icon family (Material, Lucide, Font Awesome) in Ekko product UI. If an icon
  truly doesn't exist, pick the closest Hugeicons match and mention it.

## Figma

Instantiate the icon component and set `Style`. Swap icons inside components through their
`❖ Icon` instance-swap properties instead of detaching.
