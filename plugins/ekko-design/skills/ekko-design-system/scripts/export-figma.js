// Ekko DS — Figma export script
// --------------------------------------------------------------------------
// Exports every variable, style, component set and icon from the
// "[Ekko UI] - Design System" Figma file into ONE JSON object that matches
// assets/tokens/tokens.json.
//
// How to run (pick one):
//   A) Claude Code + figma-console MCP: ask Claude
//        "Chạy scripts/export-figma.js trong Figma và cập nhật tokens.json"
//      Claude passes this file's content to `figma_execute` and writes the
//      returned JSON to assets/tokens/tokens.json (+ icons.json).
//   B) Figma desktop → Plugins → Development → "Open console", wrap this file
//      in `(async () => { ...file... })().then(r => copy(JSON.stringify(r, null, 2)))`
//      then paste the clipboard into assets/tokens/tokens.json.
//
// After updating tokens.json run:  python3 scripts/build_tokens.py
// --------------------------------------------------------------------------

await figma.loadAllPagesAsync();

const hex = (c, a) => {
  const h = (x) => Math.round(x * 255).toString(16).padStart(2, '0');
  const alpha = a !== undefined ? a : c.a;
  return '#' + h(c.r) + h(c.g) + h(c.b) + (alpha !== undefined && alpha < 1 ? h(alpha) : '');
};

// ---- Variables -----------------------------------------------------------
const collections = await figma.variables.getLocalVariableCollectionsAsync();
const variables = await figma.variables.getLocalVariablesAsync();
const varById = Object.fromEntries(variables.map((v) => [v.id, v]));
const colById = Object.fromEntries(collections.map((c) => [c.id, c]));

const fmtValue = (val) => {
  if (val && typeof val === 'object') {
    if (val.type === 'VARIABLE_ALIAS') {
      const target = varById[val.id];
      return target ? `{${colById[target.variableCollectionId].name}::${target.name}}` : null;
    }
    if ('r' in val) return hex(val);
  }
  return val;
};

const outCollections = {};
for (const c of collections) {
  const vars = {};
  for (const id of c.variableIds) {
    const v = varById[id];
    if (!v) continue;
    const values = {};
    for (const m of c.modes) values[m.name] = fmtValue(v.valuesByMode[m.modeId]);
    vars[v.name] = { type: v.resolvedType, values };
    if (v.description) vars[v.name].description = v.description;
  }
  outCollections[c.name] = { modes: c.modes.map((m) => m.name), variables: vars };
}

// ---- Styles --------------------------------------------------------------
const textStyles = (await figma.getLocalTextStylesAsync()).map((s) => ({
  name: s.name,
  fontFamily: s.fontName.family,
  fontStyle: s.fontName.style,
  fontSize: s.fontSize,
  lineHeight: s.lineHeight.unit === 'PIXELS' ? s.lineHeight.value
    : s.lineHeight.unit === 'PERCENT' ? `${s.lineHeight.value}%` : 'auto',
  letterSpacing: s.letterSpacing.unit === 'PERCENT' ? `${s.letterSpacing.value}%` : s.letterSpacing.value,
}));

const effectStyles = (await figma.getLocalEffectStylesAsync()).map((s) => ({
  name: s.name,
  effects: s.effects.filter((e) => e.visible !== false).map((e) => ({
    type: e.type,
    color: e.color ? hex(e.color) : undefined,
    x: e.offset ? e.offset.x : 0,
    y: e.offset ? e.offset.y : 0,
    blur: e.radius,
    spread: e.spread || 0,
  })),
}));

const gradients = (await figma.getLocalPaintStylesAsync())
  .filter((s) => s.paints[0] && s.paints[0].type.startsWith('GRADIENT'))
  .map((s) => ({
    name: s.name,
    type: s.paints[0].type,
    stops: s.paints[0].gradientStops.map((g) => [hex(g.color), Math.round(g.position * 100)]),
  }));

const grids = (await figma.getLocalGridStylesAsync()).map((s) => ({
  name: s.name,
  grids: s.layoutGrids.map((g) => ({ pattern: g.pattern, count: g.count, gutter: g.gutterSize, margin: g.offset, alignment: g.alignment })),
}));

// ---- Components & icons --------------------------------------------------
const components = [];
const icons = [];
for (const page of figma.root.children) {
  const pageName = page.name.replace(/[❖◆]/g, '').trim();
  for (const set of page.findAllWithCriteria({ types: ['COMPONENT_SET'] })) {
    let props = {};
    try {
      for (const [k, v] of Object.entries(set.componentPropertyDefinitions)) {
        props[k.split('#')[0]] = v.type === 'VARIANT' ? v.variantOptions : v.type;
      }
    } catch (e) { props = {}; }
    if (pageName === 'Icons') {
      const category = set.parent && set.parent.type === 'FRAME' ? set.parent.name.trim() : '';
      icons.push({ name: set.name, category, styles: props.Style || props.Color || [], tags: set.description || '' });
    } else if (!set.name.startsWith('_')) {
      components.push({ page: pageName, name: set.name, key: set.key, properties: props, description: set.description || '' });
    }
  }
}

return {
  meta: {
    source: figma.root.name,
    fileKey: figma.fileKey,
    exportedAt: new Date().toISOString(),
  },
  collections: outCollections,
  textStyles,
  effectStyles,
  gradients,
  grids,
  components,
  icons,
};
