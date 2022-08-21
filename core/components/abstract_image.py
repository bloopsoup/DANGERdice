from .rectangle import Rectangle


class AbstractImage:
    """An abstract image class. Implement with library specific components."""

    def __init__(self, path: str):
        self.path, self.image = path, None
        self.width, self.height = 0, 0

    def get_width(self) -> int:
        """Gets the width of the image."""
        return self.width

    def get_height(self) -> int:
        """Gets the height of the image."""
        return self.height

    def get_rectangle(self) -> Rectangle:
        """Gets the rectangle representation of the image."""
        return Rectangle((0, 0), self.width, self.height)

    def blit(self, pos: tuple[int, int]):
        """Draws the image on screen."""
        raise NotImplementedError
