# Rocky Point Club — Website Rebuild

A modern rebuild of the [Rocky Point Club](https://www.rockypointclub.com) website — a
family sailing and swimming club on Long Island Sound in Old Greenwich, Connecticut,
established 1927.

Built by members, for the club. **Stage one** is the public-facing site (this repo).
**Stage two** adds the secure members area (directory, dues, forms, bulletin archive)
via Supabase auth.

**Status:** Initial Spike — stage one complete and deploy-ready.

---

## Stack

| Layer        | Choice                                  |
| ------------ | --------------------------------------- |
| Framework    | Next.js 15 (App Router, static export)  |
| Language     | TypeScript                              |
| Styling      | Tailwind CSS v4 (custom nautical theme) |
| Fonts        | Fraunces (display) + Inter (body), self-hosted via `next/font` |
| Hosting      | Vercel (zero-config)                    |
| Stage two    | Supabase (auth + member directory)      |

Every page is statically prerendered — no server, no database, fast and cheap to host.

## Project layout

```
src/
├── app/                 # Routes (App Router)
│   ├── page.tsx         # Home (Welcome + Bigelow quote + admissions CTA)
│   ├── about/           # About Rocky Point (history) + Board of Governors
│   ├── admissions/      # Membership criteria, bylaw, senior waiting list
│   ├── aquatics/        # Aquatics Programs Overview
│   ├── sailing/         # Sailing Information + Junior Sailing Programs
│   ├── entertainment/   # Entertainment & Event Information (calendar link)
│   ├── contact/         # Contact Us — address, phones, directions
│   └── members/         # Members Only — stage-two placeholder
├── components/          # Nav, Footer, Burgee, shared UI
└── content/site.ts      # ← Single source of truth for ALL copy
```

### Editing content

All site copy lives in **`src/content/site.ts`** as plain data, so a member can
update the season's board or a program schedule without touching components.

**The copy is the club's own words, verbatim** from the live site. This rebuild
modernizes the look and structure only — it does not rewrite the language.
When updating, match the live site's wording exactly; any rewording is a
decision for club members, not this codebase. See `NOTES.md` ("Content
principle").

## Develop

```bash
cd apps/rocky-point-club
bun install
bun run dev          # http://localhost:3000
```

Build / preview production:

```bash
bun run build
bun run start
```

## Deploy to Vercel

1. Import the `claude-speriments` repo in Vercel.
2. Set **Root Directory** to `apps/rocky-point-club`.
3. Framework preset auto-detects as **Next.js**. No env vars needed for stage one.
4. Deploy. Point the `rockypointclub.com` domain at the Vercel project when ready.

## Content source

All copy is reproduced **verbatim** from the existing rockypointclub.com public
pages (crawled May 2026): About Rocky Point (history), the 2026 Board of
Governors, the admissions/membership criteria and bylaw text, the aquatics and
sailing programs, and the contact details. The password-protected members-only
section (photo directory, dues, forms, Rocky Pointer archive, tennis, video) is
deferred to stage two — see `ICEBOX.md`. The Senior Waiting List's personal
roster is intentionally not committed to this repo (see `NOTES.md`).

## Notes & roadmap

- `NOTES.md` — design and implementation decisions
- `ICEBOX.md` — stage two (Supabase members area) and future ideas
