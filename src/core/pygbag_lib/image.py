import pygame
from .constants import surface
from ..components import AbstractImage


class Image(AbstractImage):
    def __init__(self, image: pygame.Surface):
        super().__init__(image)
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def blit_border(self, pos: tuple[int, int], color: tuple[int, int, int], size: int):
        rect = self.image.get_rect()
        rect.update(pos, (self.width, self.height))
        pygame.draw.rect(surface, color, rect, size)

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.image, pos)
