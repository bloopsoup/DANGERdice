import pygame
from .interactive import Interactive


class Button(Interactive):
    """A button that runs a function on click."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event):
        # Uses three images: [inactive, hovered, clicked]
        super().__init__(images, pos, theme, on_event)
        self.clicked = False
        self.hovered = False

    def current_picture_index(self) -> int:
        """Determines image index to use to reflect the state of the widget."""
        if self.clicked:
            return 2
        elif self.hovered:
            return 1
        else:
            return 0

    def handle_event(self, event):
        """When button is clicked, play sfx and call on_event."""
        if self.reference.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if event.type == pygame.MOUSEBUTTONDOWN and self.on_event is not None:
                self.clicked = True
                self.theme["play_sfx"]()
                self.on_event()
            else:
                self.clicked = False
        else:
            self.hovered = False

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        surface.blit(self.images[self.current_picture_index()], (self.pos.x, self.pos.y))
        self.draw_border(surface)
