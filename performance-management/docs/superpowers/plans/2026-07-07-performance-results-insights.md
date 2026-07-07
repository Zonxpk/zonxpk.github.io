# Performance Results & Insights — Implementation Plan

> **For agentic workers:** This builds a single self-contained clickable HTML prototype. No test framework — each task's "verify" is opening `index.html` in a browser and observing the described result. Steps use checkbox (`- [ ]`) syntax.

**Goal:** A manager-facing "Performance Results & Insights" clickable prototype for empeo that surfaces all four evaluation sources together, adds trend/peer/synthesis layers, and derives an auditable pay/promotion recommendation.

**Architecture:** One self-contained `index.html` (inline CSS + vanilla JS). A single JS mock-data object drives every block. Charts hand-rolled in CSS/SVG. A tiny render layer reads the data object and paints blocks; interactions mutate a small state object and re-render affected blocks.

**Tech Stack:** HTML5, CSS (custom properties), vanilla JS (ES6), SVG. Google Fonts (Noto Sans Thai). No framework, no build, no dependencies.

## Global Constraints

- Single file: `index.html`. No external files except the Google Fonts link.
- Thai-first UI copy; empeo terminology (ผลการประเมิน, ประเมินตนเอง/จากหัวหน้า/เพื่อนร่วมงาน/องค์กร, น้ำหนัก).
- All scores stored /5 per topic; overall rolled to % + grade band.
- Grade bands: Excellence ≥90 · Exceeds 80–89 · Meets 65–79 · Below <65.
- Merit ranges: Excellence 8–10% · Exceeds 5–7% · Meets 3–4% · Below 0–2%.
- Gap flags: `self−others≥1.0`→blind spot(amber) · `others−self≥1.0`→sells-short(blue) · all high&tight→consistent strength(green) · mgr vs peer diverge→needs calibration.
- Brand: coral→orange gradient header, white cards on `#F7F7F5`, rounded corners, soft shadows.
- All numbers are illustrative mock data.

---

### Task 1: Skeleton, tokens, mock data, render scaffold

**Files:** Create `index.html`

**Produces:** global `DATA` object (employee, cycles, dimensions[], sources, comments), `STATE` object (`cycle`, `visibleSources`, `decision`), `render()` dispatcher, CSS custom-property token set (colors, spacing, radius, shadow), Noto Sans Thai loaded.

- [ ] HTML shell: `<head>` with Google Fonts Noto Sans Thai; `:root` tokens (brand orange, gray bg, semantic green/amber/blue/red, radius, shadow); base body styles; a `<main id="app">` container.
- [ ] Define `DATA`: one exemplar employee (name/role/team/tenure, Thai), two cycles (2024, 2025), 4 dimensions each with 4 source scores (/5) + weight + per-topic rows + comments, peer distribution array, per-cycle overall.
- [ ] Define `STATE = { cycle:'2025', visibleSources:{self,manager,peer,org:true}, decision:{merit,bonus,notes} }`.
- [ ] `render()` that clears `#app` and calls block renderers (stubbed to empty for now).
- **Verify:** open `index.html` — page loads, Thai font applied, no console errors, `DATA`/`STATE` inspectable.
- [ ] Commit: `feat: prototype scaffold — tokens, mock data, render dispatcher`

### Task 2: Verdict header (block 1) + helpers

**Files:** Modify `index.html`

**Consumes:** `DATA`, `STATE`. **Produces:** `overallPct(cycle)`, `gradeBand(pct)`, `recommend(cycle)` → `{merit, bonus, promo, whyLine}`; `renderHeader()`.

- [ ] Helpers: `overallPct` (weighted roll-up of dimension org/weighted scores → %), `gradeBand`, `recommend` applying the band→merit/bonus/promo mapping nudged by trend + peer percentile, producing the Thai "why" line.
- [ ] `renderHeader()`: coral→orange gradient card — avatar, name, role, team, tenure, cycle; big overall grade + %; 1-line synthesis; recommended-action pill.
- **Verify:** header renders with correct grade chip and a coherent recommendation pill for the 2025 exemplar.
- [ ] Commit: `feat: verdict header with derived recommendation`

### Task 3: 360 scorecard (block 2)

**Files:** Modify `index.html`

**Consumes:** `DATA.dimensions`, `STATE.visibleSources`. **Produces:** `gapFlag(dim)` → `{type,label,color}`; `renderScorecard()` with SVG/CSS marker tracks.

- [ ] `gapFlag(dim)` implementing the four gap rules against the dimension's source scores.
- [ ] `renderScorecard()`: one row per dimension — a 0–5 track (SVG or CSS) with four source markers (colored per source), weighted-average bar behind, dimension label, weighted score, and the gap badge. Respect `STATE.visibleSources`.
- **Verify:** four dimension rows render; a seeded blind-spot dimension shows amber badge; a consensus dimension shows green.
- [ ] Commit: `feat: 360 scorecard with source markers and gap flags`

### Task 4: Trend (block 3) + peer position (block 4)

**Files:** Modify `index.html`

**Consumes:** `DATA` cycles + peer distribution. **Produces:** `renderTrend()`, `renderPeer()`.

- [ ] `renderTrend()`: SVG sparkline of overall % across cycles/rounds + small per-dimension direction arrows.
- [ ] `renderPeer()`: SVG distribution curve/bars for the role with the employee marked + percentile text; trend-slope caption as potential proxy.
- **Verify:** trend line reflects cycle values; employee marker sits at the stated percentile on the distribution.
- [ ] Commit: `feat: trend sparkline and peer-position distribution`

### Task 5: Strengths & risks (block 5) + detailed breakdown (block 6)

**Files:** Modify `index.html`

**Consumes:** `DATA.dimensions`, `gapFlag`. **Produces:** `renderSynthesis()`, `renderDetail()` (collapsible).

- [ ] `renderSynthesis()`: auto-derived — top strengths (high + consensus), watch areas (low or high-gap), notable comments pulled from data.
- [ ] `renderDetail()`: faithful empeo table per dimension (topic · น้ำหนัก · per-source /5 · comment · rounds), collapsed by default with expand/collapse toggle.
- **Verify:** synthesis lists correct strengths/risks; detail table expands/collapses and matches source data.
- [ ] Commit: `feat: strengths/risks synthesis and expandable detail table`

### Task 6: Manager decision panel (block 7) + sticky bar (block 0)

**Files:** Modify `index.html`

**Consumes:** `recommend`, `STATE.decision`. **Produces:** `renderDecision()`, `renderStickyBar()`, scroll handler.

- [ ] `renderDecision()`: editable merit % / bonus / notes prefilled from `recommend()`; live "why" rationale line; readiness verdict. Edits update `STATE.decision` and the why-line.
- [ ] `renderStickyBar()` + scroll listener: shows name · cycle · grade · "ไปที่การตัดสินใจ" (smooth-scroll to block 7) once the header scrolls out.
- **Verify:** editing merit updates the why-line live; sticky bar appears on scroll and jump button scrolls to decision panel.
- [ ] Commit: `feat: manager decision panel and sticky context bar`

### Task 7: Interactions — cycle switch + source toggles + tooltips

**Files:** Modify `index.html`

**Consumes:** all renderers, `STATE`. **Produces:** wired controls.

- [ ] Cycle selector (2024/2025) → sets `STATE.cycle`, calls `render()`; numbers/trend update.
- [ ] Source toggle chips (self/manager/peer/org) → flip `STATE.visibleSources`, re-render scorecard.
- [ ] Hover tooltips on gap badges explaining each flag (Thai text).
- **Verify:** switching cycle changes header/scorecard/trend; toggling a source hides its markers; hovering a badge shows the explanation.
- [ ] Commit: `feat: cycle switching, source toggles, gap tooltips`

### Task 8: Polish + responsive + final review

**Files:** Modify `index.html`

- [ ] Spacing/typography/alignment pass to match empeo brand; ensure grade/gap colors are consistent; check contrast.
- [ ] Basic responsive behavior (readable down to a laptop width; graceful narrow layout).
- [ ] Final walkthrough: full scroll top→decision reads as a coherent decision narrative; no console errors.
- **Verify:** open in browser, drive every interaction end to end.
- [ ] Commit: `polish: layout, responsive, final pass`

## Self-Review

- **Spec coverage:** blocks 0–7 → Tasks 1–7; visual/brand → Tasks 1 & 8; tech (single file, vanilla, hand-rolled charts) → Task 1; interactions → Tasks 6–7; data exemplar → Task 1; optional 2nd profile intentionally deferred (stretch, not planned). Recommendation logic → Task 2. All covered.
- **Placeholders:** none — each task names concrete functions and what to verify.
- **Type consistency:** helper names (`overallPct`, `gradeBand`, `recommend`, `gapFlag`) and `STATE`/`DATA` shapes are used consistently across tasks.
