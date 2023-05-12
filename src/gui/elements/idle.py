from .interactive import Interactive
from ..utils import IndexCycler
from src.core import AbstractImage


class Idle(Interactive):
    """An element with an idle animation. Can call a function when the element is clicked."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], on_event, idle_handler: IndexCycler):
        super().__init__(images, pos, {}, on_event)
        self.image = self.images[0]
        self.idle_handler, self.idle = idle_handler, True

    def set_image(self, i: int):
        """Set the image of the Idle element to the ith image."""
        self.image = self.images[i]

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
        self.idle_animate(dt)

    def draw(self):
        """Displays itself."""
        self.image.blit(self.get_position())
