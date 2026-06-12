"""
Tests for PluginLoader.
"""

import pytest
from plugins.loader import PluginLoader


class DummyPlugin:
    def run(self, x):
        return x * 2


def test_register_and_load():
    loader = PluginLoader()
    plugin = DummyPlugin()

    loader.register("dummy", plugin)
    result = loader.load("dummy", 5)

    assert result == 10


def test_unload():
    loader = PluginLoader()
    plugin = DummyPlugin()

    loader.register("dummy", plugin)
    loader.unload("dummy")

    with pytest.raises(KeyError):
        loader.load("dummy", 5)
