import type { Metadata } from "next";
import { aquatics } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Aquatics",
  description:
    "Swim team, dive team, lessons, pre-team, and water polo at Rocky Point Club.",
};

export default function AquaticsPage() {
  return (
    <>
      <PageHeader
        eyebrow="By the Water"
        title={aquatics.title}
        intro={aquatics.intro}
      />

      <Section>
        <div className="mb-12 inline-flex items-center gap-3 rounded-full bg-brass-500/15 px-5 py-2 text-sm font-semibold text-brass-600">
          <span className="h-2 w-2 rounded-full bg-brass-500" />
          {aquatics.registrationNote}
        </div>

        <div className="space-y-6">
          {aquatics.programs.map((p) => (
            <article
              key={p.name}
              className="rounded-card border border-sand-200 bg-cream p-7 md:p-9"
            >
              <div className="flex flex-wrap items-baseline justify-between gap-3">
                <h3 className="text-2xl">{p.name}</h3>
                <span className="text-sm font-medium tracking-wide text-marine-600">
                  {p.schedule}
                </span>
              </div>
              <p className="mt-1 text-sm font-semibold tracking-wide text-brass-600 uppercase">
                {p.ages}
              </p>
              <p className="mt-4 leading-relaxed text-ink/75">{p.body}</p>
            </article>
          ))}
        </div>
      </Section>
    </>
  );
}
