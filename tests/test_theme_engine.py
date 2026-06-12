"""
Tests for ThemeEngine.
"""

import pytest
from themes.engine import ThemeEngine


def test_apply_theme():
    engine = ThemeEngine()

    theme = engine.apply_theme("black")

    assert theme["background"] == "#000000"
    assert engine.get_theme()["background"] == "#000000"


def test_list_themes():
    engine = ThemeEngine()

    themes = engine.list_themes()

    assert "blue" in themes
    assert "black" in themes
