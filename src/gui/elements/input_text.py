from .interactive import Interactive
from core import AbstractImage, Label, Event, EventType, Key, SOUND_PLAYER


class InputText(Interactive):
    """A place to input text. Uses two images: [active, inactive]."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], theme: dict, on_event):
        super().__init__(images, pos, theme, on_event)
        self.active = False
        self.text, self.text_surface = "", Label("", self.theme["font"], (0, 0, 0))

    def current_picture_index(self) -> int:
        """Determines image index to use to reflect the state of the widget."""
        return 0 if self.active else 1

    def will_overflow(self, char: str) -> bool:
        """Determines whether adding char will make the text go past its boundaries."""
        char_s = Label(char, self.theme["font"], (0, 0, 0))
        return self.text_surface.get_width() + char_s.get_width() + self.theme["padding"] >= self.get_width()

    def submit_text(self):
        """Calls on_event with self.text as an argument then clears itself."""
        self.on_event(self.text)
        self.text = ""

    def handle_event(self, event: Event):
        """Clicking toggles the box which allows inputting text. ENTER to submit the text."""
        # Clicking on the input box
        if event.get_type() == EventType.MOUSE_DOWN:
            if self.is_mouse_over_element(event):
                self.active = not self.active
            else:
                self.active = False

        # ENTER/BACKSPACE
        if self.active and event.get_type() == EventType.KEY_DOWN:
            if event.get_key() == Key.ENTER:
                SOUND_PLAYER.play_sfx(self.theme["sfx"])
                self.submit_text()
            elif event.get_key() == Key.BACKSPACE:
                self.text = self.text[:-1]

        # Typing into the input box
        if self.active and event.get_type() == EventType.TEXT_INPUT and not self.will_overflow(event.get_text()):
            self.text += event.get_text()

    def draw(self):
        """Displays itself."""
        # Draw the input box
        selected_image = self.current_picture_index()
        self.images[selected_image].blit(self.get_position())
        self.draw_border()

        # Draw the text
        self.text_surface = Label(self.text, self.theme["font"], (0, 0, 0))
        pos, offset = self.get_position(), self.find_center_offset(self.text_surface.get_rectangle())
        self.text_surface.blit((pos[0] + offset[0], pos[1] + offset[1]))
