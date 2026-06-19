import type { Article, ContactFormData } from "./types";
import { ENDPOINTS } from "./endpoints";

async function request<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
    ...init,
  });

  if (response.status === 404) {
    return null as T;
  }

  const data = await response.json().catch(() => null);

  if (!response.ok) {
    const message =
      data && typeof data === "object" && "error" in data
        ? String(data.error)
        : `Request failed with status ${response.status}`;
    throw new Error(message);
  }

  return data as T;
}

export async function getAllNews(): Promise<Article[]> {
  return request<Article[]>(ENDPOINTS.allNews);
}

export async function getLatestNews(): Promise<Article[]> {
  return request<Article[]>(ENDPOINTS.latestNews);
}

export async function getTrendingNews(): Promise<Article[]> {
  return request<Article[]>(ENDPOINTS.trendingNews);
}

export async function getNewsByCategory(category: string): Promise<Article[]> {
  return request<Article[]>(ENDPOINTS.newsByCategory(category));
}

export async function getNewsBySlug(slug: string): Promise<Article | null> {
  return request<Article | null>(ENDPOINTS.newsBySlug(slug));
}

export async function searchNews(query: string): Promise<Article[]> {
  if (!query.trim()) return [];
  return request<Article[]>(ENDPOINTS.searchNews(query));
}

export async function submitNewsletter(email: string): Promise<{ ok: true }> {
  return request<{ ok: true }>(ENDPOINTS.newsletter, {
    method: "POST",
    body: JSON.stringify({ email }),
  });
}

export async function submitContactForm(data: ContactFormData): Promise<{ ok: true }> {
  return request<{ ok: true }>(ENDPOINTS.contact, {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function submitComment(
  articleId: string,
  comment: { author: string; content: string },
): Promise<{ ok: true }> {
  return request<{ ok: true }>(ENDPOINTS.comments, {
    method: "POST",
    body: JSON.stringify({ articleId, ...comment }),
  });
}
