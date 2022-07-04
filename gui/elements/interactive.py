import pygame
from .displayable import Displayable


class Interactive(Displayable):
    """A generic Canvas element to be interacted with which calls on_event."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event):
        super().__init__(images, pos, theme)
        self.on_event = on_event

    def handle_event(self, event):
        """Trigger an event by clicking on the interactive element."""
        if self.reference.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            if self.on_event is not None:
                self.on_event()

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        raise NotImplementedError
