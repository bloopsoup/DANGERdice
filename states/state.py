import pygame

from asset_bank import AssetBank


class State:
    """A state abstract class. Persisting information goes here."""

    player = None
    quit = False

    def __init__(self, bank: AssetBank):
        self.bank = bank
        self.done = False
        self.next = None
        self.previous = None
        self.canvas = None
        self.effects = None

    def startup(self):
        """Setup when entering a state, such as loading songs or images."""
        raise NotImplementedError

    def cleanup(self):
        """Cleaning up components before leaving the state. This is not always necessary."""
        pass

    def handle_event(self, event):
        """Handles events in this state."""
        self.canvas.handle_event(event)

    def update(self, surface: pygame.Surface, dt: float):
        """Draws objects pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(surface, dt)
        # State.player.update(surface, dt)

    def to(self, to: str):
        """Goes to the target state."""
        self.next = to
        self.done = True

    def back(self):
        """Goes back to the previous state."""
        self.to(self.previous)

    @staticmethod
    def quit_game():
        """Quits the game."""
        State.quit = True
