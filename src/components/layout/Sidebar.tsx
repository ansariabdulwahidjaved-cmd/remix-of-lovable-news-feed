import type { ReactNode } from "react";

export function Sidebar({ children, title }: { children: ReactNode; title?: string }) {
  return (
    <aside className="space-y-6">
      {title && (
        <h3 className="text-lg font-bold border-l-4 border-primary pl-3">{title}</h3>
      )}
      {children}
    </aside>
  );
}
