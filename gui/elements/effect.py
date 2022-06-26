import pygame
from .displayable import Displayable
from ..utils import IndexCycler


class Effect(Displayable):
    """An effect which is meant to be shown when activated and automatically disables itself once finished."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], effect_handler: IndexCycler):
        super().__init__(images, pos, {})
        self.image = self.images[0]
        self.active = False
        self.effect_handler = effect_handler

    def set_active(self, active: bool):
        """Enable the animation."""
        self.active = active

    def reset(self):
        """Resets the effect's state."""
        self.image = self.images[0]
        self.set_active(False)

    def update(self, dt: float):
        """Updating itself."""
        if not self.active or self.effect_handler.will_end_list(dt):
            self.effect_handler.update(dt)
            self.reset()
            return

        result = self.effect_handler.update(dt)
        if result != -1:
            self.image = self.images[result]

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        if not self.active:
            return
        surface.blit(self.image, (self.pos.x, self.pos.y))
