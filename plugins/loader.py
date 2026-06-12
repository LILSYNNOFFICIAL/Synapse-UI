"""
Plugin system for Project Synapse.
Provides dynamic plugin registration and lifecycle management.
"""

from typing import Any, Dict, Callable


class PluginLoader:
    """Simple plugin loader/registry."""

    def __init__(self) -> None:
        self._plugins: Dict[str, Any] = {}

    def register(self, name: str, plugin: Any) -> None:
        """Register a plugin instance."""
        self._plugins[name] = plugin

    def load(self, name: str, *args, **kwargs) -> Any:
        """Load (initialize) a plugin if it has a 'run' method."""
        plugin = self._plugins.get(name)
        if plugin is None:
            raise KeyError(f"Plugin '{name}' not found")

        if hasattr(plugin, "run") and callable(plugin.run):
            return plugin.run(*args, **kwargs)

        return plugin

    def unload(self, name: str) -> None:
        """Unload a plugin."""
        if name in self._plugins:
            del self._plugins[name]
