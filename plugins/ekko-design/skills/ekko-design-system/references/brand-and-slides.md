# Brand and slides

From the **Brand Guideline v2.0** pages inside the same Figma file (Band Identity page, updated Mar 2026).
Use this for slides, pitch decks, one-pagers, social posts, posters and any marketing piece.

> **The colors here supersede the older Brand Guidelines v1** (which listed `#3C51CD`, `#CDF836`,
> `#0F0F36`, `#CAE4E2`). The canonical values are the ones in the DS variables and logo SVGs:
> Payday Blue `#3E58F1`, Lime `#B3F42C`, Midnight `#00034F`, Jade `#AEDFDA`.

## Brand foundation

- **What Ekko is:** financial wellness and inclusive fintech that paves the way for the *future of prosperity*.
  The product is Earned/Early Wage Access (EWA): workers access pay they've already earned instead of
  waiting for payday.
- **Who for:** first the hardworking Vietnamese workforce (frontline, factory, construction, delivery,
  office), then the enterprises that employ them. B2B2C.
- **Purpose:** technology for good that democratizes financial services.
- **Mission:** Ekko exists to *make everyday count*. Break the cycle of living paycheck-to-paycheck.
  "Make every day, pay."
- **Vision:** Boosting financial wellness and nurturing prosperous workforces across South-East Asian enterprises.
- **What makes us different:** Humanity through Inclusion · Security and Data Protection · Product Flexibility.
- **Story arc (useful for pitch decks):** Challenge (monthly pay cycles are outdated, and workers fall to
  high-interest lenders) → Solution (tech-enabled EWA, pay that flows like life does) → Result (a happier
  workforce, lower turnover, everybody wins).

## Voice and tone

The voice is an optimistic, determined fighter who isn't afraid of a challenge for the greater good. It cuts through
the convolution of old-school finance and speaks for the worker.

| Be | …but not |
|---|---|
| Optimistic | naive |
| Visionary | arrogant |
| Ambitious | stubborn |
| Charismatic | inauthentic |

- Plain, warm, active and forward-moving. No finance jargon, hedging or corporate stiffness.
- Flow/water metaphors fit naturally: ride the waves, go with the flow, ebbs and flows, stay afloat.
- Worker-facing copy is warm and personal. Employer-facing (B2B) copy focuses on outcomes: retention,
  turnover, wellbeing, productivity.
- Vietnamese copy uses the same spirit: simple, positive, with no stiff bureaucratic tone ("Có Ekko là Ok!").

**Taglines and lines:** *Make everyone count.* · *Make everyday count.* · Break the cycle of living
paycheck-to-paycheck. · Our business is to *make pay-day history.* · Work today. Get paid today. ·
Your Salary. When You Need It. · Early Access to Your *Pay.* · Simple. Secure. Instant. · Don't wait for payday.

**Hashtags:** #OnDemandPay #MoneyMatters #FinancialWellbeing #EarnedWageAccess #CashFlowFreedom
#PlanYourMoney #ForWorkers #EmpowerEmployees #PayFlexibly #WorkSmartEarnSmart #SalaryAdvance
#FinancialApp #SaveBetter #FinancialEducation #MoneyTips #BetterWorkLife

## Logo

Files in `assets/logos/` (SVG, transparent):

| File | What | When |
|---|---|---|
| `ekko-primary-<color>.svg` | Wordmark "ekko" with the K-Wave tail on the o | **First choice** for all communications |
| `ekko-secondary-<color>.svg` | Cephalopod symbol + wordmark | When more brand presence is needed |
| `ekko-symbol-<color>.svg` | Symbol alone (8-arm "cephalopod" asterisk) | Slide headers, avatars, favicons, app icon, small spaces |
| `ekko-wordmark-k-wave-payday-blue.svg` | Wordmark with extended K-Wave tail | Hero/brand moments |

Colors: `payday-blue`, `midnight` (Figma calls it "Beyond Blue"), `lime` ("Fluorescent"), `jade` ("Amicable Jade").

| Background | Logo color |
|---|---|
| White / light grey | Payday Blue (default) or Midnight |
| Jade | Payday Blue or Midnight |
| Payday Blue | White* or Lime |
| Midnight / Black `#1B1C1D` | Lime, Jade or White* |
| Photography | White* on calm areas, or Payday Blue on light photos |

*White isn't in the SVG set. Recolor the SVG `fill` to `#FFFFFF`. That's the only allowed recolor
(it's used on photos in the guideline).

**Clear space:** keep at least the height of the "k" ascender (≈ ⅓ of the logo height) empty on all sides.
**Minimum size:** primary logo 80px wide on screen. Below that use the symbol (≥ 24px).

**Don't:** set the logo in secondary colors · use multiple colors in one logo · angle or rotate it · rotate
the symbol · change the symbol/wordmark positions · pair the symbol with another typeface · add outlines,
shadows or effects · stretch it · re-type "ekko" in a font.

Partner lockup: Ekko logo + thin vertical divider + partner logo, both optically the same height.
Tagline lockup: logo with "Ekko exists to make everyday count." beside or below it.

## The K-Wave

The K-Wave is Ekko's visual expression of its FLOW state. It's a continuous, looping line that grows from
the logo's tail and is "used to dynamically populate content by connecting, stretching, and expanding."

Assets in `assets/k-wave/`:
- `k-wave-line-payday-blue.svg`: a thin looping line, used across photos and over card tops.
- `k-wave-loop-jade.svg` and `k-wave-s-jade.svg`: **thick ribbon** shapes (Jade-300 tone on a Jade background)
  for background panels.

How to use it:
- Use **one** wave per layout. It should feel effortless and unbroken, entering and exiting off the edges.
- Thick-ribbon backgrounds: a slightly darker tone of the panel color (Jade on Jade, `payday-blue-400` on
  Payday Blue, Payday Blue on Midnight). Text sits on top in Midnight or White with ≥ 4.5:1 contrast.
- Thin line: Payday Blue over photos/white, or Lime over Midnight/Payday Blue.
- **Line text:** a short brand phrase set along the wave path, for marketing/social only.
- Recolor the SVG fill to the needed brand color. Scale and crop freely, but never distort, skew or
  break the curve.

## Photography

Real Vietnamese workers (construction, factory, logistics, retail, office) shown with dignity: mid-work,
proud, or using the phone app, in natural light. Combine photos with a Payday Blue K-Wave or Jade panels.
Avoid generic Western-office stock and staged handshakes.

## Slide master (1920 × 1080)

Measured from the guideline pages. Scale proportionally for other sizes (1280×720 → ×0.667).

```
┌──────────────────────────────────────────────────────────────── 1920 ─┐
│ 56                                                                     │
│ [symbol 54]  Deck name   Date      Section    Subsection         07   │ ← header row y=56, h=54
│             x=174        x=430     x=686      x=942          right=1864│   20/26 Light
│                                                                        │
│                         CONTENT AREA                                   │
│                  x 56 → 1864 (1808 wide), y 170 → 1024                 │
│                                                                        │
│ Section title (60/68 Medium)            Body / description (24/32)    │ ← y≈956, bottom-aligned
└────────────────────────────────────────────────────────────── 1080 ───┘
```

- **Margins:** 56 on all sides. **Header row:** symbol logo (54px) at x=56. Meta labels at x=174, 430, 686,
  942 (256px apart, 192 wide) in **Bricolage Light 20/26**: deck name (can be Bold on the cover), date,
  section, subsection. Page number right-aligned at the right margin.
- **Header color:** Midnight `#00034F` on light backgrounds, White on dark/photo.
- **Footer-style titles:** the slide title often sits **bottom-left** (y≈956, Medium 60/68) with the description
  paragraph bottom-right (x≈823 or 976, 24/32 Regular/Light). It's an editorial, magazine-like rhythm.
- **Columns:** 3 columns of 581 with 32 gaps (x = 56 / 669 / 1282), or 2 columns of 889 with a 30 gap (x = 56 / 975).
- **Cards/media panels:** radius **48**, full column width, height ≈ 693 (y 171 → 864).

### Type for slides

| Element | Spec |
|---|---|
| Cover title | Bricolage **Regular 128px**, line-height 1.2, 2 lines max, bottom-left |
| Statement | Regular/Medium **128px**, centered or left, one phrase in **Newsreader Italic** Payday Blue |
| Slide title | **Medium 60/68** (or 64) |
| Column heading | **Medium 48/56** |
| Big number / KPI | Medium/SemiBold 96–128 |
| Body | **Regular or Light 24/32** (min 20px when projecting) |
| Meta / labels | Light 20/26. Uppercase Medium 20/30 for colophon blocks (VERSION 2.0 · LAST UPDATED) |

### Backgrounds (pick one per slide)

| Background | Text | Accent | Mood |
|---|---|---|---|
| White `#FFFFFF` | `#1B1C1D` / Midnight | Payday Blue italic | Default content slides |
| Black `#1B1C1D` | White | Lime | Covers, openers, dramatic |
| Midnight `#00034F` | White | Lime / Jade | Statements, values, closing |
| Payday Blue `#3E58F1` | White | Lime | Section dividers, big claims |
| Jade `#AEDFDA` | Midnight | Payday Blue (large) | Soft K-Wave panels, quotes |
| Full-bleed photo | White | Payday Blue K-Wave line | Applications, human stories |

Keep a deck mostly White with 1 in 4 or 5 slides on a dark/brand background for rhythm.

### Slide archetypes

1. **Cover**: Black or Midnight. Header row in white. Title 128 bottom-left ("Brand / Guideline *for* Ekko"
   style, with a Newsreader italic connector word). Colophon block bottom-right (4 lines, uppercase 20).
2. **Section divider**: big number "01" + section name, Payday Blue or Midnight background, K-Wave line.
3. **Statement**: white background, one 128px sentence centered with an italic Payday Blue phrase, and a
   supporting paragraph bottom-right with a bottom-left label (e.g. "Our Mission").
4. **Three pillars**: Midnight background, 3 columns (48/56 Medium heading + 24/32 body), slide title bottom-left.
5. **Media + text**: 2 cards (r48). Left has the logo/visual on white with a `border-secondary` outline. Right has a photo with
   a K-Wave line + a white 44px statement + logo bottom-right.
6. **Data/KPI**: white background, 3–4 KPI blocks (number 96–128 Medium Payday Blue, label 24 Light), source note 20 Light grey.
   Charts use the brand chart palette from `color-usage.md`.
7. **Product screens**: device mockups of the app on Jade or `bg-secondary`, 1–2 lines of copy.
8. **Closing**: Midnight or Payday Blue, "Thank you!" (Newsreader italic allowed), ekko.vn, contact info.

### Pitch-deck flow (Ekko default)

Cover → Problem (paycheck-to-paycheck cycle, predatory lending) → Solution (EWA via Ekko) → How it works
(3 steps) → Product (app screens) → Market (SEA workforce) → Traction/KPIs → Business model (B2B2C) →
Why Ekko (Inclusion · Security · Flexibility) → Team → Ask/Roadmap → Thank you.

## Other formats

- **Social square 1080×1080 / story 1080×1920:** margin 64, symbol top-left, one headline (≥ 72px) with an italic
  emphasis, K-Wave, logo or CTA at the bottom. Payday Blue, Jade or photo backgrounds.
- **Poster / OOH (portrait):** wordmark top-left (Payday Blue or White), big headline in Payday Blue on
  Jade or white over a photo, QR code bottom-right, 2-line subcopy bottom-left (see "Applications" pages).
- **One-pager / report (A4):** white, 48 margin, Bricolage headings (Medium), 11–12pt Light/Regular body,
  Payday Blue for headings/rules, Jade panels for callouts, logo top-left, page numbers in the footer.
- **Email:** 600px column, white card on `bg-secondary`, primary logo 120px, Brand button (lg style).

## Tool notes

- **HTML decks:** start from `assets/templates/slide-template.html`. It's 1920×1080, scales to the viewport and
  uses arrow-key navigation.
- **PowerPoint / Google Slides / Keynote:** set the slide size to 16:9 (1920×1080 px = 13.333×7.5 in). Install
  Bricolage Grotesque + Newsreader from Google Fonts (embed fonts in PPTX when sharing). Recreate the
  header row on the master layout. Insert logos as SVG. Use exact hex values from `tokens.md`.
- **Figma Slides / Figma Design:** use the variables + text styles from the library. The guideline pages use
  a shared `Head` component (from a linked library) for the header row. Duplicate a guideline slide to
  reuse it, or rebuild it to the measurements above.
