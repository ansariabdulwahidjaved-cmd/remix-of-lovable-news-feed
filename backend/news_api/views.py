import json

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods

from .models import Article, Comment, ContactMessage, NewsletterSubscriber


def article_to_dict(article):
    return {
        "id": str(article.id),
        "title": article.title,
        "slug": article.slug,
        "summary": article.summary,
        "content": article.content,
        "image": article.image,
        "category": article.category,
        "author": article.author,
        "publishedAt": article.published_at.isoformat().replace("+00:00", "Z"),
        "readTime": article.read_time,
        "views": article.views,
        "tags": article.tags,
        "isTrending": article.is_trending,
        "isFeatured": article.is_featured,
    }


def comment_to_dict(comment):
    return {
        "id": str(comment.id),
        "articleId": str(comment.article_id),
        "author": comment.author,
        "content": comment.content,
        "createdAt": comment.created_at.isoformat().replace("+00:00", "Z"),
    }


def parse_json_body(request):
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return None


def bad_request(message, errors=None):
    payload = {"ok": False, "error": message}
    if errors:
        payload["errors"] = errors
    return JsonResponse(payload, status=400)


@require_GET
def all_news(request):
    articles = Article.objects.all()
    return JsonResponse([article_to_dict(article) for article in articles], safe=False)


@require_GET
def latest_news(request):
    limit = int(request.GET.get("limit", "12"))
    articles = Article.objects.order_by("-published_at", "-id")[:limit]
    return JsonResponse([article_to_dict(article) for article in articles], safe=False)


@require_GET
def trending_news(request):
    articles = Article.objects.filter(is_trending=True).order_by("-views", "-published_at")
    return JsonResponse([article_to_dict(article) for article in articles], safe=False)


@require_GET
def news_by_category(request, category):
    articles = Article.objects.filter(category__iexact=category)
    return JsonResponse([article_to_dict(article) for article in articles], safe=False)


@require_GET
def news_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    Article.objects.filter(pk=article.pk).update(views=article.views + 1)
    article.views += 1
    return JsonResponse(article_to_dict(article))


@require_GET
def search_news(request):
    query = request.GET.get("query", "").strip()
    if not query:
        return JsonResponse([], safe=False)

    articles = Article.objects.filter(
        Q(title__icontains=query)
        | Q(summary__icontains=query)
        | Q(content__icontains=query)
        | Q(category__icontains=query)
        | Q(author__icontains=query)
        | Q(tags__icontains=query)
    )
    return JsonResponse([article_to_dict(article) for article in articles], safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def newsletter(request):
    data = parse_json_body(request)
    if data is None:
        return bad_request("Invalid JSON body.")

    email = str(data.get("email", "")).strip().lower()
    try:
        validate_email(email)
    except ValidationError:
        return bad_request("A valid email address is required.", {"email": "Invalid email."})

    subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
    return JsonResponse({"ok": True, "id": str(subscriber.id), "created": created}, status=201)


@csrf_exempt
@require_http_methods(["POST"])
def contact(request):
    data = parse_json_body(request)
    if data is None:
        return bad_request("Invalid JSON body.")

    required = ["name", "email", "subject", "message"]
    errors = {field: "This field is required." for field in required if not str(data.get(field, "")).strip()}
    try:
        validate_email(str(data.get("email", "")).strip())
    except ValidationError:
        errors["email"] = "Invalid email."

    if errors:
        return bad_request("Please fix the highlighted fields.", errors)

    message = ContactMessage.objects.create(
        name=str(data["name"]).strip(),
        email=str(data["email"]).strip().lower(),
        subject=str(data["subject"]).strip(),
        message=str(data["message"]).strip(),
    )
    return JsonResponse({"ok": True, "id": str(message.id)}, status=201)


@csrf_exempt
def comments(request):
    if request.method == "GET":
        article_id = request.GET.get("articleId")
        article_slug = request.GET.get("slug")
        qs = Comment.objects.filter(is_approved=True)
        if article_id:
            qs = qs.filter(article_id=article_id)
        if article_slug:
            qs = qs.filter(article__slug=article_slug)
        return JsonResponse([comment_to_dict(comment) for comment in qs], safe=False)

    if request.method != "POST":
        return HttpResponseNotAllowed(["GET", "POST"])

    data = parse_json_body(request)
    if data is None:
        return bad_request("Invalid JSON body.")

    article_id = str(data.get("articleId", "")).strip()
    author = str(data.get("author", "")).strip()
    content = str(data.get("content", "")).strip()
    errors = {}
    if not article_id:
        errors["articleId"] = "This field is required."
    if not author:
        errors["author"] = "This field is required."
    if not content:
        errors["content"] = "This field is required."
    if errors:
        return bad_request("Please fix the highlighted fields.", errors)

    article = get_object_or_404(Article, pk=article_id)
    comment = Comment.objects.create(article=article, author=author, content=content)
    return JsonResponse({"ok": True, "comment": comment_to_dict(comment)}, status=201)
