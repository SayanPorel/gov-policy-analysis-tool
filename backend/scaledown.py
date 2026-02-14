from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def scale_down(text, ratio=0.75):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = [summarizer(chunk, max_length=int(len(chunk)*ratio), min_length=50)[0]['summary_text'] for chunk in chunks]
    return ' '.join(summaries) 
