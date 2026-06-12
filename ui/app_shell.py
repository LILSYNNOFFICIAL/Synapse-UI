"""
Application shell for Project Synapse.
Coordinates EventBus, PluginLoader, and ThemeEngine lifecycle.
"""

from engines.events import EventBus
from plugins.loader import PluginLoader
from themes.engine import ThemeEngine


class AppShell:
    """Main application shell orchestrating system components."""

    def __init__(self) -> None:
        self.events = EventBus()
        self.plugins = PluginLoader()
        self.themes = ThemeEngine()
        self.running = False

    def start(self) -> None:
        """Start the application shell."""
        self.running = True
        self.events.emit("app:start")

    def stop(self) -> None:
        """Stop the application shell."""
        self.running = False
        self.events.emit("app:stop")

    def load_plugin(self, name: str, plugin: object) -> None:
        """Register and load a plugin."""
        self.plugins.register(name, plugin)
        self.plugins.load(name)

    def set_theme(self, name: str) -> None:
        """Apply a theme."""
        self.themes.apply_theme(name)
