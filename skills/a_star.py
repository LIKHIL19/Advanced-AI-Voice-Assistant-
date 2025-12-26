import wikipedia
from typing import List, Dict
import heapq
import re

def calculate_heuristic(content: str, goal_query: str) -> float:
    """
    heuristic function that estimates how relevant an article is to the goal query.
    Returns a lower score for more relevant articles (since we're using a min heap).
    """
    # Convert both to lowercase for case-insensitive matching
    content_lower = content.lower()
    goal_lower = goal_query.lower()
    
    # Count exact matches of goal query words
    goal_words = set(re.findall(r'\w+', goal_lower))
    matches = sum(1 for word in goal_words if word in content_lower)
    
    # Calculate word overlap ratio
    if not goal_words:
        return float('inf')
    
    # Lower score means more relevant (since we're using a min heap)
    return 1.0 / (matches + 1)  # Add 1 to avoid division by zero

def a_star_search(start_title: str, goal_query: str) -> List[str]:
    """
    A* search implementation for Wikipedia articles with heuristic.
    """
    # Initialize start node
    try:
        start_content = wikipedia.summary(start_title, sentences=1)
    except:
        return [f"Could not find article: {start_title}"]

    # Simple node structure
    start_node = {
        'title': start_title,
        'content': start_content,
        'parent': None,
        'cost': 0,
        'heuristic': calculate_heuristic(start_content, goal_query)
    }

    # Initialize open and closed sets
    open_set = [(start_node['heuristic'], start_node)]  # Priority queue with (f_score, node)
    closed_set = set()
    visited = {start_title: start_node}

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current['title'] in closed_set:
            continue

        closed_set.add(current['title'])

        # Check if current node is close enough to goal
        if goal_query.lower() in current['content'].lower():
            # Reconstruct path
            path = []
            node = current
            while node:
                path.append(node['title'])
                node = node['parent']
            return path[::-1]

        # Get related articles
        try:
            page = wikipedia.page(current['title'])
            for next_title in page.links[:5]:
                if next_title in closed_set:
                    continue

                try:
                    next_content = wikipedia.summary(next_title, sentences=1)
                    heuristic = calculate_heuristic(next_content, goal_query)
                    next_node = {
                        'title': next_title,
                        'content': next_content,
                        'parent': current,
                        'cost': current['cost'] + 1,
                        'heuristic': heuristic
                    }
                    if next_title not in visited:
                        visited[next_title] = next_node
                        f_score = next_node['cost'] + next_node['heuristic']
                        heapq.heappush(open_set, (f_score, next_node))
                except:
                    continue
        except:
            continue

    return [f"No path found to goal query: {goal_query}"] 