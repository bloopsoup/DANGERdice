import pyglet
from .image import Image
from ..components import AbstractImage, AbstractSpritesheet, tl_to_bl


class Spritesheet(AbstractSpritesheet):
    def __init__(self, spritesheet: pyglet.image, height: int, width: int, rows: int, cols: int):
        super().__init__(spritesheet, height, width, rows, cols)

    def load_image(self, row: int, col: int) -> AbstractImage:
        pos = tl_to_bl((col * self.width, (row * self.height) + self.height), self.spritesheet.height)
        image = self.spritesheet.get_region(x=pos[0], y=pos[1], width=self.width, height=self.height)
        return Image(image)
