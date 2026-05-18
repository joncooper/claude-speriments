export function Burgee({ className = "h-8 w-8" }: { className?: string }) {
  // Stylized swallowtail burgee — the club's flag motif.
  return (
    <svg
      viewBox="0 0 64 64"
      className={className}
      aria-hidden="true"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <line
        x1="10"
        y1="6"
        x2="10"
        y2="58"
        stroke="currentColor"
        strokeWidth="2.5"
        strokeLinecap="round"
      />
      <path
        d="M10 9 L58 17 L44 27 L58 37 L10 45 Z"
        fill="currentColor"
      />
      <circle cx="26" cy="27" r="4.5" fill="var(--color-sand-50)" />
    </svg>
  );
}
