import Link from "next/link";
import { club, bigelowQuote, home, homeSections } from "@/content/site";
import { Burgee } from "@/components/Burgee";
import { Section, WaveDivider } from "@/components/ui";

export default function HomePage() {
  return (
    <>
      {/* Hero — the club's name and its own founding quote */}
      <section className="relative overflow-hidden bg-navy-950">
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(120% 90% at 75% 15%, #2f7aa8 0%, #14466b 38%, #0a2440 68%, #061629 100%)",
          }}
        />
        <div
          className="absolute -top-24 right-[12%] h-72 w-72 rounded-full opacity-40 blur-3xl"
          style={{
            background: "radial-gradient(circle, #d6b471, transparent 70%)",
          }}
        />
        <div className="relative">
          <div className="container-rpc flex min-h-[72vh] flex-col justify-center py-24">
            <div className="flex items-center gap-3 text-brass-400">
              <Burgee className="h-10 w-10" />
              <span className="text-xs font-semibold tracking-[0.3em] uppercase">
                Old Greenwich, CT
              </span>
            </div>
            <h1 className="mt-8 text-5xl text-cream md:text-7xl">
              {club.name}
            </h1>
            <figure className="mt-8 max-w-2xl">
              <blockquote className="font-display text-xl leading-relaxed text-sky-100/90 italic md:text-2xl">
                “{bigelowQuote.text}”
              </blockquote>
              <figcaption className="mt-4 text-sm text-sky-100/60">
                {bigelowQuote.attribution}
              </figcaption>
            </figure>
          </div>
        </div>
        <WaveDivider className="relative text-sand-50" />
      </section>

      {/* Welcome — verbatim from the live home page */}
      <Section className="text-center">
        <div className="mx-auto max-w-2xl">
          <p className="text-xs font-semibold tracking-[0.3em] text-brass-600 uppercase">
            {home.heading}
          </p>
          <p className="mt-6 font-display text-2xl leading-relaxed text-navy-900 md:text-3xl">
            {home.bulletinLine}
          </p>
          <div className="mx-auto mt-8 h-px w-24 bg-brass-500" />
          <p className="mt-8 text-lg text-ink/75">{home.admissionsCta}</p>
          <Link
            href="/admissions"
            className="mt-6 inline-block rounded-full bg-brass-500 px-7 py-3.5 text-sm font-semibold tracking-wide text-navy-950 transition-colors hover:bg-brass-400"
          >
            Admissions
          </Link>
        </div>
      </Section>

      {/* Section navigation — the club's own section names only */}
      <div className="bg-sky-50">
        <Section>
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {homeSections.map((s) => (
              <Link
                key={s.href}
                href={s.href}
                className="group flex items-center justify-between rounded-card border border-sand-200 bg-cream p-7 transition-all hover:-translate-y-1 hover:border-brass-400 hover:shadow-lg"
              >
                <span className="font-display text-2xl text-navy-900">
                  {s.label}
                </span>
                <Burgee className="h-7 w-7 text-marine-500 transition-colors group-hover:text-brass-500" />
              </Link>
            ))}
          </div>
        </Section>
      </div>
    </>
  );
}
