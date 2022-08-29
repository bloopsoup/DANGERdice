from .displayable import Displayable
from .interactive import Interactive
from core import AbstractImage, Label, Event


class Tooltip(Interactive):
    """A wrapper around a displayable element which displays text when you mouse over it."""

    def __init__(self, pos: tuple[int, int], theme: dict, text: str, element: Displayable):
        super().__init__([AbstractImage(None)], pos, theme, None)
        self.text = text
        self.element = element
        self.hovered = False

    def set_text(self, text: str):
        """Sets the tooltip's text."""
        self.text = text

    def handle_event(self, event: Event):
        """When hovering over the element and process events for the contained element."""
        self.element.handle_event(event)
        if event.is_mouse_event():
            self.hovered = self.element.is_mouse_over_element(event)

    def update(self, dt: float):
        """Update the contained element and the tooltip's position."""
        self.element.update(dt)

    def draw(self):
        """Displays the tooltip and the contained element."""
        self.element.draw()
        if self.hovered:
            Label(self.text, self.theme["font"], (0, 0, 0)).blit(self.get_position())
