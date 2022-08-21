from .state import State
from .event import Event


class StateManager:
    """Runs one state at a time where it will switch out states when prompted."""

    def __init__(self, start: str, states: dict[str, State]):
        self.done = False
        self.states, self.state_name = states, start
        self.state = self.states[self.state_name]
        self.state.startup()

    def is_done(self) -> bool:
        """Is the state manager exiting?"""
        return self.done

    def to_state(self):
        """Move to another state."""
        # Leaving current state
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()

        # Moving onto the next
        self.state = self.states[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def pass_event(self, event: Event):
        """Passes events to the state."""
        self.state.handle_event(event)

    def update(self, dt: float):
        """Exits or moves to another state when prompted. Then, update your screen."""
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.to_state()
        self.state.update(dt)

    def draw(self):
        """Calls the current state's draw function."""
        self.state.draw()
