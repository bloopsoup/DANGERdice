from .command import Command


class TimerCommand(Command):
    """Command which performs an action after a certain amount of time."""

    def __init__(self, frames: float, func):
        super().__init__()
        self.dt_runner.set_frames(frames)
        self.func = func

    def stop(self):
        """Call the function when you are done."""
        self.done = True
        self.func()

    def update(self, dt: float):
        """Waiting for time to pass."""
        if self.done:
            return
        self.dt_runner.dt_update(dt, self.stop)
