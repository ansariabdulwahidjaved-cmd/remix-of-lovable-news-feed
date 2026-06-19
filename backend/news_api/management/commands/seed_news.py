from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime

from news_api.models import Article


LONG_CONTENT = """
<p>In a developing story that has captured global attention, experts are weighing in on the latest developments and their potential long-term implications for industries, communities, and the broader public.</p>
<p>Analysts point to a series of converging factors - economic shifts, technological acceleration, and changing public sentiment - that together create a moment of unusual complexity. "We're seeing the kind of structural change that only comes once in a generation," one observer noted.</p>
<h2>What we know so far</h2>
<p>Officials confirmed the timeline of events earlier today, releasing a detailed statement that addressed many of the questions raised over the past 48 hours. Independent verification of key claims is still ongoing, but early indications suggest the broader narrative holds up.</p>
<p>Community leaders have called for calm and patience as more facts emerge. Several organizations have already pledged resources to support affected groups, and government agencies are coordinating their response across multiple jurisdictions.</p>
<h2>What comes next</h2>
<p>The coming days will be critical. Decisions made now are likely to shape outcomes for months - perhaps years - to come. We'll continue to update this story as new information becomes available.</p>
<p>Readers can subscribe to our newsletter for daily briefings, or follow individual journalists for in-depth reporting on the angles that matter most to them.</p>
""".strip()


def image(seed):
    return f"https://picsum.photos/seed/news{seed}/1200/800"


ARTICLES = [
    {
        "title": "Global Leaders Convene for Historic Climate Summit in Geneva",
        "slug": "global-leaders-climate-summit-geneva",
        "summary": "World leaders gather to negotiate a landmark agreement on emissions, financing, and adaptation as climate impacts intensify.",
        "image": image(1),
        "category": "World",
        "author": "Sarah Mitchell",
        "published_at": "2026-06-14T09:30:00Z",
        "read_time": 6,
        "views": 24890,
        "tags": ["climate", "policy", "geneva"],
        "is_trending": True,
        "is_featured": True,
    },
    {
        "title": "Tech Giants Unveil New Generation of On-Device AI Chips",
        "slug": "tech-giants-on-device-ai-chips",
        "summary": "A new wave of silicon promises private, low-latency AI directly on phones and laptops, reshaping the cloud landscape.",
        "image": image(2),
        "category": "Technology",
        "author": "Daniel Park",
        "published_at": "2026-06-13T15:10:00Z",
        "read_time": 5,
        "views": 18230,
        "tags": ["ai", "chips", "hardware"],
        "is_trending": True,
        "is_featured": True,
    },
    {
        "title": "Central Banks Signal Coordinated Shift in Monetary Policy",
        "slug": "central-banks-monetary-policy-shift",
        "summary": "Markets react as policymakers hint at synchronized cuts amid cooling inflation and slowing global demand.",
        "image": image(3),
        "category": "Business",
        "author": "Priya Raman",
        "published_at": "2026-06-13T08:00:00Z",
        "read_time": 4,
        "views": 15402,
        "tags": ["markets", "rates", "economy"],
        "is_trending": True,
        "is_featured": False,
    },
    {
        "title": "Underdogs Stun Champions in Dramatic Cup Final Comeback",
        "slug": "underdogs-stun-champions-cup-final",
        "summary": "A 3-goal comeback in the second half delivers one of the most unexpected results in the tournament's history.",
        "image": image(4),
        "category": "Sports",
        "author": "Marco Silva",
        "published_at": "2026-06-12T22:45:00Z",
        "read_time": 3,
        "views": 33120,
        "tags": ["football", "cup", "comeback"],
        "is_trending": True,
        "is_featured": False,
    },
    {
        "title": "New Research Links Sleep Quality to Long-Term Cognitive Health",
        "slug": "sleep-quality-cognitive-health",
        "summary": "A multi-year study finds that consistent deep sleep significantly reduces cognitive decline risk in older adults.",
        "image": image(5),
        "category": "Health",
        "author": "Dr. Amelia Brooks",
        "published_at": "2026-06-12T11:20:00Z",
        "read_time": 7,
        "views": 9874,
        "tags": ["sleep", "research", "wellness"],
        "is_trending": False,
        "is_featured": True,
    },
    {
        "title": "Indie Studio's Surprise Hit Tops Streaming Charts Worldwide",
        "slug": "indie-studio-streaming-hit",
        "summary": "A small team's risk-taking series becomes a cultural phenomenon, dominating watch-time across major platforms.",
        "image": image(6),
        "category": "Entertainment",
        "author": "Lena Hoffmann",
        "published_at": "2026-06-11T19:00:00Z",
        "read_time": 4,
        "views": 21765,
        "tags": ["streaming", "tv", "indie"],
        "is_trending": True,
        "is_featured": False,
    },
    {
        "title": "Parliament Passes Sweeping Digital Privacy Reform Bill",
        "slug": "parliament-digital-privacy-reform",
        "summary": "The landmark legislation introduces strict data rights, hefty penalties, and new oversight for major platforms.",
        "image": image(7),
        "category": "Politics",
        "author": "James O'Connor",
        "published_at": "2026-06-11T10:15:00Z",
        "read_time": 6,
        "views": 12044,
        "tags": ["privacy", "law", "regulation"],
        "is_trending": False,
        "is_featured": True,
    },
    {
        "title": "Breakthrough Battery Tech Promises Week-Long EV Range",
        "slug": "breakthrough-battery-ev-range",
        "summary": "A solid-state prototype demonstrates record energy density in independent lab testing.",
        "image": image(8),
        "category": "Technology",
        "author": "Yuki Tanaka",
        "published_at": "2026-06-10T13:45:00Z",
        "read_time": 5,
        "views": 17320,
        "tags": ["ev", "battery", "innovation"],
        "is_trending": False,
        "is_featured": False,
    },
    {
        "title": "Startups Pour Into Africa's Booming Fintech Corridor",
        "slug": "startups-africa-fintech-corridor",
        "summary": "Cross-border payments, lending, and savings apps attract record venture funding across the continent.",
        "image": image(9),
        "category": "Business",
        "author": "Chinwe Adekunle",
        "published_at": "2026-06-10T07:30:00Z",
        "read_time": 5,
        "views": 8421,
        "tags": ["fintech", "africa", "vc"],
        "is_trending": False,
        "is_featured": False,
    },
    {
        "title": "Olympic Committee Confirms Bold New Host City Selection",
        "slug": "olympic-committee-host-city",
        "summary": "The decision marks a strategic pivot toward emerging markets and sustainable venue planning.",
        "image": image(10),
        "category": "Sports",
        "author": "Hannah Becker",
        "published_at": "2026-06-09T16:00:00Z",
        "read_time": 4,
        "views": 14200,
        "tags": ["olympics", "ioc"],
        "is_trending": False,
        "is_featured": False,
    },
    {
        "title": "Global Vaccine Initiative Reaches One Billion Doses Delivered",
        "slug": "vaccine-initiative-one-billion-doses",
        "summary": "A milestone for international cooperation, with the program now expanding to non-communicable diseases.",
        "image": image(11),
        "category": "Health",
        "author": "Dr. Amelia Brooks",
        "published_at": "2026-06-09T09:45:00Z",
        "read_time": 5,
        "views": 7650,
        "tags": ["vaccines", "global-health"],
        "is_trending": False,
        "is_featured": False,
    },
    {
        "title": "Award-Winning Director Announces Ambitious Sci-Fi Trilogy",
        "slug": "director-announces-scifi-trilogy",
        "summary": "Production is set to begin next spring with a cast that has already sent fans buzzing.",
        "image": image(12),
        "category": "Entertainment",
        "author": "Lena Hoffmann",
        "published_at": "2026-06-08T18:20:00Z",
        "read_time": 3,
        "views": 19880,
        "tags": ["film", "scifi"],
        "is_trending": False,
        "is_featured": False,
    },
]


class Command(BaseCommand):
    help = "Seed the database with starter news articles."

    def handle(self, *args, **options):
        created = 0
        updated = 0

        for item in ARTICLES:
            payload = {
                **item,
                "content": LONG_CONTENT,
                "published_at": parse_datetime(item["published_at"]),
            }
            _, was_created = Article.objects.update_or_create(
                slug=item["slug"],
                defaults=payload,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete: {created} created, {updated} updated."))
