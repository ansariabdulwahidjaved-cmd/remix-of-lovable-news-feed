import { Link } from "@tanstack/react-router";
import { Newspaper } from "lucide-react";
import { CATEGORIES } from "@/data/mockNews";

export function Footer() {
  return (
    <footer className="mt-16 border-t border-border bg-muted/40">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12 grid gap-10 md:grid-cols-4">
        <div>
          <Link to="/" className="flex items-center gap-2">
            <span className="grid h-9 w-9 place-items-center rounded-md bg-primary text-primary-foreground">
              <Newspaper className="h-5 w-5" />
            </span>
            <span className="text-xl font-bold">
              News<span className="text-primary">Hub</span>
            </span>
          </Link>
          <p className="mt-3 text-sm text-muted-foreground max-w-xs">
            Independent reporting on the stories that shape our world — every day.
          </p>
        </div>
        <div>
          <h4 className="text-sm font-semibold mb-3">Sections</h4>
          <ul className="space-y-2 text-sm text-muted-foreground">
            {CATEGORIES.slice(0, 5).map((c) => (
              <li key={c}>
                <Link
                  to="/category/$category"
                  params={{ category: c.toLowerCase() }}
                  className="hover:text-primary"
                >
                  {c}
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h4 className="text-sm font-semibold mb-3">Company</h4>
          <ul className="space-y-2 text-sm text-muted-foreground">
            <li><Link to="/about" className="hover:text-primary">About</Link></li>
            <li><Link to="/contact" className="hover:text-primary">Contact</Link></li>
            <li><Link to="/bookmarks" className="hover:text-primary">Bookmarks</Link></li>
          </ul>
        </div>
        <div>
          <h4 className="text-sm font-semibold mb-3">Follow</h4>
          <ul className="space-y-2 text-sm text-muted-foreground">
            <li>Twitter</li>
            <li>Facebook</li>
            <li>LinkedIn</li>
          </ul>
        </div>
      </div>
      <div className="border-t border-border py-4 text-center text-xs text-muted-foreground">
        © {new Date().getFullYear()} NewsHub. All rights reserved.
      </div>
    </footer>
  );
}
