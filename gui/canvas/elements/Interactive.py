import pygame

from gui.canvas.elements.Displayable import Displayable


class Interactive(Displayable):
    """A generic Canvas element to be interacted with which calls on_event."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event):
        super().__init__(images, pos, theme)
        self.on_event = on_event

    def handle_event(self, event):
        """Handles user input."""
        raise NotImplementedError

    def update(self, surface: pygame.Surface, dt: float):
        """Displays itself onto surface."""
        raise NotImplementedError
