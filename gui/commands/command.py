from ..utils import DeltaTimeRunner


class Command:
    """Actions relying on dt updates to execute."""

    def __init__(self, func):
        self.func = func
        self.dt_runner = DeltaTimeRunner(0.01)
        self.done = False

    def is_done(self) -> bool:
        """Has the command finished?"""
        return self.done

    def stop(self):
        """Stop the command and call func."""
        self.done = True
        if self.func is not None:
            self.func()

    def update(self, dt: float):
        """Executing the command each update."""
        raise NotImplementedError
