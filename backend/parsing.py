from openai import OpenAI
import json

client = OpenAI(api_key='your-key')  # Use config.OPENAI_API_KEY

def parse_legalese(text):
    prompt = f"Parse this legislation into JSON: {{'clauses': [], 'stakeholders': [], 'implications': []}}. Text: {text[:4000]}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)
