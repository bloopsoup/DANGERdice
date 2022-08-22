import pygame
from constants import surface
from core.components import AbstractImage


class Image(AbstractImage):
    def __init__(self, path: str):
        super().__init__(path)
        self.image = pygame.Surface.convert_alpha(pygame.image.load(path))
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.image, pos)
