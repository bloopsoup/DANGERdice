import pygame


class Displayable:
    """A generic Canvas element to be displayed which supports themes for aesthetic customization."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict):
        self.images = images
        self.pos = pygame.Vector2(pos)
        self.theme = theme

        # A reference rectangle of the widget
        self.reference = self.images[0].get_rect()
        self.reference.move_ip(self.pos.x, self.pos.y)

        self.count = 0
        self.frames = 0.01

    def set_position(self, pos: pygame.Vector2):
        """Sets the position of the element."""
        self.pos = pos

    def draw_border(self, surface: pygame.Surface):
        """Draws the border around the element."""
        if self.theme["border_size"] > 0:
            pygame.draw.rect(surface, (0, 0, 0), self.reference, self.theme["border_size"])

    def handle_event(self, event):
        """Note: Required to be implemented if object is Interactive."""
        pass

    def dt_update(self, dt: float, func):
        """Handles func that are called each frame."""
        self.count += dt
        if self.count >= self.frames:
            func()
            self.count = 0

    def update(self, surface: pygame.Surface, dt: float):
        """Displays itself onto surface."""
        raise NotImplementedError
