import pyglet
from ..components import AbstractImage


class Image(AbstractImage):
    def __init__(self, image: pyglet.image):
        super().__init__(image)
        self.width, self.height = self.image.width, self.image.height

    def blit(self, pos: tuple[int, int]):
        self.image.blit(pos[0], pos[1])
