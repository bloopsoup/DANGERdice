import pygame


class Spritesheet:
    """Spritesheet providing methods of cutting out proper frames given the unit dimensions
       and total dimensions in terms of units. Rows and columns of a spritesheet are zero indexed."""

    def __init__(self, path: str, height: int, width: int, rows: int, cols: int):
        try:
            self.sheet = pygame.image.load(path).convert_alpha()
        except pygame.error:
            print('Unable to load spritesheet image:', path)
            raise SystemExit

        self.height = height
        self.width = width
        self.rows = rows
        self.cols = cols

    def load_image(self, row: int, col: int) -> pygame.Surface:
        """Load the frame at the specified row and col."""
        reference = pygame.Rect(col * self.width, row * self.height, self.width, self.height)
        image = pygame.Surface(reference.size).convert_alpha()
        image.fill((0, 0, 0, 0))
        image.blit(self.sheet, (0, 0), reference)
        return image

    def load_some_images(self, row: int, col: int, amount: int) -> list[pygame.Surface]:
        """Starting from the given position, load next amount of images, including the current
           position. Assume that amount is within the grid."""
        images = []
        for r in range(row, self.rows):
            for c in range(col, self.cols):
                if amount <= 0:
                    break
                images.append(self.load_image(r, c))
                amount -= 1
        return images

    def load_all_images(self) -> list[pygame.Surface]:
        """Loads all images, going row by row from left to right."""
        return [self.load_image(r, c) for r in range(self.rows) for c in range(self.cols)]
