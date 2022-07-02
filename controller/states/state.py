import pygame
from ..loader import create_player
from gui import Canvas
from gui.commands import CommandQueue


class State:
    """A state abstract class."""

    player = create_player()

    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.canvas = Canvas()
        self.command_queue = CommandQueue()

    def setup_canvas(self):
        """Sets up the canvas for the state."""
        raise NotImplementedError

    def setup_commands(self):
        """Sets up initial commands to run if needed."""
        pass

    def startup(self):
        """Setup when entering a state, such as loading songs or images."""
        self.setup_canvas()
        self.setup_commands()

    def cleanup(self):
        """Cleaning up components before leaving the state."""
        self.canvas.delete_all()

    def handle_event(self, event):
        """Handles events in this state."""
        self.canvas.handle_event(event)

    def update_components(self):
        """Update dynamic components based on external information.."""
        pass

    def update(self, dt: float):
        """Update objects pertaining to this state."""
        self.command_queue.update(dt)
        self.update_components()
        self.canvas.update(dt)

    def draw(self, surface: pygame.Surface):
        """Draws objects pertaining to this state."""
        self.canvas.draw(surface)

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
