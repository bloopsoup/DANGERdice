from .constants import loaded_fonts, surface
from ..components import AbstractLabel


class Label(AbstractLabel):
    def __init__(self, text: str, font: str, color: tuple[int, int, int]):
        assert font in loaded_fonts, f"{font} is not a valid font"
        super().__init__(text, font, color)
        self.rendered_text = loaded_fonts[font].render(text, True, color)
        self.width, self.height = self.rendered_text.get_width(), self.rendered_text.get_height()

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.rendered_text, pos)
