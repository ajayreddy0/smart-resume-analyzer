import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[\r\n]', ' ', text)
    return text.strip()
