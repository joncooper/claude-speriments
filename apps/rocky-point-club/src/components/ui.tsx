import { ReactNode } from "react";

export function PageHeader({
  eyebrow,
  title,
  intro,
}: {
  eyebrow?: string;
  title: string;
  intro?: string;
}) {
  return (
    <section className="bg-navy-900 text-cream">
      <div className="container-rpc py-20 md:py-28">
        {eyebrow && (
          <p className="mb-3 text-xs font-semibold tracking-[0.25em] text-brass-400 uppercase">
            {eyebrow}
          </p>
        )}
        <h1 className="max-w-3xl text-4xl text-cream md:text-6xl">{title}</h1>
        {intro && (
          <p className="mt-6 max-w-2xl text-lg leading-relaxed text-sky-100/80">
            {intro}
          </p>
        )}
      </div>
      <WaveDivider className="text-sand-50" />
    </section>
  );
}

export function Section({
  children,
  className = "",
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <section className={`container-rpc py-16 md:py-24 ${className}`}>
      {children}
    </section>
  );
}

export function SectionHeading({
  eyebrow,
  title,
  children,
}: {
  eyebrow?: string;
  title: string;
  children?: ReactNode;
}) {
  return (
    <div className="mb-12 max-w-2xl">
      {eyebrow && (
        <p className="mb-3 text-xs font-semibold tracking-[0.25em] text-brass-600 uppercase">
          {eyebrow}
        </p>
      )}
      <h2 className="text-3xl md:text-4xl">{title}</h2>
      {children && (
        <p className="mt-4 text-lg leading-relaxed text-ink/75">{children}</p>
      )}
    </div>
  );
}

export function WaveDivider({ className = "" }: { className?: string }) {
  return (
    <svg
      className={`wave-divider ${className}`}
      viewBox="0 0 1440 48"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        d="M0 24c120-20 240-20 360 0s240 20 360 0 240-20 360 0 240 20 360 0v24H0z"
      />
    </svg>
  );
}
