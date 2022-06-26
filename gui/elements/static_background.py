import pygame
from .displayable import Displayable


class StaticBG(Displayable):
    """A static background."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos, {})

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        surface.blit(self.images[0], (self.pos.x, self.pos.y))
