from ..config import create_player, create_shop_inventory
from core import Event, State
from gui import Canvas
from gui.commands import CommandQueue


class GameState(State):
    """A game state."""

    player = create_player()
    shop_inventory = create_shop_inventory()

    def __init__(self):
        super().__init__()
        self.canvas, self.command_queue = Canvas(), CommandQueue()

    def reset_state(self):
        """Resets attributes for a state when leaving."""
        pass

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

    def update_components(self):
        """Update dynamic components based on external information.."""
        pass

    def startup(self):
        self.setup_state()
        self.setup_canvas()
        self.setup_commands()
        self.setup_music()

    def cleanup(self):
        self.canvas.delete_all()
        self.command_queue.clear()
        self.reset_state()

    def handle_event(self, event: Event):
        self.canvas.handle_event(event)

    def update(self, dt: float):
        self.command_queue.update(dt)
        self.update_components()
        self.canvas.update(dt)

    def draw(self):
        self.canvas.draw()
