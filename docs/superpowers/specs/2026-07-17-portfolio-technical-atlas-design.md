# Portfolio Technical Atlas Redesign

Date: 2026-07-17

Status: Approved

Target: `index.html`

## Goal

Redesign the root portfolio as a bird’s-eye technical atlas of Pakawat
Smutkun’s product-engineering work. Product artifacts replace the current
text-heavy cards and tables. Each artifact must explain a real interface,
workflow, outcome, role, capability, or action.

The result should retain the precise Teenage Engineering-inspired chassis,
grid, typography, and tactile restraint described in `OP-3d.v2.md` without
reusing the generic hardware controls from `op3d.html`.

## Audience and success

The primary audience is hiring managers, technical leads, and recruiters
scanning on laptop or mobile for one to three minutes.

Within 30 seconds, a visitor should be able to:

1. Identify Pakawat as a full-stack product engineer.
2. Understand that DMMS is the flagship system and recognize its scale:
   10 modules, 2,000+ branches, and 200+ users.
3. Open a relevant prototype or download the resume.

## Craft direction

**Craft Read:** Portfolio atlas for hiring managers and technical leads,
marketing language, Lab White full-palette coding, variance 8, signature bet:
annotated bird’s-eye product plates with coordinate pins.

- **CRAFT_LEVEL:** 9. The interface requires a full polish pass before ship.
- **MOTION_INTENSITY:** 4. Tactile response and one short plate-lift
  transition; no continuous or decorative motion.
- **VISUAL_DENSITY:** 7. Dense enough to feel like a technical catalog while
  preserving clear figure boundaries.
- **DESIGN_VARIANCE:** 8. An asymmetric editorial atlas rather than a
  conventional portfolio grid.
- **Color commitment:** Full palette, permitted for this variance and portfolio
  context. Orange, cyan, yellow, and green code distinct figures; only one is
  active within a given figure.

## Chosen approach

The approved composition is a **technical atlas**:

- A narrow system utility strip and segmented module navigation sit above the
  atlas.
- Each major portfolio area is a numbered figure with a distinct overhead
  product scene.
- Artifacts use redesigned, credible product-interface surfaces derived from
  the existing portfolio content.
- Concise annotations, outcomes, metrics, and actions replace duplicated prose.
- The page remains a normal vertical document with native scrolling.

Two alternatives were rejected:

1. **Continuous workbench:** visually cohesive but allowed projects to lose
   clear boundaries and weakened scanning.
2. **Modular flat-lay bays:** highly legible but too close to the current
   section-by-section page and less editorial than the selected atlas.

## Visual system

### View and physical language

- Every artifact uses a true top-down, orthographic composition.
- Depth comes from shallow layered edges, crisp directional shadows,
  overlapping documents, coordinate pins, and controlled plate lift.
- There is no orbit control, perspective spin, idle rotation, cursor-following
  camera, or generic hardware geometry.
- The signature coordinate-pin motif appears once per major figure to connect
  an annotation to its product evidence.

### Palette

The existing Lab White palette remains the base:

- Canvas and chassis: cool laboratory white and anodized-aluminum gray.
- Ink: near-black, not pure black for large text areas.
- Figure coding:
  - Orange: identity and shipped work
  - Cyan: runnable product lab
  - Yellow: experience
  - Green: capabilities and architecture
- Red is reserved for genuine error or recording state; fake status indicators
  are not used.
- Dark mode is designed as its own surface stack, with reduced accent chroma
  and light edge rings replacing dark shadows.

### Typography

- Display and body: a crisp geometric/system sans family.
- Technical labels and metrics: one monospace family with tabular numerals.
- Large headings use tight tracking and sentence case.
- Uppercase appears only in small tracked system labels.
- No novelty pixel font is used for body or heading copy.

### Structure and spacing

- Maximum content width remains approximately 1,200px.
- A visible grid and 1px chassis rules organize the page.
- Space within an artifact is smaller than space between artifacts, which is
  smaller than space between figures.
- Figure layouts vary; no two adjacent figures use the same composition.
- Conventional equal card grids and nested cards are not used.

## Content architecture

### Utility strip

The utility strip contains only useful information:

- Pakawat’s identity and role
- Availability and Bangkok location
- Current section
- Local time
- Functional light/dark theme control

It removes fake latency, fake memory/FPS diagnostics, decorative VU meters,
sound controls, and patent-style filler.

### Module navigation

The navigation is a segmented five-lane strip:

1. `00 Identity`
2. `01 Work`
3. `02 Lab`
4. `03 Log`
5. `04 Spec`

The active lane is identified by text, contrast, and a figure color. Color is
never the only indicator. Native anchor links remain the primary path; the
existing Q/W/E/R shortcuts remain as accelerators for Work, Lab, Log, and Spec.

### Figure 00: Identity and flagship proof

The first scan contains:

- Name and role
- “Operations, made legible.”
- A sub-20-word positioning line
- Resume and contact actions
- One dominant DMMS overhead plate cropped toward the fold
- The three flagship scale metrics beside the product evidence

The hero does not contain a generic status badge, social-proof filler, or a
decorative 3D gadget.

### Figure 01: Work systems

DMMS dominates the figure. Its product plate visualizes:

- Spatial intelligence and floorplan decisions
- Reporting and automation
- Field operations and evidence
- Business pipeline and LINE OA follow-up

Three smaller plates represent:

- Affiliate Referral System
- Market Rental Management
- Meal Order Management

Each smaller plate contains a title, one outcome, one domain label, and a
specific interface artifact. The current four-row capability prose and
three-column secondary card strip are removed.

### Figure 02: Runnable product lab

Three differently composed product plates link to:

- Performance Results
- ThaiMart Marketplace Flywheel
- EduSight Cognitive Replay

The existing runnable prototypes remain unchanged. The root page receives new
atlas artwork that truthfully represents each prototype’s workflow and links to
the existing pages.

### Figure 03: Experience dossiers

The five roles become a chronological set of overhead work-order dossiers:

- 1Moby
- blockfint
- CP ORIGIN
- Softnix
- Thai Nippon Seiki

Each dossier shows period, role, company, and one concrete contribution.
Chronology remains obvious without a traditional table.

### Figure 04: System architecture inventory

Capabilities become an exploded system map instead of a skills table:

- Frontend
- Backend
- State and testing
- Cloud and automation
- AI toolchain
- Education and languages

Connectors show how the layers support product workflows. Technology names
remain readable text rather than decorative logos or floating badges.

### Figure 05: Contact baseplate

The closing figure contains:

- One concise hiring statement
- Email
- Phone
- GitHub
- LinkedIn
- Resume download

The footer is intentionally quiet and functional. It does not repeat fake
system status, build numbers, or regulatory decoration.

## Interaction model

### Artifact interaction

- Every actionable artifact is a native link.
- Hover, keyboard focus, or touch raises the plate by 4–6px, strengthens its
  directional shadow, and reveals or emphasizes its outcome annotation.
- Press feedback is immediate and finishes in under 100ms.
- The main plate transition uses explicit transform and shadow properties.
- No interaction requires dragging, circular gestures, or 3D navigation.

### Navigation and state

- `IntersectionObserver` updates the current figure in the utility strip and
  navigation.
- Optional Q/W/E/R shortcuts ignore modifier keys and editable fields.
- Theme choice persists in `localStorage`; the system preference is used only
  until the visitor makes an explicit choice.
- Local time updates once per minute rather than running continuously.

### Motion and accessibility

- The page has no continuous animation loop.
- There are no entrance animations on every artifact.
- Hover-only effects are gated to fine pointers.
- `prefers-reduced-motion` removes spatial movement and smooth scrolling while
  retaining visible focus and state changes.
- All interactive targets are at least 44px.
- Native links, headings, sections, tables where still semantically required,
  and a skip link are used before ARIA.
- Focus states provide the same annotation and outcome information as hover.

## Responsive behavior

### Desktop

- The technical atlas uses mixed-size cells and asymmetric figure layouts.
- DMMS remains the dominant plate.
- Figure labels occupy a narrow left rail.
- Navigation remains visible and segmented.

### Tablet

- Two-column compositions collapse selectively.
- The figure rail narrows.
- Product artifacts retain their hierarchy rather than becoming equal cards.

### Mobile

- Every figure becomes a one-column document tray.
- The product artifact appears first; its title, outcome, and action follow.
- Figure labels become compact headers rather than a permanent side rail.
- The segmented navigation scrolls horizontally with a visible cut edge and
  accessible overflow.
- There is no page-level horizontal overflow.
- The primary resume and contact actions remain thumb reachable.

## Technical architecture

The implementation is DOM/SVG-first rather than WebGL.

### Files

- `index.html`: semantic page structure, copy, annotations, metrics, and links
- `assets/atlas.css`: tokens, chassis grid, themes, responsive behavior,
  artifact depth, interaction, and reduced motion
- `assets/atlas.js`: active-section tracking, local time, theme persistence,
  and Q/W/E/R keyboard shortcuts
- `assets/flatlays/*.svg`: one focused product artifact per project or figure

This boundary avoids growing `index.html` into another monolithic file like
`op3d.html`, while keeping the site compatible with GitHub Pages and its
no-build workflow.

### Rendering

- SVG provides sharp product-interface artwork at every device pixel ratio.
- HTML carries all readable labels, links, metrics, and annotations.
- CSS creates the shallow physical depth.
- No external JavaScript, animation, font, or WebGL dependency is required.
- The root page makes no network request beyond its local assets.

### Data flow

The page is static and content-first:

1. HTML loads with all content and links present.
2. CSS establishes the atlas and responsive layouts.
3. JavaScript enhances active-section state, time, theme, and shortcuts.
4. A state change updates text and attributes on existing native controls; it
   does not create or replace core content.

## Failure and degradation behavior

- With JavaScript disabled, all figures, links, resume actions, and contact
  methods remain available.
- If theme storage is unavailable, the page uses system preference without an
  error.
- If an SVG fails to load, adjacent title, outcome, metrics, and link text
  still identify the artifact.
- Reduced-motion mode presents static depth and instant state changes.
- If `IntersectionObserver` is unavailable, navigation still works and the
  utility strip keeps its neutral default state.
- The design avoids a canvas boot path, CDN dependency, and WebGL fallback
  branch entirely.

## Verification

Serve the project locally and verify:

### Layout

- Viewports: 390px, 768px, 1280px, and 1680px.
- Portrait and landscape where practical.
- `document.documentElement.scrollWidth <= window.innerWidth`.
- DMMS remains dominant at every breakpoint.
- No product label or primary action truncates incorrectly.

### Accessibility

- Keyboard traversal follows the visual reading order.
- Every artifact link has a specific accessible name.
- Focus reveals the same information as hover.
- Touch targets are at least 44px.
- Heading order, landmarks, skip link, and contact links are correct.
- Light and dark themes meet WCAG AA; APCA is used for calibration.
- Reduced-motion mode contains no spatial animation or smooth scrolling.

### Behavior

- Active-section tracking updates on scroll.
- Theme selection persists across reloads and respects explicit choice over
  system preference.
- Local time updates without a continuous loop.
- Q/W/E/R shortcuts navigate correctly and ignore editable contexts.
- There are no console errors.

### Reliability and performance

- All local prototype links return HTTP 200.
- The resume, email, phone, GitHub, and LinkedIn actions are correct.
- There is no idle `requestAnimationFrame` loop.
- No external dependency is fetched.
- SVG assets include dimensions and do not cause layout shift.
- The page remains usable with JavaScript disabled and with individual SVG
  assets blocked.

## Out of scope

- Reusing or incrementally modifying `op3d.html`
- Generic 3D controls, hardware toys, and decorative objects
- Three.js, WebGL, orbit controls, and drag-to-rotate interactions
- Fake diagnostics, sound effects, cursor flashlights, and decorative meters
- Scroll-jacking or horizontal tape navigation
- Restyling the linked prototype pages
- Adding new portfolio projects or changing the factual career content
