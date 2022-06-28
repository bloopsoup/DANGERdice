import pygame
from gui import Canvas
from gui.commands import CommandQueue


class State:
    """A state abstract class."""

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
        raise NotImplementedError

    def cleanup(self):
        """Cleaning up components before leaving the state."""
        pass

    def handle_event(self, event):
        """Handles events in this state."""
        self.canvas.handle_event(event)

    def update(self, dt: float):
        """Draws objects pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(dt)
        self.command_queue.update(dt)

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