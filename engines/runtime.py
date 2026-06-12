class SynapseRuntime:
    """Core runtime for Project Synapse"""

    def __init__(self):
        self.running = False
        self.state = {}

    def start(self):
        self.running = True
        print("Synapse Runtime started.")

    def stop(self):
        self.running = False
        print("Synapse Runtime stopped.")

    def set_state(self, key, value):
        self.state[key] = value

    def get_state(self, key, default=None):
        return self.state.get(key, default)
