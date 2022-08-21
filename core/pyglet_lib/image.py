import pyglet
from core.components import AbstractImage


class Image(AbstractImage):
    def __init__(self, path: str):
        super().__init__(path)
        self.image = pyglet.image.load(path)
        self.width, self.height = self.image.width, self.image.height

    def blit(self, pos: tuple[int, int]):
        self.image.blit(pos[0], pos[1])
