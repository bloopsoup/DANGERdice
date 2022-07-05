from .command import Command


class TimerCommand(Command):
    """Command which performs an action after a certain amount of time."""

    def __init__(self, frames: float, func):
        super().__init__(func)
        self.dt_runner.set_frames(frames)

    def update(self, dt: float):
        """Waiting for time to pass."""
        if self.done:
            return
        self.dt_runner.dt_update(dt, self.stop)
