from typing import List, Tuple
import random

def alpha_beta_search(state: List[int], depth: int, alpha: float, beta: float, is_maximizing: bool) -> Tuple[int, int]:
    """
    Simple Alpha-Beta pruning implementation.
    Used for optimized decision making in the voice assistant.
    """
    if depth == 0 or not state:
        return 0, sum(state)

    if is_maximizing:
        best_score = float('-inf')
        best_move = 0
        for i in range(len(state)):
            if state[i] > 0:
                state[i] -= 1
                score, _ = alpha_beta_search(state, depth - 1, alpha, beta, False)
                state[i] += 1
                if score > best_score:
                    best_score = score
                    best_move = i
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = 0
        for i in range(len(state)):
            if state[i] > 0:
                state[i] -= 1
                score, _ = alpha_beta_search(state, depth - 1, alpha, beta, True)
                state[i] += 1
                if score < best_score:
                    best_score = score
                    best_move = i
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score, best_move

def make_decision(options: List[str]) -> str:
    """
    Make a decision using Alpha-Beta pruning.
    """
    # Convert options to numerical state
    state = [len(opt) for opt in options]
    _, best_move = alpha_beta_search(state, 3, float('-inf'), float('inf'), True)
    return options[best_move] 