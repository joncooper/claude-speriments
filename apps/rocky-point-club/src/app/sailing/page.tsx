import type { Metadata } from "next";
import { sailing, juniorSailing } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Sailing",
};

export default function SailingPage() {
  return (
    <>
      <PageHeader eyebrow="Sailing" title={sailing.heading} />

      <Section>
        <p className="font-display text-2xl text-navy-900">
          {sailing.welcome}
        </p>

        {/* Junior overview */}
        <div className="mt-12">
          <h2 className="text-2xl">{sailing.junior.heading}</h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-ink/80">
            {sailing.junior.intro}
          </p>
          <ul className="mt-6 space-y-3">
            {sailing.junior.requirements.map((r) => (
              <li key={r.slice(0, 24)} className="flex gap-3 text-ink/80">
                <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-500" />
                {r}
              </li>
            ))}
          </ul>
        </div>

        {/* Adult */}
        <div className="mt-12 rounded-card bg-sky-50 p-8 md:p-10">
          <h2 className="text-2xl">{sailing.adult.heading}</h2>
          <ul className="mt-6 space-y-3">
            {sailing.adult.requirements.map((r) => (
              <li key={r.slice(0, 24)} className="flex gap-3 text-ink/80">
                <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-500" />
                {r}
              </li>
            ))}
          </ul>
          <p className="mt-6 text-ink/75">{sailing.adult.closing}</p>
        </div>
      </Section>

      {/* Junior Sailing Programs — full detail, verbatim */}
      <div className="bg-navy-900">
        <div className="container-rpc py-16 md:py-24">
          <h2 className="text-3xl text-cream md:text-4xl">
            {juniorSailing.heading}
          </h2>
          <p className="mt-6 max-w-3xl leading-relaxed text-sky-100/80">
            {juniorSailing.intro}
          </p>
          <p className="mt-4 text-sm text-brass-400">
            {juniorSailing.scheduleLine}
          </p>

          <div className="mt-10 grid gap-5 md:grid-cols-2">
            {juniorSailing.levels.map((l) => (
              <div
                key={l.name}
                className="rounded-card bg-white/5 p-7 text-sky-100/85"
              >
                <h3 className="font-display text-xl text-cream">{l.name}</h3>
                <p className="mt-3 text-sm leading-relaxed">{l.body}</p>
                {"requirement" in l && l.requirement && (
                  <p className="mt-3 text-sm font-semibold text-brass-400">
                    {l.requirement}
                  </p>
                )}
                <ul className="mt-3 space-y-1 text-sm text-sky-100/70">
                  {l.times.map((t) => (
                    <li key={t}>{t}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>

          <div className="mt-10 rounded-card bg-white/5 p-7">
            <h3 className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
              {juniorSailing.firstDay.heading}
            </h3>
            <ul className="mt-4 space-y-2 text-sm text-sky-100/85">
              {juniorSailing.firstDay.items.map((i) => (
                <li key={i} className="flex gap-3">
                  <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-400" />
                  {i}
                </li>
              ))}
            </ul>
          </div>

          <div className="mt-10 grid gap-8 md:grid-cols-2">
            {juniorSailing.sections.map((s) => (
              <div key={s.heading}>
                <h3 className="font-display text-xl text-cream">
                  {s.heading}
                </h3>
                <div className="mt-3 space-y-3 text-sm leading-relaxed text-sky-100/80">
                  {s.paragraphs.map((p) => (
                    <p key={p.slice(0, 24)}>{p}</p>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <p className="mt-10 text-sm text-sky-100/70">
            Questions?{" "}
            <a
              href={`mailto:${juniorSailing.questionsEmail}`}
              className="text-brass-400 link-underline"
            >
              {juniorSailing.questionsEmail}
            </a>
          </p>
        </div>
      </div>
    </>
  );
}
