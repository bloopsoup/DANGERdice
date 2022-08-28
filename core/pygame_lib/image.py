import pygame
from .constants import surface
from ..components import AbstractImage


class Image(AbstractImage):
    def __init__(self, image: pygame.Surface):
        super().__init__(image)
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.image, pos)
