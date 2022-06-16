import pygame
from gui.elements.displayable import Displayable
from gui.utils.index_cycler import IndexCycler


class Idle(Displayable):
    """An element with an idle animation."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], idle_handler: IndexCycler):
        super().__init__(images, pos, {})
        self.image = self.images[0]
        self.idle = True
        self.idle_handler = idle_handler

    def set_idle(self, on: bool):
        """Indicates whether the element is idle or not."""
        self.idle = on

    def idle_animate(self, dt: float):
        """Change the current image quickly to simulate an idle animation."""
        if not self.idle:
            return
        result = self.idle_handler.update(dt)
        if result != -1:
            self.image = self.images[result]

    def update(self, dt: float):
        """Updating itself."""
        self.reference.move_ip(self.pos)
        self.idle_animate(dt)

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        surface.blit(self.image, (self.pos.x, self.pos.y))
