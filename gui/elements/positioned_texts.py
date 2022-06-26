import pygame
from .displayable import Displayable


class PositionedTexts(Displayable):
    """An element displaying positioned text elements which change frequently over time. Note that
       images and pos represent an anchor point for relative text positioning (rather than absolute)."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], font: pygame.font,
                 num_fields: int, offsets: list[tuple[float, float]], h_centered: bool):
        assert num_fields == len(offsets), "number of fields and offsets should match"
        super().__init__(images, pos, {})
        self.font = font
        self.texts = ["" for _ in range(num_fields)]
        self.offsets = [pygame.Vector2(offset) for offset in offsets]
        self.h_centered = h_centered

    def set_text(self, i: int, text: str):
        """Sets the ith field to text."""
        assert i < len(self.texts), "text index out of bounds"
        self.texts[i] = text

    def set_texts(self, texts: list[str]):
        """Sets the texts."""
        self.texts = texts

    def draw(self, surface: pygame.Surface):
        """Displays its text onto surface."""
        for (text, offset) in zip(self.texts, self.offsets):
            if not len(text):
                continue
            text_surface = self.font.render(text, True, (0, 0, 0))
            adjusted_pos = self.pos + offset
            if self.h_centered:
                adjusted_pos.update(self.horizontal_center_offset(text_surface), adjusted_pos.y)
            surface.blit(text_surface, (adjusted_pos.x, adjusted_pos.y))
