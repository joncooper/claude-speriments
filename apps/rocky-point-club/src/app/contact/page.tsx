import type { Metadata } from "next";
import { club } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Contact",
  description:
    "Contact Rocky Point Club — address, phone, email, and directions in Old Greenwich, CT.",
};

const directions = [
  "Take Exit 5 off I-95 (approximately 2.6 miles to the club).",
  "Turn onto U.S. Route 1 North.",
  "Continue to Sound Beach Avenue, then Shore Road.",
  "Turn onto Rocky Point Road and follow it to the end.",
  "Please observe the 15 mph speed limit on Rocky Point Road.",
];

export default function ContactPage() {
  const mapSrc = `https://www.google.com/maps?q=${encodeURIComponent(
    `${club.address.line1}, ${club.address.line2}`
  )}&output=embed`;

  return (
    <>
      <PageHeader
        eyebrow="Visit"
        title="Contact"
        intro="At the end of Rocky Point Road, where the peninsula meets Long Island Sound."
      />

      <Section>
        <div className="grid gap-12 md:grid-cols-2">
          <div>
            <h2 className="text-2xl">The Club</h2>
            <address className="mt-4 text-lg not-italic text-ink/80">
              {club.address.line1}
              <br />
              {club.address.line2}
            </address>
            <p className="mt-1 font-mono text-xs tracking-wide text-ink/50">
              {club.coords.label}
            </p>

            <dl className="mt-8 space-y-4">
              {club.phones.map((p) => (
                <div key={p.label}>
                  <dt className="text-xs font-semibold tracking-widest text-brass-600 uppercase">
                    {p.label}
                  </dt>
                  <dd className="text-lg text-ink/85">
                    <a href={`tel:${p.value.replace(/-/g, "")}`}>{p.value}</a>
                  </dd>
                </div>
              ))}
              <div>
                <dt className="text-xs font-semibold tracking-widest text-brass-600 uppercase">
                  Email
                </dt>
                <dd className="text-lg">
                  <a
                    href={`mailto:${club.email}`}
                    className="text-marine-600 link-underline"
                  >
                    {club.email}
                  </a>
                </dd>
              </div>
            </dl>

            <div className="mt-8">
              <h3 className="text-xs font-semibold tracking-widest text-brass-600 uppercase">
                Staff
              </h3>
              <ul className="mt-3 space-y-1 text-ink/80">
                {club.staff.map((s) => (
                  <li key={s.name}>
                    <span className="font-medium">{s.name}</span>
                    <span className="text-ink/55"> — {s.role}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          <div>
            <div className="overflow-hidden rounded-card border border-sand-200">
              <iframe
                title="Map to Rocky Point Club"
                src={mapSrc}
                className="h-72 w-full"
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
              />
            </div>
            <h3 className="mt-8 text-xs font-semibold tracking-widest text-brass-600 uppercase">
              Directions
            </h3>
            <ol className="mt-3 space-y-2 text-sm text-ink/75">
              {directions.map((d, i) => (
                <li key={d} className="flex gap-3">
                  <span className="font-display text-brass-600">{i + 1}.</span>
                  {d}
                </li>
              ))}
            </ol>
          </div>
        </div>
      </Section>
    </>
  );
}
