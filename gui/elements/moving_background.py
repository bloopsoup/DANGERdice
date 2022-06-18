import pygame
from gui.elements.displayable import Displayable


class MovingBackgroundElement(Displayable):
    """A moving background that moves cardinally and automatically resets itself."""

    def __init__(self, images: list[pygame.Surface], velocity: tuple[float, float], window_size: tuple[float, float]):
        super().__init__(images, (0, 0), {})

        # Assumes background is much bigger than the window size
        self.window_size = pygame.Vector2(window_size)
        self.velocity = pygame.Vector2(velocity)
        self.starting_pos = pygame.Vector2(self.calculate_starting_position())
        self.set_position(self.starting_pos)

    def calculate_starting_position(self) -> tuple:
        """Determines the starting position based on window_size and the velocity."""
        return (0 if self.velocity.x <= 0 else self.window_size.x - self.reference.width,
                0 if self.velocity.y <= 0 else self.window_size.y - self.reference.height)

    def out_of_bounds(self) -> bool:
        """Determines if the moving background is OOB."""
        return (self.pos.x > 2 * self.window_size.x - self.reference.width and self.velocity.x > 0) \
            or (self.pos.x < self.window_size.x - self.reference.width and self.velocity.x <= 0) \
            or (self.pos.y > 2 * self.window_size.y - self.reference.height and self.velocity.y > 0) \
            or (self.pos.y < self.window_size.y - self.reference.height and self.velocity.y <= 0)

    def move(self):
        """Moves the background image according to velocity. Resets itself if out of bounds."""
        self.pos = self.pos + self.velocity
        if self.out_of_bounds():
            self.set_position(self.starting_pos)

    def update(self, dt: float):
        """Updating itself."""
        self.dt_runner.dt_update(dt, self.move)

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        surface.blit(self.images[0], (self.pos.x, self.pos.y))
