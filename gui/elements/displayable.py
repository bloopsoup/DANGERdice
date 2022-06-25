import pygame
from gui.utils.delta_time_runner import DeltaTimeRunner


class Displayable:
    """A generic Canvas element to be displayed which supports themes for aesthetic customization."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict):
        self.dt_runner = DeltaTimeRunner(0.01)

        self.images = images
        self.pos = pygame.Vector2(pos)
        self.theme = theme

        # A reference rectangle of the widget
        self.reference = self.images[0].get_rect()
        self.reference.move_ip(self.pos.x, self.pos.y)

    def get_position(self) -> pygame.Vector2:
        """Gets the position of the element."""
        return self.pos

    def add_position(self, pos: pygame.Vector2):
        """Adds pos to the current position."""
        self.pos = self.pos + pos

    def set_position(self, pos: pygame.Vector2):
        """Sets the position of the element."""
        self.pos = pos

    def find_center(self, text_surface: pygame.Surface) -> int:
        """Returns the width to use in order to center text with respect to the element."""
        return int((self.reference.width - text_surface.get_width()) / 2)

    def draw_border(self, surface: pygame.Surface):
        """Draws the border around the element."""
        if self.theme["border_size"] > 0:
            pygame.draw.rect(surface, (0, 0, 0), self.reference, self.theme["border_size"])

    def handle_event(self, event):
        """Note: Required to be implemented if object is Interactive."""
        pass

    def update(self, dt: float):
        """Executing the command each update."""
        pass

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        raise NotImplementedError
