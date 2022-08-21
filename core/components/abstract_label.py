class AbstractLabel:
    """An abstract label class. Implement with library-specific functions."""

    def __init__(self, text: str, preset: str):
        self.text, self.rendered_text = text, None
        self.preset = preset
        self.width, self.height = 0, 0

    def get_width(self) -> int:
        """Gets the width of the image."""
        return self.width

    def get_height(self) -> int:
        """Gets the height of the image."""
        return self.height

    def blit(self, pos: tuple[int, int]):
        """Draws text on screen at position."""
        raise NotImplementedError
