import type { Metadata } from "next";
import Link from "next/link";
import { members, club } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Members",
  description:
    "The Rocky Point Club members area — coming in stage two with secure login.",
};

export default function MembersPage() {
  return (
    <>
      <PageHeader
        eyebrow="Members Only"
        title={members.title}
        intro={members.intro}
      />

      <Section>
        <div className="mx-auto max-w-2xl rounded-card border border-sand-200 bg-cream p-8 text-center md:p-12">
          <p className="inline-flex items-center gap-2 rounded-full bg-brass-500/15 px-4 py-1.5 text-xs font-semibold tracking-widest text-brass-600 uppercase">
            Coming in stage two
          </p>
          <p className="mt-6 leading-relaxed text-ink/75">
            {members.stageTwoNote}
          </p>

          <div className="mt-8 grid gap-2 text-left sm:grid-cols-2">
            {members.plannedSections.map((s) => (
              <div
                key={s}
                className="flex items-center gap-3 rounded-md bg-sky-50 px-4 py-3 text-sm text-ink/70"
              >
                <span className="h-1.5 w-1.5 rounded-full bg-marine-500" />
                {s}
              </div>
            ))}
          </div>

          <p className="mt-8 text-sm text-ink/60">
            Need a form or document now?{" "}
            <a
              href={`mailto:${club.email}`}
              className="text-marine-600 link-underline"
            >
              {club.email}
            </a>
          </p>
          <Link
            href="/"
            className="mt-8 inline-block text-sm font-semibold tracking-wide text-marine-600 uppercase"
          >
            ← Back home
          </Link>
        </div>
      </Section>
    </>
  );
}
