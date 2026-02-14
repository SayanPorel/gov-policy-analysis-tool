import requests
import pdfplumber

def ingest_policy(url):
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)
    with pdfplumber.open('temp.pdf') as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages)
    return text
