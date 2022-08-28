from .abstract_image import AbstractImage


class AbstractSpritesheet:
    """Spritesheet providing methods of cutting out proper frames given the unit dimensions
       and total dimensions in terms of units. Rows and columns of a spritesheet are zero indexed."""

    def __init__(self, spritesheet, height: int, width: int, rows: int, cols: int):
        self.spritesheet = spritesheet
        self.height, self.width = height, width
        self.rows, self.cols = rows, cols

    def load_image(self, row: int, col: int) -> AbstractImage:
        """Load the frame at the specified row and col."""
        raise NotImplementedError

    def load_some_images(self, row: int, col: int, amount: int) -> list[AbstractImage]:
        """Starting from the given position, load next amount of images, including the current
           position. Assume that amount is within the grid."""
        images = []
        for r in range(row, self.rows):
            for c in range(col, self.cols):
                if len(images) >= amount:
                    break
                images.append(self.load_image(r, c))
        return images

    def load_all_images(self) -> list[AbstractImage]:
        """Loads all images, going row by row from left to right."""
        return [self.load_image(r, c) for r in range(self.rows) for c in range(self.cols)]
