from .rectangle import Rectangle


class AbstractLabel:
    """An abstract label class. Implement with library-specific functions."""

    def __init__(self, text: str, font: str, color: tuple[int, int, int]):
        self.text, self.rendered_text = text, None
        self.font, self.color = font, color
        self.width, self.height = 0, 0

    def get_width(self) -> int:
        """Gets the width of the image."""
        return self.width

    def get_height(self) -> int:
        """Gets the height of the image."""
        return self.height

    def get_rectangle(self) -> Rectangle:
        """Gets the rectangle representation of the label."""
        return Rectangle((0, 0), self.width, self.height)

    def blit(self, pos: tuple[int, int]):
        """Draws text on screen at position."""
        raise NotImplementedError
