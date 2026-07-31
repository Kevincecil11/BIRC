# BIRC Project Context

Last updated: 2026-07-31

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
- Official logo asset: `https://ik.imagekit.io/18ab23oqaj/birc-mark-white-solid.png`

### Deployment caution

Several temporary workflow files were created while enabling Pages and applying changes. The active publishing approach uploads the current repository to GitHub Pages with `actions/upload-pages-artifact` and `actions/deploy-pages`.

If a Pages update does not appear:

1. Confirm the intended code is committed to `main`.
2. Check GitHub Actions for an older deployment stuck in progress.
3. Cancel the stuck deployment if it blocks the current queued run.
4. Trigger the current publish workflow.
5. Verify the live URL after the run succeeds.

Do not assume a commit is live until the Pages URL is checked.

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
7. Experience Zones carousel
8. October 23, 24, 25 date composition
9. Three-day programme timeline
10. Industry leader quotes
11. Why BIRC
12. Impressions gallery
13. Plan your visit 2 x 2 grid
14. Final registration CTA with 3D rice-grain background
15. Footer and sticky registration CTA

The Speakers section was removed from the homepage and moved to `conference.html`.

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
- Experience: `index.html#zones`
- Partnership: currently points to the homepage participation area until a dedicated page is created
- Plan Visit: `index.html#visit`
- Contact: current page footer contact anchor

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
- Final registration CTA uses restrained animated 3D rice grains behind the content.
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

- Event dates: 23–25 October 2026
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
