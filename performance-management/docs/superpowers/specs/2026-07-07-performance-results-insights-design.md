# Performance Results & Insights — Redesign (empeo take-home)

**Date:** 2026-07-07
**Role framing:** Product Owner of empeo redesigning the Performance Evaluation Results experience.
**Deliverable:** Clickable HTML prototype (single self-contained file) in this repo.

## Problem

empeo's current Performance Results screen fails on the three complaints in the brief:

1. **Not all dimensions at once** — evaluation sources (self / manager / peer / org) are siloed behind toggles; you can't compare them side by side, and there's no gap analysis.
2. **No decision insight** — results are a flat table of *topic · weight · score*; no trend, no peer comparison, no synthesis of strengths/risks.
3. **Doesn't support pay/promotion** — nothing links a score to a recommendation or trajectory.

Evidence: the two current-design screens are (a) a profile modal → ผลการประเมิน tab with a left rail that shows **one source at a time** and a right-side flat table (topic · น้ำหนัก · ผลลัพธ์, mixed /5 · ⭐ · ❤ widgets, overall 90/100 · Excellence); (b) a print-style report scoring weighted topics across rounds (ครั้งที่ 1–4) to a total %.

## Scope

- **Primary persona:** manager reviewing **one direct report** for **one review cycle** to make salary / bonus / promotion calls.
- **Model:** keep empeo's real model — weighted evaluation topics + multi-source (360-style) input + overall grade — and **add** the missing comparison, trend, synthesis, and decision layers. No full 9-box (would require a potential axis empeo doesn't have); use peer distribution + trend slope as an honest calibration proxy.
- **Language:** Thai-first UI, matching empeo terminology.
- Out of scope: HR org-wide dashboard, employee self-view, real backend, authoring/editing evaluations.

## Structure (single scrolling decision report + sticky summary)

Read top-to-bottom toward a decision:

| # | Block | Delivers | New/kept |
|---|-------|----------|----------|
| 0 | Sticky context bar (on scroll) | name, cycle, overall grade, "ไปที่การตัดสินใจ" jump | new |
| 1 | Verdict header | identity + overall grade + 1-line plain-language synthesis + **recommended-action pill** | new |
| 2 | 360 scorecard | dimensions × 4 sources side-by-side with gap flags | new |
| 3 | Trend | overall + per-dimension across cycles/rounds | new |
| 4 | Peer position | distribution + percentile vs team/role + trend slope | new |
| 5 | Strengths & risks | auto-surfaced strengths, watch areas, notable comments | new |
| 6 | Detailed breakdown (expandable) | faithful empeo table: topic · น้ำหนัก · per-source · comment · rounds | kept |
| 7 | Manager decision panel | confirm rating, comp rec, promotion readiness, notes + "why" | new |

## Block details

### Block 2 — 360 scorecard
- One row per dimension (dimensions group empeo's weighted topics, e.g. การส่งมอบงาน / การทำงานร่วมกัน / ความเป็นเจ้าของงาน / ทักษะเฉพาะทาง).
- Row = a **0–5 track** with the four sources plotted as markers, weighted average as a bar behind.
- Clustered markers = consensus; spread = contested — **the gap is the insight**.
- **Gap flags (computed):**
  - `self − others ≥ 1.0` → จุดบอด (blind spot, amber)
  - `others − self ≥ 1.0` → ประเมินตนเองต่ำไป (sells self short, blue)
  - all high & tight → จุดแข็งที่สอดคล้อง (consistent strength, green)
  - manager vs peer diverge → ต้องปรับเทียบ (needs calibration)
- Scale: native **/5 per topic**, rolled up to **overall % + grade** (matches "90/100 · Excellence" / "80%").

### Blocks 1 & 7 — recommendation logic (transparent, auditable)
Rollup shown with its "why" line, e.g.:
`Excellence (92%) · improving 3 cycles ↗ · top 12% of role → merit 8–10% · bonus 1.5× · promotion-ready`

- **Grade band** from overall %: Excellence ≥90 · Exceeds 80–89 · Meets 65–79 · Below <65.
- **Merit range** by band (Excellence 8–10% · Exceeds 5–7% · Meets 3–4% · Below 0–2%), nudged by trend + peer percentile.
- **Promotion readiness** = high band ＋ upward trend ＋ top-quartile peer ＋ enough time-in-role; else "strong, hold" / "develop first."
- Manager can override in block 7 (editable merit %, bonus, notes); "why" line updates live.
- All numbers are illustrative mock data.

### Block 4 — peer position
- Distribution curve of the role/team with the employee marked + percentile.
- Trend slope as a lightweight potential proxy. No fabricated 9-box.

## Visual language
- Read as evolved empeo: coral→orange gradient header, white cards on `#F7F7F5`, rounded corners, soft shadows, existing grade chips.
- Font: Noto Sans Thai (or Sarabun) via Google Fonts.
- Semantic gap/band colors: green / amber / blue / red as above.

## Tech
- **Single self-contained `index.html`** — inline CSS + vanilla JS. No framework, no build, no dependencies.
- Charts hand-rolled in CSS/SVG (marker tracks, sparkline trend, distribution). No chart library.
- Mock data as one JS object at top of file for easy tweaking.

## Interactions
- Sticky context bar on scroll + "ไปที่การตัดสินใจ" jump-to-decision.
- Expand/collapse detailed breakdown (block 6).
- Toggle each source on/off on the 360 tracks.
- Switch review cycle (2024/2025) → numbers + trend update.
- Hover tooltips explaining each gap flag.
- Editable decision panel (merit %, bonus, notes) with live "why" rationale.

## Data
- One fully-populated exemplar employee.
- Optional stretch (only after core is solid): toggle to a second contrasting profile (star vs struggling report) for demo contrast.

## Success criteria
- All four evaluation sources are visible together with divergence made obvious.
- A manager can reach a defensible pay/promotion decision from this one screen, with the reasoning traceable to the data.
- Reads unmistakably as an improved empeo screen (brand, Thai, terminology).
- Runs by opening `index.html` in a browser — no build step.
