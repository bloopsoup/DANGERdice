import pygame

from gui.canvas.elements.displayable import Displayable


class StaticBG(Displayable):
    """A static background."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos, {})

    def update(self, surface: pygame.Surface, dt: float):
        """Displays itself onto surface."""
        surface.blit(self.images[0], (self.pos.x, self.pos.y))
