import type { Metadata } from "next";
import Link from "next/link";
import { membership, club } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Membership",
  description:
    "Membership categories at Rocky Point Club and how the admissions process works.",
};

export default function MembershipPage() {
  return (
    <>
      <PageHeader
        eyebrow="Admissions"
        title={membership.title}
        intro={membership.intro}
      />

      <Section>
        <div className="grid gap-6 md:grid-cols-2">
          {membership.categories.map((c) => (
            <div
              key={c.name}
              className="rounded-card border border-sand-200 bg-cream p-7"
            >
              <h3 className="text-xl">{c.name}</h3>
              <p className="mt-3 leading-relaxed text-ink/75">{c.summary}</p>
            </div>
          ))}
        </div>

        <div className="mt-16 grid items-center gap-10 rounded-card bg-navy-900 p-10 text-cream md:grid-cols-[1.4fr_1fr] md:p-14">
          <div>
            <p className="mb-3 text-xs font-semibold tracking-[0.25em] text-brass-400 uppercase">
              How to join
            </p>
            <h2 className="text-3xl text-cream">
              An introduction, a sponsor, and a seconder
            </h2>
            <p className="mt-4 leading-relaxed text-sky-100/80">
              {membership.applyNote}
            </p>
          </div>
          <div className="rounded-card bg-white/5 p-7">
            <p className="text-sm font-semibold tracking-widest text-brass-400 uppercase">
              Start the conversation
            </p>
            <a
              href={`mailto:${club.email}?subject=Membership%20Inquiry`}
              className="mt-3 block font-display text-xl text-cream link-underline w-fit"
            >
              {club.email}
            </a>
            <p className="mt-4 text-sm text-sky-100/70">
              {club.phones[0].label}: {club.phones[0].value}
            </p>
            <Link
              href="/contact"
              className="mt-6 inline-block text-sm font-semibold tracking-wide text-brass-400 uppercase"
            >
              All contact details →
            </Link>
          </div>
        </div>

        <p className="mt-10 text-center text-sm text-ink/55">
          Member forms, dues &amp; fees, and applications will move into the
          secure <Link href="/members" className="text-marine-600 underline">members area</Link> in
          stage two.
        </p>
      </Section>
    </>
  );
}
