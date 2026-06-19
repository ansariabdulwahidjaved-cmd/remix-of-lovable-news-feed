from django.urls import path

from . import views


urlpatterns = [
    path("news/", views.all_news, name="all-news"),
    path("news/latest/", views.latest_news, name="latest-news"),
    path("news/trending/", views.trending_news, name="trending-news"),
    path("news/search", views.search_news, name="search-news"),
    path("news/search/", views.search_news, name="search-news-slash"),
    path("news/category/<str:category>", views.news_by_category, name="news-by-category"),
    path("news/category/<str:category>/", views.news_by_category, name="news-by-category-slash"),
    path("news/<slug:slug>", views.news_by_slug, name="news-by-slug"),
    path("news/<slug:slug>/", views.news_by_slug, name="news-by-slug-slash"),
    path("newsletter/", views.newsletter, name="newsletter"),
    path("contact/", views.contact, name="contact"),
    path("comments/", views.comments, name="comments"),
]
