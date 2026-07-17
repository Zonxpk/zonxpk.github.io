# OP Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `index.html` as a Teenage Engineering OP-style "Lab White" instrument page per `docs/superpowers/specs/2026-07-17-op-redesign-design.md`.

**Architecture:** One static HTML file containing all CSS and JS. Four color-coded bordered modules (01 WORK orange, 02 LAB cyan, 03 LOG yellow, 04 SPEC green) on a white chassis with a fixed instrument header. Verification is manual browser checks per task (no test framework exists; site is no-build).

**Tech Stack:** Vanilla HTML/CSS/JS. Zero dependencies, zero webfonts, zero requests beyond the document.

## Global Constraints

- Single file: `index.html`. No build step, no external requests (delete existing Google Fonts links).
- Colors: chassis `#f4f4f2`, panels `#e8e8e6`, ink `#111`, orange `#ff4d00`, cyan `#00a4c8`, yellow `#f5c400`, green `#3fa435`, LED red `#e03616`.
- Type: mono = `"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace` (labels/data/headers, uppercase, `letter-spacing:.08em`); body = `"Helvetica Neue", Helvetica, Arial, sans-serif`.
- Borders `1px solid #111`; no gradients, no blur shadows, corner radius ≤ 2px.
- Body text is always ink on white/aluminum. Accent colors only on UI/coding elements at ≥3:1.
- `prefers-reduced-motion: reduce` disables reveals, REC blink, SVG self-draw.
- Sound off by default; opt-in via header toggle; state in `localStorage['snd']`.
- All copy comes from the content inventory below — no invented facts.

## Content inventory (extracted from current index.html — the source of truth)

- Identity: Pakawat Smutkun · Bangkok, Thailand · pakawat.zon@gmail.com · (+66) 97-142-7997
- Links: resume `https://drive.google.com/uc?export=download&id=1B2tvM8jNeyZd6OBbq5haLpY4j3sO8lss`, GitHub `https://github.com/Zonxpk`, LinkedIn `https://www.linkedin.com/in/zonpk/`
- Thesis: 5+ years building systems where floorplans, reports, workflows, and field teams operate as one product. Status: available for technical product owner and full-stack roles.
- Hero stats: 5+ years · 200+ active users · 2,000+ branches · 10 DMMS modules
- WORK / DMMS: 10-module mall-operations platform; capability rows: Spatial intelligence (floorplan mapping, occupancy, revenue overlays, event booking) / Automation backbone (branch templates, validation, consolidation, custom exports) / Field operations (task assignment, SLA, check-ins, photo records) / Business pipeline (lead lifecycle, LINE OA bot reminders, pipeline reporting).
- WORK / secondary: Affiliate Referral System (LINE OA · attribution), Market Rental Management (floorplan · booking), Meal Order Management (QR menu · ops).
- LAB: empeo Performance Results → `performance-management/index.html` + handoff `performance-management/handoff.html`; ThaiMart → `thaimart/index.html` (+ 01/02/03 sub-pages); EduSight → `edusight/index.html`.
- LOG: 2026–now Software Engineer / 1Moby (ThaiBulkSMS: Pipedrive lead routing, banner management, SMS history search) · 2026 Software Engineer / blockfint (eKYC prototypes, integration support, 3 mo) · 2021–2026 Frontend Developer / CP ORIGIN (DMMS, ERP + LINE OA for 200+ users, reporting for 2,000+ branches, 4+ yrs) · 2020–2021 Software Engineer / Softnix Technology (PDPA product owner, mentorship, 1 yr) · 2020 Programmer / Thai Nippon Seiki (document approval system, factory ERP, 7 mo).
- SPEC: Frontend (React, Next.js, TypeScript, Vue, Angular, HTML, CSS) · Backend (Node.js, NestJS, Express, Go, Python, PHP, SQL) · State/Testing (React Query, Zustand, XState, Jest, Vitest, Agile/Scrum) · Cloud/Automation (GCP, AWS, Docker, Firebase, Git, n8n, AI integration, LINE OA) · AI toolchain (Cursor Composer 2.5 — everyday code; Claude Opus 4.8 — design/frontend; Codex GPT 5.5 — debugging; skills: Superpowers, Obsidian Vault, Ponytail, Loop Engineering) · Also: JavaScript, Kotlin, C#, QR workflows, reporting pipelines · Education: B.Sc. Software Engineering, Burapha University, 2020, GPA 3.53 · Languages: Thai native, English conversational.
- Footer: "Ready to make operations legible." · open to full-stack and product-engineering roles · email · © 2026 · shortcuts row.

---

### Task 1: Chassis — tokens, grid, header, footer skeleton

**Files:**
- Modify: `index.html` (full rewrite; old version stays in git history)

**Produces:** CSS custom properties (`--chassis --panel --ink --c-orange --c-cyan --c-yellow --c-green --c-led`), `.mono` label style, `.key` mechanical-button pattern, `.module` bordered-section pattern with left number rail, fixed header with `● REC` dot + section readout `<span id="readout">` + `SND` toggle `<button id="snd" aria-pressed="false">`, skip link, empty `<main>` with 4 module placeholders, footer shell.

- [ ] **Step 1:** Write the new document skeleton. Mechanical key pattern:

```css
.key {
  border: 1px solid var(--ink);
  background: var(--chassis);
  box-shadow: 2px 2px 0 var(--ink);
  transition: none;
}
.key:active { transform: translate(2px, 2px); box-shadow: none; }
.key:focus-visible { outline: 2px solid var(--c-orange); outline-offset: 2px; }
```

- [ ] **Step 2:** Verify: `python3 -m http.server 8000`, load page — header, empty modules, footer render with 1px borders; no console errors; zero external requests in the network tab.
- [ ] **Step 3:** Commit: `git commit -m "feat: OP chassis skeleton"`

### Task 2: Hero module + SVG signal path

**Files:** Modify: `index.html`

- [ ] **Step 1:** Hero: name as `h1`, thesis line, status readout (`AVAILABLE — TPO / FULL-STACK`), 4 hero stats as a mono data strip, contact keys (resume/GitHub/LinkedIn as `.key` links). Inline SVG schematic (`stroke:#111`, accent nodes in toy colors) with self-draw:

```css
.signal path { stroke-dasharray: 600; stroke-dashoffset: 600; animation: draw 1.2s steps(12) forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
@media (prefers-reduced-motion: reduce) { .signal path { animation: none; stroke-dashoffset: 0; } }
```

- [ ] **Step 2:** Verify in browser; commit.

### Task 3: Module 01 WORK (orange)

**Files:** Modify: `index.html`

- [ ] **Step 1:** DMMS flagship panel (title, one-paragraph frame, mono stat row `10 MODULES · 2,000+ BRANCHES · 200+ USERS`), 4 capability rows as bordered table-like rows (name + one terse line + tag chips), secondary strip: 3 compact bordered cells (name, one line, mono tag).
- [ ] **Step 2:** Verify; commit.

### Task 4: Module 02 LAB (cyan)

**Files:** Modify: `index.html`

- [ ] **Step 1:** 3 "cartridge" tiles, each: small SVG glyph, name, one-line pitch, `.key` links (empeo: report + handoff; ThaiMart: hub + 3 sub-links; EduSight: prototype). Hover lights a LED square in the module color (`.cart:hover .led { background: var(--c-cyan); }`).
- [ ] **Step 2:** Verify all 7 links resolve locally; commit.

### Task 5: Module 03 LOG (yellow)

**Files:** Modify: `index.html`

- [ ] **Step 1:** Experience as a semantic table (`<table>`, mono): YEAR · ROLE · UNIT · NOTE, 5 rows per content inventory. Mobile: rows stack via `display:block` at `<720px`.
- [ ] **Step 2:** Verify; commit.

### Task 6: Module 04 SPEC (green) + footer content

**Files:** Modify: `index.html`

- [ ] **Step 1:** One spec-sheet table: rows FRONTEND / BACKEND / STATE+TESTING / CLOUD+AUTOMATION / AI TOOLCHAIN / ALSO / EDUCATION / LANGUAGES, values comma-separated mono text. Footer: CTA line, email key, tel, © 2026, shortcuts spec row (`Q W E R → 01–04`).
- [ ] **Step 2:** Verify; commit.

### Task 7: Interactions — sound, readout, keys, reveals

**Files:** Modify: `index.html` (single `<script>` before `</body>`)

- [ ] **Step 1:** Implement:

```js
// sound: synthesized click, opt-in
let ctx = null;
const sndBtn = document.getElementById('snd');
let snd = localStorage.getItem('snd') === '1';
function paint() { sndBtn.setAttribute('aria-pressed', String(snd)); sndBtn.textContent = 'SND ' + (snd ? '●' : '○'); }
function click() {
  if (!snd) return;
  ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
  const o = ctx.createOscillator(), g = ctx.createGain();
  o.type = 'square'; o.frequency.value = 2200;
  g.gain.setValueAtTime(0.12, ctx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.02);
  o.connect(g).connect(ctx.destination); o.start(); o.stop(ctx.currentTime + 0.03);
}
sndBtn.addEventListener('click', () => { snd = !snd; localStorage.setItem('snd', snd ? '1' : '0'); paint(); click(); });
document.addEventListener('pointerdown', e => { if (e.target.closest('.key, .nav a')) click(); });
paint();

// readout: current section in header
const sections = [...document.querySelectorAll('section[data-code]')];
const readout = document.getElementById('readout');
new IntersectionObserver(es => {
  es.forEach(e => { if (e.isIntersecting) readout.textContent = e.target.dataset.code; });
}, { rootMargin: '-40% 0px -55% 0px' }).observe && sections.forEach(s =>
  new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) readout.textContent = e.target.dataset.code; }),
  { rootMargin: '-40% 0px -55% 0px' }).observe(s));

// QWER + 1-4 jump keys (ignore when typing)
const jump = { q: 0, w: 1, e: 2, r: 3, 1: 0, 2: 1, 3: 2, 4: 3 };
document.addEventListener('keydown', e => {
  if (e.target.matches('input, textarea, select') || e.metaKey || e.ctrlKey || e.altKey) return;
  const i = jump[e.key.toLowerCase()];
  if (i !== undefined && sections[i]) sections[i].scrollIntoView({ behavior: 'smooth' });
});

// reveals: quantized slide-in
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); }
}), { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
```

with CSS `.reveal { opacity:0; translate:0 8px; } .reveal.on { opacity:1; translate:0; transition: all .35s steps(4); }` gated behind `@media (prefers-reduced-motion: no-preference)`.

- [ ] **Step 2:** Verify: SND toggle persists across reload, click audible only when on; readout tracks scroll; Q/W/E/R and 1–4 jump; typing in future form fields would not trigger jumps; reveals fire once.
- [ ] **Step 3:** Commit: `git commit -m "feat: OP interactions (sound, readout, QWER, reveals)"`

### Task 8: A11y + final verification

**Files:** Modify: `index.html`

- [ ] **Step 1:** Pass: single `h1`, logical heading order, skip link works, all interactive elements reachable and visibly focused, REC blink disabled under reduced motion, contrast spot-check (ink on chassis = 16:1; accents only on ≥3:1 UI).
- [ ] **Step 2:** Browser verify desktop (1280px) + mobile (375px) screenshots; zero console errors; zero external requests.
- [ ] **Step 3:** Final commit.

## Self-review

- Spec coverage: all spec sections map to tasks 1–8 (visual system→1, hero/SVG→2, modules→3–6, tactility/sound/QWER/readout→7, a11y/perf→8). No gaps.
- No placeholders: copy is pinned in the content inventory; key code shown for the non-obvious patterns.
- Consistency: ids `snd`/`readout`, `data-code` attribute, `.key`/`.module`/`.reveal` class names used consistently across tasks.
