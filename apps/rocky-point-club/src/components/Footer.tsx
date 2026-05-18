import Link from "next/link";
import { club, nav } from "@/content/site";
import { Burgee } from "./Burgee";

export function Footer() {
  return (
    <footer className="mt-24 bg-navy-950 text-sky-100">
      <div className="container-rpc grid gap-12 py-16 md:grid-cols-3">
        <div>
          <div className="flex items-center gap-3 text-cream">
            <Burgee className="h-9 w-9 text-brass-500" />
            <span className="font-display text-xl font-semibold">
              {club.name}
            </span>
          </div>
          <p className="mt-4 text-sm text-sky-100/70">{club.legalName}</p>
          <p className="mt-4 font-mono text-xs tracking-wide text-sky-100/50">
            {club.coordsLine}
          </p>
        </div>

        <div>
          <h2 className="text-xs font-semibold tracking-widest text-brass-400 uppercase">
            Explore
          </h2>
          <ul className="mt-4 space-y-2 text-sm">
            {nav.map((item) => (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className="text-sky-100/80 transition-colors hover:text-cream"
                >
                  {item.label}
                </Link>
              </li>
            ))}
            <li>
              <Link
                href="/members"
                className="text-sky-100/80 transition-colors hover:text-cream"
              >
                Members Only
              </Link>
            </li>
          </ul>
        </div>

        <div>
          <h2 className="text-xs font-semibold tracking-widest text-brass-400 uppercase">
            Visit
          </h2>
          <address className="mt-4 space-y-1 text-sm not-italic text-sky-100/80">
            <p>{club.address.line1}</p>
            <p>{club.address.line2}</p>
          </address>
          <ul className="mt-4 space-y-1 text-sm text-sky-100/80">
            <li>
              <span className="text-sky-100/50">Gatehouse</span>{" "}
              {club.phones.gatehouse}
            </li>
            <li>
              <a
                href={`mailto:${club.email}`}
                className="transition-colors hover:text-cream"
              >
                {club.email}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div className="border-t border-white/10">
        <div className="container-rpc flex flex-col items-center justify-between gap-2 py-6 text-xs text-sky-100/50 md:flex-row">
          <p>
            © {new Date().getFullYear()} {club.legalName}
          </p>
          <p>Old Greenwich, Connecticut</p>
        </div>
      </div>
    </footer>
  );
}
