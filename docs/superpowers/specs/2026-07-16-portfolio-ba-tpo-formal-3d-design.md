# Portfolio BA/TPO Formal 3D Redesign

Date: 2026-07-16
Target: `/Users/pakawat/Projects/labs/portfolio/index.html`
Source handoff: `/var/folders/4n/g6dxxmhs5rj6frc1f3q2wwbw0000gn/T/portfolio-ba-tpo-handoff.md`

## Goal

Reposition the portfolio toward Business Analyst (BA) and Technical Product Owner (TPO) roles without weakening or rewriting the owner's true full-stack development background. The first screen must communicate three facts quickly:

- Full-stack development is the foundation.
- BA and TPO work are the intended direction.
- The PDPA compliance project is the one genuine end-to-end product-ownership proof point.

The redesign should feel formal, business-facing, and dimensional. It must not resemble a developer console, a playful workshop, or a sci-fi/WebGL showcase.

## Approved Direction

Use a full-page Formal Product Dossier visual system:

- White and warm-white page backgrounds
- Formal blue for typography, structure, and primary interface states
- Restrained formal orange for proof points, active paths, and emphasis
- Editorial document styling with disciplined grids, fine rules, and controlled shadows
- A focused CSS 3D dossier in the hero
- Motion only in response to direct engagement
- No Three.js, WebGL, canvas animation, or continuous ambient motion

This specification supersedes `docs/superpowers/specs/2026-06-30-portfolio-ambient-starfield-design.md` for the root portfolio. The existing starfield canvas and dormant Three.js code should be removed.

## Content Integrity

The redesign is additive. It must not manufacture BA or product experience.

- Do not claim that the owner wrote specifications.
- General BA/product involvement is limited to joining requirements conversations, giving input, and pushing back when implementation reality matters.
- Keep all existing development job titles and development verbs.
- Treat Business Systems Analysis as requirements, process, workflow, and systems integration work, not data analysis.
- Preserve the PDPA role as real product ownership from requirements through delivery.
- Do not add or repeat personal contact information outside its existing locations.

## Required Copy Changes

Apply the handoff's exact content changes.

### Document title

Replace:

`Pakawat Smutkun - Technical Product Owner & Full-Stack Developer`

With:

`Pakawat Smutkun — Full-Stack Developer moving toward BA & Product`

### Availability line

Replace:

`Available for technical product owner and full-stack roles`

With:

`Open to Business Analyst & Technical Product Owner roles — a developer who works close to the business side.`

### PDPA proof line

Add this line immediately below the existing four-cell evidence grid:

`Once owned a product end-to-end — PDPA compliance build, requirements to delivery.`

The evidence grid remains four columns on desktop. The proof line is a separate, quiet element rather than a fifth statistic.

### Metadata audit

Search the description, Open Graph, and Twitter metadata for the old positioning. If `og:title` or `twitter:title` exists or is added, use the new document title exactly. The current meta description does not contain the old title and may remain unchanged. Preserve the existing Open Graph image.

### Content that remains unchanged

- Hero name and subtitle
- Existing PDPA experience bullet
- All job titles and experience verbs
- Skills content
- Prototype Lab content
- Background section language
- Existing links and calls to action

## Visual System

### Color tokens

Use this light-only palette across the entire page:

- Page canvas: `#FAFAF8`
- Primary paper surface: `#FFFFFF`
- Blue-tinted section surface: `#EEF3F6`
- Formal blue ink: `#17324A`
- Secondary blue: `#315A78`
- Formal orange: `#A94724`
- Muted text: `#5C6973`
- Rules and borders: `#D7DEE3`
- Soft shadow: `rgba(23, 50, 74, 0.12)`

Formal orange is an accent, not a second body-text color. Use it for proof markers, active routes, small rules, and focus/hover emphasis. UI chrome and diagrams should stay within blue, orange, white, and neutral gray. Third-party technology logos may retain their intrinsic colors.

The portfolio intentionally stays light when the operating system prefers dark mode. There is no automatic dark theme in this scope.

### Typography

- Display and major section headings: `Source Serif 4`, with Georgia as the fallback
- Body and interface copy: existing `Source Sans 3`
- Metadata and small technical labels: existing `Azeret Mono`

Extend the existing Google Fonts request to include `Source Serif 4`; do not add another stylesheet origin. Use the serif selectively for formal editorial authority. Body content, navigation, controls, and dense project descriptions remain sans-serif. Mono labels should be sparse so the page does not drift back toward a developer-console aesthetic.

### Shape and elevation

- Prefer squared or lightly rounded corners between 2px and 8px.
- Use fine blue-gray rules instead of glowing borders.
- Use shallow, blue-tinted shadows rather than black floating-card shadows.
- Avoid pills except where an existing compact status label genuinely needs one.
- Remove playful rotations, sticky-note styling, neon glows, and autonomous floating objects.

## Page Structure

Keep the current information architecture and section order:

1. Hero
2. Portfolio evidence
3. Experience
4. Digital Mall case study
5. Prototype Lab
6. Skills
7. Background
8. Footer

The redesign changes presentation, not the content model.

### Navigation

Use a white translucent sticky surface, formal-blue text, a fine bottom rule, and a compact orange active/focus cue. Keep the current navigation links and mobile menu behavior.

### Hero

Retain the two-column desktop structure:

- Left: updated availability statement, existing name, existing hero subtitle, existing calls to action, and existing contact strip
- Right: the Formal Product Dossier composition

The hero background uses a very light ruled or grid texture. It should read as editorial structure, not a blueprint or terminal.

### Formal Product Dossier

Build the hero artwork from three aligned HTML document layers using CSS perspective. The layers represent:

- Business context
- Constraints and decisions
- PDPA delivery evidence

The front document may visibly label the PDPA compliance project and the requirements-to-delivery path. The artwork must not introduce claims about writing specifications. Because the same meaningful proof appears in the normal document flow below the evidence strip, the layered artwork is decorative and should be hidden from assistive technology.

The composition uses straight alignment, fine rules, formal blue text, and one orange proof block. It must avoid tilted cards, speech bubbles, sticky notes, or dashboard-like sci-fi panels.

### Evidence strip

Keep the current four statistics and four-column desktop grid. Restyle it as a formal evidence register with white surfaces, blue dividers, and restrained blue typography. Add the PDPA proof line underneath with a short orange rule and formal-blue text.

### Remaining sections

Preserve existing layouts unless a small spacing adjustment is necessary for the new typography. Convert dark panels and diagrams to white paper surfaces over alternating white and blue-tinted section backgrounds. Recolor existing inline SVG and CSS illustrations to the formal blue/orange/neutral palette.

Depth outside the hero is limited to shallow elevation on existing interactive cards and links. Do not create additional 3D scenes.

## Interaction Design

### Hero response

The dossier responds only while a visitor directly engages with the hero on a fine-pointer device.

- Normalize pointer position within the hero to a bounded `-1` to `1` range.
- Apply the result through CSS custom properties.
- Cap the front composition near 4 degrees on the X axis and 6 degrees on the Y axis.
- Keep document-layer separation between approximately 18px and 48px.
- Reset to the neutral composition on pointer exit, window blur, or document visibility loss.
- Do not run an idle animation or permanent `requestAnimationFrame` loop.

Pointer events may schedule a single animation-frame update to avoid layout churn. The controller should write transform variables only; it should not calculate layout continuously.

### Focus and keyboard behavior

The artwork itself is not interactive and must not enter the tab order. Existing links and buttons retain visible focus states. When focus is within the hero actions, the dossier may use one fixed, subtle emphasis state through `:focus-within`; it must not simulate pointer tracking.

### Existing reveals

Retain the existing one-time intersection reveals, but tune them toward short opacity and vertical-position transitions. Remove blur-heavy or theatrical motion that conflicts with the formal direction.

## Architecture and Boundaries

The site remains a single static `index.html` with no build step.

### Style layer

Define the new palette and typography through root custom properties. Group component rules by navigation, hero/dossier, evidence, shared sections, and responsive behavior. Existing selectors may be reused where they still match the component's responsibility.

### Dossier component

The dossier markup and styles form one isolated hero component. Its internal layers should not be coupled to unrelated project cards or section diagrams. A static centered composition is its default state.

### Pointer controller

Use one small inline controller scoped to the hero/dossier elements. Its data flow is:

1. Receive a pointer event inside the hero.
2. Normalize and clamp the pointer coordinates.
3. Schedule at most one pending visual update.
4. Set dossier CSS custom properties.
5. Reset properties when engagement ends.

The controller has no application state, persistence, API calls, or dependency on section content.

### Existing page behavior

Keep the navigation toggle, scroll progress, and intersection observer behavior isolated from the dossier controller. Remove the unused starfield canvas element and the entire commented Three.js module block.

## Responsive Design

- Desktop: retain the two-column hero and full document-layer separation.
- Tablet: allow the hero columns to narrow while reducing dossier perspective and shadow depth.
- Mobile: stack the dossier below the hero copy, reduce layer separation, and use a stable aspect ratio with no horizontal overflow.
- Coarse pointers: keep the dossier static rather than mapping touch movement.
- The evidence strip may follow its existing responsive collapse, but it must keep exactly four statistics.

## Accessibility

- Preserve semantic landmarks, headings, skip navigation, and existing link labels.
- Keep body text and interactive states at WCAG AA contrast or better.
- Use the darker formal orange where orange text must carry meaning; lighter orange treatments may be decorative only.
- Keep the dossier `aria-hidden="true"` because it duplicates visible proof content.
- Do not add focusable decorative layers.
- Ensure focus rings remain visible on white and blue-tinted surfaces.
- Under `prefers-reduced-motion: reduce`, disable pointer transforms and nonessential transitions while preserving the static depth composition.

## Error Handling and Fallbacks

- Without JavaScript, the dossier remains centered and fully composed.
- Without CSS 3D transform support, the documents appear as a legible two-dimensional stack.
- On reduced-motion or coarse-pointer devices, the dossier stays static.
- If the web font request fails, Georgia, the existing sans-serif fallback, and the system monospace fallback preserve hierarchy.
- A dossier-controller failure must not affect navigation, links, section reveals, or content visibility.

## Performance Constraints

- Add no JavaScript or rendering dependency.
- Make no Three.js or WebGL request.
- Remove the unused canvas and commented Three.js implementation.
- Avoid continuous animation frames.
- Update only CSS custom properties during pointer response.
- Avoid layout reads after the initial hero bounds are captured for an interaction; refresh bounds on resize or a new pointer entry.
- Keep shadows and backdrop filters restrained, especially on mobile.

## Verification

### Content checks

- Confirm the exact new document title.
- Confirm the exact new availability line.
- Confirm the exact PDPA proof line directly below the four-cell evidence strip.
- Confirm the old `Technical Product Owner & Full-Stack Developer` phrase is absent from title and social metadata.
- Confirm the text of the hero subtitle, PDPA experience bullet, job titles, experience verbs, skills, Prototype Lab, and Background content remains unchanged.

### Visual checks

Inspect the full page at approximately:

- 1440 x 900 desktop
- 768 x 1024 tablet
- 390 x 844 mobile

Check hierarchy, type wrapping, dossier legibility, four-stat evidence layout, section rhythm, inline SVG recoloring, focus visibility, and horizontal overflow. Confirm the page remains intentionally light under both operating-system color preferences.

### Behavior checks

- Verify pointer response occurs only within the hero on fine-pointer devices.
- Verify the dossier resets on pointer exit and window blur.
- Verify there is no idle motion.
- Verify the artwork is static under reduced motion and coarse pointers.
- Verify keyboard navigation and the mobile navigation menu still work.
- Verify the page remains complete with JavaScript disabled.
- Verify the browser console has no errors.

### Dependency checks

- Confirm there is no Three.js import.
- Confirm there is no WebGL renderer or starfield canvas.
- Confirm there is no continuous dossier animation loop.

## Risks and Mitigations

Risk: A full light-theme conversion makes the long portfolio feel flat.
Mitigation: Alternate white and blue-tinted section surfaces, use disciplined rules, and reserve shallow elevation for interactive content.

Risk: The 3D dossier implies formal specification ownership.
Mitigation: Use neutral labels such as business context, constraints, decisions, and delivery; anchor the only end-to-end ownership claim to PDPA.

Risk: Orange becomes decorative noise.
Mitigation: Restrict orange to proof, active paths, and interaction emphasis.

Risk: Pointer tilt feels playful.
Mitigation: Keep rotation caps low, remove idle motion, and reset promptly when engagement ends.

Risk: Recoloring all existing diagrams creates scope creep.
Mitigation: Preserve their structure and behavior; change only palette tokens, surface treatment, and necessary contrast values.

## Success Criteria

The redesign is complete when:

- The first screen clearly communicates developer foundation, BA/TPO direction, and PDPA product ownership.
- The full page consistently uses the approved white, formal-blue, and formal-orange system.
- The hero feels dimensional through controlled CSS depth without appearing technical, playful, or theatrical.
- All handoff content constraints remain true.
- Desktop, tablet, mobile, keyboard, reduced-motion, coarse-pointer, and JavaScript-disabled fallbacks are usable.
- The root portfolio remains a maintainable single static file with no new JavaScript or rendering dependency.
