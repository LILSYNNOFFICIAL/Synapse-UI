"""State store for Project Synapse."""

from typing import Any, Dict


class StateStore:
    """Simple key/value state storage."""

    def __init__(self) -> None:
        self._state: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._state[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._state.get(key, default)

    def remove(self, key: str) -> None:
        self._state.pop(key, None)

    def clear(self) -> None:
        self._state.clear()
