import Link from "next/link";
import { Burgee } from "@/components/Burgee";

export default function NotFound() {
  return (
    <div className="container-rpc flex min-h-[60vh] flex-col items-center justify-center text-center">
      <Burgee className="h-12 w-12 text-marine-500" />
      <h1 className="mt-6 text-4xl">Off the chart</h1>
      <p className="mt-3 max-w-md text-ink/70">
        That page has drifted out of these waters. Let&apos;s get you back to
        the Point.
      </p>
      <Link
        href="/"
        className="mt-8 rounded-full bg-marine-600 px-6 py-3 text-sm font-semibold tracking-wide text-cream transition-colors hover:bg-marine-700"
      >
        Return home
      </Link>
    </div>
  );
}
