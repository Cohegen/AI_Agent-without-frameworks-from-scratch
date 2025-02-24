def generate_response(user_input):
    """Generate a response based on user input."""
    from query_processing import clean_text, extract_keywords
    from knowledge_base import search_knowledge

    cleaned_text = clean_text(user_input)
    keywords = extract_keywords(cleaned_text)
    
    if not keywords:
        return "Can you be more specific?"
    
    info = search_knowledge(keywords)
    return info
