import type { Metadata } from "next";
import { entertainment } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Entertainment",
};

export default function EntertainmentPage() {
  return (
    <>
      <PageHeader eyebrow="Entertainment" title={entertainment.heading} />

      <Section>
        <div className="mx-auto max-w-2xl rounded-card border border-sand-200 bg-cream p-10 text-center">
          <p className="text-ink/70">
            The club&apos;s events are published on the Events Calendar.
          </p>
          <a
            href={entertainment.calendarUrl}
            target="_blank"
            rel="noreferrer"
            className="mt-6 inline-block rounded-full bg-brass-500 px-7 py-3.5 text-sm font-semibold tracking-wide text-navy-950 transition-colors hover:bg-brass-400"
          >
            {entertainment.calendarLabel}
          </a>
        </div>
      </Section>
    </>
  );
}
