from .displayable import Displayable
from core import AbstractImage, Label


class PTexts(Displayable):
    """An element displaying positioned text elements which change frequently over time. Note that
       images and pos represent an anchor point for relative text positioning (rather than absolute)."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], theme: dict,
                 offsets: list[tuple[int, int]], h_centered: bool):
        assert len(offsets) > 0, "must have at least 1 offset"
        super().__init__(images, pos, theme)
        self.texts = ["" for _ in range(len(offsets))]
        self.offsets, self.h_centered = offsets, h_centered

    def set_text(self, i: int, text: str):
        """Sets the ith field to text."""
        assert i < len(self.texts), "text index out of bounds"
        self.texts[i] = text

    def set_texts(self, texts: list[str]):
        """Sets the texts."""
        assert len(texts) == len(self.texts), "texts length should match original"
        self.texts = texts

    def draw(self):
        """Displays its text onto surface."""
        for (text, offset) in zip(self.texts, self.offsets):
            if not len(text):
                continue
            pos, text_surface = self.get_position(), Label(text, self.theme["font"], self.theme["color"])
            adjusted_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if self.h_centered:
                adjusted_pos = (pos[0] + self.horizontal_center_offset(text_surface.get_rectangle()), adjusted_pos[1])
            text_surface.blit(adjusted_pos)
