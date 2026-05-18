"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { nav } from "@/content/site";
import { Burgee } from "./Burgee";

export function Nav() {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);

  const isActive = (href: string) =>
    href === "/" ? pathname === "/" : pathname.startsWith(href);

  return (
    <header className="sticky top-0 z-50 border-b border-sand-200 bg-sand-50/90 backdrop-blur">
      <nav className="container-rpc flex h-16 items-center justify-between md:h-20">
        <Link
          href="/"
          className="flex items-center gap-3 text-navy-900"
          onClick={() => setOpen(false)}
        >
          <Burgee className="h-8 w-8 text-marine-600 md:h-9 md:w-9" />
          <span className="font-display text-lg leading-none font-semibold tracking-tight md:text-xl">
            Rocky Point Club
          </span>
        </Link>

        <ul className="hidden items-center gap-8 md:flex">
          {nav.map((item) => (
            <li key={item.href}>
              <Link
                href={item.href}
                className={`link-underline text-sm font-medium tracking-wide uppercase ${
                  isActive(item.href)
                    ? "text-marine-600"
                    : "text-navy-800 hover:text-marine-600"
                }`}
              >
                {item.label}
              </Link>
            </li>
          ))}
          <li>
            <Link
              href="/members"
              className="rounded-full border border-marine-600 px-4 py-2 text-xs font-semibold tracking-widest text-marine-600 uppercase transition-colors hover:bg-marine-600 hover:text-cream"
            >
              Members
            </Link>
          </li>
        </ul>

        <button
          type="button"
          aria-label="Toggle menu"
          aria-expanded={open}
          onClick={() => setOpen((v) => !v)}
          className="flex h-10 w-10 items-center justify-center text-navy-900 md:hidden"
        >
          <span className="relative block h-4 w-6">
            <span
              className={`absolute left-0 block h-0.5 w-6 bg-current transition-transform ${
                open ? "top-1.5 rotate-45" : "top-0"
              }`}
            />
            <span
              className={`absolute top-1.5 left-0 block h-0.5 w-6 bg-current transition-opacity ${
                open ? "opacity-0" : "opacity-100"
              }`}
            />
            <span
              className={`absolute left-0 block h-0.5 w-6 bg-current transition-transform ${
                open ? "top-1.5 -rotate-45" : "top-3"
              }`}
            />
          </span>
        </button>
      </nav>

      {open && (
        <div className="border-t border-sand-200 bg-sand-50 md:hidden">
          <ul className="container-rpc flex flex-col py-2">
            {nav.map((item) => (
              <li key={item.href}>
                <Link
                  href={item.href}
                  onClick={() => setOpen(false)}
                  className={`block py-3 text-sm font-medium tracking-wide uppercase ${
                    isActive(item.href) ? "text-marine-600" : "text-navy-800"
                  }`}
                >
                  {item.label}
                </Link>
              </li>
            ))}
            <li>
              <Link
                href="/members"
                onClick={() => setOpen(false)}
                className="mt-2 mb-3 inline-block rounded-full border border-marine-600 px-4 py-2 text-xs font-semibold tracking-widest text-marine-600 uppercase"
              >
                Members
              </Link>
            </li>
          </ul>
        </div>
      )}
    </header>
  );
}
