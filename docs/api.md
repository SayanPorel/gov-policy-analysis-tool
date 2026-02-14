 # API Reference

## Endpoints
- **POST /api/ingest**: Ingest policy. Body: `{"url": "string", "title": "string"}`.
- **GET /api/search**: Search. Query: `?q=term`.
- **POST /api/translate**: Translate. Body: `{"text": "string"}`.
- **GET /api/impact**: Impact for ID. Query: `?id=1`.
- **GET /api/metrics**: Engagement data.

## Authentication
- Use API keys in headers for secure endpoints.
