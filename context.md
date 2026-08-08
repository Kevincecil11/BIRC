# BIRC Project Context

Last updated: 2026-08-03 (Partnership added; Experience made full-bleed) (detailed Experience page added)

This is the living handoff file for the BIRC website. Read this file first whenever the repository is opened in a new chat, coding session, or by a new contributor. Keep it accurate whenever pages, navigation, content, styling rules, deployment, or project decisions change.

## 1. Required reading order

Before making any change:

1. Read `context.md` for project state, architecture, links, and pending work.
2. Read `design.md` for mandatory visual, interaction, typography, color, motion, accessibility, and content-preservation rules.
3. Inspect the current target HTML file before editing it.
4. Treat repository files on `main` as the source of truth, not old chat artifacts or screenshots.

If `context.md` and the repository disagree, inspect recent commits and update `context.md` as part of the same change.

## 2. Project purpose

BIRC is the mobile-first website for the Bharat International Rice Conference 2026. The experience positions India at the centre of the global rice industry and communicates conference participation, programme, exhibition, experience zones, partnership, travel, and registration information.

The visual direction is cinematic, editorial, premium, precise, and easy to understand. Existing approved content must be preserved when restyling supplied page files.

## 3. Repository and deployment

- Repository: `https://github.com/Kevincecil11/BIRC`
- Default branch: `main`
- GitHub Pages site: `https://kevincecil11.github.io/BIRC/`
- Pages is deployed through GitHub Actions workflows in `.github/workflows/`.
- The repository is public so GitHub Pages can deploy under the current GitHub plan.
- Official logo asset: `https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png`

### Deployment caution

Several temporary workflow files were created while enabling Pages and applying changes. The active publishing approach uploads the current repository to GitHub Pages with `actions/upload-pages-artifact` and `actions/deploy-pages`.

If a Pages update does not appear:

1. Confirm the intended code is committed to `main`.
2. Check GitHub Actions for an older deployment stuck in progress.
3. Cancel the stuck deployment if it blocks the current queued run.
4. Trigger the current publish workflow.
5. Verify the live URL after the run succeeds.

Do not assume a commit is live until the Pages URL is checked.

The official dated ivory BIRC logo is used on every current HTML page: `https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png`.

## 4. Current source files

### `index.html`

The homepage and original implementation source of truth.

Current homepage sections include:

1. Fixed header and hamburger menu
2. Hero
3. Conference highlights ticker
4. Purpose statement
5. Three participation pathways: Attend, Exhibit, Sponsor
6. BIRC statistics
7. Knowledge Sessions: 9 sessions across Day 1 and Day 2
8. What Makes the Knowledge Sessions Different: 9 expandable differentiators
9. Experience Zones carousel
10. October 23, 24, 25 date composition
11. Three-day programme timeline
12. Industry leader quotes
13. Why BIRC
14. Impressions gallery
15. Plan your visit 2 x 2 grid
16. Final registration CTA with 3D rice-grain background
17. Footer and sticky registration CTA

The Speakers section was removed from the homepage and moved to `conference.html`.


### Homepage Knowledge Sessions

Two sections sit immediately above Experience Zones in `index.html`:

1. `#knowledge-sessions`: all nine Knowledge Sessions across Friday 23 October and Saturday 24 October.
2. `#knowledge-difference`: the EY report note plus nine expandable reasons the BIRC 2026 sessions are different.

The copy was extracted from two user-supplied images on 2026-08-01 and must remain unchanged unless revised source content is supplied. The differentiators use a one-open-at-a-time accordion.

### `about.html`

A separate About page built from the supplied About content and restyled to match the BIRC system.

Current flow:

1. About hero
2. Mission statement
3. Values: Collaboration, Innovation, Leadership
4. Our Story
5. Results and statistics
6. Organisers placeholders
7. Advisory Board placeholders
8. Industry Overview
9. Industry pillars
10. Footer

Content originated from the user-provided About HTML. Preserve that approved content unless the user supplies replacements.




### `creators.html`

Influencers is three separate pages: Content Creators (`creators.html`), Rice Masterchef (`rice-masterchef.html`), and Artists / Rice Art Showcase (`artists.html`). Content Creators is implemented from approved mobile screenshots, including access outcomes, scoring factors, eligibility, application flow, form fields, and FAQ questions. Rice Masterchef is implemented from six approved mobile screenshots, including competition proposition, three participation benefits, ₹1,00,000 prize, Media Byte, On-Stage Recognition, creator access tiers, and application form. Artists is implemented from ten approved Rice Art Showcase screenshots, including material manifesto, eight pathways, ₹1,00,000 prize, recognition, and application form. Influencers appears immediately above Partnership as a three-item hamburger submenu across all current pages.

### `partnership.html`

A separate Partnership page built from the user-supplied sponsorship content and styled with `design.md`. Partnership is one direct hamburger link with no submenu. The page preserves all supplied sponsorship tiers, prices, GST notes, package benefits, promotional visibility, special opportunities, and partner logo placeholders. Keep the detailed accordion content intact unless approved replacements are supplied.



### `contact.html`

Dedicated Contact page based on the mobile `birc.in/contact` structure and BIRC `design.md`. Approved visible copy includes “We’d love to hear from you,” “Contact Us,” “Questions about BIRC 2026? Our team is here to help,” “Get in touch,” and “You Have Questions. We Have Answers.” The page routes users toward Visit, Exhibition, Partnership, or Conference and includes a working enquiry form that opens the user’s email client with a prefilled subject/body. Official source details are now included: 73 LGF, World Trade Center, Barakhamba Avenue, Connaught Place, New Delhi 110001; Mon–Sun 09:00–18:00 local; booking@birc.in; visit@birc.in; +91-7303093821. The enquiry form routes Visiting enquiries to visit@birc.in and other enquiries to booking@birc.in. Contact is a direct hamburger link on all current pages.

### `plan-visit.html`

Dedicated Plan Visit page built from supplied content and `design.md`. Sections and submenu anchors: Venue & Location (`#venue`), Hotels (`#hotels`), How to Reach (`#travel`), and FAQs (`#faqs`). Travel includes Metro, Airport, Railway, Bus, and Car/Taxi tabs. All current site menus expose this four-item Plan Visit submenu.

### `experience.html`

A dedicated detailed Experience page containing all nine approved zones in this order:

1. The Rice Route Map
2. Seed Cloud
3. The Rice Archive
4. Rice Through Time
5. How the World Eats Rice
6. Hands of Rice
7. The World Within
8. Rice Mirror
9. Beyond the Bowl

Each zone has its own anchor, abstract visual treatment, and the approved homepage description. The page has no numeric rail and no zone submenu. Experience is one direct hamburger link across all pages. The approved layout uses a dark cinematic hero, then a consistent linen editorial body where every zone retains its immersive abstract visual inside a full-bleed ink panel, followed by dark closing CTA and footer. Zone visuals touch both edges of the 520px canvas; do not add left or right gutters around them. Do not invent longer zone claims without supplied content.

### `conference.html`

A separate Conference page linked from the hamburger menu.

Required content flow:

1. Speakers
2. Agenda and Schedule
3. Workshops
4. Learning Academy

Current state:

- Speakers are implemented and were moved from the homepage.
- Agenda and Schedule is a styled placeholder awaiting the user's file.
- Workshops is a styled placeholder awaiting content.
- Learning Academy is a styled placeholder awaiting content.

When the files arrive, replace the matching placeholder section while preserving the order above.

### `design.md`

The mandatory design system and page adaptation guide. It defines exact colors, typography, spacing, motion, components, accessibility, section patterns, and content-preservation rules.

All new pages and edits must follow `design.md`.

### `context.md`

This file. It records the living project state, page relationships, decisions, deployment information, and pending work.

## 5. Planned pages

### `exhibition.html`

Not created yet. It will be linked from the Exhibition hamburger item and must contain this flow:

1. Why exhibit
2. Exhibitor profile
3. Space rental

The submenu links are already prepared as:

- `exhibition.html#why-exhibit`
- `exhibition.html#exhibitor-profile`
- `exhibition.html#space-rental`

Do not fabricate the Exhibition page content. Wait for the user's supplied file or content.

### Future supplied Conference sections

Pending:

- Agenda and Schedule file
- Workshops content/file
- Learning Academy content/file

## 6. Navigation architecture

The hamburger menu must remain consistent across every page.

Current top-level order:

1. Home
2. About
3. Conference
4. Exhibition
5. Experience
6. Partnership
7. Plan Visit
8. Contact

### Current destinations

- Home: `index.html`
- About: `about.html`
- Conference: `conference.html`
- Exhibition: expandable submenu
- Experience: direct link to `experience.html`; no dropdown or numbered submenu
- Partnership: `partnership.html`, direct link with no dropdown
- Plan Visit: one direct link to `plan-visit.html`; no dropdown
- Contact: direct link to `contact.html`

### Dropdown rules

- About has no dropdown.
- Conference has no dropdown.
- Exhibition has exactly three submenu items.
- Exhibition submenu labels align left and their numbers align right:
  - Why exhibit | 01
  - Exhibitor profile | 02
  - Space rental | 03
- Partnership and Plan Visit currently retain dropdown indicators from the approved menu direction, but dedicated submenu structures have not yet been supplied.

### Social links

The drawer footer includes:

- Instagram
- LinkedIn

Their final URLs have not yet been supplied. Do not invent them.


### Homepage quick-action dock

The homepage has one floating circular `+` button to avoid clutter. Tapping it reveals four stacked actions: Book your stand, Register to visit, Login, and WhatsApp. Tapping outside, choosing an action, or pressing Escape closes it. Final Login and WhatsApp destination URLs are still pending and must not be invented.

The approved final CTA background is the supplied rice-grain world map stored at `assets/rice-world-map.png`. Preserve the full-bleed crop and dark readability overlay.

### Homepage gallery scale

BIRC in pictures image/video placeholders are intentionally 20% larger than the earlier gallery dimensions. Preserve this scale unless explicitly changed.

Experience navigation must remain a single direct link. Do not add the nine zones as hamburger submenus or restore a numbered 1–9 rail.

Experience visual panels must remain full-bleed across the mobile canvas with zero left/right spacing. Text keeps 22px padding above or below the visual.

Experience page styling must match the rest of BIRC: dark hero, linen content body, ink visual panels, gold accents, dark CTA/footer. Keep the immersive abstract zone visuals from the original version, but no numeric rail and no nine-item hamburger submenu.

Partnership card rule: Sponsorship Package cards and Special Opportunity cards must use the exact same linen background, one-pixel ink border, shadow-free surface, black action bar, expanded divider, and keyboard focus treatment.

Partnership styling: Sponsorship Packages and Special Opportunities both use the cream section background and black one-pixel card frames. No card is highlighted by default; the gold outer outline appears only while that card is opened to view benefits. Do not make the Sponsorship Packages section black.

Canonical menu rule: every page uses the same top-level order and styling. Only Exhibition has a dropdown. About, Conference, Experience, Partnership, and Plan Visit are direct links.

Exhibition profile rule: do not show the separate horizontal Rice Millers / Exporters / Traders selector bar. Use the expandable profile list only. Part 1, Part 2, and Part 3 eyebrow labels use the same gold treatment.

Contact social controls use inline SVG icons for Instagram, LinkedIn, Facebook, and X; do not revert them to text initials. The official contact block begins directly with “Reach the BIRC team.” and has no “Contact details” eyebrow.

Visible event date ranges use `23-24-25`, never `23–25` or `23-25`. Influencers sits directly above Partnership and contains exactly Content Creators, Rice Masterchef, and Artists.

Influencer pages must never use navy or blue. Use only the exact design.md ink, raised ink, linen, gold, editorial grey, and muted tokens. Each Influencers submenu item opens its own separate HTML page.

Influencer pages have a zero-blue rule: use `#0d0d0b` ink and `#191916` raised ink for every dark surface. Source-site navy values such as `#17354c`, `#18334b`, and `#0f253a` are forbidden.

Content Creators scoring factors are displayed as five bullet rows, not a matrix. The VIP Creator Pass must always use high-contrast linen heading text on raised ink. In Artists, the four “Tiny Material. Infinite Expression.” tiles are an equal 2 x 2 grid with identical dimensions.

Homepage Register actions open an accessible native dialog with exactly three choices: Register as Visitor (`https://birc.in/register/visitor`), Register as Exhibitor (`https://birc.in/register/exhibitor`), and Register as Buyer (`https://birc.in/register/buyer`). The dialog also links registered users to `https://birc.in/login`. Preserve this chooser instead of sending generic Register buttons directly to one role.

Registration uses one shared minimal two-step page at `register.html?type=visitor|exhibitor|buyer`. Step 1 is identical for all roles: name, company, mobile/country code, WhatsApp match, country, email, remember me. Step 2 is identical: multi-select Industry Type plus declaration. Only the title and submission routing differ by role. Homepage chooser links to these local forms.

## 7. Design decisions that must persist

Follow `design.md` for full details. Important current decisions:

- Fonts: Poppins for display/UI and Inter for body copy.
- Mobile canvas: maximum width `520px`.
- Primary colors: ink, linen, and gold.
- Editorial grey: `#2b2b27`.
- The old moss green `#566746` has been retired and must not be reintroduced.
- Editorial grey replaces moss in large background words, programme numbers, and quiet narrative accents.
- Homepage programme numbers `01`, `02`, `03` use the editorial grey and are intentionally subtle.
- Header contains the official logo and menu icon only. No Register button in the fixed header.
- Participation cards are vertically stacked with matching dimensions.
- Speakers use symmetrical 3:4 portrait rectangles with no staggered offsets.
- Plan your visit uses an image-free 2 x 2 grid.
- Final registration CTA uses the supplied rice world-map image at `assets/rice-world-map.png`, replacing both the original 3D grains and the temporary Rice Current.
- Motion must be purposeful and reduced-motion-safe.

## 8. Content handling rules

When the user supplies an HTML page with correct content but incorrect styling:

1. Extract and preserve all meaningful supplied content.
2. Remove artifact chrome, obsolete inline styling, and conflicting visual systems.
3. Rebuild it as a separate, editable HTML page in this repository.
4. Apply `design.md` without losing or rewriting content.
5. Add the page to navigation where requested.
6. Update cross-page links on all existing pages.
7. Update `context.md` in the same change.
8. Publish and verify GitHub Pages.

Do not merge every page into `index.html`. Separate pages are intentional so they remain easy to edit.

## 9. Content placeholders

Some current content is intentionally placeholder content because final assets were not supplied:

- Speaker portraits
- About organiser logos
- About Advisory Board names, titles, and portraits
- Conference Agenda and Schedule content
- Conference Workshops content
- Conference Learning Academy content
- Exhibition page and all its content
- Instagram and LinkedIn URLs

Do not present placeholders as verified facts. Replace them only with supplied approved content.

## 10. Current factual and copy constraints

Approved recurring facts currently include:

- Event dates: 23-24-25 October 2026
- Venue: Bharat Mandapam, Halls 4 and 5, New Delhi
- 30,000+ participants
- 120+ countries
- 250+ speakers
- 300+ exhibitors
- ₹30,435 Cr in MoUs
- Nine Experience Zones

Do not change these without explicit updated content from the user.

## 11. Change checklist

Every material edit must include:

- Change the correct source HTML file.
- Keep the navigation consistent across all pages.
- Follow `design.md`.
- Preserve approved content.
- Update `context.md` with new pages, removed sections, changed links, pending items, or design decisions.
- Commit changes to `main`.
- Trigger GitHub Pages publishing when appropriate.
- Verify the live page, not only the repository commit.

## 12. How to update this file

Update `context.md` whenever any of these happen:

- a page is added, renamed, moved, or deleted
- a section moves between pages
- navigation or submenu structure changes
- a placeholder is replaced with final content
- design tokens or fonts change
- a new permanent asset or external URL is introduced
- deployment architecture changes
- a major UI or motion decision is approved
- the user establishes a new standing project rule

Keep this file factual and concise enough to scan. Remove stale instructions rather than stacking contradictory history.

## 13. Immediate next work

Expected next steps:

1. Receive Exhibition page content and create `exhibition.html`.
2. Receive Agenda and Schedule content and add it to `conference.html`.
3. Receive Workshops content and add it to `conference.html`.
4. Receive Learning Academy content and add it to `conference.html`.
5. Replace remaining logos, portraits, names, and social URLs when supplied.

## 14. New-chat instruction

When starting work in a new chat, use this instruction:

> Read `context.md`, then `design.md`, then inspect the current target file. Treat repository `main` as the source of truth. Preserve supplied content, keep navigation synchronized across pages, update `context.md` with every structural decision, and verify GitHub Pages after publishing.


## Exhibition display rule

Exhibition is a hash-driven single-section experience. Selecting a submenu or section switcher item shows only that section and hides the other two. The default view is Why exhibit. Do not return it to one long scrolling page unless explicitly requested.

All three Exhibition views use the same black/ink background system. Do not switch Exhibitor Profile or Space Rental back to linen; only gold, linen text, muted grey, and editorial grey may vary within the dark surfaces.
- Registration flow: every homepage registration CTA opens a native chooser for Visitor, Exhibitor, or Buyer; each choice routes to `register.html?type=<role>`.
## Desktop homepage architecture

- `index.html` remains the mobile homepage and source for shared homepage content.
- `desktop.html` is the dedicated desktop homepage, currently the only desktop-specific page.
- Automatic routing chooses desktop at 900px+ with a fine pointer and mobile below that. Manual Desktop view and Mobile view controls override detection for the browser session.
- For now, secondary pages remain their existing mobile implementations.
- Desktop homepage content and registration behavior must stay synchronized with `index.html`.
- Desktop homepage v2 uses desktop-native section compositions, bounded 1440px rhythm, non-obstructive header actions, compact statistics, aligned date composition, and no floating desktop CTA/dock.
- Desktop homepage v4 was rebuilt with one clean 1240px editorial grid and audited section-by-section for hierarchy, alignment, overflow, interaction placement, and desktop readability. Artifact editing chrome is excluded from the published desktop page.
## Supplied influencer source documents audit (2026-08-08)

The mobile Content Creators, Rice Masterchef, and Artists pages were checked against the three supplied BIRC source documents. Missing approved application fields, qualification details, process steps, access rules, FAQs, Rice Art opportunity sections, curatorial journey, and Why BIRC content were added. Desktop files were not changed.
## Desktop About page

- `desktop-about.html` is the purpose-built desktop About experience.
- It preserves the approved mobile About content while using desktop-native hero, mission, three-column values, split story, results, organisers, Advisory Board, industry overview, registration chooser, and quick-action dock.
- The mobile `about.html` remains unchanged.
