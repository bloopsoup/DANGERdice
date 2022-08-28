import pyglet
from .image import Image
from core.components import AbstractImage, AbstractSpritesheet


class Spritesheet(AbstractSpritesheet):
    def __init__(self, spritesheet: pyglet.image, height: int, width: int, rows: int, cols: int):
        super().__init__(spritesheet, height, width, rows, cols)

    def load_image(self, row: int, col: int) -> AbstractImage:
        image = self.spritesheet.get_region(x=col*self.width, y=row*self.height, width=self.width, height=self.height)
        return Image(image)
