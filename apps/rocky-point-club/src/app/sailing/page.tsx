import type { Metadata } from "next";
import { sailing } from "@/content/site";
import { PageHeader, Section, SectionHeading } from "@/components/ui";

export const metadata: Metadata = {
  title: "Sailing",
  description:
    "Junior and adult sailing at Rocky Point Club — Optis, Fevas, Lasers, and Ideal 18s on Long Island Sound.",
};

export default function SailingPage() {
  return (
    <>
      <PageHeader
        eyebrow="The Heart of Rocky"
        title={sailing.title}
        intro={sailing.intro}
      />

      {/* Junior */}
      <Section>
        <SectionHeading eyebrow="Ages 6–17" title={sailing.junior.title}>
          {sailing.junior.body}
        </SectionHeading>

        <div className="grid gap-5 md:grid-cols-2">
          {sailing.junior.levels.map((l) => (
            <div
              key={l.name}
              className="rounded-card border border-sand-200 bg-cream p-7"
            >
              <div className="flex items-baseline justify-between">
                <h3 className="text-xl">{l.name}</h3>
                <span className="rounded-full bg-marine-600/10 px-3 py-1 text-xs font-semibold tracking-wide text-marine-700">
                  Ages {l.ages}
                </span>
              </div>
              <p className="mt-3 text-sm leading-relaxed text-ink/75">
                {l.detail}
              </p>
            </div>
          ))}
        </div>

        <div className="mt-10 grid gap-8 rounded-card bg-sky-50 p-8 md:grid-cols-2 md:p-10">
          <div>
            <h4 className="text-sm font-semibold tracking-widest text-brass-600 uppercase">
              Requirements
            </h4>
            <ul className="mt-4 space-y-2 text-sm text-ink/75">
              {sailing.junior.requirements.map((r) => (
                <li key={r} className="flex gap-2">
                  <span className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-500" />
                  {r}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-semibold tracking-widest text-brass-600 uppercase">
              Costs
            </h4>
            <p className="mt-4 text-sm leading-relaxed text-ink/75">
              {sailing.junior.costNote}
            </p>
            <a
              href={`mailto:${sailing.junior.contact}`}
              className="mt-4 inline-block text-sm font-semibold text-marine-600 link-underline w-fit"
            >
              {sailing.junior.contact}
            </a>
          </div>
        </div>
      </Section>

      {/* Adult */}
      <div className="bg-navy-900">
        <div className="container-rpc py-16 md:py-24">
          <div className="mb-8 max-w-2xl">
            <p className="mb-3 text-xs font-semibold tracking-[0.25em] text-brass-400 uppercase">
              For Members
            </p>
            <h2 className="text-3xl text-cream md:text-4xl">
              {sailing.adult.title}
            </h2>
            <p className="mt-4 leading-relaxed text-sky-100/80">
              {sailing.adult.body}
            </p>
          </div>
          <div className="grid gap-8 md:grid-cols-2">
            <div className="rounded-card bg-white/5 p-7">
              <h4 className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
                Requirements
              </h4>
              <ul className="mt-4 space-y-2 text-sm text-sky-100/80">
                {sailing.adult.requirements.map((r) => (
                  <li key={r} className="flex gap-2">
                    <span className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-400" />
                    {r}
                  </li>
                ))}
              </ul>
            </div>
            <div className="rounded-card bg-white/5 p-7">
              <h4 className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
                Contact
              </h4>
              <a
                href={`mailto:${sailing.adult.contact}`}
                className="mt-4 inline-block font-display text-lg text-cream link-underline w-fit"
              >
                {sailing.adult.contact}
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
