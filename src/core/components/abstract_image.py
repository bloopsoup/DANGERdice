from .rectangle import Rectangle


class AbstractImage:
    """An abstract image class. Implement with library specific components."""

    def __init__(self, image):
        self.image = image
        self.width, self.height = 0, 0

    def get_image(self):
        """Gets the underlying image itself."""
        return self.image

    def get_width(self) -> int:
        """Gets the width of the image."""
        return self.width

    def get_height(self) -> int:
        """Gets the height of the image."""
        return self.height

    def get_rectangle(self) -> Rectangle:
        """Gets the rectangle representation of the image."""
        return Rectangle((0, 0), self.width, self.height)

    def blit_border(self, pos: tuple[int, int], color: tuple[int, int, int], size: int):
        """Draws a border around the image on screen."""
        raise NotImplementedError

    def blit(self, pos: tuple[int, int]):
        """Draws the image on screen."""
        raise NotImplementedError
