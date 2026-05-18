import type { Metadata } from "next";
import { history, board } from "@/content/site";
import { PageHeader, Section, SectionHeading } from "@/components/ui";

export const metadata: Metadata = {
  title: "About",
  description:
    "The history of Rocky Point Club and the 2026 Board of Governors.",
};

export default function AboutPage() {
  return (
    <>
      <PageHeader eyebrow="Since 1927" title={history.title} intro={history.intro} />

      <Section>
        <ol className="relative mx-auto max-w-3xl border-l-2 border-brass-400 pl-8">
          {history.timeline.map((t) => (
            <li key={t.year} className="mb-12 last:mb-0">
              <span className="absolute -left-[9px] mt-2 h-4 w-4 rounded-full border-2 border-brass-500 bg-sand-50" />
              <p className="font-display text-3xl text-brass-600">{t.year}</p>
              <h3 className="mt-1 text-xl">{t.title}</h3>
              <p className="mt-2 leading-relaxed text-ink/75">{t.body}</p>
            </li>
          ))}
        </ol>

        <div className="mx-auto mt-16 max-w-3xl rounded-card bg-sky-50 p-8 md:p-10">
          <p className="font-display text-xl leading-relaxed text-navy-900 italic">
            {history.philosophy}
          </p>
        </div>
      </Section>

      <div className="bg-navy-900">
        <div className="container-rpc py-16 md:py-24">
          <div className="mb-12 max-w-2xl">
            <p className="mb-3 text-xs font-semibold tracking-[0.25em] text-brass-400 uppercase">
              Leadership
            </p>
            <h2 className="text-3xl text-cream md:text-4xl">
              {board.year} {board.title}
            </h2>
          </div>

          <div className="grid gap-12 md:grid-cols-2">
            <div>
              <h3 className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
                Officers
              </h3>
              <ul className="mt-6 divide-y divide-white/10">
                {board.officers.map((o) => (
                  <li
                    key={o.role}
                    className="flex items-baseline justify-between py-3"
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
