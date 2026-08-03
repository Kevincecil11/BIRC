# BIRC 2026 Design System

This file is the visual source of truth for every BIRC page. Use it to restyle existing page content without rewriting, shortening, inventing, or removing that content.

## 1. Core rule: preserve content

When adapting an existing page:

- Keep every supplied heading, paragraph, label, date, name, statistic, link, and section.
- Do not paraphrase or replace approved copy.
- Do not invent speakers, testimonials, numbers, schedules, venues, CTAs, or claims.
- Preserve the original information hierarchy and destination of every link.
- Layout, typography, color, spacing, interaction, and animation may change.
- If content does not fit, redesign the layout. Never delete or truncate the content to solve a visual problem.
- Do not change BIRC facts unless updated content is explicitly provided.

## 2. Brand direction

BIRC should feel like a global industry summit, not a generic trade-show template. The visual language is cinematic, editorial, precise, premium, and distinctly mobile-first.

The interface should communicate:

- India at the centre of global rice trade
- authority without corporate stiffness
- scale without visual clutter
- clear actions and understandable sections
- agricultural character through restrained grain, route, archive, and field motifs

Avoid obvious rice-industry clichés such as green farm photography everywhere, rustic textures, decorative leaves on every section, or excessive gold.

## 3. Source of truth and assets

- Main implementation: `index.html`
- Design rules: `design.md`
- Official logo: `https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png`
- The logo must use `object-fit: contain` and must never be stretched, recolored, redrawn, or replaced with plain text.
- Recommended mobile width for the dated ivory logo: `150px` to `164px`; preserve its intrinsic aspect ratio.

## 4. Color system

Use these exact colors. Do not substitute generic black, white, beige, green, or orange.

```css
:root {
  --birc-ink: #0d0d0b;
  --birc-ink-raised: #191916;
  --birc-linen: #faf0e6;
  --birc-gold: #ebb341;
  --birc-gold-deep: #c98e25;
  --birc-editorial-grey: #2b2b27;
  --birc-dark-muted: #aba49c;
  --birc-light-muted: #6d6862;
  --birc-dark-line: #35332e;
  --birc-light-line: #d8cec3;
}
```

### Color roles

- `--birc-ink`: primary dark background and dark interactive surface.
- `--birc-ink-raised`: subtle elevation on dark sections, pathways, and visual placeholders.
- `--birc-linen`: light sections, primary text on dark, and warm neutral space.
- `--birc-gold`: primary CTA, focus rings, dates, active progress, and rare high-priority emphasis.
- `--birc-gold-deep`: labels and accents on linen where the brighter gold lacks contrast.
- `--birc-editorial-grey`: large background words, oversized programme numbers, and quiet editorial narrative accents only.
- Muted colors: secondary copy and metadata.
- Line colors: dividers and structure, never decorative boxes around everything.

### Distribution

- Dark and linen sections should alternate to create rhythm.
- Gold should remain scarce and purposeful, roughly 10% of the visual weight.
- Editorial grey is not a second CTA color. Use it only for oversized background typography and quiet narrative accents.
- Never use pure `#000000` or `#ffffff`.
- Never use gradient text.

## 5. Typography

### Font families

```css
font-family: "Poppins", sans-serif; /* display and UI */
font-family: "Inter", sans-serif;   /* body copy */
```

Load from Google Fonts:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
```

### Type roles

- Hero and section titles: Poppins 600, tight tracking, balanced wrapping.
- Card or feature titles: Poppins 600.
- Buttons, labels, dates, numbers, and navigation: Poppins 600.
- Body and supporting copy: Inter 300 or 400.
- Never use another font without explicit approval.

### Mobile type scale

```css
--type-label: 10px;
--type-body: 16px;
--type-card: 17px;
--type-subhead: 28px;
--type-section: clamp(38px, 11vw, 58px);
--type-hero: clamp(43px, 13.7vw, 68px);
```

### Typography rules

- Hero line-height: approximately `0.91`.
- Section heading line-height: approximately `0.96`.
- Display tracking: `-0.05em` to `-0.07em`.
- Labels: uppercase with `0.14em` to `0.18em` tracking.
- Body line-height: `1.55` to `1.65`.
- Body text must remain at least `16px`.
- Body measure should stay under `65ch`; mobile supporting copy is usually `30ch` to `38ch`.
- Use `font-variant-numeric: tabular-nums` for countdowns, dates, and aligned figures.

## 6. Mobile-first canvas

The current experience is intentionally mobile-oriented.

```css
.page {
  width: min(100%, 520px);
  margin-inline: auto;
  overflow: hidden;
  background: var(--birc-ink);
}
```

### Layout rules

- Design the page at `320px`, `375px`, `390px`, and `520px` widths.
- Default horizontal padding: `22px`.
- Default major section padding: `88px` to `104px` vertically.
- Minimum touch target: `44px`.
- Use full-width sections. Do not wrap every section in a floating card.
- Use spacing and dividers before adding containers.
- Do not create desktop multi-column layouts inside this mobile version.
- Horizontally scrolling content must use scroll snapping or explicit navigation.
- Keep speaker portraits symmetrical in a two-column grid with identical `3 / 4` rectangles and no staggered vertical offsets.

## 7. Spatial rhythm

Use a 4px spacing foundation:

```text
4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 72, 88, 96, 104
```

Recommended assignments:

- label to heading: `16px`
- heading to supporting copy: `16px` to `24px`
- section heading block to content: `40px` to `48px`
- repeated rows: `20px` to `28px`
- major section separation: `88px` to `104px`

Do not use identical padding for every section. Alternate compact, immersive, and editorial sections to create pace.

## 8. Section language

### Header

- Fixed at the top of the `520px` canvas.
- Official white BIRC logo on the left.
- Menu icon on the right.
- No Register button in the top navigation.
- On scroll, use a solid ink background and a subtle dark divider.

### Hero

- Full viewport height.
- Large Poppins statement, left aligned.
- Gold primary CTA and outlined secondary CTA.
- Compact two-column facts grid below actions.
- Subtle geometric or grain-inspired background only. It must not reduce legibility.

### Editorial statements

- Use a small eyebrow, a large statement, and restrained metadata.
- Give these sections deliberate top and bottom padding.
- Never leave accidental empty space between the statement and the next section.

### Participation pathways

- Use three vertically stacked panels of identical height and shape.
- Each panel includes number, audience label, title, description, and action.
- Keep visual treatment consistent across Attend, Exhibit, and Sponsor.

### Statistics

- Use large Poppins figures and small right-aligned labels.
- Separate rows with light dividers.
- Use tabular numerals.
- Do not turn statistics into generic dashboard cards.

### Experience Zones

- Present one immersive zone at a time.
- Allow swipe plus Previous and Next controls.
- Keep the counter and progress indicator visible.
- Give each zone a distinct abstract motion treatment based on its meaning.
- Animation is explanatory, not decoration.
- Preserve all nine names and descriptions.

### Dates and programme

- Combine month and dates into one composition.
- `October` is a large Poppins heading.
- `23 24 25` sits directly below in the same size and style, all in BIRC gold.
- Follow with the three-day vertical programme timeline.
- The timeline fills progressively as the user scrolls.

### Leader quotes

- One large editorial quote per view.
- Support swipe and explicit Previous/Next controls.
- Keep speaker name and role anchored below a divider.
- Avoid testimonial cards.

### Why BIRC

- Use four full-width editorial panels.
- Large words `INDIA`, `TRADE`, `365`, and `ONE` use exact editorial grey `#2b2b27`.
- Odd panels enter from right to left; even panels enter from left to right.
- The large word settles behind the readable foreground copy.
- Keep the descriptive copy high contrast and unobstructed.

### Speakers

- Use a symmetrical two-column grid.
- Every portrait placeholder uses the same `aspect-ratio: 3 / 4`.
- No alternating top margins and no masonry effect.
- Role in gold, name in linen, organization in muted text.

### Plan your visit

Use a clear `2 x 2` grid:

- Venue: Bharat Mandapam
- Stay: Partner hotels
- Travel: Getting here
- Support: Visas & FAQs

Each cell contains:

1. gold category label
2. Poppins title
3. concise action at the bottom
4. optional tap-to-expand detail using the approved content

Rules:

- Equal cell heights.
- Thin linen-context dividers.
- No images, maps, illustrations, or decorative icons.
- On tap, the dark surface rises from the bottom and reveals detail.
- Keep a small practical note below the grid if required.

### Final registration CTA

- Centre `Be in the room.` with strong Poppins typography.
- Use a gold full-width CTA.
- Countdown sits below with four equal columns.
- Use a restrained 3D rice-grain field in the background.
- Grains remain behind content and must never reduce text or button contrast.

### Footer

- Ink background, linen text, subtle dividers.
- Newsletter field first, navigation second, legal copy last.
- Do not add unnecessary social icons or extra navigation labels.

## 9. Buttons and links

### Primary button

```css
.button-primary {
  min-height: 56px;
  padding-inline: 22px;
  background: var(--birc-gold);
  color: var(--birc-ink);
  font: 600 13px "Poppins", sans-serif;
}
```

### Secondary button

- Transparent on dark.
- One-pixel dark-line border.
- Linen text.

### Interaction rules

- Keep button shapes rectangular, not pill-shaped.
- Use the north-east arrow `↗` for external or conversion actions.
- Use `→` for next-step navigation.
- Active press: translate no more than `1px` or invert the surface.
- Keyboard focus: `3px` BIRC gold outline with `2px` offset.
- Never remove focus styling.

## 10. Motion system

Motion should explain sequence, hierarchy, or spatial movement.

### Easing

```css
--ease-out-expo: cubic-bezier(.16, 1, .3, 1);
--ease-in: cubic-bezier(.7, 0, .84, 0);
--ease-in-out: cubic-bezier(.65, 0, .35, 1);
```

### Durations

- press and color feedback: `100ms` to `150ms`
- tabs, arrows, and active states: `200ms` to `300ms`
- accordion and carousel transitions: `400ms` to `550ms`
- section entrances: `650ms` to `800ms`

### Approved motion patterns

- Fade and rise: `opacity: 0` plus `translateY(22px)` to rest.
- Horizontal story entrance: translate from outside the relevant edge to rest.
- Carousel: translate the track on the x-axis.
- Progress: scale or width from the correct origin.
- Grain drift: very slow, low-amplitude transform animation.
- Accordion: `grid-template-rows: 0fr` to `1fr` only when progressive disclosure is necessary.

### Motion restrictions

- Prefer `transform` and `opacity`.
- No bounce, elastic, spinning UI, or constant decorative motion.
- Do not animate every element in a section.
- Stagger at `50ms` to `120ms`, capped below `500ms` total.
- Respect `prefers-reduced-motion` by removing nonessential animations and transitions.

## 11. Interaction and accessibility

- Use semantic `header`, `nav`, `main`, `section`, `article`, `footer`, and button elements.
- Every image requires useful alt text. Decorative images use empty alt text.
- Menu button requires an accessible label and Escape-to-close behavior.
- Expandable content must use buttons and expose state through `aria-expanded`.
- Active carousel item and progress must be understandable without motion.
- Maintain WCAG AA contrast for body text and controls.
- Do not place muted text over complex backgrounds.
- Inputs require labels or accessible names.
- Do not rely on color alone to communicate selected or expanded states.

## 12. Content adaptation workflow

Use this sequence when styling another BIRC page:

1. Inventory every existing content block and link.
2. Copy the content exactly into semantic HTML.
3. Assign each block to the closest BIRC section pattern.
4. Apply the shared tokens, Poppins/Inter hierarchy, and mobile canvas.
5. Add only the minimum motion required to explain the section.
6. Verify no content was lost, shortened, reordered incorrectly, or fabricated.
7. Test at 320px, 375px, 390px, and 520px.
8. Test keyboard focus, reduced motion, menu behavior, and overflow.
9. Compare against `index.html` for visual consistency.

## 13. Technical convention

New pages should reuse the same CSS custom properties and class vocabulary wherever practical. If the project is later split into shared files, use:

```text
/index.html
/design.md
/assets/
/styles/tokens.css
/styles/base.css
/styles/components.css
/scripts/site.js
/pages/<page-name>.html
```

Until that refactor is approved, `index.html` remains the implementation source of truth. Do not silently introduce a framework or build system.

## 14. Do not do this

- Do not rewrite approved content to fit a layout.
- Do not add a new palette.
- Do not swap Poppins or Inter.
- Do not add gradient text.
- Do not use glassmorphism.
- Do not make every section a card grid.
- Do not use excessive rounded corners or pill buttons.
- Do not stagger speaker portraits.
- Do not put images in Plan your visit.
- Do not add a Register button to the fixed navbar.
- Do not use generic stock-rice photography as a default.
- Do not animate layout properties continuously.
- Do not ship a page that only looks correct at one phone width.

## 15. Final acceptance checklist

A new page is ready only when:

- all original content is present and unchanged
- official BIRC logo is used
- colors match the exact tokens
- headings use Poppins and body copy uses Inter
- the page is mobile-first and works from 320px to 520px
- spacing follows the established editorial rhythm
- actions are clear and have accessible states
- motion is purposeful and reduced-motion-safe
- no horizontal overflow exists
- the page visually belongs beside `index.html`
