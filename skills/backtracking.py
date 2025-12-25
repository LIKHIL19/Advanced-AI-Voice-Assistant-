from googletrans import Translator
from typing import List

def backtracking_translate(text: str, dest_lang: str = "en") -> str:
    """
    Simple backtracking implementation for translations.
    """
    translator = Translator()
    max_attempts = 2

    # Try different translation approaches
    for attempt in range(max_attempts):
        try:
            # First attempt: direct translation
            if attempt == 0:
                result = translator.translate(text, dest=dest_lang)
                return result.text
            
            # Second attempt: translate with English as source
            else:
                result = translator.translate(text, dest=dest_lang, src="en")
                return result.text
                
        except Exception as e:
            if attempt == max_attempts - 1:
                return f"[Translation Error: {str(e)}]"
            continue

    return f"[Translation Error: Could not translate to {dest_lang}]" 