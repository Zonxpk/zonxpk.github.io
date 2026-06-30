# Portfolio Ambient Starfield Design

Date: 2026-06-30
Target: `/Users/pakawat/Projects/labs/portfolio/index.html`
Reference inspiration: `sanidhyy/space-portfolio`

## Goal

Adapt the atmospheric space feel from the reference portfolio into the existing static homepage without replacing the current editorial and systems-map identity. The result should add depth and motion behind the page while keeping the current content structure, readability, and performance profile intact.

## Scope

In scope:

- Add a full-page ambient starfield layer behind the existing homepage content
- Animate the field continuously with slow autonomous drift
- Add subtle pointer-reactive parallax motion
- Respect `prefers-reduced-motion`
- Keep the implementation compatible with the current no-build static HTML setup

Out of scope:

- Rebuilding the page in React, Next.js, or React Three Fiber
- Replacing the hero copy, navigation, or systems-map panel
- Adding planets, nebula scenes, or other heavy foreground illustrations
- Changing the overall information architecture of the homepage

## Recommended Approach

Use a lightweight `Canvas 2D` starfield instead of importing Three.js directly.

Why:

- The reference repo's most relevant Three.js-inspired behavior for this request is the moving starfield background
- The homepage is a static HTML file with no build pipeline, so a canvas layer fits naturally
- A 2D canvas can deliver the required effect with less weight and operational complexity than adding a CDN Three.js scene
- This preserves the site's current maintainability and loading profile

## Visual Direction

The starfield should feel ambient rather than theatrical.

- Most stars should be soft white with limited brightness variance
- A small minority can pick up existing site accent tones similar to `--signal` and `--draft-light`
- Density should stay low enough that text and line-art remain easy to read
- Motion should feel like depth and drift, not arcade motion or a cursor-chasing effect
- The canvas should support the existing dark grid-and-systems visual language instead of replacing it

## Layout Integration

Add one fixed canvas that spans the viewport and sits in the background stack:

- Above the static body background gradients
- Below all page content and interactive controls
- Non-interactive via `pointer-events: none`

The current sections, hero structure, and map-shell composition remain unchanged. The starfield is a new atmosphere layer, not a new content block.

## Motion Design

The animation has two motion sources:

1. Autonomous drift
   - Stars move slowly over time to avoid a static wallpaper feel
   - Drift speed should remain low and continuous
   - Different star depths can move at slightly different rates

2. Pointer-reactive parallax
   - Pointer movement shifts the apparent star positions subtly
   - Near stars react a little more than far stars
   - Motion should be eased so the field glides rather than snaps
   - The effect should settle smoothly back toward center when pointer input stops

The pointer response should be intentionally restrained. The page should feel polished and dimensional, not playful or distracting.

## Accessibility

Support reduced motion explicitly:

- If `prefers-reduced-motion: reduce` is active, remove reactive movement and either pause drift entirely or keep only a minimal, near-static motion level
- The effect must not reduce text contrast or interfere with focus visibility
- The canvas must never capture pointer or keyboard interaction

## Performance Constraints

The effect should remain lightweight for a static site.

- Particle count should scale by viewport size instead of using a fixed heavy count
- Animation should be driven by `requestAnimationFrame`
- Resize behavior should update canvas dimensions cleanly
- The script should avoid expensive per-frame allocations
- The effect should remain visually acceptable on mobile, with lower density if necessary

## Implementation Shape

Expected page changes:

- Add a background canvas element near the top of the document body
- Add CSS for fixed positioning, stacking, and blend/opacity tuning
- Add a small inline script or linked local script to:
  - initialize particles
  - animate drift
  - track pointer position
  - interpolate parallax motion
  - handle resize
  - handle reduced-motion preferences

This should stay self-contained and avoid introducing a framework or dependency chain.

## Error Handling And Fallbacks

- If canvas setup fails, the page should degrade silently to the existing static background
- If JavaScript is unavailable, the homepage should remain fully usable with its current visual design
- If reduced motion is requested after load, the script should respond without requiring a refresh if practical

## Verification

Validate the result against the following checks:

- Desktop: starfield is visible but does not overpower content
- Mobile: density and motion remain smooth and readable
- Pointer movement: reaction is noticeable but subtle
- Reduced motion: effect is absent or materially softened
- Layering: navigation, hero, and map-shell remain fully interactive and legible
- Performance: no obvious jank during scroll or pointer movement on a typical laptop

## Risks And Mitigations

Risk: The effect makes the homepage feel too space-themed and weakens the current enterprise/systems tone.
Mitigation: Keep density low, use restrained accent color, and preserve the existing map-shell hero language.

Risk: Background animation reduces readability in the hero.
Mitigation: Lower star brightness behind text zones and keep overall opacity modest.

Risk: Pointer reactivity feels gimmicky.
Mitigation: Cap offset distance and ease movement heavily.

Risk: Static-site implementation grows messy.
Mitigation: Keep the canvas logic isolated and dependency-free.

## Success Criteria

This adaptation is successful if:

- The homepage clearly feels more alive and dimensional
- The effect reads as a natural extension of the current design
- Users notice gentle motion without losing focus on the portfolio content
- The page remains simple to host and maintain as a static site
