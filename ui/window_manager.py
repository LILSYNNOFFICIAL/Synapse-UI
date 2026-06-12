class WindowManager:
    """Basic window manager for Synapse UI layer"""

    def __init__(self):
        self.windows = []

    def create_window(self, name: str):
        window = {
            "name": name,
            "state": "active"
        }
        self.windows.append(window)
        return window

    def list_windows(self):
        return self.windows

    def close_window(self, name: str):
        self.windows = [w for w in self.windows if w["name"] != name]
