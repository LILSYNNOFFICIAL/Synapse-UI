class SynapseNode:
    """
    Base class for all Synapse nodes.
    Each node can process state and optionally produce outputs.
    """

    def __init__(self, node_id: str):
        self.node_id = node_id
        self.inputs = {}
        self.outputs = {}

    def set_input(self, key, value):
        self.inputs[key] = value

    def get_input(self, key, default=None):
        return self.inputs.get(key, default)

    def set_output(self, key, value):
        self.outputs[key] = value

    def get_output(self, key, default=None):
        return self.outputs.get(key, default)

    def process(self, state: dict):
        """
        Override in subclasses to implement node behavior.
        """
        raise NotImplementedError("process() must be implemented by subclasses")
