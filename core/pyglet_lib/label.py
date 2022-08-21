import pyglet
from constants import font_presets
from core.components import AbstractLabel


class Label(AbstractLabel):
    def __init__(self, text: str, preset: str):
        assert preset in font_presets, "{0} is not a valid font preset".format(preset)
        super().__init__(text, preset)
        font_name, font_size = font_presets[preset]
        self.rendered_text = pyglet.text.Label(text, font_name=font_name, font_size=font_size, x=0, y=0)
        self.width, self.height = self.rendered_text.content_width, self.rendered_text.content_height

    def blit(self, pos: tuple[int, int]):
        self.rendered_text.x, self.rendered_text.y = pos[0], pos[1]
        self.rendered_text.draw()
