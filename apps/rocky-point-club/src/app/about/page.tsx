import type { Metadata } from "next";
import { history, board, bigelowQuote } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "About",
};

export default function AboutPage() {
  return (
    <>
      <PageHeader eyebrow="About" title={history.heading} />

      <Section>
        <figure className="mx-auto max-w-3xl text-center">
          <blockquote className="font-display text-2xl leading-relaxed text-navy-900 italic md:text-3xl">
            “{bigelowQuote.text}”
          </blockquote>
          <figcaption className="mt-6 text-sm text-ink/60">
            {history.attribution}
          </figcaption>
        </figure>

        <div className="mx-auto mt-16 max-w-2xl">
          <p className="text-xs font-semibold tracking-[0.25em] text-brass-600 uppercase">
            {history.briefHistoryLabel}
          </p>
          <div className="mt-6 space-y-6 text-lg leading-relaxed text-ink/80">
            <p>{history.paragraphs[0]}</p>
            <blockquote className="border-l-2 border-brass-400 pl-6 text-base text-ink/70 italic">
              {history.beachQuote}
            </blockquote>
            {history.paragraphs.slice(1).map((p) => (
              <p key={p.slice(0, 24)}>{p}</p>
            ))}
          </div>
        </div>
      </Section>

      <div className="bg-navy-900">
        <div className="container-rpc py-16 md:py-24">
          <h2 className="mb-12 text-3xl text-cream md:text-4xl">
            {board.heading}
          </h2>
          <div className="grid gap-12 md:grid-cols-2">
            <div>
              <h3 className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
                Officers
              </h3>
              <ul className="mt-6 divide-y divide-white/10">
                {board.officers.map((o) => (
                  <li
                    key={o.role}
                    className="flex items-baseline justify-between gap-4 py-3"
                  >
                    <span className="text-sky-100/70">{o.role}</span>
                    <span className="font-display text-lg text-cream">
                      {o.name}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h3 className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
                Committee Chairs
              </h3>
              <ul className="mt-6 divide-y divide-white/10">
                {board.chairs.map((c) => (
                  <li
                    key={c.role}
                    className="flex items-baseline justify-between gap-4 py-3"
                  >
                    <span className="text-sky-100/70">{c.role}</span>
                    <span className="font-display text-lg text-cream text-right">
                      {c.name}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
