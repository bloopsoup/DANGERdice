from .event import Event


class State:
    """A state abstract class."""

    def __init__(self):
        self.done, self.quit = False, False
        self.next, self.previous = None, None

    def startup(self):
        """Setup when entering a state, such as loading songs or images."""
        raise NotImplementedError

    def cleanup(self):
        """Cleaning up components before leaving the state."""
        raise NotImplementedError

    def handle_event(self, event: Event):
        """Handles events in this state."""
        raise NotImplementedError

    def update(self, dt: float):
        """Update objects pertaining to this state."""
        raise NotImplementedError

    def draw(self):
        """Draws objects pertaining to this state."""
        raise NotImplementedError

    def to(self, to: str):
        """Goes to the target state."""
        self.next = to
        self.done = True

    def back(self):
        """Goes back to the previous state."""
        self.to(self.previous)

    def quit_game(self):
        """Quits the game."""
        self.quit = True
