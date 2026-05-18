import Link from "next/link";
import {
  heroQuote,
  welcome,
  highlights,
  history,
  club,
} from "@/content/site";
import { Burgee } from "@/components/Burgee";
import { Section, SectionHeading, WaveDivider } from "@/components/ui";

export default function HomePage() {
  return (
    <>
      {/* Hero — the Sound at golden hour */}
      <section className="relative overflow-hidden bg-navy-950">
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(120% 90% at 75% 15%, #2f7aa8 0%, #14466b 38%, #0a2440 68%, #061629 100%)",
          }}
        />
        {/* sun glow */}
        <div
          className="absolute -top-24 right-[12%] h-72 w-72 rounded-full opacity-40 blur-3xl"
          style={{ background: "radial-gradient(circle, #d6b471, transparent 70%)" }}
        />
        <div className="relative">
          <div className="container-rpc flex min-h-[78vh] flex-col justify-center py-24">
            <div className="flex items-center gap-3 text-brass-400">
              <Burgee className="h-10 w-10" />
              <span className="text-xs font-semibold tracking-[0.3em] uppercase">
                Est. {club.established} · Old Greenwich, CT
              </span>
            </div>
            <h1 className="mt-8 max-w-4xl text-5xl leading-[1.05] text-cream md:text-7xl">
              A family club on Long Island Sound, the way it has always been.
            </h1>
            <p className="mt-6 max-w-xl text-lg leading-relaxed text-sky-100/85">
              {welcome.body}
            </p>
            <div className="mt-10 flex flex-wrap gap-4">
              <Link
                href="/membership"
                className="rounded-full bg-brass-500 px-7 py-3.5 text-sm font-semibold tracking-wide text-navy-950 transition-colors hover:bg-brass-400"
              >
                Explore membership
              </Link>
              <Link
                href="/about"
                className="rounded-full border border-sky-100/30 px-7 py-3.5 text-sm font-semibold tracking-wide text-cream transition-colors hover:border-sky-100/70"
              >
                Our story
              </Link>
            </div>
          </div>
        </div>
        <WaveDivider className="relative text-sand-50" />
      </section>

      {/* Heritage quote */}
      <Section className="text-center">
        <figure className="mx-auto max-w-3xl">
          <div className="mx-auto mb-8 h-px w-24 bg-brass-500" />
          <blockquote className="font-display text-2xl leading-relaxed text-navy-900 italic md:text-3xl">
            “{heroQuote.text}”
          </blockquote>
          <figcaption className="mt-6 text-sm font-semibold tracking-widest text-brass-600 uppercase">
            — {heroQuote.attribution}
          </figcaption>
        </figure>
      </Section>

      {/* Highlights */}
      <div className="bg-sky-50">
        <Section>
          <SectionHeading eyebrow="A Rocky Summer" title="What the season holds">
            Three programs and a calendar of evenings by the water — the shape of
            summer at the Point.
          </SectionHeading>
          <div className="grid gap-6 md:grid-cols-3">
            {highlights.map((h) => (
              <Link
                key={h.title}
                href={h.href}
                className="group rounded-card border border-sand-200 bg-cream p-8 transition-all hover:-translate-y-1 hover:border-brass-400 hover:shadow-lg"
              >
                <Burgee className="h-8 w-8 text-marine-500 transition-colors group-hover:text-brass-500" />
                <h3 className="mt-5 text-2xl">{h.title}</h3>
                <p className="mt-3 leading-relaxed text-ink/70">{h.blurb}</p>
                <span className="mt-5 inline-block text-sm font-semibold tracking-wide text-marine-600 uppercase">
                  Learn more →
                </span>
              </Link>
            ))}
          </div>
        </Section>
      </div>

      {/* Heritage strip */}
      <Section>
        <div className="grid items-center gap-12 md:grid-cols-2">
          <div>
            <SectionHeading eyebrow="Since 1927" title="Saved, more than once, by its members">
              {history.intro}
            </SectionHeading>
            <p className="leading-relaxed text-ink/75">{history.philosophy}</p>
            <Link
              href="/about"
              className="link-underline mt-6 inline-block text-sm font-semibold tracking-wide text-marine-600 uppercase"
            >
              Read the full history →
            </Link>
          </div>
          <ul className="space-y-6 border-l-2 border-brass-400 pl-8">
            {history.timeline.slice(0, 4).map((t) => (
              <li key={t.year}>
                <p className="font-display text-2xl text-brass-600">{t.year}</p>
                <p className="mt-1 font-semibold text-navy-900">{t.title}</p>
                <p className="mt-1 text-sm leading-relaxed text-ink/70">
                  {t.body}
                </p>
              </li>
            ))}
          </ul>
        </div>
      </Section>

      {/* Membership CTA */}
      <section className="bg-navy-900">
        <div className="container-rpc py-20 text-center md:py-28">
          <Burgee className="mx-auto h-12 w-12 text-brass-500" />
          <h2 className="mx-auto mt-6 max-w-2xl text-3xl text-cream md:text-4xl">
            Interested in joining Rocky Point Club?
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-sky-100/80">
            Membership has always been small, family-oriented, and introduced
            through a sponsor. Learn how it works.
          </p>
          <Link
            href="/membership"
            className="mt-8 inline-block rounded-full bg-brass-500 px-8 py-3.5 text-sm font-semibold tracking-wide text-navy-950 transition-colors hover:bg-brass-400"
          >
            About membership
          </Link>
        </div>
      </section>
    </>
  );
}
