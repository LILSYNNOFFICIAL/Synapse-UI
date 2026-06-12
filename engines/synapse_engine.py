"""
Execution engine for Project Synapse.
"""

from models.synapse_model import SynapseModel


class SynapseEngine:
    """Primary engine responsible for model execution."""

    def __init__(self) -> None:
        self.model = SynapseModel()
        self.running = False

    def start(self) -> None:
        self.model.load()
        self.running = True

    def stop(self) -> None:
        self.model.unload()
        self.running = False
