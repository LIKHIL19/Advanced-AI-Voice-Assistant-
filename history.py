from collections import deque
import json
import os
from datetime import datetime

class History:
    def __init__(self, max_len=50):
        self.buffer = deque(maxlen=max_len)
        self.history_file = "conversation_history.json"
        self.load_history()

    def add(self, role: str, text: str):
        """
        Add a new message to the conversation history.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = {
            "role": role,
            "text": text,
            "timestamp": timestamp
        }
        self.buffer.append(message)
        self.save_history()

    def get(self, limit: int = None):
        """
        Get the conversation history.
        If limit is specified, returns only the last 'limit' messages.
        """
        if limit is None:
            return list(self.buffer)
        return list(self.buffer)[-limit:]

    def clear(self):
        """
        Clear the conversation history.
        """
        self.buffer.clear()
        self.save_history()

    def save_history(self):
        """
        Save the conversation history to a file.
        """
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(list(self.buffer), f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        """
        Load the conversation history from a file.
        """
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                    self.buffer = deque(history, maxlen=self.buffer.maxlen)
        except Exception as e:
            print(f"Error loading history: {e}")

    def get_formatted_history(self, limit: int = None):
        """
        Get the conversation history in a formatted string.
        """
        messages = self.get(limit)
        formatted = []
        for msg in messages:
            timestamp = msg.get('timestamp', '')
            role = msg.get('role', '').capitalize()
            text = msg.get('text', '')
            formatted.append(f"[{timestamp}] {role}: {text}")
        return "\n".join(formatted)