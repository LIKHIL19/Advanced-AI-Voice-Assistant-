from .backtracking import backtracking_translate

def translate(text: str, dest: str = "en") -> str:
    """
    Translate text using backtracking.
    """
    result = backtracking_translate(text, dest_lang=dest)
    return result
