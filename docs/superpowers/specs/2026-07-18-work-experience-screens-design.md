# Work Section — Experience Screens (garri.design-style)

**Date:** 2026-07-18 · **Branch:** redesign/op · **Status:** approved-pending-user-review

## Goal

Replicate the reading experience of garri.design's `#work` — pinned project
meta on the left, product screens scrolling past on the right — inside
`index.html`'s existing control-panel aesthetic, covering all 5 employers.

## Decisions (user-approved)

1. **Mockup style:** in-aesthetic UI screens. Hand-built HTML/CSS drawn with
   the site's own tokens (chassis bg, ink hairlines, mono caps, accent chips).
   No fake screenshots, no image assets.
2. **Coverage:** all 5 employers, weighted. CP ORIGIN/DMMS is the flagship
   with 4 screens; others get 1–2. 11 screens total.
3. **Placement:** replaces the flagship card + `.secondary` grid inside
   `01 WORK`. `03 LOG` table stays as the fast-scan CV. Numbering unchanged.
4. **Mechanics:** vertical scroll-past. `.proj-meta` is `position: sticky`;
   screens stack vertically and scroll past it. Pure CSS, zero new JS.

## Structure

```
section.module.m-work#work            (shell unchanged: rail, module-head)
  .module-body
    lede / note                       (copy rewritten, see Copy)
    .projects
      article.proj                    ×5, newest first
        .proj-meta                    sticky; top ≈ 60px; align-self: start
          h3   unit + mono period
          p    1–2 sentence narrative
          dl   years / role / scope [/ stack] [/ side systems]
        .proj-screens
          figure.screen[.screen--phone]  ×1–4
            .screen-top               mono titlebar: SYSTEM · MODULE + LED dot
            .screen-body              the mockup (aria-hidden="true")
            figcaption                mono, one line, real description
```

- `.proj`: 2-col grid `minmax(260px, 300px) 1fr`, gap ~32px.
- Screen bezel: 1px ink border, `2px 2px 0` ink shadow, mono titlebar —
  same family as `.key` / `.cart`.
- Desktop panel: full column width, roughly 4:3. Phone frame: `max-width:
  320px`, tall, centered. Framing follows what the product actually was.
- Shared mockup primitives (one CSS block, reused by all screens):
  `.scr-row` (table row), `.scr-chip` (status chip), `.scr-bar` (progress /
  sparkline bars), `.scr-key` (mini button), `.scr-cell` (floorplan cell).
- Existing `.reveal` IntersectionObserver reused on `.screen` elements.

## Content map — 11 screens

### 01 · 1MOBY — 2026–now — Software Engineer
Narrative: ThaiBulkSMS full-stack support across lead flow and messaging ops.
1. **SMS history search** (desktop): query bar; date/sender/status filters;
   results table (msg id, recipient, segments, delivered/failed chips);
   volume sparkline.
2. **Pipedrive lead routing** (desktop): inbound lead queue; routing rules
   (source → owner → pipeline stage); sync-status LEDs.

### 02 · BLOCKFINT — 2026 (3 mo) — Software Engineer
Narrative: eKYC onboarding prototypes for banking and lending scenarios.
3. **eKYC onboarding** (phone): step rail (ID doc → liveness → review);
   ID capture frame; requirement checklist.
4. **Verification console** (desktop): applicant queue; doc/selfie match
   score; pass/review/fail chips.

### 03 · CP ORIGIN — 2021–2026 — Frontend Developer — ★ flagship
Narrative: DMMS — 10 modules unifying mall operations across 2,000+
branches for 200+ users. One screen per former capability row.
Extra dl row — side systems: affiliate referral · market rental · meal order.
5. **Floorplan** (desktop): zone grid with occupied/vacant cells; occupancy
   %; revenue overlay toggle; book-event key.
6. **Automation backbone** (desktop): branch template runs; per-branch
   validation states; consolidation progress; export key.
7. **Field ops** (phone): assigned task; SLA countdown; photo record slots;
   check-in key.
8. **LINE OA pipeline** (phone): bot chat with lead card and follow-up
   reminder.

### 04 · SOFTNIX — 2020–2021 — SWE / PDPA product owner
Narrative: led PDPA delivery as product owner.
9. **DSR queue** (desktop): access/erasure requests; 30-day SLA countdowns;
   status chips.
10. **Data inventory** (desktop): system × data category × lawful basis ×
    retention table.

### 05 · THAI NIPPON SEIKI — 2020 (7 mo) — Programmer
Narrative: factory document approval with multi-level sign-off.
11. **Approval chain** (desktop): doc header; requester → section head →
    dept manager → director sign-off rail; stamped/pending states;
    timestamps.

## Copy

- `module-lede`: "Six years of systems, drawn as screens."
- `module-note`: adds the honesty label — internal systems can't be
  screenshotted, so each screen is redrawn in this site's own design
  language. This label is what keeps in-aesthetic mockups credible.
- Figcaptions: mono lowercase, e.g. `floorplan · occupancy + revenue overlay`.

## Responsive / a11y / perf

- `<900px`: `.proj` collapses to 1 column; meta unpins (static) above
  screens; screens full width; phone frames stay narrow-centered.
- `.screen-body` is `aria-hidden="true"` — screen readers get the real
  figcaption, not fake data. Panel `dl` and narrative are real content.
- Zero images, zero new JS. Estimated +700–900 lines in the single file.
- Sticky offset accounts for the sticky header (~60px).

## Deletions

- Markup: `.flagship` article, `.secondary` grid (content folded into
  CP ORIGIN block).
- CSS: `.flagship*`, `.cap*`, `.secondary*` rules.

## To verify with user (non-blocking)

- Per-project stack rows: only CP ORIGIN's stack is documented on the page.
  Others drafted from the spec section's known tools; user corrects wording
  at content review.
- Whether the 3 side systems are all CP ORIGIN-era (assumed yes).

## Out of scope

- Dot pagination, custom cursor, scroll-driven panning (rejected as fragile).
- Any changes to the LAB, LOG, or SPEC modules.
