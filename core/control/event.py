from ..enums import EventType, Key, MouseButton


class Event:
    """An event class for GUI components."""

    def __init__(self, event_type: EventType, key: Key = None, text: str = None, mouse_button: MouseButton = None,
                 pos: tuple[float, float] = None):
        self.event_type = event_type
        self.key, self.text = key, text
        self.mouse_button, self.pos = mouse_button, pos

    def get_type(self) -> EventType:
        """Gets the event's type."""
        return self.event_type

    def is_key_event(self) -> bool:
        """Is this event key press related?"""
        return self.event_type == EventType.KEY_DOWN or self.event_type == EventType.KEY_UP

    def is_mouse_event(self) -> bool:
        """Is this event mouse related?"""
        return self.event_type == EventType.MOUSE_DOWN or self.event_type == EventType.MOUSE_UP or self.event_type == EventType.MOUSE_MOVE

    def is_mouse_press_event(self) -> bool:
        """Is this event mouse press related?"""
        return self.event_type == EventType.MOUSE_DOWN or self.event_type == EventType.MOUSE_UP

    def get_key(self) -> Key:
        """Gets the event's key (must be a key event)."""
        assert self.is_key_event(), "must be a key event"
        return self.key

    def get_text(self) -> str:
        """Gets the event's text (must be a text event)."""
        assert self.event_type == EventType.TEXT_INPUT, "must be a text event"
        return self.text

    def get_mouse_button(self) -> MouseButton:
        """Gets the event's mouse button (must be a mouse event)."""
        assert self.is_mouse_press_event(), "must be a mouse event"
        return self.mouse_button

    def get_mouse_position(self) -> tuple[float, float]:
        """Gets the event's mouse position (must be a mouse event)."""
        assert self.is_mouse_event(), "must be a mouse event"
        return self.pos
