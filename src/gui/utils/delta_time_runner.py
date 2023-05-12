class DeltaTimeRunner:
    """Responsible for running functions periodically based on delta time."""

    def __init__(self, frames: float = 0):
        self.count = 0
        self.frames = frames

    def set_frames(self, frames: float):
        """Sets the number of frames needed before something happens."""
        self.frames = frames

    def dt_update(self, dt: float, func):
        """Handles func that are called each frame."""
        self.count += dt
        if self.count >= self.frames:
            func()
            self.count = 0
