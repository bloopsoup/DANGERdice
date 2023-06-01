import pygame
from .image import Image
from ..components import AbstractImage, AbstractSpritesheet


class Spritesheet(AbstractSpritesheet):
    def __init__(self, spritesheet: pygame.Surface, height: int, width: int, rows: int, cols: int):
        super().__init__(spritesheet, height, width, rows, cols)

    def load_image(self, row: int, col: int) -> AbstractImage:
        reference = pygame.Rect(col * self.width, row * self.height, self.width, self.height)
        image = pygame.Surface(reference.size).convert_alpha()
        image.fill((0, 0, 0, 0))
        image.blit(self.spritesheet, (0, 0), reference)
        return Image(image)
