# BIRC Project Context

Last updated: 2026-08-26. Consolidated rewrite. Previous versions stacked chronological "desktop polish" notes at the bottom until the top sections contradicted the repository. That history has been removed and folded into the sections below. Per section 12, remove stale instructions rather than stacking them.

This is the living handoff file for the BIRC website. Read it first whenever the repository is opened in a new chat, coding session, or by a new contributor.

## 1. Required reading order

Before making any change:

1. Read `context.md` for project state, architecture, and pending work.
2. Read `design.md` for mandatory visual, typography, colour, motion, and content-preservation rules.
3. Inspect the current target HTML file before editing it.
4. Treat repository `main` as the source of truth, not old chat artifacts or screenshots.

If this file and the repository disagree, inspect recent commits and correct this file in the same change.

## 2. Project purpose

The website for the Bharat International Rice Conference 2026. It positions India at the centre of the global rice industry and communicates conference, exhibition, experience, partnership, travel, and registration information.

Visual direction: cinematic, editorial, premium, precise. Approved content must be preserved when restyling.

## 3. Repository and deployment

- Repository: `https://github.com/Kevincecil11/BIRC`
- Default branch: `main`
- Live site: `https://kevincecil11.github.io/BIRC/`
- Public repo, required for Pages on the current plan.
- Logo asset (every page): `https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png`
- Registration logo, desktop only: `https://ik.imagekit.io/18ab23oqaj/birc.png?updatedAt=1786729307998`. Supplied by Kevin on 2026-08-15 and swapped in by script at 900px and above. Mobile `register.html` keeps the dated ivory logo.
- Rice world map asset: `assets/rice-world-map.png`
- `publish-refresh.html` at the repository root is a deployment marker only. It exists to retrigger Pages and carries no content.

### Publishing

`.github/workflows/publish-desktop-home.yml` is the active publish workflow. It watches `**.html` and deploys the repository root with `actions/upload-pages-artifact` and `actions/deploy-pages`. Concurrency group `pages`, `cancel-in-progress: true`.

**CSS and JS commits do not trigger publishing on their own.** The workflow only watches HTML, so a change limited to `assets/*.css` or `assets/*.js` needs an accompanying HTML commit (touch `publish-refresh.html`) or it will never reach the live site.

If an update does not appear live:

1. Confirm the code is committed to `main`.
2. Check Actions for an older deployment stuck queued or in progress.
3. Cancel the stuck run.
4. Re-trigger the publish workflow.
5. Verify the live URL, never just the commit.

### Workflow debt

Around 70 single-purpose workflow files have accumulated in `.github/workflows/`. Most are spent one-shot patches. Only `publish-desktop-home.yml` and `deploy-pages.yml` matter going forward. The rest can be deleted in a cleanup pass. **Batch related edits into one workflow instead of writing a new file per fix.** The per-fix pattern was the single largest source of wasted round trips on this project.

Notes on writing patch workflows, learned the hard way:

- Exact-string matching inside Python heredocs fails silently. Use `re.subn` and assert the match count.
- Never reference a CSS `var()` from JavaScript. Use a literal.
- Playwright screenshot workflows were attempted twice and abandoned. Verify with a live page fetch instead.

## 4. Two parallel experiences

The site maintains a mobile experience and a separate desktop experience as distinct files.

- Every `desktop-*.html` page begins with a redirect script: below 900px it replaces location with its mobile counterpart.
- Every desktop page has a `Mobile view` control in the masthead or menu pointing at its own mobile file.
- **The mobile layouts are approved and must not be redesigned. A content-only parity audit across all 13 mobile pages was completed on 2026-08-26; future desktop content changes must be mirrored on mobile without changing its approved visual system.**

### Mobile pages (13)

`index.html`, `about.html`, `conference.html`, `exhibition.html`, `experience.html`, `creators.html`, `rice-masterchef.html`, `artists.html`, `partnership.html`, `plan-visit.html`, `contact.html`, `register.html`, `media-coverage.html`

Mobile canvas is capped at `520px` with a centred `.page` wrapper.

### Desktop pages (14)

`desktop.html`, `desktop-about.html`, `desktop-conference.html`, `desktop-exhibition.html`, `desktop-exhibitor-profile.html`, `desktop-space-rental.html`, `desktop-experience.html`, `desktop-creators.html`, `desktop-rice-masterchef.html`, `desktop-artists.html`, `desktop-partnership.html`, `desktop-plan-visit.html`, `desktop-contact.html`, `desktop-media-coverage.html`

## 5. The most important desktop lesson

**Do not build a desktop page by copying mobile markup and layering desktop CSS overrides on top. It fails every time.**

This was attempted repeatedly and rejected every time. The homepage took five attempts before a from-scratch rewrite was accepted. Six pages built with the copy-and-override method later had to be redesigned. The failure mode is concrete, not aesthetic: those pages ended up carrying four competing stylesheets (mobile base, an anonymous desktop block, `#dt-polish`, `#desk-refine`), and mobile border rules such as `.venue-row:last-child{border:0}` and `.route:nth-child(n+3){border-bottom:0}` survived every override and drew half-finished grid lines. Brittle `body > main:nth-child(...)` colour patches were also used to fix text colour and were the cause of the wrong-coloured form text.

**Author every desktop page as a standalone document with exactly one stylesheet.** No mobile CSS, no override layers, no `nth-child` path selectors.

### Clean, single-stylesheet pages

`desktop-partnership.html`, `desktop-plan-visit.html`, `desktop-contact.html`, `desktop-conference.html`. Use these four as the reference implementation for any new or rebuilt desktop page.

### Pages still carrying layered stylesheets

`desktop-creators.html`, `desktop-rice-masterchef.html`, `desktop-artists.html`, and the About / Exhibition / Experience set. They render correctly today but are fragile. Rebuild them as standalone documents when they next need substantive work rather than patching them again.

## 6. Desktop design system

Tokens used by the clean pages:

```
--sh: min(1680px, calc(100% - 64px))    /* homepage wide content shell */
--side: max(56px, calc((100vw - 1320px)/2))  /* section gutter */
--nav: 76px                              /* masthead height */
--e: cubic-bezier(.16,1,.3,1)            /* ease out */
body { min-width: 1100px }
```

- Section rhythm: `132px` vertical padding on standard sections, `104px + nav` on heroes.
- Desktop Experience Zones heading sits directly above the large visual stage and aligns to the square's inner content edge near its 01 marker. The complete three-day statement and October/date composition are centered across the page, while the `Three days` eyebrow remains on the left editorial rail. Voices is a continuously moving four-column grid that travels **right to left**; the `04 voices in view` and `Pause on hover` labels were removed.
- Desktop homepage uses a wide 1680px shell with 32px minimum side gutters. Its hero is a balanced 1:1 composition: the copy column and summit dossier have equal 620px height and matching top/bottom edges, while the dossier uses a fixed label column, five equal fact rows, and four equal countdown cells.
- Breakpoint at `1180px` narrows the shell to `calc(100% - 64px)` and the gutter to `32px`.

### Shared desktop controls

`assets/desktop-controls.js` owns the desktop countdown and the registration role chooser. The countdown writes to `[data-shared-clock]`, `[data-clock]`, `#navClock`, `#cd/#ch/#cm/#cs`, and every `.countdown`, `.clockrow` or `.final .clock` block by ordered `strong` elements, so masthead and footer clocks stay in sync. It refreshes on `visibilitychange` and `pageshow`.

Close controls are square, thin-bordered and top-right. No circular close buttons anywhere on desktop.

### Masthead

Desktop homepage masthead is 88px high and uses the official logo at 170 x 55px. The navigation is organized into three deliberate groups: the enlarged brand, a shared utility rail containing Search plus the EY report, Buyer facilitation, and 2026 agenda links, then the countdown, Login, Register, and sandwich menu at the extreme right. The three document labels use the same 11px Poppins weight and tracking as Login and Register; at narrower desktop widths they retain their icons while their labels collapse to keep the header breathable. The sandwich drawer is a single, left-aligned vertical stack: primary links have no numbers, while submenu items retain their small sequence numbers. The Mobile view control is removed from this homepage masthead. Book your stand and green WhatsApp actions are stacked at the bottom-right as compact 158 x 46px controls. All 14 desktop pages use the same homepage-derived navigation.

Desktop homepage eyebrow titles use 13.2px Poppins. The Purpose section uses a compact editorial rhythm with balanced 3-line copy, 52-66px on wide desktop, reduced section padding, and aligned label/content columns.

### Left alignment is a standing rule

All desktop pages use the shared 1680px shell, 32px minimum gutters, 13.2px eyebrow labels, and homepage navigation. Desktop homepage section introductions share one editorial grid token: a 240px label rail and 88px content gap on wide screens, scaling to 190/56 and 160/40 at narrower desktop widths. Purpose metadata uses an explicit aligned three-column grid beneath the statement.

Eyebrows, headings, leads, lists, forms, and FAQ stacks are all left-aligned with `margin-left: 0`. Nothing on desktop is centred, including forms and FAQ blocks that were previously `margin: auto`.

### Connected grids

**Never build a connected grid from per-cell borders.** Use `gap: 1px` with the line colour as the grid container background and the surface colour on each cell:

- `.mesh.light`: `--ll` lines, `--l` cells
- `.mesh.dark`: `--dl` lines, `--j2` cells

Every cell then shares a true hairline and nothing dangles. Also **keep cell counts even**: a 3-up row with four items leaves a visible orphan. Either pad the row with a genuine content cell or change the column count.

### Shared form treatment

Application and enquiry forms sit on a **gold section background** with a **linen panel** inside. Applies to `.apply` (Creators), `#apply.apply` (Artists), `.master-apply` (Masterchef), and the Contact enquiry section.

- Panel: `--l` background, `1px solid --ll`, `48px` padding, max width ~960px, left-aligned.
- Two-column field grid; textarea fields span full width.
- Labels: uppercase Poppins, `600 10px`, `.14em` tracking, colour `#4a453e`.
- Inputs: `#fffaf2` background, `1px solid --ll`, square corners, `15px` Inter.
- Focus: `2px solid --g2` outline with `2px` offset.
- Submit: ink background, linen text, auto width, left-aligned, `58px` min height.
- Followed by a small `doc-note` disclaimer.

## 7. Palette and type

Exact tokens from `design.md`:

| Token | Value | Role |
| --- | --- | --- |
| `--j` | `#0d0d0b` | ink |
| `--j2` | `#191916` | raised ink |
| `--l` | `#faf0e6` | linen |
| `--g` | `#ebb341` | gold |
| `--g2` | `#c98e25` | deep gold |
| `--m` | `#2b2b27` | editorial grey |
| `--dm` | `#aba49c` | muted on dark |
| `--lm` | `#6d6862` | muted on light |
| `--dl` | `#35332e` | line on dark |
| `--ll` | `#d8cec3` | line on light |

**Zero blue, ever.** Source-site navy values `#17354c`, `#18334b`, `#0f253a` are forbidden. The retired moss green `#566746` must not return; editorial grey replaced it in large background words and programme numbers.

Fonts: **Poppins** for display and UI, **Inter** for body. No other families.

Side-stripe accent borders (`border-left` as decoration) are banned. The Masterchef prize block was converted from a gold left stripe to a full gold border panel for this reason.

Decorative checkmarks are replaced by the angled gold pointer motif used in the Creator score bullets. Native form checkboxes keep their default behaviour and checked state.

## 8. Page-specific rules

### Homepage

- `index.html` mobile, `desktop.html` desktop. Content must stay synchronized.
- Desktop homepage was rebuilt from scratch on one editorial grid. Why BIRC is a 2x2 with large background words.
- Desktop homepage controls: countdown lives in the masthead; Book your stand and the green WhatsApp action with its official mark are stacked at the bottom-right. There is no full-width bottom bar and no desktop Mobile view control. Mobile controls remain unchanged.
- Mobile has one floating `+` dock revealing Book your stand, Register to visit, Login, WhatsApp. Login and WhatsApp URLs are still pending; do not invent them.
- The homepage Passes section and Published Across rail use explicit mobile overrides even when Mobile view is forced on a wide desktop browser; do not let desktop media queries compress or offset them.
- Desktop and mobile homepages share a native search dialog with live client-side results and popular queries. Desktop opens it from the navbar search control. Mobile adds Search and Documents icons beside the menu; Documents reveals the same EY report, Buyer facilitation, and 2026 agenda PDFs used on desktop.
- A continuously moving media coverage rail titled `Published across / 80` sits below the hero on desktop and mobile. Every publisher mark is clickable, motion pauses on hover and respects reduced motion. `See the coverage` opens the dedicated local coverage page.
- Desktop `BIRC in pictures` is a full-viewport chapter with 72vw by 68vh image panels; mobile keeps the approved compact gallery.
- Experience cards on the desktop homepage flip in place with yellow backs. **The whole card is clickable**, not only the Read more control.
- Final CTA uses `assets/rice-world-map.png` full-bleed with a dark readability overlay.
- Header holds logo and menu only. No Register button in the mobile fixed header.
- Public opening time is 10:00 AM daily. Homepage countdowns target 10:00 AM on 23 October 2026.

### Registration

Every Register CTA opens an accessible native `<dialog>` chooser with three choices, each routing to the shared local form:

- Visitor → `register.html?type=visitor`
- Exhibitor → `register.html?type=exhibitor`
- Buyer → `register.html?type=buyer`

The dialog also links existing users to `https://birc.in/login`. `register.html` is a two-step form: step 1 is name, company, mobile with country code, WhatsApp match, country, email, remember me; step 2 is multi-select Industry Type plus declaration. Only the title, logo and routing differ by role. Do not send a generic Register button straight to one role, and do not merge the three routes into one screen with role tabs.

Locked registration decisions:

- Preserve the current registration colours.
- The dark left panel is editorial and balanced: dated logo, statement, and When/Where metadata. It must not read as an empty logo block.
- `WhatsApp number is the same as mobile` sits beneath the field grid, not beside the phone field.
- On desktop the close control is **square** and pinned to the **top-right of the form panel**, not the dark panel. It follows the view, so it moves onto the success panel after submit.

### Exhibition

Desktop Exhibition is **three genuinely separate pages**: `desktop-exhibition.html` (Why exhibit), `desktop-exhibitor-profile.html`, `desktop-space-rental.html`. The navbar dropdown is the only navigation between them. The side-by-side section switcher and the centred yellow page-label strip were both removed and must not return.

Mobile `exhibition.html` stays hash-driven: selecting a submenu item shows one section and hides the other two, defaulting to Why exhibit. Do not convert it back to one long scroll.

All three views use the dark ink background system. Do not switch Exhibitor Profile or Space Rental to linen. Do not restore the horizontal Rice Millers / Exporters / Traders selector bar; use the expandable profile list only.

### Influencers

Three separate pages, never a combined one: Content Creators, Rice Masterchef, Artists. Sits directly above Partnership in the nav.

**The Creators page is the approved structural pattern.** Its flow is: hero (eyebrow, large title, lead, gold CTA, three-stat row) → light access section with numbered rows → score section with five bullet rows plus VIP, Standard and Day-3 pass cards → dark criteria section with pointer rows → light process section with numbered step cards → gold apply section containing the linen form panel → light FAQ accordions. When a sibling influencer page needs a redesign, match this.

- Creator access rows 01, 02 and 03 sit in **one connected desktop row**, not a 2x2 with an orphan.
- Scoring factors are five bullet rows, not a matrix.
- VIP Creator Pass must use high-contrast linen headings on raised ink.
- In Artists, the four "Tiny Material. Infinite Expression." tiles are an equal 2x2 with identical dimensions.
- Masterchef and Artists prize is `₹1,00,000`.

### Partnership

One direct nav link, no submenu. Desktop was rebuilt from scratch: hero with a spec list, then a **five-tier master/detail** (left rail of tiers, right benefit panel, gold outline on the selected tier), then Special Opportunities as a varied grid with Gala Dinner as a wide feature and a gold enquiry panel, then a partner marquee.

All supplied tiers, prices, GST notes, package benefits, promotional visibility, and special opportunities are preserved verbatim. Tiers: Platinum ₹50,00,000 / $57,480, Diamond ₹30,00,000 / $34,490, Gold ₹20,00,000 / $23,000, Silver ₹10,00,000 / $11,500, Bronze ₹5,00,000 / $5,750. Six special opportunities: Gala Dinner ₹20,00,000, Transport ₹15,00,000, Lunch ₹10,00,000 per day, Exhibition Entry Gates ₹10,00,000, Exhibitors'/Buyer Kit ₹10,00,000, Registration Counter ₹8,00,000.

**Content correction:** the supplied Lunch Sponsor line read "October 30 & 31", which contradicts the event dates. Desktop now reads "24 & 25 October". Mobile and desktop now both read "24 & 25 October".

On mobile, Sponsorship Package and Special Opportunity cards share one treatment: linen background, one-pixel ink border, no shadow, black action bar. No card is highlighted by default; the gold outer outline appears only while a card is open. Do not make the Sponsorship Packages section black.

### Plan Visit

Mobile `plan-visit.html` keeps its four-anchor structure: `#venue`, `#hotels`, `#travel`, `#faqs`, with Metro, Airport, Railway, Bus, and Car/Taxi tabs.

Desktop was rebuilt from scratch: venue stats as a connected 2x2 mesh, hotels as a 3-up where the third cell is an honest "full list coming" panel so the row is never orphaned, and Travel as a **sticky left tab rail** with the panel on the right and route rows in connected 2-up meshes. Every panel was padded to an even cell count.

**Metro fare figures were removed from both desktop and mobile** (₹60–80 in the Metro and Airport tabs, ₹30–40 for New Delhi Railway). A fare-less row beside a fare row read as unfinished. The ₹600–900 taxi estimate was deliberately kept as genuinely useful.

### Contact

Approved copy to preserve: "We'd love to hear from you", "Contact Us", "Questions about BIRC 2026? Our team is here to help", "Get in touch", "You Have Questions. We Have Answers."

Official details: 73 LGF, World Trade Center, Barakhamba Avenue, Connaught Place, New Delhi 110001. Mon–Sun 09:00–18:00 local. `booking@birc.in`, `visit@birc.in`, `+91-7303093821`.

The enquiry form routes Visiting enquiries to `visit@birc.in` and everything else to `booking@birc.in` via a prefilled mailto.

Desktop was rebuilt from scratch: the four route cards are a connected **2x2** (previously a 3-up with an orphan fourth), official details is a 3-up of bordered ink panels plus a full-width social row, and the enquiry form uses the shared gold-and-linen treatment.

Social controls use inline SVG icons for Instagram, LinkedIn, Facebook, and X. Do not revert to text initials. The official contact block begins directly with the heading and has no "Contact details" eyebrow.

### Experience

Nine approved zones in this order: The Rice Route Map, Seed Cloud, The Rice Archive, Rice Through Time, How the World Eats Rice, Hands of Rice, The World Within, Rice Mirror, Beyond the Bowl.

One direct nav link. **Never** add the nine zones as a submenu and never restore the numbered 1–9 rail. On mobile, zone visuals are full-bleed to both canvas edges with zero horizontal gutter; text keeps 22px padding above or below. Keep the immersive abstract CSS visuals. Do not invent longer zone claims.

The Experience page is treated as the site's main selling point. Concept explorations for an interactive redesign were produced on 2026-08-15 and none is committed yet; `desktop-experience.html` still carries the approved alternating zone list.

### About

About flow: hero, mission, three values (Collaboration, Innovation, Leadership), Our Story, results, organisers, Advisory Board, industry overview, industry pillars. On desktop the "Who we are" and "Our Story" headings stay at the top; only body copy is bottom-aligned with the visual.

### Conference / Knowledge Sessions

`conference.html` mobile, `desktop-conference.html` desktop. The nav label is Conference; the page title is Knowledge Sessions.

Desktop was rebuilt from scratch on 2026-08-15 as a **standalone single-stylesheet document**. Its order is fixed:

1. Full-viewport hero: breadcrumb, `BIRC 2026 programme` eyebrow, `Knowledge Sessions` title, the nine-decision lead, the delegate-pass note, `Get your BIRC 2026 pass` and `Speak at BIRC`, and a programme dossier on the right holding four fact rows plus three session plates.
2. Gold datebar: `BIRC 2026 | 23-24-25 October 2026 | Bharat Mandapam, New Delhi`.
3. All nine sessions as connected linen rows grouped under `Day 1` (4 sessions) and `Day 2` (5 sessions), each row carrying its number, topic label, full session title, a permanent 16:10 visual, and an Open control linking to its dedicated page.
4. Speakers as a connected four-column grid on raised ink, with symmetrical 3:4 portrait placeholders and a note that photography follows.
5. Closing statement `The data is public. The interpretation is not.` with the pass CTA.

Rules for this page:

- Session images are **permanent row plates**. The old hover-only floating previews and the "Hover to preview the visual" line were removed; do not reintroduce them.
- The `Agenda and Schedule`, `Workshops` and `Learning Academy` placeholder blocks were **removed from desktop at Kevin's request on 2026-08-15**. The mobile placeholder blocks were removed during the 2026-08-26 parity pass and replaced with the same nine complete session topics used on desktop.
- Speaker portraits stay symmetrical 3:4 rectangles with no staggered offsets.
- The page no longer loads `assets/knowledge-sessions.css` or `assets/knowledge-sessions.js`. Those files remain in the repository for the nine dedicated session pages.

The nine dedicated desktop session pages (`desktop-knowledge-*.html`) are unchanged and still carry the full scope, outcomes, audience and FAQ content for each topic.

## 9. Approved facts, do not change without new source content

- Dates: **23-24-25 October 2026**. Always written `23-24-25`, never `23–25` or `23-25`.
- Venue: Bharat Mandapam, Pragati Maidan, New Delhi. Halls 4 and 5. Delegate entry Gate 10.
- 30,000+ participants, 120+ countries, 250+ speakers, 300+ exhibitors, 3,000+ buyers
- ₹30,435 Cr in MoUs
- Nine Experience Zones
- Nine Knowledge Sessions, four on Day 1 and five on Day 2
- Venue infrastructure: 5 halls, 50,000+ sqm, 940+ exhibition halls metric, 30+ conference rooms, 900+ parking, 15+ food courts

## 10. Outstanding placeholders

Do not present these as verified facts and do not invent replacements:

- Speaker portraits
- About organiser logos
- About Advisory Board names, titles, portraits
- Instagram and LinkedIn URLs
- Homepage WhatsApp destination URL, currently `https://wa.me/`
- Partner logos on Partnership (placeholder marquee)
- Hotel names on Plan Visit (currently Hotel A / Hotel B)

## 11. Change checklist

Every material edit must:

1. Change the correct file, and only that file.
2. Keep navigation consistent across every page in that experience.
3. Follow `design.md`.
4. Preserve approved content.
5. Leave mobile untouched during desktop work unless explicitly asked.
6. Update `context.md` in the same change.
7. Commit to `main` and trigger publishing. Remember that CSS-only and JS-only commits do not trigger the workflow.
8. Verify the live URL, not the commit.

## 12. How to update this file

Update it whenever a page is added, renamed, moved, or deleted; a section moves between pages; navigation changes; a placeholder is replaced; design tokens change; a permanent asset or external URL is introduced; deployment changes; or the user establishes a new standing rule.

Keep it factual and scannable. **Rewrite stale sections rather than appending contradictory notes at the bottom.** The previous version of this file grew to 23KB of stacked chronology and its opening sections no longer matched the repository.

## 13. Immediate next work

1. Replace remaining logos, portraits, names, hotel names, and social URLs when supplied.
2. Keep the 13 mobile pages content-synchronized with desktop while preserving their approved layouts.
3. Decide on any future Experience page expansion only when new approved content is supplied.
4. Optional cleanup: delete the ~68 spent one-shot workflow files.
5. Optional hardening: rebuild `desktop-creators.html`, `desktop-rice-masterchef.html`, `desktop-artists.html` and the About / Exhibition / Experience set as standalone single-stylesheet documents.

## 14. New-chat instruction

> Read `context.md`, then `design.md`, then inspect the target file. Treat repository `main` as the source of truth. Author desktop pages as standalone single-stylesheet documents, never as mobile markup with CSS overrides. Do not modify mobile files during desktop work unless explicitly asked. Keep navigation synchronized, preserve approved content, update `context.md` with every structural decision, and verify the live Pages URL after publishing.
