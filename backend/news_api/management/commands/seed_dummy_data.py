from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from news_api.models import Article, Comment, ContactMessage, NewsletterSubscriber


CONTENT = """
<p>This is a sample article body for development and UI testing. It includes enough paragraph text to make article pages feel realistic while the editorial workflow is still being built.</p>
<p>The story gives designers and developers useful data for cards, search results, category pages, and detail views. Replace this copy with real reporting when the production CMS is ready.</p>
<h2>Background</h2>
<p>Teams often need stable demo content while backend features, moderation tools, and publishing flows are still moving. This seeded content keeps the site usable during that stage.</p>
<h2>Next steps</h2>
<p>Editors can use the Django admin to revise headlines, categories, images, tags, and article metadata as the project matures.</p>
""".strip()


ARTICLES = [
    {
        "title": "City Transit Agency Launches All-Electric Bus Fleet",
        "slug": "city-transit-electric-bus-fleet",
        "summary": "The first phase adds 120 electric buses across high-traffic routes, cutting fuel costs and local emissions.",
        "image": "https://picsum.photos/seed/dummy-transit/1200/800",
        "category": "World",
        "author": "Nora Ellis",
        "published_at": "2026-06-15T07:45:00Z",
        "read_time": 4,
        "views": 8920,
        "tags": ["transit", "climate", "cities"],
        "is_trending": True,
        "is_featured": False,
    },
    {
        "title": "Local Schools Adopt AI Tutoring Pilot for Math Classes",
        "slug": "schools-ai-tutoring-math-pilot",
        "summary": "Teachers will use adaptive tutoring tools to identify gaps while keeping lesson planning and grading under human control.",
        "image": "https://picsum.photos/seed/dummy-school-ai/1200/800",
        "category": "Technology",
        "author": "Omar Siddiqui",
        "published_at": "2026-06-15T06:20:00Z",
        "read_time": 5,
        "views": 11340,
        "tags": ["education", "ai", "schools"],
        "is_trending": True,
        "is_featured": True,
    },
    {
        "title": "Small Businesses Report Strong Summer Hiring Demand",
        "slug": "small-businesses-summer-hiring-demand",
        "summary": "Hospitality, logistics, and retail owners say seasonal hiring is stronger than expected despite higher operating costs.",
        "image": "https://picsum.photos/seed/dummy-hiring/1200/800",
        "category": "Business",
        "author": "Mina Patel",
        "published_at": "2026-06-14T18:05:00Z",
        "read_time": 3,
        "views": 6475,
        "tags": ["jobs", "small-business", "economy"],
        "is_trending": False,
        "is_featured": False,
    },
    {
        "title": "National Team Announces Squad for Continental Championship",
        "slug": "national-team-continental-championship-squad",
        "summary": "A mix of veteran leadership and first-time callups headlines the final roster before the opening match.",
        "image": "https://picsum.photos/seed/dummy-sports-squad/1200/800",
        "category": "Sports",
        "author": "Leo Grant",
        "published_at": "2026-06-14T15:35:00Z",
        "read_time": 4,
        "views": 17680,
        "tags": ["football", "national-team", "championship"],
        "is_trending": True,
        "is_featured": False,
    },
    {
        "title": "Streaming Platform Orders Documentary Series on Deep Sea Research",
        "slug": "streaming-documentary-deep-sea-research",
        "summary": "The six-part series follows scientists mapping unexplored ocean habitats with new robotic vessels.",
        "image": "https://picsum.photos/seed/dummy-deep-sea/1200/800",
        "category": "Entertainment",
        "author": "Iris Cole",
        "published_at": "2026-06-13T21:10:00Z",
        "read_time": 4,
        "views": 7325,
        "tags": ["streaming", "documentary", "science"],
        "is_trending": False,
        "is_featured": True,
    },
    {
        "title": "Hospitals Expand Weekend Clinics to Reduce Wait Times",
        "slug": "hospitals-weekend-clinics-wait-times",
        "summary": "The expanded schedule targets routine diagnostics and follow-up visits that often crowd weekday calendars.",
        "image": "https://picsum.photos/seed/dummy-clinic/1200/800",
        "category": "Health",
        "author": "Dr. Theo Morgan",
        "published_at": "2026-06-13T09:25:00Z",
        "read_time": 5,
        "views": 5840,
        "tags": ["healthcare", "clinics", "access"],
        "is_trending": False,
        "is_featured": False,
    },
    {
        "title": "Election Commission Publishes Updated Voting Guidelines",
        "slug": "election-commission-updated-voting-guidelines",
        "summary": "The new guidance clarifies registration deadlines, mail-in ballot rules, and accessibility requirements.",
        "image": "https://picsum.photos/seed/dummy-voting/1200/800",
        "category": "Politics",
        "author": "Grace Kim",
        "published_at": "2026-06-12T14:50:00Z",
        "read_time": 6,
        "views": 10110,
        "tags": ["elections", "voting", "policy"],
        "is_trending": False,
        "is_featured": True,
    },
    {
        "title": "Researchers Demo Wearable Sensor for Early Heat Stress Alerts",
        "slug": "wearable-sensor-heat-stress-alerts",
        "summary": "The lightweight device monitors hydration and body temperature for workers in extreme conditions.",
        "image": "https://picsum.photos/seed/dummy-wearable/1200/800",
        "category": "Technology",
        "author": "Yara Nascimento",
        "published_at": "2026-06-12T08:40:00Z",
        "read_time": 5,
        "views": 9380,
        "tags": ["wearables", "safety", "sensors"],
        "is_trending": True,
        "is_featured": False,
    },
]


class Command(BaseCommand):
    help = "Add extra dummy articles, comments, subscribers, and contact messages."

    def handle(self, *args, **options):
        articles = []
        created_articles = 0
        updated_articles = 0

        for item in ARTICLES:
            article, created = Article.objects.update_or_create(
                slug=item["slug"],
                defaults={**item, "content": CONTENT, "published_at": parse_datetime(item["published_at"])},
            )
            articles.append(article)
            created_articles += int(created)
            updated_articles += int(not created)

        subscribers = ["alex.reader@example.com", "maya.news@example.com", "sam.daily@example.com"]
        for email in subscribers:
            NewsletterSubscriber.objects.get_or_create(email=email)

        ContactMessage.objects.get_or_create(
            email="partnerships@example.com",
            subject="Partnership inquiry",
            defaults={
                "name": "Avery Stone",
                "message": "We would like to discuss a potential local reporting partnership.",
                "is_resolved": False,
            },
        )
        ContactMessage.objects.get_or_create(
            email="feedback@example.com",
            subject="Reader feedback",
            defaults={
                "name": "Jordan Lee",
                "message": "The category pages are helpful. Please add more local business coverage.",
                "is_resolved": False,
            },
        )

        comments = [
            ("Alex Rivera", "This sample story is useful for testing the article detail layout."),
            ("Maya Chen", "The related cards and search results have enough variety now."),
            ("Sam Carter", "Please keep a few trending and featured stories in the seed set."),
        ]
        for article in articles[:4]:
            for author, content in comments:
                Comment.objects.get_or_create(
                    article=article,
                    author=author,
                    content=content,
                    defaults={"created_at": timezone.now()},
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Dummy data ready: "
                f"{created_articles} articles created, {updated_articles} articles updated, "
                f"{len(subscribers)} subscribers ensured, 2 contact messages ensured."
            )
        )
