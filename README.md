# Government Policy Analysis Tool

## Overview
A tool to analyze government policies with AI-driven parsing, summarization, and impact assessment.

## Setup
1. Backend: `cd backend && pip install -r requirements.txt && python app.py`
2. Frontend: `cd frontend && npm install && npm start`
3. Ingest data: POST to `/api/ingest` with a policy URL.

## Features
- Policy search and summarization.
- Impact analysis and plain language translation.
- Civic engagement tracking.

## Deployment
Use Docker: `docker build -t policy-tool . && docker run -p 5000:5000 policy-tool`
