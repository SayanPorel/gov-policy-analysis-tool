# Architecture

## High-Level Diagram

[Data Sources] → [Ingestion] → [Parsing (GPT-4)] → [ScaleDown] → [DB] ↓ [Frontend] ← [API] ← [Analysis Models]


## Components
- **Backend**: Flask for logic, models for DB.
- **Frontend**: React components.
- **AI Pipeline**: OpenAI for parsing, Transformers for summarization.
- **Database**: PostgreSQL with SQLAlchemy.
