from .displayable import Displayable
from src.core import AbstractImage, Event, EventType


class Interactive(Displayable):
    """A generic Canvas element to be interacted with which calls on_event."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], theme: dict, on_event):
        super().__init__(images, pos, theme)
        self.on_event = on_event
        self.clickable = True

    def toggle_click(self):
        """Toggles whether clicking on the interactive element does something."""
        self.clickable = not self.clickable

    def handle_event(self, event: Event):
        """Trigger an event by clicking on the interactive element."""
        if self.is_mouse_over_element(event) and event.get_type() == EventType.MOUSE_DOWN and self.clickable and self.on_event:
            self.on_event()

    def draw(self):
        """Displays itself."""
        raise NotImplementedError
