import type { Metadata } from "next";
import { aquatics } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Aquatics",
};

export default function AquaticsPage() {
  return (
    <>
      <PageHeader eyebrow="Aquatics" title={aquatics.heading} />

      <Section>
        <div className="mb-12 inline-flex items-center gap-3 rounded-full bg-brass-500/15 px-5 py-2 text-sm font-semibold text-brass-600">
          <span className="h-2 w-2 rounded-full bg-brass-500" />
          {aquatics.registrationLine}
        </div>

        <div className="space-y-6">
          {aquatics.programs.map((p) => (
            <article
              key={p.name}
              className="rounded-card border border-sand-200 bg-cream p-7 md:p-9"
            >
              <h2 className="text-2xl">{p.name}</h2>
              <div className="mt-4 space-y-4 leading-relaxed text-ink/80">
                {p.paragraphs.map((para) => (
                  <p key={para.slice(0, 24)}>{para}</p>
                ))}
              </div>
              {"ages" in p && p.ages && (
                <ul className="mt-5 space-y-1 border-l-2 border-brass-400 pl-5 text-sm text-ink/75">
                  {p.ages.map((a) => (
                    <li key={a}>{a}</li>
                  ))}
                </ul>
              )}
            </article>
          ))}
        </div>
      </Section>
    </>
  );
}
