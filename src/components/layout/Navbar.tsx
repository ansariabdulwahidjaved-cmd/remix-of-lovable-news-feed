import { Link } from "@tanstack/react-router";
import { Bookmark, Menu, Newspaper } from "lucide-react";
import { useState } from "react";
import { CATEGORIES } from "@/data/mockNews";
import { SearchBar } from "@/components/common/SearchBar";
import { MobileMenu } from "./MobileMenu";

const linkCls =
  "text-sm font-medium text-foreground/80 hover:text-primary transition-colors";

export function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 border-b border-border bg-background/95 backdrop-blur">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between gap-4">
          <Link to="/" className="flex items-center gap-2 shrink-0">
            <span className="grid h-9 w-9 place-items-center rounded-md bg-primary text-primary-foreground">
              <Newspaper className="h-5 w-5" />
            </span>
            <span className="text-xl font-bold tracking-tight">
              News<span className="text-primary">Hub</span>
            </span>
          </Link>

          <nav className="hidden lg:flex items-center gap-5">
            <Link to="/" className={linkCls} activeOptions={{ exact: true }}>
              Home
            </Link>
            {CATEGORIES.map((c) => (
              <Link
                key={c}
                to="/category/$category"
                params={{ category: c.toLowerCase() }}
                className={linkCls}
              >
                {c}
              </Link>
            ))}
          </nav>

          <div className="flex items-center gap-2">
            <div className="hidden md:block w-56">
              <SearchBar compact />
            </div>
            <Link
              to="/bookmarks"
              className="inline-flex h-9 w-9 items-center justify-center rounded-md text-foreground/80 hover:bg-secondary hover:text-primary transition-colors"
              aria-label="Bookmarks"
            >
              <Bookmark className="h-5 w-5" />
            </Link>
            <button
              onClick={() => setOpen(true)}
              className="lg:hidden inline-flex h-9 w-9 items-center justify-center rounded-md hover:bg-secondary"
              aria-label="Menu"
            >
              <Menu className="h-5 w-5" />
            </button>
          </div>
        </div>
      </div>
      <MobileMenu open={open} onClose={() => setOpen(false)} />
    </header>
  );
}
