export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "https://backend-r1zu.onrender.com/api";

export const ENDPOINTS = {
  allNews: `${API_BASE_URL}/news/`,
  latestNews: `${API_BASE_URL}/news/latest/`,
  trendingNews: `${API_BASE_URL}/news/trending/`,
  newsByCategory: (category: string) => `${API_BASE_URL}/news/category/${category}`,
  newsBySlug: (slug: string) => `${API_BASE_URL}/news/${slug}`,
  searchNews: (query: string) => `${API_BASE_URL}/news/search?query=${encodeURIComponent(query)}`,
  newsletter: `${API_BASE_URL}/newsletter/`,
  contact: `${API_BASE_URL}/contact/`,
  comments: `${API_BASE_URL}/comments/`,
};
