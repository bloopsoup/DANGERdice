from .interactive import Interactive
from core import AbstractImage, Event, EventType, SOUND_PLAYER


class Button(Interactive):
    """A button that runs a function on click. Uses three images: [inactive, hovered, clicked]."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], theme: dict, on_event):
        super().__init__(images, pos, theme, on_event)
        self.clicked, self.hovered = False, False

    def current_picture_index(self) -> int:
        """Determines image index to use to reflect the state of the widget."""
        if self.clicked:
            return 2
        elif self.hovered:
            return 1
        else:
            return 0

    def handle_event(self, event: Event):
        """When button is clicked, play sfx and call on_event."""
        if not event.is_mouse_event():
            return
        if self.is_mouse_over_element(event):
            self.hovered = True
            if event.get_type() == EventType.MOUSE_DOWN and self.on_event:
                SOUND_PLAYER.play_sfx(self.theme["sfx"])
                self.clicked = True
                self.on_event()
            else:
                self.clicked = False
        else:
            self.hovered = False

    def draw(self):
        """Displays itself."""
        self.images[self.current_picture_index()].blit(self.get_position())
        self.draw_border()
