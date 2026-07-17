# Portfolio Technical Atlas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the root portfolio with a bird’s-eye technical atlas whose product artifacts communicate Pakawat Smutkun’s real systems, scale, experience, and capabilities.

**Architecture:** Keep the site static and DOM/SVG-first. `index.html` owns semantic content and links, focused SVG files own product artwork, `assets/atlas.css` owns the visual system and responsive behavior, and `assets/atlas.js` adds progressive enhancement without becoming required for navigation or content.

**Tech Stack:** HTML5, CSS, inline-safe SVG assets, vanilla ES modules, Node.js built-in test runner, Python static server, GitHub Pages.

## Global Constraints

- Target only the root portfolio and new root assets; do not restyle linked prototype pages.
- Do not reuse or incrementally modify `op3d.html`.
- No Three.js, WebGL, canvas boot path, animation library, webfont, or external runtime dependency.
- No generic 3D controls, hardware toys, sound effects, fake diagnostics, decorative meters, cursor flashlights, orbit controls, or drag-to-rotate interaction.
- Use a true top-down composition for every product artifact.
- Product flat lays replace text-heavy cards and tables; visible prose is limited to titles, outcomes, metrics, annotations, and actions.
- Preserve factual career content, project links, resume link, email, phone, GitHub, and LinkedIn destinations from the current `index.html`.
- Preserve Q/W/E/R as optional accelerators for Work, Lab, Log, and Spec; native anchor links remain primary.
- Every actionable artifact is a native link with a specific accessible name.
- Touch targets are at least 44px.
- Respect `prefers-reduced-motion`; no continuous animation or idle `requestAnimationFrame`.
- Light and dark modes are intentional; an explicit saved choice overrides system preference.
- The page must work with JavaScript disabled and when an individual SVG asset fails.
- Mobile must have no page-level horizontal overflow.
- Use exact section IDs: `identity`, `work`, `lab`, `log`, `spec`, and `contact`.

## File map

| Path | Responsibility |
| --- | --- |
| `index.html` | Semantic atlas, factual content, links, annotations, and metadata |
| `assets/atlas.css` | Tokens, chassis layout, figure layouts, artifact depth, themes, interaction states, responsive rules, reduced motion |
| `assets/atlas.js` | Theme persistence, Bangkok time, active-section tracking, Q/W/E/R shortcuts |
| `.ui-craft/tokens.md` | Durable primitive, semantic, and component token decisions for future UI work |
| `assets/flatlays/dmms.svg` | DMMS floorplan, reports, field operations, and pipeline product surface |
| `assets/flatlays/affiliate-referral.svg` | Referral attribution and LINE OA surface |
| `assets/flatlays/market-rental.svg` | Stall map and booking calendar surface |
| `assets/flatlays/meal-order.svg` | QR menu and order queue surface |
| `assets/flatlays/performance-results.svg` | 360° review and decision report surface |
| `assets/flatlays/thaimart.svg` | Demand, fulfillment, and supply flywheel surface |
| `assets/flatlays/edusight.svg` | IDE event timeline and learning-support surface |
| `assets/flatlays/experience-dossiers.svg` | Five chronological role dossiers |
| `assets/flatlays/system-architecture.svg` | Frontend, backend, cloud, testing, and AI relationship map |
| `assets/flatlays/contact-baseplate.svg` | Contact and resume channel surface |
| `package.json` | Root test and local-serve commands; no dependencies |
| `tests/atlas-structure.test.mjs` | Required landmarks, content, banned legacy patterns, local assets |
| `tests/atlas-behavior.test.mjs` | Pure behavior functions for theme, shortcuts, and time |
| `tests/flatlay-assets.test.mjs` | SVG dimensions, safety, local-only references, and required artifact files |

---

### Task 1: Establish the dependency-free test harness

**Files:**
- Create: `package.json`
- Create: `tests/atlas-structure.test.mjs`
- Create: `tests/flatlay-assets.test.mjs`

**Interfaces:**
- Consumes: current root `index.html`
- Produces: `npm test`, `assertFlatlayMarkup(file, svg)`, and baseline factual assertions used by every later task

- [ ] **Step 1: Add the root package scripts**

Create `package.json`:

```json
{
  "name": "pakawat-portfolio",
  "private": true,
  "type": "module",
  "scripts": {
    "test": "node --test tests/*.test.mjs",
    "serve": "python3 -m http.server 8000"
  }
}
```

- [ ] **Step 2: Write the baseline atlas structure test**

Create `tests/atlas-structure.test.mjs`:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const html = await readFile(new URL('../index.html', import.meta.url), 'utf8');

test('baseline page contains the factual flagship metrics and primary actions', () => {
  for (const text of ['10 modules', '2,000+ branches', '200+ users']) {
    assert.ok(html.includes(text), `missing ${text}`);
  }
  assert.match(html, /Download resume/i);
  assert.match(html, /mailto:pakawat\.zon@gmail\.com/);
  assert.match(html, /https:\/\/github\.com\/Zonxpk/);
  assert.match(html, /https:\/\/www\.linkedin\.com\/in\/zonpk\//);
});
```

- [ ] **Step 3: Write the reusable flat-lay contract test**

Create `tests/flatlay-assets.test.mjs`:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
export function assertFlatlayMarkup(file, svg) {
  assert.match(svg, /<svg[^>]+viewBox="0 0 800 520"/, `${file} needs the standard viewBox`);
  assert.equal(/<script|https?:\/\/|xlink:href/i.test(svg), false, `${file} contains active or external content`);
  assert.match(svg, /<title(?:\s[^>]*)?>[^<]+<\/title>/, `${file} needs a title`);
}

test('flat-lay contract rejects active external content', () => {
  const unsafe = '<svg viewBox="0 0 800 520"><title>Unsafe</title><script src="https://example.com/x.js"/></svg>';
  assert.throws(() => assertFlatlayMarkup('unsafe.svg', unsafe), /active or external content/);
});
```

- [ ] **Step 4: Run the baseline tests**

Run:

```bash
npm test
```

Expected: both baseline tests pass against the current portfolio.

- [ ] **Step 5: Commit the test harness**

```bash
git add package.json tests/atlas-structure.test.mjs tests/flatlay-assets.test.mjs
git commit -m "test: define portfolio atlas acceptance structure"
```

---

### Task 2: Build the atlas shell and identity figure

**Files:**
- Create: `.ui-craft/tokens.md`
- Create: `assets/atlas.css`
- Create: `assets/flatlays/dmms.svg`
- Modify: `index.html`
- Modify: `tests/atlas-structure.test.mjs`

**Interfaces:**
- Consumes: existing resume, contact, GitHub, and LinkedIn URLs
- Produces: `.utility-strip`, `.module-nav`, `.atlas`, `.figure`, `.artifact`, `.artifact-link`, `.artifact-plate`, `.coordinate-pin`, and the `#identity` figure used by all later tasks

- [ ] **Step 1: Extend the structure test for the identity figure**

Add to `tests/atlas-structure.test.mjs`:

```js
test('identity figure is concise and product-led', () => {
  assert.match(html, /<section[^>]+id=["']identity["'][^>]*>/);
  assert.match(html, /Operations,\s*made legible\./);
  assert.match(html, /assets\/flatlays\/dmms\.svg/);
  assert.match(html, /aria-label=["']View Digital Mall Management System work["']/);
});
```

Add to `tests/flatlay-assets.test.mjs`:

```js
import { readFile } from 'node:fs/promises';

test('DMMS flat lay follows the asset contract', async () => {
  const svg = await readFile(new URL('../assets/flatlays/dmms.svg', import.meta.url), 'utf8');
  assertFlatlayMarkup('dmms.svg', svg);
});
```

- [ ] **Step 2: Run the identity test and verify it fails**

Run:

```bash
node --test --test-name-pattern="identity figure" tests/atlas-structure.test.mjs
```

Expected: the identity assertion fails and the flat-lay test fails with `ENOENT` for `dmms.svg`.

- [ ] **Step 3: Record the approved token spine**

Create `.ui-craft/tokens.md`:

```markdown
# Portfolio atlas tokens

## Primitive

- Neutral: `#fafaf7`, `#f4f4f0`, `#e8e8e3`, `#c8c8c1`, `#595954`, `#181817`
- Figure colors: orange `#ff4d00`, cyan `#00a4c8`, yellow `#f5c400`, green `#3fa435`
- Spacing: 4, 8, 16, 24, 32, 48, 64px
- Type: system geometric sans for display/body; system monospace for labels and data
- Radius: square chassis and plates; circles only for coordinate pins
- Motion: 120ms interaction feedback with `cubic-bezier(.22, 1, .36, 1)`
- Depth: 6px plate edge plus one ambient shadow; all artifacts share one light direction

## Semantic

- Light canvas/chassis/plate: `#e8e8e3` / `#f4f4f0` / `#fafaf7`
- Light primary/secondary text: `#181817` / `#595954`
- Dark canvas/chassis/plate: `#171716` / `#20201e` / `#2a2a27`
- Dark primary/secondary text: `#f1f1eb` / `#b4b4ac`
- Focus: orange in both themes
- Figure coding: Identity and Work orange; Lab cyan; Log yellow; Spec green; Contact orange

## Component

- Utility strip: 44px minimum height, 1px strong rules, sticky
- Module lane: 44px minimum target, text + contrast + 3px active indicator
- Artifact plate: 1px strong outline, 6px physical edge, ambient shadow
- Artifact interaction: link plates lift 5px on hover/focus and compress 1px on press
- Coordinate pin: 14px circle, one per major figure, connected by a 70px rule
- Primary key: orange solid; secondary key: neutral outline

## Constraints

- One active figure color per viewport region
- No gradients, glow, glass, generic hardware controls, or continuous motion
- Reduced motion removes spatial movement and smooth scrolling
- Dark mode uses light edge rings instead of darker shadows where needed
```

- [ ] **Step 4: Create the token spine and atlas shell CSS**

Create `assets/atlas.css` with this initial content:

```css
:root {
  color-scheme: light dark;
  --neutral-0: #fafaf7;
  --neutral-50: #f4f4f0;
  --neutral-100: #e8e8e3;
  --neutral-300: #c8c8c1;
  --neutral-600: #595954;
  --neutral-900: #181817;
  --orange: #ff4d00;
  --cyan: #00a4c8;
  --yellow: #f5c400;
  --green: #3fa435;
  --surface-canvas: var(--neutral-100);
  --surface-chassis: var(--neutral-50);
  --surface-plate: var(--neutral-0);
  --surface-sunken: #deded8;
  --text-primary: var(--neutral-900);
  --text-secondary: var(--neutral-600);
  --border-strong: var(--neutral-900);
  --border-soft: color-mix(in srgb, var(--neutral-900) 20%, transparent);
  --plate-edge: #c9c9c2;
  --focus: var(--orange);
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: 1rem;
  --space-4: 1.5rem;
  --space-5: 2rem;
  --space-6: 3rem;
  --space-7: 4rem;
  --text-xs: .75rem;
  --text-sm: .875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-hero: clamp(2.8rem, 7vw, 5.8rem);
  --font-sans: "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  --motion-fast: 120ms;
  --ease-out: cubic-bezier(.22, 1, .36, 1);
  --z-sticky: 20;
}

[data-theme="dark"] {
  --surface-canvas: #171716;
  --surface-chassis: #20201e;
  --surface-plate: #2a2a27;
  --surface-sunken: #111110;
  --text-primary: #f1f1eb;
  --text-secondary: #b4b4ac;
  --border-strong: #efefe8;
  --border-soft: color-mix(in srgb, #efefe8 22%, transparent);
  --plate-edge: #111110;
  --orange: #e95a22;
  --cyan: #299ab2;
  --yellow: #d5b62b;
  --green: #55a44f;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    --surface-canvas: #171716;
    --surface-chassis: #20201e;
    --surface-plate: #2a2a27;
    --surface-sunken: #111110;
    --text-primary: #f1f1eb;
    --text-secondary: #b4b4ac;
    --border-strong: #efefe8;
    --border-soft: color-mix(in srgb, #efefe8 22%, transparent);
    --plate-edge: #111110;
    --orange: #e95a22;
    --cyan: #299ab2;
    --yellow: #d5b62b;
    --green: #55a44f;
  }
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--surface-canvas);
  color: var(--text-primary);
  font: 400 var(--text-base)/1.5 var(--font-sans);
  -webkit-font-smoothing: antialiased;
}
a { color: inherit; }
img, svg { display: block; max-width: 100%; }
button, a { touch-action: manipulation; }
:focus-visible { outline: 2px solid var(--focus); outline-offset: 3px; }
.mono {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-variant-numeric: tabular-nums;
  letter-spacing: .08em;
}
.skip-link {
  position: fixed;
  left: var(--space-3);
  top: var(--space-3);
  z-index: 100;
  translate: 0 -200%;
  padding: .7rem 1rem;
  background: var(--text-primary);
  color: var(--surface-chassis);
}
.skip-link:focus { translate: 0; }
.chassis {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
  background: var(--surface-chassis);
  border-inline: 1px solid var(--border-strong);
}
.utility-strip {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  display: grid;
  grid-template-columns: 1.5fr 1fr auto;
  min-height: 36px;
  border-bottom: 1px solid var(--border-strong);
  background: var(--surface-chassis);
}
.utility-strip > * {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  min-width: 0;
  padding: .55rem .8rem;
  border-right: 1px solid var(--border-strong);
}
.utility-strip > *:last-child { border-right: 0; }
.theme-toggle {
  min-height: 44px;
  border: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  cursor: pointer;
}
.module-nav {
  position: sticky;
  top: 44px;
  z-index: calc(var(--z-sticky) - 1);
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  overflow-x: auto;
  border-bottom: 1px solid var(--border-strong);
  background: var(--surface-chassis);
}
.module-nav a {
  min-width: 120px;
  min-height: 44px;
  padding: .85rem;
  border-right: 1px solid var(--border-strong);
  text-decoration: none;
}
.module-nav a:last-child { border-right: 0; }
.module-nav a[aria-current="true"] {
  background: color-mix(in srgb, var(--lane-accent) 12%, var(--surface-chassis));
  box-shadow: inset 0 -3px var(--lane-accent);
}
.atlas { display: block; }
.figure {
  --figure-accent: var(--orange);
  display: grid;
  grid-template-columns: 88px minmax(0, 1fr);
  border-bottom: 1px solid var(--border-strong);
  scroll-margin-top: 92px;
}
.figure-rail {
  padding: var(--space-4) .8rem;
  border-right: 1px solid var(--border-strong);
}
.figure-marker {
  width: 14px;
  aspect-ratio: 1;
  margin-bottom: var(--space-2);
  border: 1px solid var(--border-strong);
  background: var(--figure-accent);
}
.figure-body { min-width: 0; padding: clamp(1.25rem, 4vw, 3rem); }
.figure-heading {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}
.figure-heading h2 {
  margin: 0;
  font-size: clamp(1.5rem, 3vw, 2.6rem);
  letter-spacing: -.03em;
  text-wrap: balance;
}
.artifact {
  position: relative;
  display: block;
  min-height: 44px;
  border: 1px solid var(--border-strong);
  background: var(--surface-plate);
  box-shadow: 0 6px 0 var(--plate-edge), 0 12px 24px rgb(20 20 18 / 10%);
  text-decoration: none;
  transition: transform var(--motion-fast) var(--ease-out),
              box-shadow var(--motion-fast) var(--ease-out);
}
@media (hover: hover) and (pointer: fine) {
  .artifact-link:hover {
    transform: translateY(-5px);
    box-shadow: 0 11px 0 var(--plate-edge), 0 18px 28px rgb(20 20 18 / 14%);
  }
}
.artifact-link:focus-visible {
  transform: translateY(-5px);
  box-shadow: 0 11px 0 var(--plate-edge), 0 18px 28px rgb(20 20 18 / 14%);
}
.artifact-link:active {
  transform: translateY(1px);
  box-shadow: 0 3px 0 var(--plate-edge), 0 6px 12px rgb(20 20 18 / 9%);
}
.artifact-art {
  aspect-ratio: 800 / 520;
  overflow: hidden;
  background:
    linear-gradient(var(--border-soft) 1px, transparent 1px),
    linear-gradient(90deg, var(--border-soft) 1px, transparent 1px),
    var(--surface-sunken);
  background-size: 20px 20px;
}
.artifact-art img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  outline: 1px solid rgb(0 0 0 / 10%);
  outline-offset: -1px;
  pointer-events: none;
  user-select: none;
  -webkit-user-drag: none;
}
[data-theme="dark"] .artifact-art img {
  outline-color: rgb(255 255 255 / 10%);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) .artifact-art img {
    outline-color: rgb(255 255 255 / 10%);
  }
}
.coordinate-pin {
  position: absolute;
  z-index: 2;
  right: 8%;
  top: 12%;
  width: 14px;
  aspect-ratio: 1;
  border: 1px solid var(--border-strong);
  border-radius: 50%;
  background: var(--figure-accent);
}
.coordinate-pin::after {
  content: "";
  position: absolute;
  right: 7px;
  top: 6px;
  width: 70px;
  border-top: 1px solid var(--border-strong);
  transform: rotate(-18deg);
  transform-origin: right center;
}
.artifact-copy { padding: var(--space-3); border-top: 1px solid var(--border-strong); }
.artifact-copy strong { display: block; font-size: var(--text-lg); letter-spacing: -.02em; }
.artifact-copy span { color: var(--text-secondary); }
.identity-layout {
  display: grid;
  grid-template-columns: .85fr 1.15fr;
  gap: var(--space-5);
  align-items: center;
}
.identity-copy h1 {
  max-width: 9ch;
  margin: 0 0 var(--space-3);
  font-size: var(--text-hero);
  line-height: .94;
  letter-spacing: -.055em;
  text-wrap: balance;
}
.identity-copy p { max-width: 36ch; color: var(--text-secondary); }
.action-row { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-top: var(--space-4); }
.key {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: .7rem 1rem;
  border: 1px solid var(--border-strong);
  background: var(--surface-plate);
  box-shadow: 0 3px 0 var(--plate-edge);
  font: 700 var(--text-xs) var(--font-mono);
  letter-spacing: .06em;
  text-decoration: none;
}
.key--primary { background: var(--orange); color: #fff; }
.metric-strip {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin-top: var(--space-4);
  border: 1px solid var(--border-strong);
}
.metric { padding: var(--space-3); border-right: 1px solid var(--border-strong); }
.metric:last-child { border-right: 0; }
.metric strong { display: block; font: 700 clamp(1.4rem, 3vw, 2.2rem) var(--font-mono); }
.metric span { color: var(--text-secondary); font-size: var(--text-sm); }
```

- [ ] **Step 5: Create the DMMS flat-lay SVG**

Create `assets/flatlays/dmms.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title desc">
  <title id="title">Digital Mall Management System product surface</title>
  <desc id="desc">Top-down interface showing a floorplan, reports, field activity, and lead pipeline.</desc>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <g stroke="#181817" stroke-width="3">
    <rect x="70" y="58" width="470" height="336" fill="#fafaf7"/>
    <rect x="92" y="84" width="426" height="32" fill="#181817"/>
    <rect x="94" y="142" width="244" height="220" fill="#f4f4f0"/>
    <path d="M94 216h244M176 142v220M258 142v220" fill="none"/>
    <rect x="362" y="142" width="156" height="62" fill="#fff"/>
    <rect x="362" y="222" width="156" height="62" fill="#fff"/>
    <rect x="362" y="302" width="156" height="60" fill="#fff"/>
    <rect x="570" y="112" width="160" height="270" fill="#fafaf7"/>
    <path d="M592 168h116M592 220h86M592 272h104M592 324h72" fill="none"/>
  </g>
  <g fill="#ff4d00"><rect x="106" y="154" width="58" height="50"/><circle cx="590" cy="168" r="8"/></g>
  <g fill="#00a4c8"><rect x="188" y="228" width="58" height="50"/><circle cx="590" cy="220" r="8"/></g>
  <g fill="#f5c400"><rect x="270" y="290" width="56" height="58"/><circle cx="590" cy="272" r="8"/></g>
  <g fill="#3fa435"><circle cx="590" cy="324" r="8"/></g>
  <g fill="#181817" font-family="monospace" font-size="16">
    <text x="108" y="106">DMMS / FLOORPLAN OPERATIONS</text>
    <text x="380" y="180">REPORTS</text>
    <text x="380" y="260">FIELD OPS</text>
    <text x="380" y="340">PIPELINE</text>
    <text x="588" y="142">ACTIVITY</text>
  </g>
</svg>
```

- [ ] **Step 6: Replace the current header and hero with the atlas shell**

In `index.html`:

1. Add `<link rel="stylesheet" href="assets/atlas.css">` immediately after the legacy `</style>` tag so the atlas rules win during the staged migration.
2. Replace the source range beginning at the current skip link and ending after the closing tag of `.stats` with:

```html
<a class="skip-link" href="#main">Skip to content</a>
<div class="chassis">
  <header>
    <div class="utility-strip mono">
      <div><strong>Pakawat&nbsp;Smutkun</strong><span>Product engineer</span></div>
      <div><output id="current-section">00 Identity</output><output id="local-time">ICT</output></div>
      <button class="theme-toggle" id="theme-toggle" type="button" aria-pressed="false" aria-label="Switch to dark theme">
        <span aria-hidden="true">◐</span><span id="theme-label">Light</span>
      </button>
    </div>
    <nav class="module-nav mono" aria-label="Portfolio sections">
      <a href="#identity" style="--lane-accent:var(--orange)" aria-current="true">00 Identity</a>
      <a href="#work" style="--lane-accent:var(--orange)">01 Work</a>
      <a href="#lab" style="--lane-accent:var(--cyan)">02 Lab</a>
      <a href="#log" style="--lane-accent:var(--yellow)">03 Log</a>
      <a href="#spec" style="--lane-accent:var(--green)">04 Spec</a>
    </nav>
  </header>
  <main class="atlas" id="main">
    <section class="figure" id="identity" data-section="00 Identity" style="--figure-accent:var(--orange)">
      <div class="figure-rail mono"><span class="figure-marker" aria-hidden="true"></span>FIG 00</div>
      <div class="figure-body">
        <div class="identity-layout">
          <div class="identity-copy">
            <h1>Operations, made legible.</h1>
            <p>Full-stack product engineer turning complex operations into reliable systems people can act on.</p>
            <div class="action-row">
              <a class="key key--primary" href="https://drive.google.com/uc?export=download&amp;id=1B2tvM8jNeyZd6OBbq5haLpY4j3sO8lss">Download resume</a>
              <a class="key" href="mailto:pakawat.zon@gmail.com">Email Pakawat</a>
            </div>
          </div>
          <a class="artifact artifact-link" href="#work" aria-label="View Digital Mall Management System work">
            <div class="artifact-art"><img src="assets/flatlays/dmms.svg" alt="" width="800" height="520" fetchpriority="high" decoding="sync"></div>
            <span class="coordinate-pin" aria-hidden="true"></span>
            <div class="artifact-copy"><strong>Digital Mall Management System</strong><span>Floorplans · reports · workflows · field teams</span></div>
          </a>
        </div>
        <div class="metric-strip" aria-label="Flagship system scale">
          <p class="metric"><strong>10</strong><span>modules</span></p>
          <p class="metric"><strong>2,000+</strong><span>branches</span></p>
          <p class="metric"><strong>200+</strong><span>users</span></p>
        </div>
      </div>
    </section>
```

During this task, keep the existing Work, Lab, Log, Spec, footer, and their existing closing `</main></div>` tags after the new identity section so every current destination remains available. The replacement range removes the old header, old `<main>` opening tag, old hero, and duplicate metric strip.

- [ ] **Step 7: Run the focused tests**

Run:

```bash
node --test --test-name-pattern="identity figure|factual flagship" tests/atlas-structure.test.mjs
node --test --test-name-pattern="DMMS flat lay" tests/flatlay-assets.test.mjs
```

Expected: both commands pass.

- [ ] **Step 8: Serve and inspect the identity figure**

Run:

```bash
npm run serve
```

Open `http://127.0.0.1:8000/`. Expected: the utility strip, module navigation, identity copy, DMMS overhead surface, and three metrics render without horizontal overflow at 1280px.

- [ ] **Step 9: Commit**

```bash
git add .ui-craft/tokens.md index.html assets/atlas.css assets/flatlays/dmms.svg tests/atlas-structure.test.mjs tests/flatlay-assets.test.mjs
git commit -m "feat: establish portfolio atlas shell and identity"
```

---

### Task 3: Replace Work with product evidence

**Files:**
- Create: `assets/flatlays/affiliate-referral.svg`
- Create: `assets/flatlays/market-rental.svg`
- Create: `assets/flatlays/meal-order.svg`
- Modify: `assets/atlas.css`
- Modify: `index.html`
- Modify: `tests/atlas-structure.test.mjs`

**Interfaces:**
- Consumes: `.figure`, `.artifact-link`, and `.artifact-copy`
- Produces: `.work-layout`, `.secondary-work`, and four complete Work artifacts

- [ ] **Step 1: Add the failing Work assertions**

Add:

```js
test('Work is product-led and keeps all shipped systems', () => {
  for (const asset of ['dmms.svg', 'affiliate-referral.svg', 'market-rental.svg', 'meal-order.svg']) {
    assert.ok(html.includes(`assets/flatlays/${asset}`), `missing ${asset}`);
  }
  for (const project of ['Digital Mall Management System', 'Affiliate Referral System', 'Market Rental Management', 'Meal Order Management']) {
    assert.ok(html.includes(project), `missing ${project}`);
  }
  assert.equal(html.includes('class="secondary"'), false);
  assert.equal(html.includes('class="cap-rows"'), false);
});
```

Add to `tests/flatlay-assets.test.mjs`:

```js
test('Work flat lays follow the asset contract', async () => {
  for (const file of ['affiliate-referral.svg', 'market-rental.svg', 'meal-order.svg']) {
    const svg = await readFile(new URL(`../assets/flatlays/${file}`, import.meta.url), 'utf8');
    assertFlatlayMarkup(file, svg);
  }
});
```

- [ ] **Step 2: Verify the Work tests fail**

Run:

```bash
node --test --test-name-pattern="Work is product-led" tests/atlas-structure.test.mjs
node --test --test-name-pattern="Work flat lays" tests/flatlay-assets.test.mjs
```

Expected: the structure test fails on missing `affiliate-referral.svg` and the asset test fails with `ENOENT`.

- [ ] **Step 3: Create the three secondary Work SVGs**

Create `assets/flatlays/affiliate-referral.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">Affiliate referral attribution surface</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <rect x="82" y="70" width="636" height="360" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <rect x="110" y="98" width="580" height="38" fill="#181817"/>
  <g fill="none" stroke="#181817" stroke-width="3">
    <path d="M190 260h130M380 190h120M380 330h120M560 260h80"/>
    <circle cx="170" cy="260" r="48"/><circle cx="350" cy="190" r="40"/><circle cx="350" cy="330" r="40"/>
    <circle cx="530" cy="190" r="40"/><circle cx="530" cy="330" r="40"/><circle cx="660" cy="260" r="36"/>
  </g>
  <g fill="#3fa435"><circle cx="170" cy="260" r="18"/><circle cx="350" cy="190" r="14"/><circle cx="350" cy="330" r="14"/></g>
  <g fill="#ff4d00"><circle cx="530" cy="190" r="14"/><circle cx="530" cy="330" r="14"/><circle cx="660" cy="260" r="12"/></g>
  <text x="128" y="123" fill="#fafaf7" font-family="monospace" font-size="18">LINE OA / REFERRAL ATTRIBUTION</text>
</svg>
```

Create `assets/flatlays/market-rental.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">Market rental stall map and calendar</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <rect x="66" y="74" width="420" height="360" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <rect x="514" y="104" width="220" height="300" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <g stroke="#181817" stroke-width="3" fill="#f4f4f0">
    <path d="M92 132h366M92 204h366M92 276h366M92 348h366M184 132v288M276 132v288M368 132v288"/>
    <path d="M540 158h168M540 202h168M540 246h168M540 290h168M540 334h168M582 158v220M624 158v220M666 158v220"/>
  </g>
  <g fill="#00a4c8"><rect x="96" y="208" width="84" height="64"/><rect x="280" y="352" width="84" height="64"/></g>
  <g fill="#f5c400"><rect x="188" y="136" width="84" height="64"/><rect x="372" y="280" width="82" height="64"/></g>
  <text x="96" y="112" font-family="monospace" font-size="18">STALL AVAILABILITY</text>
  <text x="540" y="142" font-family="monospace" font-size="18">BOOKING</text>
</svg>
```

Create `assets/flatlays/meal-order.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">Meal order QR menu and operations queue</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <rect x="84" y="84" width="238" height="330" rx="12" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <rect x="354" y="68" width="366" height="368" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <g fill="#181817">
    <rect x="122" y="130" width="46" height="46"/><rect x="238" y="130" width="46" height="46"/>
    <rect x="122" y="246" width="46" height="46"/><rect x="180" y="188" width="34" height="34"/>
    <rect x="238" y="246" width="46" height="46"/><rect x="180" y="304" width="34" height="34"/>
  </g>
  <g stroke="#181817" stroke-width="3" fill="none">
    <path d="M386 142h302M386 214h302M386 286h302M386 358h302"/>
  </g>
  <g fill="#ff4d00"><circle cx="410" cy="178" r="12"/><circle cx="410" cy="250" r="12"/></g>
  <g fill="#3fa435"><circle cx="410" cy="322" r="12"/><circle cx="410" cy="394" r="12"/></g>
  <text x="118" y="112" font-family="monospace" font-size="18">QR MENU</text>
  <text x="386" y="116" font-family="monospace" font-size="18">ORDER QUEUE</text>
</svg>
```

- [ ] **Step 4: Add the Work layout CSS**

Append to `assets/atlas.css`:

```css
.work-layout { display: grid; grid-template-columns: 1.45fr .75fr; gap: var(--space-3); }
.secondary-work { display: grid; grid-template-rows: repeat(3, 1fr); gap: var(--space-3); }
.secondary-work .artifact-copy strong { font-size: var(--text-base); }
.secondary-work .artifact-copy span { font-size: var(--text-sm); }
```

- [ ] **Step 5: Replace the old Work module**

Replace the current `#work` section with:

```html
<section class="figure" id="work" data-section="01 Work" style="--figure-accent:var(--orange)">
  <div class="figure-rail mono"><span class="figure-marker" aria-hidden="true"></span>FIG 01</div>
  <div class="figure-body">
    <div class="figure-heading"><h2>Work systems</h2><span class="mono">Shipped at operational scale</span></div>
    <div class="work-layout">
      <div class="artifact artifact-plate">
        <div class="artifact-art"><img src="assets/flatlays/dmms.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <span class="coordinate-pin" aria-hidden="true"></span>
        <div class="artifact-copy" id="dmms-note"><strong>Digital Mall Management System</strong><span>10 connected modules across spatial decisions, automation, field work, and pipeline visibility.</span></div>
      </div>
      <div class="secondary-work">
        <article class="artifact artifact-plate">
          <div class="artifact-art"><img src="assets/flatlays/affiliate-referral.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
          <div class="artifact-copy"><strong>Affiliate Referral System</strong><span>LINE OA attribution from invite to conversion.</span></div>
        </article>
        <article class="artifact artifact-plate">
          <div class="artifact-art"><img src="assets/flatlays/market-rental.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
          <div class="artifact-copy"><strong>Market Rental Management</strong><span>Visual stall availability connected to booking.</span></div>
        </article>
        <article class="artifact artifact-plate">
          <div class="artifact-art"><img src="assets/flatlays/meal-order.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
          <div class="artifact-copy"><strong>Meal Order Management</strong><span>QR ordering with an operator-ready queue.</span></div>
        </article>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 6: Run Work and asset tests**

Run:

```bash
node --test --test-name-pattern="Work is product-led" tests/atlas-structure.test.mjs
node --test --test-name-pattern="DMMS flat lay|Work flat lays" tests/flatlay-assets.test.mjs
```

Expected: both commands pass.

- [ ] **Step 7: Commit**

```bash
git add index.html assets/atlas.css assets/flatlays/affiliate-referral.svg assets/flatlays/market-rental.svg assets/flatlays/meal-order.svg tests/atlas-structure.test.mjs tests/flatlay-assets.test.mjs
git commit -m "feat: replace work cards with product flat lays"
```

---

### Task 4: Replace Lab with runnable product plates

**Files:**
- Create: `assets/flatlays/performance-results.svg`
- Create: `assets/flatlays/thaimart.svg`
- Create: `assets/flatlays/edusight.svg`
- Modify: `assets/atlas.css`
- Modify: `index.html`
- Modify: `tests/atlas-structure.test.mjs`

**Interfaces:**
- Consumes: `.artifact-link` and existing prototype URLs
- Produces: `.lab-layout` and three fully linked Lab artifacts

- [ ] **Step 1: Add the failing Lab assertions**

Add:

```js
test('Lab plates keep all runnable prototype destinations', () => {
  const destinations = [
    'performance-management/index.html',
    'thaimart/index.html',
    'edusight/index.html'
  ];
  for (const href of destinations) assert.ok(html.includes(`href="${href}"`), `missing ${href}`);
  for (const asset of ['performance-results.svg', 'thaimart.svg', 'edusight.svg']) {
    assert.ok(html.includes(`assets/flatlays/${asset}`), `missing ${asset}`);
  }
  assert.equal(html.includes('class="carts"'), false);
});
```

Add to `tests/flatlay-assets.test.mjs`:

```js
test('Lab flat lays follow the asset contract', async () => {
  for (const file of ['performance-results.svg', 'thaimart.svg', 'edusight.svg']) {
    const svg = await readFile(new URL(`../assets/flatlays/${file}`, import.meta.url), 'utf8');
    assertFlatlayMarkup(file, svg);
  }
});
```

- [ ] **Step 2: Verify the Lab tests fail**

Run:

```bash
node --test --test-name-pattern="Lab plates" tests/atlas-structure.test.mjs
node --test --test-name-pattern="Lab flat lays" tests/flatlay-assets.test.mjs
```

Expected: the structure test fails on missing `performance-results.svg` and the asset test fails with `ENOENT`.

- [ ] **Step 3: Create the three Lab SVGs**

Create `assets/flatlays/performance-results.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">Performance Results decision report</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <rect x="76" y="62" width="648" height="388" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <rect x="104" y="92" width="592" height="38" fill="#181817"/>
  <g stroke="#181817" stroke-width="3" fill="none">
    <path d="M156 332l50-126 76 88 74-154 72 126 84-86 116 152"/>
    <path d="M126 358h534M126 184v174"/>
    <rect x="126" y="378" width="156" height="44"/><rect x="302" y="378" width="156" height="44"/><rect x="478" y="378" width="156" height="44"/>
  </g>
  <g fill="#00a4c8"><circle cx="206" cy="206" r="10"/><circle cx="356" cy="140" r="10"/><circle cx="512" cy="180" r="10"/></g>
  <text x="126" y="118" fill="#fafaf7" font-family="monospace" font-size="18">360 REVIEW / DECISION REPORT</text>
</svg>
```

Create `assets/flatlays/thaimart.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">ThaiMart marketplace flywheel</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <g fill="#fafaf7" stroke="#181817" stroke-width="3">
    <rect x="66" y="82" width="210" height="344"/><rect x="296" y="82" width="210" height="344"/><rect x="526" y="82" width="210" height="344"/>
  </g>
  <g fill="none" stroke="#181817" stroke-width="3">
    <circle cx="171" cy="238" r="62"/><circle cx="401" cy="238" r="62"/><circle cx="631" cy="238" r="62"/>
    <path d="M226 172l104-42M456 172l104-42M686 302l-514 76"/>
  </g>
  <g fill="#ff4d00"><circle cx="171" cy="238" r="16"/></g>
  <g fill="#00a4c8"><circle cx="401" cy="238" r="16"/></g>
  <g fill="#3fa435"><circle cx="631" cy="238" r="16"/></g>
  <g font-family="monospace" font-size="18" fill="#181817">
    <text x="118" y="126">DEMAND</text><text x="330" y="126">FULFILLMENT</text><text x="584" y="126">SUPPLY</text>
  </g>
</svg>
```

Create `assets/flatlays/edusight.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">EduSight coding behavior replay</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <rect x="64" y="64" width="672" height="388" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <rect x="90" y="92" width="390" height="286" fill="#181817"/>
  <rect x="506" y="92" width="202" height="286" fill="#f4f4f0" stroke="#181817" stroke-width="3"/>
  <g stroke="#00a4c8" stroke-width="4" fill="none">
    <path d="M120 154h230M120 198h310M120 242h174M120 286h278"/>
  </g>
  <g stroke="#181817" stroke-width="3"><path d="M110 414h578"/></g>
  <g fill="#ff4d00"><circle cx="190" cy="414" r="12"/><circle cx="334" cy="414" r="12"/></g>
  <g fill="#3fa435"><circle cx="528" cy="414" r="12"/><circle cx="646" cy="414" r="12"/></g>
  <text x="532" y="132" font-family="monospace" font-size="18">SUPPORT</text>
</svg>
```

- [ ] **Step 4: Add the Lab layout CSS**

Append:

```css
.lab-layout {
  display: grid;
  grid-template-columns: 1.15fr .85fr 1fr;
  gap: var(--space-3);
  align-items: start;
}
.lab-layout .artifact-link:nth-child(2) { margin-top: var(--space-5); }
.lab-layout .artifact-link:nth-child(3) { margin-top: var(--space-3); }
```

- [ ] **Step 5: Replace the old Lab module**

Replace `#lab` with:

```html
<section class="figure" id="lab" data-section="02 Lab" style="--figure-accent:var(--cyan)">
  <div class="figure-rail mono"><span class="figure-marker" aria-hidden="true"></span>FIG 02</div>
  <div class="figure-body">
    <div class="figure-heading"><h2>Runnable product lab</h2><span class="mono">Three product bets</span></div>
    <div class="lab-layout">
      <a class="artifact artifact-link" href="performance-management/index.html" aria-label="Open Performance Results prototype">
        <div class="artifact-art"><img src="assets/flatlays/performance-results.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <span class="coordinate-pin" aria-hidden="true"></span>
        <div class="artifact-copy"><strong>Performance Results</strong><span>360° review evidence translated into manager decisions.</span></div>
      </a>
      <a class="artifact artifact-link" href="thaimart/index.html" aria-label="Open ThaiMart prototype hub">
        <div class="artifact-art"><img src="assets/flatlays/thaimart.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <div class="artifact-copy"><strong>Marketplace Flywheel</strong><span>Demand, fulfillment, and supply as one operating loop.</span></div>
      </a>
      <a class="artifact artifact-link" href="edusight/index.html" aria-label="Open EduSight prototype">
        <div class="artifact-art"><img src="assets/flatlays/edusight.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <div class="artifact-copy"><strong>Cognitive Replay</strong><span>Learning signals turned into visible support moments.</span></div>
      </a>
    </div>
  </div>
</section>
```

- [ ] **Step 6: Run the Lab and flat-lay tests**

Run:

```bash
node --test --test-name-pattern="Lab plates" tests/atlas-structure.test.mjs
node --test --test-name-pattern="Lab flat lays" tests/flatlay-assets.test.mjs
```

Expected: both commands pass.

- [ ] **Step 7: Commit**

```bash
git add index.html assets/atlas.css assets/flatlays/performance-results.svg assets/flatlays/thaimart.svg assets/flatlays/edusight.svg tests/atlas-structure.test.mjs tests/flatlay-assets.test.mjs
git commit -m "feat: turn product lab into runnable flat lays"
```

---

### Task 5: Replace Experience and Spec with atlas artifacts

**Files:**
- Create: `assets/flatlays/experience-dossiers.svg`
- Create: `assets/flatlays/system-architecture.svg`
- Modify: `assets/atlas.css`
- Modify: `index.html`
- Modify: `tests/atlas-structure.test.mjs`

**Interfaces:**
- Consumes: factual role periods and capability groups from current `index.html`
- Produces: `.dossier-list`, `.spec-layout`, five experience dossiers, and the system architecture inventory

- [ ] **Step 1: Add failing Log and Spec assertions**

Add:

```js
test('Experience and Spec are artifacts rather than tables', () => {
  for (const company of ['1Moby', 'blockfint', 'CP ORIGIN', 'Softnix', 'Thai Nippon Seiki']) {
    assert.ok(html.includes(company), `missing ${company}`);
  }
  for (const capability of ['Frontend', 'Backend', 'State + testing', 'Cloud + automation', 'AI toolchain']) {
    assert.ok(html.includes(capability), `missing ${capability}`);
  }
  assert.ok(html.includes('assets/flatlays/experience-dossiers.svg'));
  assert.ok(html.includes('assets/flatlays/system-architecture.svg'));
  assert.equal(/<table[^>]+class=["'](?:log|spec)["']/.test(html), false);
});
```

Add to `tests/flatlay-assets.test.mjs`:

```js
test('Experience and Spec flat lays follow the asset contract', async () => {
  for (const file of ['experience-dossiers.svg', 'system-architecture.svg']) {
    const svg = await readFile(new URL(`../assets/flatlays/${file}`, import.meta.url), 'utf8');
    assertFlatlayMarkup(file, svg);
  }
});
```

- [ ] **Step 2: Verify the tests fail**

Run:

```bash
node --test --test-name-pattern="Experience and Spec" tests/atlas-structure.test.mjs
node --test --test-name-pattern="Experience and Spec flat lays" tests/flatlay-assets.test.mjs
```

Expected: the structure test fails because the old tables remain and the asset test fails with `ENOENT`.

- [ ] **Step 3: Create the Experience and Spec SVGs**

Create `assets/flatlays/experience-dossiers.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">Five chronological experience dossiers</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <g stroke="#181817" stroke-width="3">
    <rect x="70" y="72" width="240" height="148" fill="#fafaf7" transform="rotate(-2 190 146)"/>
    <rect x="280" y="96" width="240" height="148" fill="#fafaf7" transform="rotate(2 400 170)"/>
    <rect x="490" y="68" width="240" height="148" fill="#fafaf7" transform="rotate(-1 610 142)"/>
    <rect x="164" y="284" width="240" height="148" fill="#fafaf7" transform="rotate(2 284 358)"/>
    <rect x="426" y="286" width="240" height="148" fill="#fafaf7" transform="rotate(-2 546 360)"/>
    <path d="M92 134h196M302 158h196M512 130h196M186 346h196M448 348h196"/>
  </g>
  <g font-family="monospace" font-size="17" fill="#181817">
    <text x="94" y="112">2026 / 1MOBY</text><text x="304" y="136">2026 / BLOCKFINT</text>
    <text x="514" y="108">2021–26 / CP ORIGIN</text><text x="188" y="324">2020–21 / SOFTNIX</text>
    <text x="450" y="326">2020 / THAI NIPPON SEIKI</text>
  </g>
  <g fill="#f5c400"><rect x="92" y="174" width="54" height="14"/><rect x="302" y="198" width="54" height="14"/><rect x="512" y="170" width="54" height="14"/></g>
</svg>
```

Create `assets/flatlays/system-architecture.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">System architecture capability map</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <g stroke="#181817" stroke-width="3" fill="#fafaf7">
    <rect x="68" y="86" width="176" height="82"/><rect x="68" y="220" width="176" height="82"/><rect x="68" y="354" width="176" height="82"/>
    <rect x="312" y="124" width="176" height="82"/><rect x="312" y="316" width="176" height="82"/>
    <rect x="556" y="86" width="176" height="82"/><rect x="556" y="220" width="176" height="82"/><rect x="556" y="354" width="176" height="82"/>
    <path d="M244 127h68M244 261h68M244 395h68M488 165h68M488 357h68M400 206v110"/>
  </g>
  <g font-family="monospace" font-size="16" fill="#181817">
    <text x="96" y="136">FRONTEND</text><text x="96" y="270">STATE + TEST</text><text x="96" y="404">PRODUCT FLOW</text>
    <text x="340" y="174">BACKEND</text><text x="340" y="366">AUTOMATION</text>
    <text x="584" y="136">CLOUD</text><text x="584" y="270">AI TOOLCHAIN</text><text x="584" y="404">EDUCATION</text>
  </g>
  <g fill="#3fa435"><circle cx="278" cy="127" r="8"/><circle cx="278" cy="261" r="8"/><circle cx="522" cy="357" r="8"/></g>
</svg>
```

- [ ] **Step 4: Add Experience and Spec CSS**

Append:

```css
.log-layout { display: grid; grid-template-columns: 1.1fr .9fr; gap: var(--space-4); }
.dossier-list { display: grid; align-content: start; border-block: 1px solid var(--border-strong); }
.dossier {
  display: grid;
  grid-template-columns: 9ch 1fr;
  gap: var(--space-3);
  padding: .85rem 0;
  border-bottom: 1px solid var(--border-soft);
}
.dossier:last-child { border-bottom: 0; }
.dossier dt { font-family: var(--font-mono); font-size: var(--text-xs); }
.dossier dd { margin: 0; }
.dossier strong { display: block; }
.dossier span { color: var(--text-secondary); font-size: var(--text-sm); }
.spec-layout { display: grid; grid-template-columns: 1.15fr .85fr; gap: var(--space-4); }
.capability-list { display: grid; align-content: start; }
.capability {
  display: grid;
  grid-template-columns: 10rem 1fr;
  gap: var(--space-3);
  padding: .8rem 0;
  border-bottom: 1px solid var(--border-soft);
}
.capability dt { font: 700 var(--text-xs) var(--font-mono); letter-spacing: .06em; }
.capability dd { margin: 0; color: var(--text-secondary); }
```

- [ ] **Step 5: Replace Log and Spec**

Use:

```html
<section class="figure" id="log" data-section="03 Log" style="--figure-accent:var(--yellow)">
  <div class="figure-rail mono"><span class="figure-marker" aria-hidden="true"></span>FIG 03</div>
  <div class="figure-body">
    <div class="figure-heading"><h2>Experience dossiers</h2><span class="mono">2020–now</span></div>
    <div class="log-layout">
      <div class="artifact artifact-plate">
        <div class="artifact-art"><img src="assets/flatlays/experience-dossiers.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <span class="coordinate-pin" aria-hidden="true"></span>
        <div class="artifact-copy"><strong>Enterprise systems, shipped in sequence</strong><span>Five roles connected by one operating theme.</span></div>
      </div>
      <dl class="dossier-list">
        <div class="dossier"><dt>2026–now</dt><dd><strong>Software Engineer · 1Moby</strong><span>ThaiBulkSMS full-stack support across lead routing, banners, and message history.</span></dd></div>
        <div class="dossier"><dt>2026</dt><dd><strong>Software Engineer · blockfint</strong><span>eKYC onboarding prototypes and banking integration support.</span></dd></div>
        <div class="dossier"><dt>2021–2026</dt><dd><strong>Frontend Developer · CP ORIGIN</strong><span>DMMS, ERP + LINE OA, and reporting across 2,000+ branches.</span></dd></div>
        <div class="dossier"><dt>2020–2021</dt><dd><strong>Software Engineer · Softnix</strong><span>PDPA product ownership and full-stack trainee mentoring.</span></dd></div>
        <div class="dossier"><dt>2020</dt><dd><strong>Programmer · Thai Nippon Seiki</strong><span>Multi-level document approval and factory ERP maintenance.</span></dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="figure" id="spec" data-section="04 Spec" style="--figure-accent:var(--green)">
  <div class="figure-rail mono"><span class="figure-marker" aria-hidden="true"></span>FIG 04</div>
  <div class="figure-body">
    <div class="figure-heading"><h2>System architecture inventory</h2><span class="mono">The stack follows the workflow</span></div>
    <div class="spec-layout">
      <div class="artifact artifact-plate">
        <div class="artifact-art"><img src="assets/flatlays/system-architecture.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <span class="coordinate-pin" aria-hidden="true"></span>
        <div class="artifact-copy"><strong>Product system map</strong><span>Interface, services, automation, and delivery connected.</span></div>
      </div>
      <dl class="capability-list">
        <div class="capability"><dt>Frontend</dt><dd>React, Next.js, TypeScript, Vue, Angular, HTML, CSS</dd></div>
        <div class="capability"><dt>Backend</dt><dd>Node.js, NestJS, Express, Go, Python, PHP, SQL</dd></div>
        <div class="capability"><dt>State + testing</dt><dd>React Query, Zustand, XState, Jest, Vitest</dd></div>
        <div class="capability"><dt>Cloud + automation</dt><dd>GCP, AWS, Docker, Firebase, Git, n8n, LINE OA</dd></div>
        <div class="capability"><dt>AI toolchain</dt><dd>Cursor, Claude, Codex, AI integration workflows</dd></div>
        <div class="capability"><dt>Background</dt><dd>B.Sc. Software Engineering · Thai native · English conversational</dd></div>
      </dl>
    </div>
  </div>
</section>
```

- [ ] **Step 6: Run the focused tests**

Run:

```bash
node --test --test-name-pattern="Experience and Spec" tests/atlas-structure.test.mjs
node --test --test-name-pattern="Experience and Spec flat lays" tests/flatlay-assets.test.mjs
```

Expected: both commands pass.

- [ ] **Step 7: Commit**

```bash
git add index.html assets/atlas.css assets/flatlays/experience-dossiers.svg assets/flatlays/system-architecture.svg tests/atlas-structure.test.mjs tests/flatlay-assets.test.mjs
git commit -m "feat: reshape experience and capabilities as atlas figures"
```

---

### Task 6: Complete Contact, cleanup, responsive behavior, and degradation

**Files:**
- Create: `assets/flatlays/contact-baseplate.svg`
- Modify: `assets/atlas.css`
- Modify: `index.html`
- Modify: `tests/atlas-structure.test.mjs`

**Interfaces:**
- Consumes: final atlas figures and contact destinations
- Produces: complete static page without legacy styles or scripts

- [ ] **Step 1: Add failing completion assertions**

Add:

```js
test('contact baseplate exposes every direct contact action', () => {
  assert.ok(html.includes('assets/flatlays/contact-baseplate.svg'));
  assert.match(html, /mailto:pakawat\.zon@gmail\.com/);
  assert.match(html, /tel:\+66971427997/);
  assert.match(html, /https:\/\/github\.com\/Zonxpk/);
  assert.match(html, /https:\/\/www\.linkedin\.com\/in\/zonpk\//);
});

test('root page exposes the complete atlas landmark structure', () => {
  for (const id of ['identity', 'work', 'lab', 'log', 'spec', 'contact']) {
    assert.match(html, new RegExp(`id=["']${id}["']`), `missing #${id}`);
  }
  assert.match(html, /aria-label=["']Portfolio sections["']/);
  assert.match(html, /id=["']theme-toggle["']/);
  assert.match(html, /id=["']local-time["']/);
  assert.match(html, /id=["']current-section["']/);
  assert.equal((html.match(/class=["']coordinate-pin["']/g) ?? []).length, 6);
});

test('legacy embedded presentation code is removed', () => {
  assert.equal(/<style>[\s\S]*--chassis/.test(html), false);
  assert.equal(html.includes('revealIO'), false);
  assert.equal(html.includes('AudioContext'), false);
  assert.match(html, /<link rel=["']stylesheet["'] href=["']assets\/atlas\.css["']/);
  assert.match(html, /<script type=["']module["'] src=["']assets\/atlas\.js["']/);
});

test('root page excludes rejected decorative systems', () => {
  for (const banned of ['three.module.js', '<canvas', 'id="snd"', 'VU meter', 'SYS_STATUS', 'MEMORY: OK']) {
    assert.equal(html.includes(banned), false, `found banned pattern: ${banned}`);
  }
});
```

Add to `tests/flatlay-assets.test.mjs`:

```js
test('Contact flat lay follows the asset contract', async () => {
  const svg = await readFile(new URL('../assets/flatlays/contact-baseplate.svg', import.meta.url), 'utf8');
  assertFlatlayMarkup('contact-baseplate.svg', svg);
});
```

- [ ] **Step 2: Verify completion assertions fail**

Run:

```bash
node --test --test-name-pattern="contact baseplate|complete atlas|legacy embedded|excludes rejected" tests/atlas-structure.test.mjs
node --test --test-name-pattern="Contact flat lay" tests/flatlay-assets.test.mjs
```

Expected: the structure tests fail on the missing contact asset and remaining inline legacy CSS/JS; the asset test fails with `ENOENT`.

- [ ] **Step 3: Create the contact SVG**

Create `assets/flatlays/contact-baseplate.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-labelledby="title">
  <title id="title">Contact and resume channel baseplate</title>
  <rect width="800" height="520" fill="#e9e9e4"/>
  <rect x="78" y="86" width="644" height="346" fill="#fafaf7" stroke="#181817" stroke-width="3"/>
  <rect x="106" y="114" width="588" height="42" fill="#181817"/>
  <g fill="#f4f4f0" stroke="#181817" stroke-width="3">
    <rect x="112" y="202" width="252" height="72"/><rect x="436" y="202" width="252" height="72"/>
    <rect x="112" y="308" width="252" height="72"/><rect x="436" y="308" width="252" height="72"/>
  </g>
  <g font-family="monospace" font-size="18" fill="#181817">
    <text x="138" y="246">EMAIL</text><text x="462" y="246">PHONE</text>
    <text x="138" y="352">GITHUB</text><text x="462" y="352">LINKEDIN</text>
  </g>
  <circle cx="668" cy="135" r="10" fill="#ff4d00"/>
</svg>
```

- [ ] **Step 4: Replace the footer with the Contact figure**

Use:

```html
<footer class="figure contact-figure" id="contact" data-section="05 Contact" style="--figure-accent:var(--orange)">
  <div class="figure-rail mono"><span class="figure-marker" aria-hidden="true"></span>FIG 05</div>
  <div class="figure-body">
    <div class="figure-heading"><h2>Ready to make operations legible.</h2><span class="mono">Bangkok · open to product engineering</span></div>
    <div class="contact-layout">
      <div class="artifact artifact-plate">
        <div class="artifact-art"><img src="assets/flatlays/contact-baseplate.svg" alt="" width="800" height="520" loading="lazy" decoding="async"></div>
        <span class="coordinate-pin" aria-hidden="true"></span>
        <div class="artifact-copy"><strong>Direct channels</strong><span>Choose the path that fits the conversation.</span></div>
      </div>
      <div class="contact-actions">
        <a class="key key--primary" href="mailto:pakawat.zon@gmail.com">Email Pakawat</a>
        <a class="key" href="tel:+66971427997">(+66) 97-142-7997</a>
        <a class="key" href="https://github.com/Zonxpk">GitHub</a>
        <a class="key" href="https://www.linkedin.com/in/zonpk/">LinkedIn</a>
        <a class="key" href="https://drive.google.com/uc?export=download&amp;id=1B2tvM8jNeyZd6OBbq5haLpY4j3sO8lss">Download resume</a>
      </div>
    </div>
  </div>
</footer>
```

- [ ] **Step 5: Add contact, responsive, fallback, and reduced-motion CSS**

Append to `assets/atlas.css`:

```css
.contact-layout { display: grid; grid-template-columns: 1.2fr .8fr; gap: var(--space-4); }
.contact-actions { display: grid; align-content: center; gap: var(--space-2); }
.contact-actions .key { width: 100%; justify-content: space-between; }
img[alt=""] { color: transparent; }

@media (max-width: 900px) {
  .identity-layout,
  .work-layout,
  .log-layout,
  .spec-layout,
  .contact-layout { grid-template-columns: 1fr; }
  .secondary-work { grid-template-columns: repeat(3, 1fr); grid-template-rows: none; }
  .lab-layout { grid-template-columns: 1fr 1fr; }
  .lab-layout .artifact-link:nth-child(2),
  .lab-layout .artifact-link:nth-child(3) { margin-top: 0; }
}

@media (max-width: 680px) {
  .chassis { width: 100%; border-inline: 0; }
  .utility-strip { grid-template-columns: 1fr auto; }
  .utility-strip > div:nth-child(2) { display: none; }
  .module-nav { top: 44px; grid-template-columns: repeat(5, minmax(112px, 1fr)); }
  .figure { grid-template-columns: 1fr; scroll-margin-top: 92px; }
  .figure-rail {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    padding: .7rem 1rem;
    border-right: 0;
    border-bottom: 1px solid var(--border-strong);
  }
  .figure-marker { margin: 0; }
  .figure-body { padding: 1.25rem 1rem 2.5rem; }
  .figure-heading { align-items: flex-start; flex-direction: column; }
  .secondary-work,
  .lab-layout { grid-template-columns: 1fr; }
  .metric-strip { grid-template-columns: 1fr; }
  .metric { border-right: 0; border-bottom: 1px solid var(--border-strong); }
  .metric:last-child { border-bottom: 0; }
  .dossier,
  .capability { grid-template-columns: 1fr; gap: var(--space-1); }
  .artifact-copy strong { font-size: var(--text-base); }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .artifact { transition: none; }
  .artifact-link:hover,
  .artifact-link:focus-visible,
  .artifact-link:active { transform: none; }
}
```

- [ ] **Step 6: Remove legacy embedded CSS and scripts**

In `index.html`:

- Delete the entire legacy `<style>` block.
- Delete the legacy inline `<script>` containing audio, reveals, and old readout behavior.
- Add `<script type="module" src="assets/atlas.js"></script>` before `</body>`.
- Ensure the new `main` and `.chassis` wrappers close immediately after the Contact figure.

Create `assets/atlas.js` with a safe empty initialization until Task 7:

```js
export function initAtlas() {}

if (typeof window !== 'undefined') initAtlas();
```

- [ ] **Step 7: Run all structural and asset tests**

Run:

```bash
npm test
```

Expected: all structure and flat-lay asset tests pass; behavior tests do not exist yet.

- [ ] **Step 8: Verify JavaScript-disabled and missing-asset behavior**

Serve the site, disable JavaScript in browser developer tools, and reload.

Expected:

- All figures and links remain present.
- Theme stays at the CSS/system default.
- Blocking `assets/flatlays/dmms.svg` leaves its adjacent DMMS title, outcome, metrics, and `#work` link usable.

- [ ] **Step 9: Commit**

```bash
git add index.html assets/atlas.css assets/atlas.js assets/flatlays/contact-baseplate.svg tests/atlas-structure.test.mjs tests/flatlay-assets.test.mjs
git commit -m "feat: complete responsive portfolio atlas"
```

---

### Task 7: Add progressive theme, time, section, and shortcut behavior

**Files:**
- Modify: `assets/atlas.js`
- Create: `tests/atlas-behavior.test.mjs`

**Interfaces:**
- Produces:
  - `resolveTheme(savedTheme: string | null, prefersDark: boolean): "light" | "dark"`
  - `formatBangkokTime(date: Date): string`
  - `shortcutTarget(key: string): string | null`
  - `initAtlas(doc?: Document, win?: Window): void`

- [ ] **Step 1: Write the failing behavior tests**

Create `tests/atlas-behavior.test.mjs`:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import { formatBangkokTime, resolveTheme, shortcutTarget } from '../assets/atlas.js';

test('saved theme wins over system preference', () => {
  assert.equal(resolveTheme('light', true), 'light');
  assert.equal(resolveTheme('dark', false), 'dark');
  assert.equal(resolveTheme(null, true), 'dark');
  assert.equal(resolveTheme('unknown', false), 'light');
});

test('Bangkok time is stable and tabular', () => {
  const utc = new Date('2026-07-17T07:05:00.000Z');
  assert.equal(formatBangkokTime(utc), '14:05 ICT');
});

test('QWER shortcuts map only to portfolio figures', () => {
  assert.equal(shortcutTarget('q'), 'work');
  assert.equal(shortcutTarget('W'), 'lab');
  assert.equal(shortcutTarget('e'), 'log');
  assert.equal(shortcutTarget('R'), 'spec');
  assert.equal(shortcutTarget('1'), null);
  assert.equal(shortcutTarget('x'), null);
});
```

- [ ] **Step 2: Run behavior tests and verify failure**

Run:

```bash
node --test tests/atlas-behavior.test.mjs
```

Expected: FAIL because the three functions are not exported.

- [ ] **Step 3: Implement the complete progressive enhancement module**

Replace `assets/atlas.js` with:

```js
const THEMES = new Set(['light', 'dark']);
const SHORTCUTS = new Map([
  ['q', 'work'],
  ['w', 'lab'],
  ['e', 'log'],
  ['r', 'spec']
]);

export function resolveTheme(savedTheme, prefersDark) {
  if (THEMES.has(savedTheme)) return savedTheme;
  return prefersDark ? 'dark' : 'light';
}

export function formatBangkokTime(date) {
  const time = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'Asia/Bangkok',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  }).format(date);
  return `${time} ICT`;
}

export function shortcutTarget(key) {
  return SHORTCUTS.get(String(key).toLowerCase()) ?? null;
}

function readStoredTheme(win) {
  try {
    return win.localStorage.getItem('portfolio-theme');
  } catch {
    return null;
  }
}

function storeTheme(win, theme) {
  try {
    win.localStorage.setItem('portfolio-theme', theme);
  } catch {
    return;
  }
}

function applyTheme(doc, theme) {
  doc.documentElement.dataset.theme = theme;
  const toggle = doc.getElementById('theme-toggle');
  const label = doc.getElementById('theme-label');
  const isDark = theme === 'dark';
  toggle?.setAttribute('aria-pressed', String(isDark));
  toggle?.setAttribute('aria-label', `Switch to ${isDark ? 'light' : 'dark'} theme`);
  if (label) label.textContent = isDark ? 'Dark' : 'Light';
  const themeColor = doc.querySelector('meta[name="theme-color"]');
  themeColor?.setAttribute('content', isDark ? '#171716' : '#f4f4f0');
}

export function initAtlas(doc = document, win = window) {
  const prefersDark = win.matchMedia?.('(prefers-color-scheme: dark)').matches ?? false;
  let theme = resolveTheme(readStoredTheme(win), prefersDark);
  applyTheme(doc, theme);

  doc.getElementById('theme-toggle')?.addEventListener('click', () => {
    theme = theme === 'dark' ? 'light' : 'dark';
    applyTheme(doc, theme);
    storeTheme(win, theme);
  });

  const time = doc.getElementById('local-time');
  const paintTime = () => {
    if (time) time.textContent = formatBangkokTime(new Date());
  };
  paintTime();
  win.setInterval(paintTime, 60_000);

  const navLinks = new Map(
    [...doc.querySelectorAll('.module-nav a[href^="#"]')].map((link) => [
      link.getAttribute('href').slice(1),
      link
    ])
  );
  const currentSection = doc.getElementById('current-section');

  if ('IntersectionObserver' in win) {
    const observer = new win.IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        for (const link of navLinks.values()) link.removeAttribute('aria-current');
        navLinks.get(entry.target.id)?.setAttribute('aria-current', 'true');
        if (currentSection) currentSection.textContent = entry.target.dataset.section;
      }
    }, { rootMargin: '-35% 0px -60% 0px' });
    doc.querySelectorAll('[data-section]').forEach((section) => observer.observe(section));
  }

  doc.addEventListener('keydown', (event) => {
    if (event.metaKey || event.ctrlKey || event.altKey) return;
    if (event.target instanceof Element && event.target.matches('input, textarea, select, [contenteditable]')) return;
    const id = shortcutTarget(event.key);
    if (!id) return;
    const reduced = win.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false;
    doc.getElementById(id)?.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
  });
}

if (typeof window !== 'undefined') initAtlas();
```

- [ ] **Step 4: Run behavior and full tests**

Run:

```bash
node --test tests/atlas-behavior.test.mjs
npm test
```

Expected: all tests pass.

- [ ] **Step 5: Verify browser behavior**

With the local server running:

1. Click the theme control; expected: theme, label, accessible name, `aria-pressed`, and browser theme color update together.
2. Reload; expected: explicit theme choice persists.
3. Press Q, W, E, and R; expected: Work, Lab, Log, and Spec scroll into view.
4. Tab through artifact links; expected: each focused plate raises and has a visible outline.
5. Enable reduced motion and press Q; expected: navigation jumps without smooth motion.

- [ ] **Step 6: Commit**

```bash
git add assets/atlas.js tests/atlas-behavior.test.mjs
git commit -m "feat: add resilient atlas interaction state"
```

---

### Task 8: Final accessibility, metadata, link, and visual verification

**Files:**
- Modify: `index.html`
- Modify: `assets/atlas.css`
- Modify: tests only if verification exposes a regression

**Interfaces:**
- Consumes: complete atlas implementation
- Produces: ship-ready root page and recorded verification evidence

- [ ] **Step 1: Verify metadata matches the redesigned surface**

Ensure `index.html` contains:

```html
<title>Pakawat Smutkun — product systems, made legible</title>
<meta name="description" content="Pakawat Smutkun is a full-stack product engineer designing operational systems across floorplans, reports, automation, and field workflows.">
<meta name="theme-color" content="#f4f4f0">
<meta property="og:title" content="Pakawat Smutkun — product systems, made legible">
<meta property="og:description" content="A technical atlas of operational products, prototypes, experience, and engineering capabilities.">
<meta property="og:image" content="/preview.webp">
```

Run:

```bash
npm test
```

Expected: all tests pass.

- [ ] **Step 2: Verify every local destination returns successfully**

Start the server, then run:

```bash
for path in / /performance-management/index.html /thaimart/index.html /edusight/index.html; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "http://127.0.0.1:8000${path}")
  test "$code" = "200" || exit 1
done
```

Expected: exit code 0.

- [ ] **Step 3: Run responsive browser checks**

At widths 390, 768, 1280, and 1680, evaluate:

```js
({
  width: window.innerWidth,
  scrollWidth: document.documentElement.scrollWidth,
  noOverflow: document.documentElement.scrollWidth <= window.innerWidth,
  figures: document.querySelectorAll('[data-section]').length,
  artifacts: document.querySelectorAll('.artifact').length
})
```

Expected:

- `noOverflow: true`
- `figures: 6`
- `artifacts` is at least 10
- DMMS remains the largest artifact
- Mobile reading order is artifact, title, outcome, action
- The navigation has an obvious horizontal overflow edge at 390px

- [ ] **Step 4: Run accessibility interaction checks**

Verify:

- Skip link becomes visible on focus and lands on `#main`.
- Heading order is one `h1`, then figure `h2` headings.
- Every actionable artifact has an accessible name that includes its project.
- Focus and hover expose the same outcome annotation.
- All controls and links have at least a 44px interactive box.
- Active navigation uses `aria-current`, contrast, and a bottom indicator.
- Light and dark body text meet WCAG AA.
- The orange primary action meets AA against white text.
- At 200% zoom, content reflows without two-dimensional scrolling.

- [ ] **Step 5: Verify failure and motion modes**

Check:

1. Disable JavaScript and reload: all content and links remain usable.
2. Block `assets/flatlays/dmms.svg`: DMMS text, metrics, and navigation remain.
3. Enable reduced motion: plates do not translate and anchor navigation does not smooth-scroll.
4. Leave the page idle for 10 seconds in the Performance panel: no repeating animation frames or timer faster than the one-minute clock update.
5. Inspect image requests: the identity DMMS image is eager with high fetch priority; every below-fold artifact is lazy and asynchronously decoded.
6. Inspect the console: zero errors.

- [ ] **Step 6: Run the ui-craft polish pass**

Inspect and fix only observed defects:

- Hero squint order is headline, DMMS product evidence, then primary resume action.
- No two adjacent figures share the same layout.
- There is exactly one coordinate-pin motif per major figure.
- No uniform three-card grid remains; the Lab plates are deliberately staggered on desktop and linear on mobile.
- Artifact shadows share one light direction.
- Large headings use tight tracking and sentence case.
- Metrics use tabular numerals.
- No visible copy contains fake system language or generic CTAs.
- Accent usage stays within one active figure color per viewport region.

After each fix, run:

```bash
npm test
```

Expected: all tests pass.

- [ ] **Step 7: Inspect the final diff**

Run:

```bash
git diff --check
git status --short
git diff --stat
```

Expected:

- No whitespace errors.
- Only the planned root page, root assets, root tests, and package file are changed.
- Existing user-owned `OP*.md` files and `.impeccable/hook.cache.json` remain untouched.

- [ ] **Step 8: Commit the verified polish**

```bash
git add index.html assets/atlas.css assets/atlas.js assets/flatlays package.json tests
git commit -m "fix: finish and verify portfolio technical atlas"
```

- [ ] **Step 9: Record final verification**

Run:

```bash
npm test
git log -8 --oneline
```

Expected: all tests pass and the task commits appear in order:

1. `test: define portfolio atlas acceptance structure`
2. `feat: establish portfolio atlas shell and identity`
3. `feat: replace work cards with product flat lays`
4. `feat: turn product lab into runnable flat lays`
5. `feat: reshape experience and capabilities as atlas figures`
6. `feat: complete responsive portfolio atlas`
7. `feat: add resilient atlas interaction state`
8. `fix: finish and verify portfolio technical atlas`

- [ ] **Step 10: Deliver the required Craft Report**

Include this evidence-based receipt in the final implementation handoff:

```markdown
## Craft Report

**Checked:** Brief success metric; anti-slop rules; hierarchy; type; full-palette figure coding; light/dark contrast; artifact interaction; keyboard and touch access; responsive behavior; reduced motion; local-link reliability; idle performance.

**Passed:** List only checks supported by the final browser run and test output.

**Changed:** Cite each final polish change with its file and the specific brief, accessibility, or ui-craft rule it satisfies.

**Left alone:** Record intentional choices such as the full four-color atlas coding, static non-link plates, and unchanged linked prototype pages.

**Verdict:** State either “ship it” or the single remaining blocker.
```
