import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
from .a_star import a_star_search

def wiki_search(query: str, sentences: int = 2) -> str:
    """
    Search and summarize a Wikipedia page for the given query.
    Uses A* search to find the most relevant article.
    """
    try:
        # First try direct summary
        return wikipedia.summary(query, sentences=sentences)
    except DisambiguationError as e:
        # If multiple pages, use A* search to find the most relevant one
        path = a_star_search(e.options[0], query)
        if len(path) > 1:
            return f"Found path to relevant article: {' -> '.join(path)}\n\n" + \
                   wikipedia.summary(path[-1], sentences=sentences)
        return f"Multiple pages match '{query}'. Try being more specific."
    except PageError:
        # If no exact page, try searching
        results = wikipedia.search(query)
        if results:
            # Use A* search to find the most relevant article
            path = a_star_search(results[0], query)
            if len(path) > 1:
                return f"Found path to relevant article: {' -> '.join(path)}\n\n" + \
                       wikipedia.summary(path[-1], sentences=sentences)
            return wikipedia.summary(results[0], sentences=sentences)
        return f"No Wikipedia page found for '{query}'."
    except Exception as e:
        return f"Unexpected error: {e}"