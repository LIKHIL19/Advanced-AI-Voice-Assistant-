import google.generativeai as genai

class AIAgent:
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def ask(self, prompt: str, context: list[dict] | None = None) -> str:
        """
        Send a prompt (with optional context) to the AI model and return the response text.
        """
        # You can build messages list from context if needed
        response = self.model.generate_content([prompt])
        return response.text if response else "No response received."