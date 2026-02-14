# Installation and Setup

## Prerequisites
- Python 3.8+.
- Node.js 16+.
- Git.
- PostgreSQL.
- API keys: OpenAI, optional data sources.

## Steps
1. Clone: `git clone https://github.com/YOUR_USERNAME/gov-policy-analysis-tool.git`
2. Backend:
   - `cd backend`
   - `pip install -r requirements.txt`
   - Set `.env` with keys.
   - `python app.py`
3. Frontend:
   - `cd frontend`
   - `npm install`
   - `npm start`
4. Database: Create DB and run `db.create_all()`.

## Deployment
- Use Docker: `docker build -t policy-tool .`
- Host on Heroku/Vercel. 
