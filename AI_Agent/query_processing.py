import re

def clean_text(text):
    """Basic text cleaning: remove special characters and extra spaces."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()

def extract_keywords(text):
    """Extract meaningful words from the query."""
    words = text.split()
    common_words = {"is", "the", "what", "how", "a", "an", "of", "for"}
    keywords = [word for word in words if word not in common_words]
    return keywords
