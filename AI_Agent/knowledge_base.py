knowledge = {
    "ai": "Artificial Intelligence is a field of computer science focused on building intelligent machines.",
    "machine learning": "Machine learning is a subset of AI that enables systems to learn patterns from data.",
    "python": "Python is a powerful programming language commonly used in AI development."
}

def search_knowledge(keywords):
    """Retrieve information from the knowledge base based on keywords."""
    for key in knowledge:
        if any(keyword in key for keyword in keywords):
            return knowledge[key]
    return "I don't have information on that."
