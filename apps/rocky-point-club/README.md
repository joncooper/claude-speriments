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
│   ├── page.tsx         # Home
│   ├── about/           # History timeline + Board of Governors
│   ├── membership/      # Admissions + membership categories
│   ├── aquatics/        # Swim/dive/water polo programs
│   ├── sailing/         # Junior + adult sailing
│   ├── events/          # Social calendar
│   ├── contact/         # Address, phones, map, directions
│   └── members/         # Stage-two portal placeholder
├── components/          # Nav, Footer, Burgee, shared UI
└── content/site.ts      # ← Single source of truth for ALL copy
```

### Editing content

All site copy lives in **`src/content/site.ts`**. Board members, program details,
event lists, contact info, and membership categories are plain data — a member can
update the season's board or program schedule there without touching any components.

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

All copy was crawled from the existing rockypointclub.com (public pages, May 2026):
history, Board of Governors (2026), membership categories, aquatics and sailing
programs, the social calendar, and contact details. The members-only section
(photo directory, dues, forms, Rocky Pointer archive, tennis, video) is intentionally
deferred to stage two — see `ICEBOX.md`.

## Notes & roadmap

- `NOTES.md` — design and implementation decisions
- `ICEBOX.md` — stage two (Supabase members area) and future ideas
