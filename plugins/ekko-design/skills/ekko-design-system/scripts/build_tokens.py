#!/usr/bin/env python3
"""Build code-ready token files from assets/tokens/tokens.json.

tokens.json is exported straight from Figma by scripts/export-figma.js and is
the single source of truth. Never hand-edit the generated files — edit Figma,
re-export, then run:

    python3 scripts/build_tokens.py

Outputs (relative to the skill folder):
    assets/tokens/ekko-tokens.css       CSS custom properties, light + dark
    assets/tokens/tailwind-theme.css    Tailwind v4 (@theme + @utility)
    assets/tokens/tailwind.preset.cjs   Tailwind v3 preset
    assets/tokens/icons.tsv             grep-friendly icon index
    references/tokens.md                every token value as tables
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "assets" / "tokens"
REFS = ROOT / "references"

data = json.loads((TOKENS / "tokens.json").read_text(encoding="utf-8"))
cols = data["collections"]
meta = data["meta"]

HEADER = (
    f"Generated from Figma \"{meta['source']}\" (export {meta['exportedAt'][:10]}). "
    "DO NOT EDIT — run scripts/build_tokens.py"
)

# ---------------------------------------------------------------------------
# Naming: Figma variable name -> CSS custom property name
# ---------------------------------------------------------------------------
PRIMITIVE_PREFIX = {
    "Base": "base",
    "Ekko": "ekko",
    "Grey": "grey",
    "Brand - Payday Blue": "payday-blue",
    "Brand - Lime": "lime",
    "Brand - Jade": "jade",
    "Success": "success",
    "Warning": "warning",
    "Error": "error",
    "White": "white",
    "Black": "black",
    "Secondary colors": "secondary",
}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def css_name(collection, name):
    parts = name.split("/")
    if collection == "Primitives":
        group, leaf = parts[0], parts[-1]
        if group in ("Spacing", "Radius"):
            return slug(leaf)  # spacing-16, radius-12
        return f"{PRIMITIVE_PREFIX.get(group, slug(group))}-{slug(leaf)}"
    if collection == "1. Color modes":
        leaf = parts[-1].replace("graident", "gradient")  # fix Figma typo
        if parts[0] == "Border" and leaf.startswith("gradient"):
            return f"border-{leaf}"
        return slug(leaf)  # text-primary, bg-brand-500, icon-primary, alpha-10
    if collection == "2. Typography":
        group, leaf = parts[0], parts[-1]
        if group == "Font family":
            return leaf.replace("font-family-", "font-")
        if group == "Font weight":
            return None  # emitted as numeric weights below
        if group == "Font size":
            return f"font-size-{leaf}"
        if group == "Line height":
            return f"line-height-{leaf}"
    if collection in ("3. Spacing", "4. Radius"):
        return slug(parts[-1])
    return slug(name)


# ---------------------------------------------------------------------------
# Alias resolution
# ---------------------------------------------------------------------------
ALIAS = re.compile(r"^\{(.+?)::(.+)\}$")


def mode_index(collection, mode):
    modes = cols[collection]["modes"]
    return modes.index(mode) if mode in modes else 0


def resolve(value, mode_idx=0):
    """Follow aliases to a literal. mode_idx picks Light(0)/Dark(1) in each hop."""
    seen = 0
    while isinstance(value, str) and ALIAS.match(value) and seen < 10:
        c, n = ALIAS.match(value).groups()
        var = cols[c]["variables"][n]
        modes = cols[c]["modes"]
        value = var["values"][modes[min(mode_idx, len(modes) - 1)]]
        seen += 1
    return value


def as_var_ref(value):
    m = ALIAS.match(value) if isinstance(value, str) else None
    if not m:
        return None
    return f"var(--{css_name(*m.groups())})"


def px(v):
    if isinstance(v, (int, float)):
        return "9999px" if v >= 9999 else f"{v:g}px"
    return v


# ---------------------------------------------------------------------------
# Collect token sets
# ---------------------------------------------------------------------------
prim = cols["Primitives"]["variables"]
sem = cols["1. Color modes"]["variables"]
typo = cols["2. Typography"]["variables"]

prim_colors = [(n, v) for n, v in prim.items() if v["type"] == "COLOR"]
spacing = [(n, resolve(v["values"]["Mode 1"])) for n, v in cols["3. Spacing"]["variables"].items()]
radius = [(n, v["values"]["Mode 1"]) for n, v in cols["4. Radius"]["variables"].items()]

FONT_PRIMARY = "'Bricolage Grotesque', system-ui, -apple-system, 'Segoe UI', sans-serif"
FONT_SECONDARY = "'Newsreader', Georgia, 'Times New Roman', serif"

WEIGHTS = {"Light": 300, "Regular": 400, "Medium": 500, "SemiBold": 600, "Bold": 700}

SIZE_KEYS = [n.split("/")[-1] for n in typo if n.startswith("Font size/")]
type_scale = []
for key in SIZE_KEYS:
    fs = typo[f"Font size/{key}"]["values"]
    lh = typo[f"Line height/{key}"]["values"]
    type_scale.append((key, fs["Desktop"], lh["Desktop"], fs["Mobile"], lh["Mobile"]))


def shadow_css(effects):
    parts = []
    for e in effects:
        inset = "inset " if e["type"] == "INNER_SHADOW" else ""
        parts.append(f"{inset}{e['x']:g}px {e['y']:g}px {e['blur']:g}px {e['spread']:g}px {e['color']}")
    # Figma lists effects bottom-up; CSS paints the first shadow on top.
    return ", ".join(reversed(parts))


def gradient_css(g):
    stops = ", ".join(f"{c} {p}%" for c, p in g["stops"])
    return f"linear-gradient(90deg, {stops})"


effects = [(e["name"], slug(e["name"].split("/")[-1]), shadow_css(e["effects"])) for e in data["effectStyles"]]
gradients = [(g["name"], "gradient-" + slug(g["name"].split("/")[-1]), gradient_css(g)) for g in data["gradients"]]

# ---------------------------------------------------------------------------
# ekko-tokens.css
# ---------------------------------------------------------------------------
L = []
w = L.append
w(f"/* {HEADER} */")
w("@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Newsreader:ital,opsz,wght@1,6..72,300..600&display=swap');")
w("")
w(":root {")
w("  /* ---- Primitive colors ---- */")
for n, v in prim_colors:
    w(f"  --{css_name('Primitives', n)}: {v['values']['Light']};")
w("")
w("  /* ---- Semantic colors (light) ---- */")
for n, v in sem.items():
    val = v["values"]["Light mode"]
    w(f"  --{css_name('1. Color modes', n)}: {as_var_ref(val) or val};")
w("")
w("  /* ---- Typography ---- */")
w(f"  --font-primary: {FONT_PRIMARY};")
w(f"  --font-secondary: {FONT_SECONDARY};")
for name, wt in WEIGHTS.items():
    w(f"  --font-weight-{slug(name)}: {wt};")
for key, fs, lh, _, _ in type_scale:
    w(f"  --font-size-{key}: {px(fs)};")
    w(f"  --line-height-{key}: {px(lh)};")
w("")
w("  /* ---- Spacing ---- */")
for n, v in spacing:
    w(f"  --{slug(n)}: {px(v)};")
w("")
w("  /* ---- Radius ---- */")
for n, v in radius:
    w(f"  --{slug(n)}: {px(v)};")
w("")
w("  /* ---- Effects ---- */")
for _, name, css in effects:
    w(f"  --{name}: {css};")
w("")
w("  /* ---- Gradients ---- */")
for _, name, css in gradients:
    w(f"  --{name}: {css};")
w("}")
w("")

dark_lines = []
for n, v in prim_colors:
    if v["values"]["Dark"] != v["values"]["Light"]:
        dark_lines.append(f"  --{css_name('Primitives', n)}: {v['values']['Dark']};")
for n, v in sem.items():
    if v["values"]["Dark mode"] != v["values"]["Light mode"]:
        val = v["values"]["Dark mode"]
        dark_lines.append(f"  --{css_name('1. Color modes', n)}: {as_var_ref(val) or val};")
dark_body = "\n".join(dark_lines)

w("/* Dark mode: follows the OS unless data-theme=\"light\" is set; force with data-theme=\"dark\". */")
w("@media (prefers-color-scheme: dark) {")
w("  :root:not([data-theme=\"light\"]) {")
w("\n".join("  " + line for line in dark_lines))
w("    color-scheme: dark;")
w("  }")
w("}")
w(":root[data-theme=\"dark\"], .theme-dark {")
w(dark_body)
w("  color-scheme: dark;")
w("}")
w("")
w("/* Mobile type scale (Figma mode \"Mobile\") */")
w("@media (max-width: 767px) {")
w("  :root {")
for key, fs, lh, mfs, mlh in type_scale:
    if (fs, lh) != (mfs, mlh):
        w(f"    --font-size-{key}: {px(mfs)};")
        w(f"    --line-height-{key}: {px(mlh)};")
w("  }")
w("}")
w("")
w("/* ---- Base ---- */")
w("body {")
w("  font-family: var(--font-primary);")
w("  font-size: var(--font-size-text-md);")
w("  line-height: var(--line-height-text-md);")
w("  color: var(--text-primary);")
w("  background: var(--bg-primary);")
w("}")
w("")
w("/* ---- Text style classes: .ekko-<size> + weight modifier, e.g. class=\"ekko-display-lg ekko-medium\" ---- */")
for key, *_ in type_scale:
    w(f".ekko-{key} {{ font-size: var(--font-size-{key}); line-height: var(--line-height-{key}); }}")
for name, wt in WEIGHTS.items():
    if name == "Bold":
        continue
    w(f".ekko-{slug(name)} {{ font-weight: {wt}; }}")
w(".ekko-italic { font-family: var(--font-secondary); font-style: italic; }")
w("")
(TOKENS / "ekko-tokens.css").write_text("\n".join(L) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# Tailwind v4 theme
# ---------------------------------------------------------------------------
T = []
t = T.append
t(f"/* {HEADER} */")
t("/* Usage:  @import \"tailwindcss\";  @import \"./tailwind-theme.css\"; */")
t("@import \"./ekko-tokens.css\";")
t("")
t("@theme inline {")
t(f"  --font-primary: {FONT_PRIMARY};")
t(f"  --font-secondary: {FONT_SECONDARY};")
t("  --font-sans: var(--font-primary);")
t("  --font-serif: var(--font-secondary);")
for n, v in prim_colors:
    t(f"  --color-{css_name('Primitives', n)}: {v['values']['Light']};")
for key, fs, lh, _, _ in type_scale:
    name = key if key.startswith("display") else key.replace("text-", "")
    t(f"  --text-{name}: var(--font-size-{key});")
    t(f"  --text-{name}--line-height: var(--line-height-{key});")
for n, v in radius:
    t(f"  --radius-{slug(n).replace('radius-', '')}: {px(v)};")
for _, name, css in effects:
    if name.startswith("shadow-"):
        t(f"  --{name}: {css};")
t("}")
t("")
t("/* Semantic colors switch automatically with light/dark — prefer these over primitives. */")
for n in sem:
    cn = css_name("1. Color modes", n)
    group = n.split("/")[0]
    if group == "Text color":
        t(f"@utility {cn} {{ color: var(--{cn}); }}")
    elif group == "Foreground":
        t(f"@utility {cn} {{ color: var(--{cn}); }}")
    elif group == "Background":
        t(f"@utility {cn} {{ background-color: var(--{cn}); }}")
    elif group == "Border":
        t(f"@utility {cn} {{ border-color: var(--{cn}); }}")
    elif group == "Unity":
        t(f"@utility bg-{cn} {{ background-color: var(--{cn}); }}")
for _, name, css in effects:
    if not name.startswith("shadow-"):
        t(f"@utility {name} {{ box-shadow: var(--{name}); }}")
for _, name, css in gradients:
    t(f"@utility bg-{name} {{ background-image: var(--{name}); }}")
(TOKENS / "tailwind-theme.css").write_text("\n".join(T) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# Tailwind v3 preset
# ---------------------------------------------------------------------------
def js_obj(d, indent=6):
    pad = " " * indent
    return "{\n" + "".join(f"{pad}'{k}': {json.dumps(v)},\n" for k, v in d.items()) + " " * (indent - 2) + "}"


text_colors, bg_colors, border_colors = {}, {}, {}
for n in sem:
    cn = css_name("1. Color modes", n)
    group = n.split("/")[0]
    ref = f"var(--{cn})"
    if group in ("Text color", "Foreground"):
        text_colors[cn.replace("text-", "", 1)] = ref
    elif group == "Background":
        bg_colors[cn.replace("bg-", "", 1)] = ref
    elif group == "Border":
        border_colors[cn.replace("border-", "", 1)] = ref
    elif group == "Unity":
        bg_colors[cn] = ref

font_sizes = {}
for key, *_ in type_scale:
    name = key if key.startswith("display") else key.replace("text-", "")
    font_sizes[name] = [f"var(--font-size-{key})", {"lineHeight": f"var(--line-height-{key})"}]

P = [
    f"// {HEADER}",
    "// Usage: tailwind.config.js -> presets: [require('./tailwind.preset.cjs')]",
    "// and import ekko-tokens.css once in your global stylesheet.",
    "module.exports = {",
    "  darkMode: ['class', '[data-theme=\"dark\"]'],",
    "  theme: {",
    "    extend: {",
    "      fontFamily: { primary: ['var(--font-primary)'], secondary: ['var(--font-secondary)'], sans: ['var(--font-primary)'], serif: ['var(--font-secondary)'] },",
    "      colors: " + js_obj({css_name('Primitives', n): v['values']['Light'] for n, v in prim_colors}),
    "      textColor: " + js_obj(text_colors),
    "      backgroundColor: " + js_obj(bg_colors),
    "      borderColor: " + js_obj(border_colors),
    "      fontSize: " + js_obj(font_sizes),
    "      borderRadius: " + js_obj({slug(n).replace("radius-", ""): px(v) for n, v in radius}),
    "      boxShadow: " + js_obj({name: css for _, name, css in effects}),
    "      backgroundImage: " + js_obj({name: css for _, name, css in gradients}),
    "    },",
    "  },",
    "};",
]
(TOKENS / "tailwind.preset.cjs").write_text("\n".join(P) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# icons.tsv
# ---------------------------------------------------------------------------
icons_path = TOKENS / "icons.json"
if icons_path.exists():
    icons = json.loads(icons_path.read_text(encoding="utf-8"))["icons"]
    rows = ["name\tcategory\tstyles\ttags"]
    for i in icons:
        rows.append("\t".join([i["name"], i["category"], "/".join(i["styles"]), i["tags"].replace("\t", " ").replace("\n", " ")]))
    (TOKENS / "icons.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# references/tokens.md
# ---------------------------------------------------------------------------
M = []
m = M.append
m("# Ekko DS — full token tables")
m("")
m(f"> {HEADER}")
m("")
m("Figma name → CSS variable → value. Semantic tokens are what you should use in")
m("designs; primitives exist so semantic tokens have something to point at.")
m("")
m("## Semantic colors (use these)")
m("")
m("| Figma token | CSS var | Light | Dark |")
m("|---|---|---|---|")
for n, v in sem.items():
    cn = css_name("1. Color modes", n)
    lv, dv = v["values"]["Light mode"], v["values"]["Dark mode"]
    def show(val, idx):
        lit = resolve(val, idx)
        ref = ALIAS.match(val).group(2) if isinstance(val, str) and ALIAS.match(val) else None
        return f"`{lit}` ({ref})" if ref else f"`{lit}`"
    m(f"| {n} | `--{cn}` | {show(lv, 0)} | {show(dv, 1)} |")
m("")
m("## Primitive colors")
m("")
m("| Figma token | CSS var | Value | Dark override |")
m("|---|---|---|---|")
for n, v in prim_colors:
    lv, dv = v["values"]["Light"], v["values"]["Dark"]
    m(f"| {n} | `--{css_name('Primitives', n)}` | `{lv}` | {'`' + dv + '`' if dv != lv else ''} |")
m("")
m("## Type scale")
m("")
m("| Token | Desktop size / line-height | Mobile size / line-height | CSS vars |")
m("|---|---|---|---|")
for key, fs, lh, mfs, mlh in type_scale:
    m(f"| {key} | {fs}/{lh} | {mfs}/{mlh} | `--font-size-{key}` `--line-height-{key}` |")
m("")
m("Text styles in Figma are named `<size>/<weight>`, e.g. `text-sm/Medium`, `display-lg/SemiBold`.")
m("Weights Light/Regular/Medium/SemiBold use **Bricolage Grotesque**; the Italic variants")
m("(`Light Italic`, `Italic`, `Medium Italic`, `SemiBold Italic`) use **Newsreader**. Letter spacing is 0 everywhere.")
m("")
m("## Spacing")
m("")
m("| Token | Value |")
m("|---|---|")
for n, v in spacing:
    m(f"| `{slug(n)}` | {px(v)} |")
m("")
m("## Radius")
m("")
m("| Token | Value |")
m("|---|---|")
for n, v in radius:
    m(f"| `{slug(n)}` | {px(v)} |")
m("")
m("## Shadows, focus rings, skeuomorphic")
m("")
m("| Figma style | CSS var | box-shadow |")
m("|---|---|---|")
for n, name, css in effects:
    m(f"| {n} | `--{name}` | `{css}` |")
m("")
m("## Gradients")
m("")
m("| Figma style | CSS var | Value |")
m("|---|---|---|")
for n, name, css in gradients:
    m(f"| {n} | `--{name}` | `{css}` |")
m("")
m("## Layout grids")
m("")
m("| Style | Columns | Gutter | Margin |")
m("|---|---|---|---|")
for g in data["grids"]:
    gg = g["grids"][0]
    m(f"| {g['name']} | {gg['count']} | {gg['gutter']}px | {gg['margin']}px |")
m("")
(REFS / "tokens.md").write_text("\n".join(M) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# references/component-inventory.md
# ---------------------------------------------------------------------------
C = []
c = C.append
c("# Component inventory")
c("")
c(f"> {HEADER}")
c("")
c("Every component set in the Figma library with its properties. Variant options are")
c("separated by `/`; BOOLEAN, TEXT and INSTANCE_SWAP are toggles, text and icon slots.")
c("`key` is the Figma component-set key (use it with `importComponentSetByKeyAsync`).")
c("")
current_page = None
for comp in data["components"]:
    if comp["page"] != current_page:
        current_page = comp["page"]
        c("")
        c(f"## {current_page}")
        c("")
    props = "; ".join(
        f"**{k or 'Count'}**: {'/'.join(v) if isinstance(v, list) else v}" for k, v in comp["properties"].items()
    )
    c(f"- **{comp['name']}**: {props or '(no properties)'}  ")
    c(f"  `key: {comp['key']}`")
c("")
(REFS / "component-inventory.md").write_text("\n".join(C) + "\n", encoding="utf-8")

print("Built:", ", ".join(p.name for p in [TOKENS / "ekko-tokens.css", TOKENS / "tailwind-theme.css", TOKENS / "tailwind.preset.cjs", TOKENS / "icons.tsv", REFS / "tokens.md", REFS / "component-inventory.md"]))
