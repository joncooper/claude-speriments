import type { Metadata } from "next";
import { club, contact } from "@/content/site";
import { PageHeader, Section } from "@/components/ui";

export const metadata: Metadata = {
  title: "Contact",
};

export default function ContactPage() {
  const mapSrc = `https://www.google.com/maps?q=${encodeURIComponent(
    `${club.address.line1}, ${club.address.line2}`
  )}&output=embed`;

  return (
    <>
      <PageHeader eyebrow="Contact" title={contact.heading} />

      <Section>
        <div className="grid gap-12 md:grid-cols-2">
          <div>
            <p className="font-display text-xl text-navy-900">
              {club.legalName}
            </p>
            <address className="mt-2 text-lg not-italic text-ink/80">
              {club.address.line1}
              <br />
              {club.address.line2}
            </address>
            <p className="mt-4">
              <a
                href={`mailto:${club.email}`}
                className="text-marine-600 link-underline"
              >
                {club.email}
              </a>
            </p>

            <dl className="mt-8 space-y-3 text-ink/80">
              <div>
                <dt className="text-xs font-semibold tracking-widest text-brass-600 uppercase">
                  Gatehouse
                </dt>
                <dd className="text-lg">
                  <a href={`tel:${club.phones.gatehouse.replace(/-/g, "")}`}>
                    {club.phones.gatehouse}
                  </a>
                </dd>
              </div>
              {club.staff.map((s) => (
                <p key={s}>{s}</p>
              ))}
              <p className="text-lg">
                <a href={`tel:${club.phones.managerGrounds.replace(/-/g, "")}`}>
                  {club.phones.managerGrounds}
                </a>
              </p>
            </dl>

            <p className="mt-8 font-mono text-xs tracking-wide text-ink/50">
              {club.coordsLine}
            </p>
          </div>

          <div>
            <div className="overflow-hidden rounded-card border border-sand-200">
              <iframe
                title="Map to Rocky Point Club"
                src={mapSrc}
                className="h-64 w-full"
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
              />
            </div>

            <h2 className="mt-8 text-xs font-semibold tracking-widest text-brass-600 uppercase">
              {contact.directionsHeading}
            </h2>
            <p className="mt-3 text-sm font-medium text-ink/80">
              {contact.directionsIntro}
            </p>
            <ol className="mt-3 space-y-2 text-sm text-ink/75">
              {contact.directions.map((d, i) => (
                <li key={d} className="flex gap-3">
                  <span className="font-display text-brass-600">{i + 1}.</span>
                  {d}
                </li>
              ))}
            </ol>
            <p className="mt-4 text-sm font-semibold text-navy-900">
              {contact.speedNotice}
            </p>
          </div>
        </div>

        <div className="mt-16 rounded-card bg-sky-50 p-8">
          <h2 className="text-xs font-semibold tracking-widest text-brass-600 uppercase">
            {contact.troubleshootingHeading}
          </h2>
          <ul className="mt-4 space-y-2 text-sm text-ink/75">
            {contact.troubleshooting.map((t) => (
              <li key={t.slice(0, 24)} className="flex gap-3">
                <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-brass-500" />
                {t}
              </li>
            ))}
          </ul>
        </div>
      </Section>
    </>
  );
}
