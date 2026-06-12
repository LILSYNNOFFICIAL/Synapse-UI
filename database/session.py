"""Session management for Project Synapse."""

from database.state_store import StateStore


class SessionManager:
    def __init__(self) -> None:
        self.store = StateStore()

    def save(self, key: str, value) -> None:
        self.store.set(key, value)

    def load(self, key: str, default=None):
        return self.store.get(key, default)

    def clear(self) -> None:
        self.store.clear()
