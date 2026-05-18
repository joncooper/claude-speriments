# Implementation Notes

## Why this stack

- **Next.js 15 + static prerender** — the user asked to deploy on Vercel. Next.js is
  zero-config there. Stage one has no dynamic data, so every route is statically
  generated: effectively a static site with React's authoring ergonomics, ready to
  grow server features in stage two without re-platforming.
- **Tailwind v4** — the `@theme` block in `globals.css` defines the entire nautical
  palette as design tokens. Colors/fonts/radii are named once and reused, so a future
  visual tweak is a one-file change.
- **Content as data (`src/content/site.ts`)** — a club website is edited by volunteers,
  not engineers. Keeping all copy in one typed object means updating the 2027 board or
  next season's sailing schedule never requires reading JSX.

## Design direction

The user chose **"Refined heritage"**: keep the club's nautical identity (deep navy,
marine blues, a brass burgee motif, an elegant display serif) but make it fast,
responsive, photo-forward, and dramatically more polished than the current Squarespace
site. Concretely:

- Palette: `navy-950/900` grounds, `marine` mid-tones, `brass` as the single heritage
  accent, warm `sand/cream` page background instead of stark white.
- Type: **Fraunces** (a warm, high-contrast serif) for headings; **Inter** for body.
  Both self-hosted via `next/font` — no layout shift, no Google runtime dependency.
- A custom **Burgee** SVG (swallowtail club flag) is the recurring brand mark in the
  nav, footer, hero, cards, and 404.
- Hero uses a layered CSS gradient evoking the Sound at golden hour rather than a
  hotlinked image — see "Imagery" below.

## Imagery decision

The existing site's photos live on the Squarespace CDN. Hotlinking them is fragile
(can break or be rate-limited) and re-hosting them here without an explicit go-ahead
felt presumptuous for a real organization's assets. Stage one therefore ships a
self-contained gradient/SVG aesthetic that looks finished on its own. The hero and
highlight cards are structured so real club photography drops straight in later
(`next/image` + `remotePatterns` for the Squarespace CDN is already configured in
`next.config.ts`). This is tracked in `ICEBOX.md`.

## Crawl notes

- The live site is Squarespace with a **site-wide password** ("gorocky") gating the
  members-only pages. Public pages (home, history, board, contact, aquatics, sailing,
  membership categories, events) crawl freely and were the source for all stage-one
  copy. The Squarespace lock POST could not be completed from this environment, but
  the gated content (photo directory, dues, forms, bulletin archive, tennis, video) is
  exactly the stage-two scope, so it is intentionally deferred rather than blocking.
- `sitemap.xml` enumerated ~70 pages — most are per-year event registration forms.
  Those are consolidated into a single maintainable Events page driven by data.

## Verification done

- `bun run build` — clean, 11 routes prerendered static.
- `bun run start` — all 8 nav routes return 200 with correct `<title>`/metadata.
- Confirmed real crawled content renders (Bigelow quote, 2026 board, sailing levels,
  contact email) and the Tailwind theme + self-hosted fonts compile into the CSS
  bundle. Not visually QA'd in a real browser from this environment — recommend a
  quick visual pass on the Vercel preview.
