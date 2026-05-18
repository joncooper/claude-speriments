import type { Metadata } from "next";
import { events } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Events",
  description:
    "The Rocky Point Club summer social calendar — cocktails, fireworks, BYO nights, the regatta, and more.",
};

export default function EventsPage() {
  return (
    <>
      <PageHeader
        eyebrow="The Social Season"
        title={events.title}
        intro={events.intro}
      />

      <Section>
        <div className="grid gap-px overflow-hidden rounded-card border border-sand-200 bg-sand-200 md:grid-cols-2">
          {events.recurring.map((e) => (
            <div key={e.name} className="bg-cream p-7">
              <div className="flex items-baseline justify-between gap-4">
                <h3 className="text-xl">{e.name}</h3>
                <span className="shrink-0 text-xs font-semibold tracking-widest text-brass-600 uppercase">
                  {e.when}
                </span>
              </div>
              <p className="mt-2 text-sm leading-relaxed text-ink/70">
                {e.body}
              </p>
            </div>
          ))}
        </div>

        <p className="mt-10 text-center text-sm text-ink/55">
          Dates, registration, and the live calendar are published in the Rocky
          Pointer bulletin each season.
        </p>
      </Section>
    </>
  );
}
