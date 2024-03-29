from .displayable import Displayable
from ..utils import IndexCycler
from src.core import AbstractImage


class Effect(Displayable):
    """An effect which is meant to be shown when activated and automatically disables itself once finished."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], effect_handler: IndexCycler):
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

    def draw(self):
        """Displays itself."""
        if not self.active:
            return
        self.image.blit(self.get_position())
