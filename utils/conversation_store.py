"""
Conversation Store
==================
Manages conversation history per user (in-memory).
In production, replace with Redis for scalability.
"""

from collections import defaultdict, deque
from datetime import datetime


class ConversationStore:
    """
    Stores the last N messages per user for context awareness.
    """

    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        # { user_id: deque([ {role, content, timestamp}, ... ]) }
        self._store: dict = defaultdict(lambda: deque(maxlen=max_history))

    def add_message(self, user_id: str, role: str, content: str):
        """Add a message to the user's history."""
        self._store[user_id].append({
            "role": role,         # "user" or "assistant"
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_history(self, user_id: str) -> list:
        """Get the conversation history for a user."""
        return list(self._store[user_id])

    def clear(self, user_id: str):
        """Clear a user's conversation history."""
        if user_id in self._store:
            self._store[user_id].clear()

    def get_last_intent(self, user_id: str) -> str | None:
        """
        Returns the intent from the last assistant message (if stored).
        Useful for follow-up context.
        """
        history = self.get_history(user_id)
        for msg in reversed(history):
            if msg["role"] == "assistant" and "intent" in msg:
                return msg.get("intent")
        return None

    def add_assistant_with_intent(self, user_id: str, content: str, intent: str):
        """Add assistant message with intent metadata."""
        self._store[user_id].append({
            "role": "assistant",
            "content": content,
            "intent": intent,
            "timestamp": datetime.utcnow().isoformat()
        })
