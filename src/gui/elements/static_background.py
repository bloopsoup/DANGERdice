from .displayable import Displayable
from src.core import AbstractImage


class StaticBG(Displayable):
    """A static background."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int]):
        super().__init__(images, pos, {})

    def draw(self):
        """Displays itself."""
        self.images[0].blit(self.get_position())
