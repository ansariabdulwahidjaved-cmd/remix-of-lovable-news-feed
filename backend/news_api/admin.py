from django.contrib import admin

from .models import Article, Comment, ContactMessage, NewsletterSubscriber


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "published_at", "is_trending", "is_featured")
    list_filter = ("category", "is_trending", "is_featured", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "content", "author", "tags")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article", "created_at", "is_approved")
    list_filter = ("is_approved", "created_at")
    search_fields = ("author", "content", "article__title")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "created_at", "is_resolved")
    list_filter = ("is_resolved", "created_at")
    search_fields = ("name", "email", "subject", "message")


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
