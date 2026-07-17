# OP Redesign — Teenage Engineering Aesthetic for index.html

Date: 2026-07-17
Status: Approved (brainstormed interactively; decisions recorded below)

## Goal

Fully redesign the root portfolio page (`index.html`) in a Teenage Engineering
OP-series visual language per `OP.md`, while keeping it scannable for hiring
managers and recruiters (`PRODUCT.md`).

## Decisions

1. **Friction level:** "TE skin, normal flow." Full OP visual language, but
   vertical scroll and a normal nav. No horizontal tape-scrub navigation.
2. **Scope:** Root `index.html` only, with content trimmed/restructured.
   Sub-projects (`edusight/`, `thaimart/`, `performance-management/`) untouched.
3. **Sound:** WebAudio-synthesized click on button press, **off by default**,
   enabled by a visible `SND` toggle (persisted to `localStorage`). No audio files.
4. **Direction:** Lab White — white/aluminum chassis, ink text, 1px module
   borders, toy-color accents on interactive/coding elements only.
5. **Stack:** Single `index.html`, no build, no dependencies, no webfonts.

## Content architecture

Four color-coded modules, vertical scroll, each a bordered "hardware module":

| # | Module | Color | Content |
|---|--------|-------|---------|
| — | Hero | orange | Name, thesis line ("systems that make operations legible"), status readout, inline SVG signal-path art. Absorbs the old `section-tight` intro strip. |
| 01 | WORK | orange | DMMS flagship panel; its 4 capability panels (spatial intelligence / automation backbone / field operations / business pipeline) compressed to 4 terse rows; secondary systems (Affiliate Referral, Market Rental, Meal Order) as a compact 3-across strip. |
| 02 | LAB | cyan | 3 clickable prototypes (empeo Performance Results, ThaiMart, EduSight) as color-lit "cartridge" tiles linking to existing sub-pages. Kept whole. |
| 03 | LOG | yellow | Experience as a mono operations-log table: year · role · company · one line, for all 5 roles (1Moby, blockfint, CP ORIGIN, Softnix Technology, Thai Nippon Seiki). |
| 04 | SPEC | green | One spec-sheet table absorbing the 4 skill clusters, 3 AI tools, education, and languages. Replaces the separate Skills and Background sections. |
| — | Footer | — | Contact ("ready to make operations legible"), links, keyboard-shortcuts spec row. |

Ordering change: WORK before LOG (shipped systems before job list).

## Visual system

**Color:**
- Chassis: `#f4f4f2` body, `#e8e8e6` aluminum panels, `#111` ink, all module
  borders `1px solid #111`.
- Toy accents (interactive/section-coding only): orange `#ff4d00`, cyan
  `#00a4c8`, yellow `#f5c400`, green `#3fa435`.
- LED red `#e03616` for the ● REC status dot.
- No gradients, no shadows (except the mechanical-key offset), no rounded
  corners above 2px. Accent colors never carry body text; text is ink-on-white.

**Type:**
- Data/headers/labels: `"JetBrains Mono", ui-monospace, monospace`, uppercase,
  letter-spacing `0.08em`. No webfont downloads — system fallbacks only.
- Body: `"Helvetica Neue", Helvetica, Arial, sans-serif`.
- Pixel/dot-matrix flavor comes from the SVG hero art, not a novelty text font.

**Grid:** 12-col, max-width 1200px, every module a bordered cell. Section
numbers (01–04) in a fixed-width left rail column that collapses on mobile.

**Art:** Inline flat SVG line-art only. Hero: abstract "signal path" schematic
that draws itself on load (stroke-dashoffset). Each LAB cartridge gets a small
glyph. No stock imagery, no 3D.

## Tactility & interaction

- **Mechanical keys:** interactive elements get 1px border + solid 2px offset
  block "shadow"; `:active` translates the element 2px down-right and removes
  the shadow. One shared CSS pattern.
- **Sound engine:** one lazily-created `AudioContext`; ~15ms square-wave burst
  with fast decay on press. `SND ○/●` header toggle (`<button aria-pressed>`),
  state in `localStorage`, default off.
- **Instrument header:** blinking ● REC dot + mono readout of current section
  (`01 WORK`) driven by IntersectionObserver. Keys Q/W/E/R (and 1–4) jump to
  the four modules; shortcuts documented in the footer spec row.
- **Motion:** section reveals slide 8px with `steps(4)` easing (quantized,
  mechanical). LAB cartridges light an LED on hover. Nothing else — no
  scroll-jacking, no cursor followers.

## Accessibility & performance

- WCAG AA: body text ink-on-white; accents on UI elements meet 3:1.
- Full keyboard support incl. skip link; QWER shortcuts ignore key events from
  form fields.
- `prefers-reduced-motion`: disables reveals, REC blink, and SVG self-draw.
- Semantic: `header/main/section/article/footer`, single `h1`, `aria-pressed`
  on toggles.
- Zero network requests beyond the document itself.

## Out of scope

- Horizontal tape navigation, dials/custom form controls (no forms exist).
- Restyling sub-project pages.
- Dark theme / theme toggle.
