import pygame
from .displayable import Displayable
from .interactive import Interactive


class Tooltip(Interactive):
    """A wrapper around a displayable element which displays text when you mouse over it."""

    def __init__(self, images: list[pygame.Surface], theme: dict, font: pygame.font.Font, text: str,
                 element: Displayable):
        super().__init__(images, (0, 0), theme, None)
        self.font = font
        self.text = text
        self.element = element
        self.hovered = False

    def handle_event(self, event: pygame.event.Event):
        """When hovering over the element and process events for the contained element."""
        self.element.handle_event(event)
        self.hovered = self.reference.collidepoint(pygame.mouse.get_pos())

    def update(self, dt: float):
        """Update the contained element."""
        self.element.update(dt)

    def draw(self, surface: pygame.Surface):
        """Displays the tooltip and the contained element to the surface."""
        self.element.draw(surface)
        if self.hovered:
            element_pos = self.element.get_position()
            surface.blit(self.images[0], (element_pos.x, element_pos.y))
            surface.blit(self.font.render(self.text, True, (0, 0, 0)), (element_pos.x, element_pos.y))
