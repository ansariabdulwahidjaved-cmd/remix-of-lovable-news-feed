import { Link } from "@tanstack/react-router";
import { X } from "lucide-react";
import { CATEGORIES } from "@/data/mockNews";
import { SearchBar } from "@/components/common/SearchBar";

interface MobileMenuProps {
  open: boolean;
  onClose: () => void;
}

export function MobileMenu({ open, onClose }: MobileMenuProps) {
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 lg:hidden">
      <div className="absolute inset-0 bg-black/50" onClick={onClose} />
      <aside className="absolute right-0 top-0 h-full w-80 max-w-[85vw] bg-background shadow-card-hover">
        <div className="flex items-center justify-between border-b border-border px-4 h-16">
          <span className="font-bold">Menu</span>
          <button
            onClick={onClose}
            className="inline-flex h-9 w-9 items-center justify-center rounded-md hover:bg-secondary"
            aria-label="Close"
          >
            <X className="h-5 w-5" />
          </button>
        </div>
        <div className="p-4 space-y-4">
          <SearchBar compact />
          <nav className="flex flex-col">
            <Link
              to="/"
              onClick={onClose}
              className="py-2.5 text-sm font-medium hover:text-primary"
            >
              Home
            </Link>
            {CATEGORIES.map((c) => (
              <Link
                key={c}
                to="/category/$category"
                params={{ category: c.toLowerCase() }}
                onClick={onClose}
                className="py-2.5 text-sm font-medium hover:text-primary"
              >
                {c}
              </Link>
            ))}
            <Link
              to="/bookmarks"
              onClick={onClose}
              className="py-2.5 text-sm font-medium hover:text-primary"
            >
              Bookmarks
            </Link>
            <Link
              to="/about"
              onClick={onClose}
              className="py-2.5 text-sm font-medium hover:text-primary"
            >
              About
            </Link>
            <Link
              to="/contact"
              onClick={onClose}
              className="py-2.5 text-sm font-medium hover:text-primary"
            >
              Contact
            </Link>
          </nav>
        </div>
      </aside>
    </div>
  );
}
