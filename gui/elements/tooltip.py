import pygame
from .displayable import Displayable
from .interactive import Interactive


class Tooltip(Interactive):
    """A wrapper around a displayable element which displays text when you mouse over it."""

    def __init__(self, pos: tuple[float, float], theme: dict, font: pygame.font.Font, text: str, element: Displayable):
        super().__init__([pygame.Surface((1, 1))], pos, theme, None)
        self.font = font
        self.text = text
        self.element = element
        self.hovered = False

    def set_text(self, text: str):
        """Sets the tooltip's text."""
        self.text = text

    def handle_event(self, event: pygame.event.Event):
        """When hovering over the element and process events for the contained element."""
        self.element.handle_event(event)
        self.hovered = self.element.is_mouse_over_element()

    def update(self, dt: float):
        """Update the contained element and the tooltip's position."""
        self.element.update(dt)

    def draw(self, surface: pygame.Surface):
        """Displays the tooltip and the contained element to the surface."""
        self.element.draw(surface)
        if self.hovered:
            surface.blit(self.font.render(self.text, True, (0, 0, 0)), (self.pos.x, self.pos.y))
