"""
Core model definitions for Project Synapse.
"""


class SynapseModel:
    """Base model object used throughout Synapse."""

    def __init__(self, name: str = "DefaultModel") -> None:
        self.name = name
        self.loaded = False

    def load(self) -> None:
        """Load the model into memory."""
        self.loaded = True

    def unload(self) -> None:
        """Unload the model from memory."""
        self.loaded = False
