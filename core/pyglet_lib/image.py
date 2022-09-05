import pyglet
from ..components import AbstractImage, tl_to_bl


class Image(AbstractImage):
    def __init__(self, image: pyglet.image):
        super().__init__(image)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.width, self.height = self.sprite.width, self.sprite.height

    def blit_border(self, pos: tuple[int, int], color: tuple[int, int, int], size: int):
        pass

    def blit(self, pos: tuple[int, int]):
        self.sprite.position = tl_to_bl((pos[0], pos[1] + self.height), 600)
        self.sprite.draw()
