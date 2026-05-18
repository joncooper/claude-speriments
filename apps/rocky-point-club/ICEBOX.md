# Icebox

## Stage two — Members area (Supabase)

The members-only section of the current site, to be rebuilt behind auth:

- **Auth** — Supabase Auth. Member email allowlist or invite-based signup; the club
  controls who gets access.
- **Photo Directory** — searchable member directory (name, household, photo). Likely
  the highest-value feature; needs a privacy review with the board first.
- **Dues & Fees** — current schedule; later, statement/balance lookup.
- **Member Forms** — car/vehicle registration, caregiver application, photo consent,
  fleet & equipment usage agreements, billing email update. Candidates for real online
  forms writing to Supabase instead of PDFs.
- **Rocky Pointer bulletin archive** — past editions, browsable by season.
- **Tennis**, **Club video & photo album**, **member contact info**.

Suggested data model: `members`, `households`, `documents`, `bulletins`, `forms_submissions`.
Gate `/members/*` with Next.js middleware checking the Supabase session.

## Imagery

- Replace the gradient hero and card placeholders with real club photography
  (opening day, regatta, pool, sunsets). `next/image` + Squarespace CDN
  `remotePatterns` already configured. Get explicit sign-off on which photos to use.
- Consider a small, members-supplied photo gallery per season.

## Content & features

- **Live calendar / iCal** — the current site has calendar subscription pages. Offer a
  subscribable feed (Google/Apple) and per-event registration in stage two.
- **Online event registration** — replace the many per-year Squarespace registration
  forms (fireworks guests, BYO nights, regatta, swim meets) with one reusable
  data-driven form.
- **Rocky Pointer** — pull the bulletin in as MDX/CMS content so Communications can
  publish without a deploy.
- **Membership inquiry form** — structured sponsor/seconder intake instead of mailto.

## Polish

- Open Graph / social share image with the burgee.
- `sitemap.xml` + `robots.txt` via Next metadata routes.
- Light analytics (privacy-respecting) so the board can see what members use.
- Accessibility pass (focus states, reduced-motion for the smooth-scroll/hover lifts).
- Wire a custom domain and confirm redirects from old Squarespace URLs.
