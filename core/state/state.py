from .event import Event


class State:
    """A state abstract class."""

    def __init__(self):
        self.done, self.quit = False, False
        self.next, self.previous = None, None

    def setup_state(self):
        """Sets attributes for a state when entering."""
        pass

    def setup_canvas(self):
        """Sets up the canvas for the state."""
        pass

    def setup_commands(self):
        """Sets up initial commands to run if needed."""
        pass

    def setup_music(self):
        """Sets up the music."""
        pass

    def startup(self):
        """Setup when entering a state, such as loading songs or images."""
        self.setup_state()
        self.setup_canvas()
        self.setup_commands()
        self.setup_music()

    def reset_state(self):
        """Resets attributes for a state when leaving."""
        pass

    def cleanup(self):
        """Cleaning up components before leaving the state."""
        self.reset_state()

    def handle_event(self, event: Event):
        """Handles events in this state."""
        print(event.get_type())

    def update_components(self):
        """Update dynamic components based on external information.."""
        pass

    def update(self, dt: float):
        """Update objects pertaining to this state."""
        self.update_components()

    def draw(self):
        """Draws objects pertaining to this state."""
        pass

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
