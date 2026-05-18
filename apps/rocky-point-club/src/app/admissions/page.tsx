import type { Metadata } from "next";
import { admissions } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Admissions",
};

export default function AdmissionsPage() {
  return (
    <>
      <PageHeader eyebrow="About" title={admissions.heading} />

      <Section>
        <p className="mx-auto max-w-2xl text-center text-lg text-ink/75">
          {admissions.homeCta}
        </p>

        <div className="mt-12 space-y-6">
          {admissions.categories.map((c) => (
            <article
              key={c.name}
              className="rounded-card border border-sand-200 bg-cream p-7 md:p-9"
            >
              <h2 className="text-2xl">{c.formTitle}</h2>

              {"criteriaLabel" in c && c.criteriaLabel && (
                <p className="mt-4 text-xs font-semibold tracking-widest text-brass-600 uppercase">
                  {c.criteriaLabel}
                </p>
              )}
              {"criteria" in c && c.criteria && (
                <ul className="mt-3 space-y-2 text-ink/80">
                  {c.criteria.map((cr) => (
                    <li key={cr} className="flex gap-3">
                      <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-500" />
                      {cr}
                    </li>
                  ))}
                </ul>
              )}

              {"statement" in c && c.statement && (
                <p className="mt-4 leading-relaxed whitespace-pre-line text-ink/80">
                  {c.statement}
                </p>
              )}

              {"bylawHeading" in c && c.bylawHeading && (
                <>
                  <h3 className="mt-6 font-display text-lg text-navy-900">
                    {c.bylawHeading}
                  </h3>
                  <p className="mt-3 text-sm leading-relaxed text-ink/70">
                    {c.bylaw}
                  </p>
                </>
              )}

              {"note" in c && c.note && (
                <p className="mt-4 text-sm text-marine-600">{c.note}</p>
              )}
            </article>
          ))}
        </div>

        <div
          id="senior-waiting-list"
          className="mt-12 scroll-mt-24 rounded-card bg-sky-50 p-8 md:p-10"
        >
          <h2 className="text-2xl">{admissions.seniorWaitingList.heading}</h2>
          <p className="mt-4 leading-relaxed text-ink/80">
            {admissions.seniorWaitingList.instructions}
          </p>
          <p className="mt-4 text-sm text-ink/55">
            {admissions.seniorWaitingList.rosterNote}
          </p>
        </div>
      </Section>
    </>
  );
}
