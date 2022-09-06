import pyglet
from .constants import loaded_fonts
from ..components import AbstractLabel, tl_to_bl


class Label(AbstractLabel):
    def __init__(self, text: str, font: str, color: tuple[int, int, int]):
        assert font in loaded_fonts, f"{font} is not a valid font"
        super().__init__(text, font, color)
        font_name, font_size = loaded_fonts[font]
        self.rendered_text = pyglet.text.Label(text, font_name=font_name, font_size=font_size, color=color + (255,))
        self.width, self.height = self.rendered_text.content_width, self.rendered_text.content_height

    def blit(self, pos: tuple[int, int]):
        self.rendered_text.position = tl_to_bl((pos[0], pos[1] + self.height - 5), 600)
        self.rendered_text.draw()
