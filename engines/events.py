"""
Event system for Project Synapse.
Provides a thread-safe pub/sub EventBus.
"""

from collections import defaultdict
from threading import RLock
from typing import Callable, Any, Dict, List


class EventBus:
    """Thread-safe event bus."""

    def __init__(self) -> None:
        self._lock = RLock()
        self._subscribers: Dict[str, List[Callable[..., Any]]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable[..., Any]) -> None:
        with self._lock:
            self._subscribers[event].append(callback)

    def unsubscribe(self, event: str, callback: Callable[..., Any]) -> None:
        with self._lock:
            if event in self._subscribers and callback in self._subscribers[event]:
                self._subscribers[event].remove(callback)

    def emit(self, event: str, **data: Any) -> None:
        with self._lock:
            callbacks = list(self._subscribers.get(event, []))

        for cb in callbacks:
            try:
                cb(**data)
            except Exception:
                pass
