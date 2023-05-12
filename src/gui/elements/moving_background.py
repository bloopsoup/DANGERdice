from .displayable import Displayable
from src.core import AbstractImage


class MovingBackgroundElement(Displayable):
    """A moving background that moves cardinally and automatically resets itself."""

    def __init__(self, images: list[AbstractImage], velocity: tuple[int, int], window_size: tuple[int, int]):
        super().__init__(images, (0, 0), {})
        self.window_size = window_size
        self.velocity = velocity
        self.starting_pos = self.calculate_starting_position()
        self.set_position(self.starting_pos)

    def calculate_starting_position(self) -> tuple:
        """Determines the starting position based on window_size and the velocity."""
        return (0 if self.velocity[0] <= 0 else self.window_size[0] - self.get_width(),
                0 if self.velocity[1] <= 0 else self.window_size[1] - self.get_height())

    def out_of_bounds(self) -> bool:
        """Determines if the moving background is OOB."""
        pos = self.get_position()
        return (pos[0] > 2 * self.window_size[0] - self.get_width() and self.velocity[0] > 0) \
            or (pos[0] < self.window_size[0] - self.get_width() and self.velocity[0] <= 0) \
            or (pos[1] > 2 * self.window_size[1] - self.get_height() and self.velocity[1] > 0) \
            or (pos[1] < self.window_size[1] - self.get_height() and self.velocity[1] <= 0)

    def move(self):
        """Moves the background image according to velocity. Resets itself if out of bounds."""
        self.add_position(self.velocity)
        if self.out_of_bounds():
            self.set_position(self.starting_pos)

    def update(self, dt: float):
        """Updating itself."""
        self.dt_runner.dt_update(dt, self.move)

    def draw(self):
        """Displays itself."""
        self.images[0].blit(self.get_position())
