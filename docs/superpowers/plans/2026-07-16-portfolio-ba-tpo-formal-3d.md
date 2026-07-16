# Portfolio BA/TPO Formal 3D Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition the root portfolio toward BA and TPO roles with an honest PDPA proof point, a formal white/blue/orange visual system, and a controlled CSS 3D product dossier.

**Architecture:** Preserve the existing single-file static homepage and its content order. Add a dependency-free Node contract test, replace the decorative hero map with an isolated HTML/CSS dossier, and use one scoped pointer controller that writes bounded CSS custom properties without a continuous animation loop.

**Tech Stack:** HTML5, CSS custom properties and 3D transforms, vanilla JavaScript, Node.js 22 built-in test runner

## Global Constraints

- Production remains one static `index.html` with no build step.
- Use no Three.js, WebGL, canvas renderer, or new JavaScript dependency.
- Use `Pakawat Smutkun — Full-Stack Developer moving toward BA & Product` as the exact document title.
- Use `Open to Business Analyst & Technical Product Owner roles — a developer who works close to the business side.` as the exact availability copy.
- Use `Once owned a product end-to-end — PDPA compliance build, requirements to delivery.` as the exact proof line.
- Keep the evidence register at exactly four statistics; the PDPA proof is not a fifth statistic.
- Keep the hero subtitle, PDPA experience bullet, job titles, experience verbs, skills, Prototype Lab, Background copy, links, and calls to action unchanged.
- Do not imply specification authorship; non-PDPA BA/product involvement is limited to joining requirements talks, giving input, and pushing back.
- Apply the white, formal-blue, and formal-orange system across the full page with no automatic dark theme.
- Restrict dimensional pointer motion to direct hero engagement; provide static coarse-pointer and reduced-motion states.
- Preserve the existing information architecture, semantic landmarks, skip link, keyboard navigation, and mobile navigation behavior.

## File Structure

- Modify: `index.html` — production content, theme, dossier component, responsive styles, and scoped interaction controller
- Create: `tests/portfolio-homepage.test.mjs` — dependency-free static contract tests for copy, structure, theme, dependency removal, and motion fallbacks
- Preserve: `preview.webp` — existing Open Graph image remains unchanged

---

### Task 1: Lock the Honest Positioning Contract

**Files:**
- Create: `tests/portfolio-homepage.test.mjs`
- Modify: `index.html:6-17`
- Modify: `index.html:629-660`
- Modify: `index.html:1835-1843`
- Modify: `index.html:2001-2020`

**Interfaces:**
- Consumes: Existing root homepage HTML and the exact copy in the approved design spec
- Produces: `tests/portfolio-homepage.test.mjs`, `.evidence-proof`, and the exact BA/TPO content contract used by every later task

- [ ] **Step 1: Create the failing content contract test**

```js
// tests/portfolio-homepage.test.mjs
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");
const compact = html.replace(/\s+/g, " ");

function sectionBetween(start, end) {
  const startIndex = html.indexOf(start);
  const endIndex = html.indexOf(end, startIndex);
  assert.notEqual(startIndex, -1, `missing start marker: ${start}`);
  assert.notEqual(endIndex, -1, `missing end marker: ${end}`);
  return html.slice(startIndex, endIndex);
}

test("uses the approved honest BA/TPO positioning", () => {
  assert.ok(
    compact.includes(
      "<title> Pakawat Smutkun — Full-Stack Developer moving toward BA &amp; Product </title>",
    ),
  );
  assert.ok(
    compact.includes(
      "Open to Business Analyst &amp; Technical Product Owner roles — a developer who works close to the business side.",
    ),
  );
  assert.ok(
    compact.includes(
      "Once owned a product end-to-end — PDPA compliance build, requirements to delivery.",
    ),
  );
  assert.doesNotMatch(
    html,
    /Technical Product Owner &(?:amp;)? Full-Stack Developer/,
  );
});

test("keeps four evidence statistics and places PDPA proof after the grid", () => {
  const evidence = sectionBetween(
    '<section class="section-tight" aria-label="Portfolio evidence">',
    '<section class="section" id="experience">',
  );

  assert.equal([...evidence.matchAll(/class="evidence-item"/g)].length, 4);
  assert.match(
    evidence,
    /<\/div>\s*<p class="wrap evidence-proof reveal">\s*Once owned a product end-to-end — PDPA compliance build, requirements to delivery\.\s*<\/p>/,
  );
});

test("preserves protected developer and PDPA copy", () => {
  assert.ok(
    compact.includes(
      "5+ Years engineering business systems where <strong>Floorplans, Reports, Workflows, and Field Teams</strong> need to operate as one reliable product.",
    ),
  );
  assert.ok(
    compact.includes(
      "<strong>PDPA Project Lead:</strong> acted as product owner, gathered requirements, and translated business needs into development work.",
    ),
  );
  assert.ok(compact.includes("Software engineering foundation, business-system bias."));
});
```

- [ ] **Step 2: Run the contract test and confirm the old homepage fails it**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: FAIL in `uses the approved honest BA/TPO positioning` because the current title and availability copy are still present.

- [ ] **Step 3: Apply the exact content changes and add the quiet proof line**

Use the exact head and hero text:

```html
<title>
  Pakawat Smutkun — Full-Stack Developer moving toward BA &amp; Product
</title>

<div class="availability reveal">
  Open to Business Analyst &amp; Technical Product Owner roles — a developer who
  works close to the business side.
</div>
```

Place this element after the closing tag for `.wrap.evidence` and before the evidence section closes:

```html
<p class="wrap evidence-proof reveal">
  Once owned a product end-to-end — PDPA compliance build, requirements to
  delivery.
</p>
```

Add the initial proof styling next to the evidence rules:

```css
.evidence-proof {
  position: relative;
  margin: 18px auto 0;
  padding-left: 18px;
  color: var(--steel);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  line-height: 1.55;
}
.evidence-proof::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.3em;
  bottom: 0.3em;
  width: 2px;
  background: var(--signal);
}
```

- [ ] **Step 4: Run the contract test and metadata audit**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 3 tests pass.

Run: `rg -n "Technical Product Owner &|og:title|twitter:title|meta name=\"description\"" index.html`

Expected: no old title match; the unchanged description and any social-title tag use no old positioning.

- [ ] **Step 5: Commit the positioning contract**

```bash
git add index.html tests/portfolio-homepage.test.mjs
git commit -m "feat: reposition portfolio for BA and TPO roles"
```

---

### Task 2: Establish the Formal Light Foundation

**Files:**
- Modify: `tests/portfolio-homepage.test.mjs`
- Modify: `index.html:13-125`
- Modify: `index.html:215-390`
- Modify: `index.html:1580-1652`
- Modify: `index.html:1790-1794`
- Modify: `index.html:3550-3933`

**Interfaces:**
- Consumes: Exact content and `.evidence-proof` from Task 1
- Produces: Approved palette tokens, `Source Serif 4`, light global surfaces, light navigation/buttons, and an HTML document with no starfield or runtime renderer code

- [ ] **Step 1: Extend the test suite with theme and dependency assertions**

Append:

```js
test("defines the approved formal light foundation", () => {
  assert.match(html, /--ink:\s*#fafaf8/i);
  assert.match(html, /--ink-2:\s*#ffffff/i);
  assert.match(html, /--ink-3:\s*#eef3f6/i);
  assert.match(html, /--paper:\s*#17324a/i);
  assert.match(html, /--draft-light:\s*#315a78/i);
  assert.match(html, /--signal:\s*#a94724/i);
  assert.match(html, /--line:\s*rgba\(23,\s*50,\s*74,\s*0\.14\)/i);
  assert.match(html, /family=Source\+Serif\+4/);
  assert.match(html, /--font-display:\s*"Source Serif 4",\s*Georgia,\s*serif/);
});

test("has no canvas or external runtime renderer", () => {
  assert.doesNotMatch(html, /starfield/i);
  assert.doesNotMatch(html, /\bTHREE\b|WebGLRenderer|<canvas\b/i);
});
```

- [ ] **Step 2: Run the tests and confirm the dark foundation fails**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: the 3 Task 1 tests pass; both new tests fail because the old dark tokens and starfield code remain.

- [ ] **Step 3: Replace the font request and root tokens**

Use one Google Fonts request:

```html
<link
  href="https://fonts.googleapis.com/css2?family=Azeret+Mono:wght@400;500;600&amp;family=Source+Sans+3:wght@400;500;600;700&amp;family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&amp;display=swap"
  rel="stylesheet"
/>
```

Replace the root palette and typography tokens with:

```css
:root {
  --ink: #fafaf8;
  --ink-2: #ffffff;
  --ink-3: #eef3f6;
  --draft: #315a78;
  --draft-light: #315a78;
  --signal: #a94724;
  --signal-dark: #7f341d;
  --paper: #17324a;
  --paper-dim: #3f5261;
  --steel: #5c6973;
  --steel-2: #7b8790;
  --coral: #a94724;
  --line: rgba(23, 50, 74, 0.14);
  --line-strong: rgba(23, 50, 74, 0.26);
  --surface: #ffffff;
  --surface-2: #f5f7f8;
  --shadow: rgba(23, 50, 74, 0.12);
  --font-display: "Source Serif 4", Georgia, serif;
  --font-body: "Source Sans 3", system-ui, sans-serif;
  --font-mono: "Azeret Mono", ui-monospace, monospace;
  --wrap: min(1160px, calc(100vw - 40px));
  --radius: 6px;
  --section: clamp(72px, 10vw, 132px);
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);
  --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
}
```

- [ ] **Step 4: Convert the global canvas, navigation, controls, and section rhythm**

Use these final shared rules, replacing only the corresponding dark declarations rather than adding a second competing theme block. Retain every unlisted sizing, layout, and transition declaration in the existing selectors:

```css
html {
  scroll-behavior: smooth;
  scroll-padding-top: 112px;
  background: var(--ink);
}
body {
  margin: 0;
  min-width: 320px;
  overflow-x: hidden;
  color: var(--paper);
  background:
    radial-gradient(circle at 12% 5%, rgba(49, 90, 120, 0.08), transparent 30rem),
    linear-gradient(rgba(23, 50, 74, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(23, 50, 74, 0.035) 1px, transparent 1px),
    var(--ink);
  background-size: auto, 42px 42px, 42px 42px, auto;
  font-family: var(--font-body);
  -webkit-font-smoothing: antialiased;
}
.nav {
  position: sticky;
  top: 0;
  z-index: 40;
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(16px);
}
.nav-links a { color: var(--steel); }
.nav-links a:hover,
.nav-links a:focus-visible { color: var(--paper); }
.btn {
  border: 1px solid var(--line-strong);
  border-radius: var(--radius);
  color: var(--paper);
  background: var(--ink-2);
}
.btn:hover,
.btn:focus-visible {
  border-color: var(--signal);
  color: var(--signal-dark);
  background: rgba(169, 71, 36, 0.06);
}
.btn-primary {
  border-color: var(--paper);
  color: var(--ink-2);
  background: var(--paper);
}
.btn-primary:hover,
.btn-primary:focus-visible {
  border-color: var(--signal);
  color: var(--ink-2);
  background: var(--signal);
}
#experience,
#prototype-lab,
#background,
.footer {
  background: var(--ink-3);
}
```

Update the mobile menu surface to `rgba(255, 255, 255, 0.98)`. Remove `body::before`, the body `grid-breathe` animation, and the obsolete dark scan treatment.

- [ ] **Step 5: Remove the unused renderer implementation**

Delete all of these units from `index.html`:

```html
<div class="starfield" aria-hidden="true">
  <canvas id="starfieldCanvas"></canvas>
</div>
```

Delete `.starfield`, `.starfield canvas`, and the entire commented `<script type="module">` block that imports Three.js. Do not replace them with another canvas or module script.

- [ ] **Step 6: Run tests and static renderer checks**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 5 tests pass.

Run: `rg -n "starfield|THREE|WebGLRenderer|<canvas" index.html`

Expected: no output.

- [ ] **Step 7: Commit the formal foundation**

```bash
git add index.html tests/portfolio-homepage.test.mjs
git commit -m "style: establish formal light portfolio theme"
```

---

### Task 3: Replace the Hero Map With the Product Dossier

**Files:**
- Modify: `tests/portfolio-homepage.test.mjs`
- Modify: `index.html:391-627`
- Modify: `index.html:1506-1549`
- Modify: `index.html:1859-1997`

**Interfaces:**
- Consumes: Task 2 palette tokens and the existing `.hero-grid`
- Produces: `#productDossier`, `.product-dossier`, `.dossier-stage`, and three decorative dossier sheets used by the pointer controller in Task 4

- [ ] **Step 1: Add a failing dossier structure test**

Append:

```js
test("renders one decorative three-layer product dossier", () => {
  assert.match(
    html,
    /id="productDossier"\s+class="product-dossier reveal"\s+aria-hidden="true"/,
  );
  assert.equal([...html.matchAll(/class="dossier-sheet /g)].length, 3);
  assert.match(html, /Business context/);
  assert.match(html, /Constraints and decisions/);
  assert.match(html, /PDPA compliance build/);
  assert.match(html, /Product owner · requirements → delivery/);
  assert.doesNotMatch(html, /class="map-shell|class="map-stage|class="map-note/);
});
```

- [ ] **Step 2: Run the test and confirm the old hero map fails it**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 5 tests pass; `renders one decorative three-layer product dossier` fails because `#productDossier` does not exist.

- [ ] **Step 3: Replace the map markup with the approved dossier markup**

Replace the entire `.map-shell` element with:

```html
<div
  id="productDossier"
  class="product-dossier reveal"
  aria-hidden="true"
>
  <div class="dossier-stage">
    <div class="dossier-sheet dossier-sheet-context">
      <div class="dossier-index">CONTEXT / 01</div>
      <div class="dossier-rule"></div>
      <div class="dossier-title">Business context</div>
      <div class="dossier-register">
        <span>Operational need</span><b>Understand</b>
        <span>Workflow impact</span><b>Clarify</b>
        <span>System constraint</span><b>Surface</b>
      </div>
    </div>
    <div class="dossier-sheet dossier-sheet-contribution">
      <div class="dossier-index">CONTRIBUTION / 02</div>
      <div class="dossier-rule"></div>
      <div class="dossier-title">Constraints and decisions</div>
      <div class="dossier-register">
        <span>Requirements talks</span><b>Join</b>
        <span>Implementation input</span><b>Give</b>
        <span>Unclear constraints</span><b>Push back</b>
      </div>
    </div>
    <div class="dossier-sheet dossier-sheet-proof">
      <div class="dossier-index">PRODUCT EVIDENCE / 03</div>
      <div class="dossier-rule"></div>
      <div class="dossier-title">PDPA compliance build</div>
      <p class="dossier-summary">
        Product owner · requirements → delivery
      </p>
      <div class="dossier-proof">OWNED END-TO-END</div>
      <div class="dossier-footer">
        <span>FULL-STACK FOUNDATION</span>
        <span>BA / TPO DIRECTION</span>
      </div>
    </div>
  </div>
</div>
```

- [ ] **Step 4: Replace hero-map styles with the isolated dossier component**

Delete the selectors from `.map-shell` through `.map-stage .map-label`, plus every `.motion-ok .map-*` rule. Add:

```css
.product-dossier {
  --dossier-rx: 0deg;
  --dossier-ry: 0deg;
  position: relative;
  min-height: 540px;
  overflow: hidden;
  perspective: 1200px;
  border: 1px solid var(--line-strong);
  border-radius: var(--radius);
  background:
    linear-gradient(rgba(23, 50, 74, 0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(23, 50, 74, 0.055) 1px, transparent 1px),
    var(--ink-3);
  background-size: 28px 28px, 28px 28px, auto;
  contain: paint;
}
.product-dossier::before {
  content: "FORMAL PRODUCT DOSSIER";
  position: absolute;
  left: 20px;
  top: 18px;
  color: var(--steel-2);
  font-family: var(--font-mono);
  font-size: 0.64rem;
  letter-spacing: 0.12em;
}
.dossier-stage {
  position: absolute;
  inset: 58px 32px 34px;
  transform-style: preserve-3d;
  transform: rotateX(var(--dossier-rx)) rotateY(var(--dossier-ry));
  transition: transform 360ms var(--ease-out-quart);
}
.dossier-sheet {
  position: absolute;
  left: 50%;
  top: 50%;
  width: min(78%, 390px);
  min-height: 330px;
  padding: clamp(24px, 3vw, 34px);
  border: 1px solid var(--line-strong);
  color: var(--paper);
  background: rgba(255, 255, 255, 0.97);
  box-shadow: 0 22px 48px var(--shadow);
  transform-style: preserve-3d;
  backface-visibility: hidden;
}
.dossier-sheet-context {
  transform: translate3d(-58%, -43%, -48px);
  opacity: 0.58;
}
.dossier-sheet-contribution {
  transform: translate3d(-54%, -47%, -24px);
  opacity: 0.8;
}
.dossier-sheet-proof {
  transform: translate3d(-50%, -50%, 0);
}
.dossier-index {
  color: var(--steel-2);
  font-family: var(--font-mono);
  font-size: 0.64rem;
  letter-spacing: 0.11em;
}
.dossier-rule {
  height: 1px;
  margin: 14px 0 22px;
  background: var(--line-strong);
}
.dossier-title {
  font-family: var(--font-display);
  font-size: clamp(1.55rem, 3vw, 2.25rem);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.025em;
}
.dossier-register {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 0;
  margin-top: 28px;
  border-top: 1px solid var(--line);
}
.dossier-register span,
.dossier-register b {
  padding: 10px 0;
  border-bottom: 1px solid var(--line);
  font-size: 0.78rem;
}
.dossier-register span { color: var(--steel); }
.dossier-register b {
  color: var(--draft-light);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  text-transform: uppercase;
}
.dossier-summary {
  margin: 18px 0 0;
  color: var(--steel);
  font-size: 0.92rem;
}
.dossier-proof {
  margin-top: 28px;
  border: 1px solid rgba(169, 71, 36, 0.5);
  padding: 11px 13px;
  color: var(--signal-dark);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.06em;
}
.dossier-footer {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  margin-top: 26px;
  color: var(--steel-2);
  font-family: var(--font-mono);
  font-size: 0.56rem;
  letter-spacing: 0.05em;
}
@supports not (transform-style: preserve-3d) {
  .dossier-stage { transform: none; }
  .dossier-sheet-context { transform: translate(-58%, -43%); }
  .dossier-sheet-contribution { transform: translate(-54%, -47%); }
  .dossier-sheet-proof { transform: translate(-50%, -50%); }
}
```

- [ ] **Step 5: Run the dossier contract test**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 6 tests pass.

Run: `rg -n "map-shell|map-stage|map-note|map-route" index.html`

Expected: no output.

- [ ] **Step 6: Commit the dossier component**

```bash
git add index.html tests/portfolio-homepage.test.mjs
git commit -m "feat: add formal product dossier hero"
```

---

### Task 4: Add Bounded Engagement-Only Motion

**Files:**
- Modify: `tests/portfolio-homepage.test.mjs`
- Modify: `index.html:3483-3548`

**Interfaces:**
- Consumes: `#productDossier`, `--dossier-rx`, and `--dossier-ry` from Task 3
- Produces: A scoped pointer controller with one pending animation-frame update, 4-degree X cap, 6-degree Y cap, and deterministic reset behavior

- [ ] **Step 1: Add a failing controller contract test**

Append:

```js
test("bounds dossier motion and only responds to direct engagement", () => {
  assert.match(html, /\(hover: hover\) and \(pointer: fine\)/);
  assert.match(html, /prefers-reduced-motion: reduce/);
  assert.match(html, /addEventListener\("pointerenter"/);
  assert.match(html, /addEventListener\("pointermove"/);
  assert.match(html, /addEventListener\("pointerleave"/);
  assert.match(html, /--dossier-rx/);
  assert.match(html, /--dossier-ry/);
  assert.match(html, /normalizedY \* 4/);
  assert.match(html, /normalizedX \* 6/);
  assert.match(html, /requestAnimationFrame\(renderDossierTilt\)/);
  assert.doesNotMatch(html, /requestAnimationFrame\(animate\)|function animate\(/);
});
```

- [ ] **Step 2: Run the test and confirm the static dossier fails it**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 6 tests pass; the new motion contract test fails because the controller is absent.

- [ ] **Step 3: Add the scoped dossier controller inside the existing inline script**

Insert after the scroll-progress setup and before the intersection observer:

```js
const productDossier = document.getElementById("productDossier");

if (productDossier) {
  const finePointer = window.matchMedia(
    "(hover: hover) and (pointer: fine)",
  );
  const reducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)",
  );
  let dossierBounds = null;
  let latestPointer = null;
  let dossierFrame = 0;

  const clampUnit = (value) => Math.min(1, Math.max(-1, value));

  const resetDossierTilt = () => {
    window.cancelAnimationFrame(dossierFrame);
    dossierFrame = 0;
    dossierBounds = null;
    latestPointer = null;
    productDossier.style.removeProperty("--dossier-rx");
    productDossier.style.removeProperty("--dossier-ry");
  };

  const renderDossierTilt = () => {
    dossierFrame = 0;
    if (!dossierBounds || !latestPointer) return;

    const normalizedX = clampUnit(
      ((latestPointer.clientX - dossierBounds.left) / dossierBounds.width) * 2 -
        1,
    );
    const normalizedY = clampUnit(
      ((latestPointer.clientY - dossierBounds.top) / dossierBounds.height) * 2 -
        1,
    );

    productDossier.style.setProperty(
      "--dossier-rx",
      `${(-normalizedY * 4).toFixed(2)}deg`,
    );
    productDossier.style.setProperty(
      "--dossier-ry",
      `${(normalizedX * 6).toFixed(2)}deg`,
    );
  };

  const queueDossierTilt = (event) => {
    if (!finePointer.matches || reducedMotion.matches) return;
    latestPointer = event;
    if (!dossierFrame) {
      dossierFrame = window.requestAnimationFrame(renderDossierTilt);
    }
  };

  productDossier.addEventListener("pointerenter", (event) => {
    if (!finePointer.matches || reducedMotion.matches) return;
    dossierBounds = productDossier.getBoundingClientRect();
    queueDossierTilt(event);
  });
  productDossier.addEventListener("pointermove", queueDossierTilt, {
    passive: true,
  });
  productDossier.addEventListener("pointerleave", resetDossierTilt);
  window.addEventListener("blur", resetDossierTilt);
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) resetDossierTilt();
  });
  window.addEventListener("resize", resetDossierTilt);
  finePointer.addEventListener("change", resetDossierTilt);
  reducedMotion.addEventListener("change", resetDossierTilt);
}
```

- [ ] **Step 4: Add the keyboard-focus emphasis without making artwork focusable**

```css
.hero:focus-within .product-dossier {
  --dossier-rx: -1deg;
  --dossier-ry: 2deg;
}
```

Keep `aria-hidden="true"` and do not add `tabindex` to the dossier or its sheets.

- [ ] **Step 5: Run the motion contract test**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 7 tests pass.

Run: `rg -n "requestAnimationFrame" index.html`

Expected: one call scheduling `renderDossierTilt`; no recursive animation loop.

- [ ] **Step 6: Commit controlled motion**

```bash
git add index.html tests/portfolio-homepage.test.mjs
git commit -m "feat: add responsive dossier interaction"
```

---

### Task 5: Migrate Every Remaining Component to the Formal Palette

**Files:**
- Modify: `tests/portfolio-homepage.test.mjs`
- Modify: `index.html:629-1474`
- Modify: `index.html:2169-3479`

**Interfaces:**
- Consumes: Task 2 palette tokens and existing section/component selectors
- Produces: Full-page white/pale-blue surfaces, formal-blue diagrams, formal-orange evidence/active states, and no legacy dark/neon color literals

- [ ] **Step 1: Add a failing legacy-palette test**

Append:

```js
test("removes the legacy dark and neon palette from the homepage", () => {
  const legacyPatterns = [
    /#101216|#171b20|#20262c/i,
    /#2f6f9f|#2f8f54|#7bd88f|#75b4d5|#ff6b5f/i,
    /#f4f7f2|#dce5dd|#a9b1b8|#79848c/i,
    /rgba\(\s*16\s*,\s*18\s*,\s*22\s*,/i,
    /rgba\(\s*123\s*,\s*216\s*,\s*143\s*,/i,
    /rgba\(\s*117\s*,\s*180\s*,\s*213\s*,/i,
    /rgba\(\s*47\s*,\s*111\s*,\s*159\s*,/i,
  ];

  for (const pattern of legacyPatterns) {
    assert.doesNotMatch(html, pattern, `legacy color remains: ${pattern}`);
  }
});
```

- [ ] **Step 2: Run the test and inventory every remaining legacy literal**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 7 tests pass; the legacy-palette test fails and names the first remaining color.

Run: `rg -n "#101216|#171b20|#20262c|#2f6f9f|#2f8f54|#7bd88f|#75b4d5|#ff6b5f|#f4f7f2|#dce5dd|#a9b1b8|#79848c|rgba\(\s*16\s*,\s*18\s*,\s*22|rgba\(\s*123\s*,\s*216\s*,\s*143|rgba\(\s*117\s*,\s*180\s*,\s*213|rgba\(\s*47\s*,\s*111\s*,\s*159" index.html`

Expected: output identifies the remaining CSS declarations and inline SVG attributes to migrate.

- [ ] **Step 3: Convert shared component surfaces in their existing selector blocks**

Use these final surface and interaction values throughout the existing component rules:

```css
.stack-mark,
.feature-panel,
.project,
.lab-panel,
.skill-cluster,
.ai-workflow,
.background-panel,
.language-row {
  border-color: var(--line);
  color: var(--paper);
  background: var(--ink-2);
  box-shadow: 0 12px 30px rgba(23, 50, 74, 0.06);
}
.feature-panel:hover,
.project:hover,
.skill-cluster:hover {
  transform: translateY(-2px);
  border-color: rgba(169, 71, 36, 0.45);
  background: var(--surface-2);
}
.prototype,
.project .prototype,
.lab-board {
  border-color: var(--line);
  background:
    linear-gradient(rgba(23, 50, 74, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(23, 50, 74, 0.05) 1px, transparent 1px),
    var(--ink-3);
  background-size: 24px 24px, 24px 24px, auto;
}
.section-kicker,
.evidence strong,
.skill-head h3,
.level-chip {
  color: var(--signal-dark);
}
.role li::before { background: var(--signal); }
.role-company,
.project-tag,
.ai-workflow-label,
.lab-bet em {
  color: var(--draft-light);
}
```

Keep compact chips/status labels rounded where they remain meaningful. Reduce card and panel corner radii to the shared 6px token; remove neon glow and black shadow declarations.

- [ ] **Step 4: Apply the context-aware literal color mapping to CSS and inline SVG**

Use this mapping for final values:

```text
#7bd88f and green rgba values       -> #a94724 / rgba(169, 71, 36, alpha)
#75b4d5 and blue rgba values        -> #315a78 / rgba(49, 90, 120, alpha)
#2f6f9f and draft rgba values       -> #315a78 / rgba(49, 90, 120, alpha)
#ff6b5f and coral rgba values       -> #a94724 / rgba(169, 71, 36, alpha)
#f4f7f2 used as text/stroke         -> #17324a
#dce5dd used as secondary text      -> #3f5261
#a9b1b8 used as muted text          -> #5c6973
#79848c used as quiet metadata      -> #7b8790
rgba(16, 18, 22, alpha) surfaces    -> rgba(255, 255, 255, alpha)
rgba(244, 247, 242, alpha) grids    -> rgba(23, 50, 74, alpha)
```

Preserve each original alpha unless it makes text fail contrast; text should use the solid approved tokens instead of translucent colors. Do not recolor third-party technology logo images.

- [ ] **Step 5: Verify the full palette migration**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 8 tests pass.

Run the legacy-color `rg` command from Step 2 again.

Expected: no output.

- [ ] **Step 6: Commit the full-page visual migration**

```bash
git add index.html tests/portfolio-homepage.test.mjs
git commit -m "style: migrate portfolio sections to formal palette"
```

---

### Task 6: Harden Motion, Responsive Layout, Accessibility, and Browser QA

**Files:**
- Modify: `tests/portfolio-homepage.test.mjs`
- Modify: `index.html:143-213`
- Modify: `index.html:1476-1778`

**Interfaces:**
- Consumes: Completed dossier, pointer controller, and full-page theme
- Produces: Formal one-time reveals, no continuous animation, tablet/mobile dossier layouts, reduced-motion behavior, and verified browser output

- [ ] **Step 1: Add failing formal-motion and responsive-fallback tests**

Append:

```js
test("uses formal one-time motion with responsive static fallbacks", () => {
  assert.doesNotMatch(html, /filter:\s*blur\(/);
  assert.doesNotMatch(html, /animation:[^;]*\binfinite\b/);
  assert.match(
    html,
    /@media \(max-width: 980px\)[\s\S]*?\.product-dossier[\s\S]*?min-height:\s*460px/,
  );
  assert.match(
    html,
    /@media \(max-width: 720px\)[\s\S]*?\.product-dossier[\s\S]*?min-height:\s*390px/,
  );
  assert.match(
    html,
    /@media \(prefers-reduced-motion: reduce\)[\s\S]*?\.product-dossier/,
  );
});
```

- [ ] **Step 2: Run the tests and confirm old theatrical motion fails**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 8 tests pass; the new motion/fallback test fails because blur and continuous pulse rules remain.

- [ ] **Step 3: Replace theatrical reveals and continuous pulses**

Use:

```css
@keyframes enter-panel {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.reveal {
  opacity: 1;
  transform: none;
}
.motion-ok .reveal {
  opacity: 0;
  transform: translateY(12px);
}
.motion-ok .reveal.in {
  animation: enter-panel 0.46s var(--ease-out-quart) both;
}
.availability::before {
  background: var(--signal);
  box-shadow: 0 0 0 4px rgba(169, 71, 36, 0.1);
}
```

Delete every `filter: blur(...)` declaration. Remove `soft-pulse` and every infinite animation assignment. Preserve existing line-draw and node-entry animations as one-time `both` animations only.

- [ ] **Step 4: Add explicit dossier breakpoints and reduced-motion behavior**

Add inside the existing media queries:

```css
@media (max-width: 980px) {
  .product-dossier { min-height: 460px; }
  .dossier-stage { inset: 54px 9vw 32px; }
}

@media (max-width: 720px) {
  .availability {
    align-items: flex-start;
    line-height: 1.5;
  }
  .product-dossier { min-height: 390px; }
  .dossier-stage { inset: 48px 12px 20px; }
  .dossier-sheet {
    width: min(84%, 330px);
    min-height: 270px;
    padding: 22px;
  }
  .dossier-sheet-context { transform: translate3d(-56%, -42%, -28px); }
  .dossier-sheet-contribution { transform: translate3d(-53%, -46%, -14px); }
  .dossier-footer { display: none; }
}

@media (prefers-reduced-motion: reduce) {
  .product-dossier {
    --dossier-rx: 0deg !important;
    --dossier-ry: 0deg !important;
  }
  .dossier-stage { transition: none; }
}
```

Keep the existing global reduced-motion reset, skip link, focus outline, mobile navigation, and no-script reveal fallback.

- [ ] **Step 5: Run automated verification**

Run: `node --test tests/portfolio-homepage.test.mjs`

Expected: 9 tests pass.

Run: `git diff --check`

Expected: no output.

Run: `rg -n "filter: blur|\binfinite\b|starfield|THREE|WebGLRenderer|<canvas" index.html`

Expected: no output.

- [ ] **Step 6: Serve the site for browser verification**

Run: `python3 -m http.server 8000`

Expected: `Serving HTTP on :: port 8000` and `http://localhost:8000/` loads the root portfolio.

- [ ] **Step 7: Verify desktop, tablet, and mobile layouts in a browser**

Inspect `http://localhost:8000/` at 1440 x 900, 768 x 1024, and 390 x 844. Confirm all of these observations:

```text
The first screen shows developer foundation, BA/TPO direction, and PDPA proof.
The page is light under both OS color preferences.
The hero dossier is legible and never clips or creates horizontal scrolling.
The evidence register contains four statistics plus one separate proof line.
All later sections use white or pale-blue surfaces with blue/orange accents.
Inline diagrams remain legible against light surfaces.
The mobile navigation opens, closes, closes on Escape, and restores focus.
Tab order reaches every existing link and button with a visible focus outline.
```

- [ ] **Step 8: Verify engagement and fallback behavior in a browser**

Confirm all of these observations:

```text
Pointer movement inside the hero produces restrained dossier tilt.
Pointer exit and window blur return the dossier to neutral.
The dossier does not move while idle.
Reduced-motion emulation keeps the dossier static and content visible.
Touch/coarse-pointer emulation keeps the dossier static.
Disabling JavaScript leaves the content and static dossier visible.
The browser console reports no errors.
```

Stop and return to the task that owns a failed observation before committing; rerun Steps 5 through 8 after the correction.

- [ ] **Step 9: Commit responsive and accessibility hardening**

```bash
git add index.html tests/portfolio-homepage.test.mjs
git commit -m "test: harden portfolio motion and responsive fallbacks"
```

---

## Final Verification

Run from `/Users/pakawat/Projects/labs/portfolio`:

```bash
node --test tests/portfolio-homepage.test.mjs
git diff --check HEAD~6..HEAD
git status --short
```

Expected:

```text
9 tests pass.
No whitespace errors are reported.
Only pre-existing unrelated workspace changes, if still present, appear in status.
```

Review the final commit range with:

```bash
git log --oneline -6
git diff --stat HEAD~6..HEAD
```

Expected: six focused commits affecting `index.html` and `tests/portfolio-homepage.test.mjs`; no change to `preview.webp`, project prototypes, or protected content files.
