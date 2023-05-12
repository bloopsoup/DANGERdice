from ..utils import DeltaTimeRunner
from src.core import AbstractImage, Rectangle, Event


class Displayable:
    """A generic Canvas element to be displayed which supports themes for aesthetic customization."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], theme: dict):
        self.dt_runner = DeltaTimeRunner(0.01)
        self.images = images
        self.theme = theme
        self.reference = self.images[0].get_rectangle()
        self.reference.set_position(pos)

    def get_width(self) -> int:
        """Gets the width of the element."""
        return self.reference.get_width()

    def get_height(self) -> int:
        """Gets the height of the element."""
        return self.reference.get_height()

    def get_position(self) -> tuple[int, int]:
        """Gets the position of the element."""
        return self.reference.get_position()

    def add_position(self, pos: tuple[int, int]):
        """Adds pos to the current position."""
        self.reference.add_position(pos)

    def set_position(self, pos: tuple[int, int]):
        """Sets the position of the element."""
        self.reference.set_position(pos)

    def horizontal_center_offset(self, rect: Rectangle) -> int:
        """Returns the offset to horizontally center rect with respect to the element."""
        return int((self.get_width() - rect.get_width()) / 2)

    def vertical_center_offset(self, rect: Rectangle) -> int:
        """Returns the offset to vertically center rect with respect to the element."""
        return int((self.get_height() - rect.get_height()) / 2)

    def find_center_offset(self, rect: Rectangle) -> tuple[int, int]:
        """Returns the offset to center the rect relative to the reference."""
        return self.horizontal_center_offset(rect), self.vertical_center_offset(rect)

    def is_mouse_over_element(self, event: Event) -> bool:
        """Is the mouse over the element?"""
        return event.is_mouse_event() and self.reference.collides_with_point(event.get_mouse_position())

    def handle_event(self, event: Event):
        """Required to be implemented if object is Interactive."""
        pass

    def update(self, dt: float):
        """Executing the command each update."""
        pass

    def draw_border(self):
        """Draws the border around the element."""
        if self.theme["border_size"] > 0:
            self.images[0].blit_border(self.get_position(), (0, 0, 0), self.theme["border_size"])

    def draw(self):
        """Displays itself."""
        raise NotImplementedError
