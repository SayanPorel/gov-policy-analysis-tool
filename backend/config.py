import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Set via environment variable
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost/policy_db') 
