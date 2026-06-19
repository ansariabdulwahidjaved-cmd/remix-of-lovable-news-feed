# Django Backend

This backend provides the API used by the news frontend.

## Setup

```powershell
cd backend
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_news
python manage.py runserver 8000
```

The frontend defaults to `http://localhost:8000/api`. You can override that with `VITE_API_BASE_URL`.

## Endpoints

- `GET /api/news/`
- `GET /api/news/latest/`
- `GET /api/news/trending/`
- `GET /api/news/category/<category>`
- `GET /api/news/<slug>`
- `GET /api/news/search?query=<term>`
- `POST /api/newsletter/` with `{ "email": "reader@example.com" }`
- `POST /api/contact/` with `{ "name", "email", "subject", "message" }`
- `GET /api/comments/?articleId=<id>`
- `POST /api/comments/` with `{ "articleId", "author", "content" }`
