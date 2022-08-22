from constants import font_presets, surface
from core.components import AbstractLabel


class Label(AbstractLabel):
    def __init__(self, text: str, preset: str):
        assert preset in font_presets, "{0} is not a valid font preset".format(preset)
        super().__init__(text, preset)
        self.rendered_text = font_presets[preset].render(text, True, (0, 0, 0))
        self.width, self.height = self.rendered_text.get_width(), self.rendered_text.get_height()

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.rendered_text, pos)
