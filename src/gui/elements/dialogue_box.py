from .interactive import Interactive
from ..utils import DialogueData
from src.core import AbstractImage, Label, Event, EventType, SOUND_PLAYER


class DialogueBox(Interactive):
    """Displays text in a box like it's typed."""

    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], theme: dict, on_event, d_data: DialogueData):
        super().__init__(images, pos, theme, on_event)
        self.dt_runner.set_frames(0.03)
        self.d_data = d_data
        self.active = False
        self.lines = [[""]]

    def toggle_visibility(self):
        """Toggles visibility of the dialogue box."""
        self.active = not self.active

    def reset_scripts(self):
        """Reset the texts and portraits to the beginning."""
        self.d_data.reset()

    def next_script(self) -> bool:
        """Moves to the next text and portrait and calls the current hook. Returns FALSE if there's no more content."""
        self.lines = [[""]]
        self.d_data.call_hook()
        if not self.d_data.advance():
            self.toggle_visibility()
            return False
        return True

    def line_overflows(self, line: list[str]) -> bool:
        """Determines whether the line is past its boundaries."""
        line_s = Label(" ".join(line), self.theme["font"], (0, 0, 0))
        return line_s.get_width() + self.theme["padding"][0] >= self.get_width()

    def add_letter(self):
        """Adds another letter from the script to the display text."""
        char, line = self.d_data.get_next_letter(), self.lines[-1]
        if char == "~":
            return
        if char == " ":
            line.append("")
        elif char != "`":
            SOUND_PLAYER.play_sfx(self.theme["sfx"])
            line[-1] += char
        if self.line_overflows(line):
            self.lines.append([line.pop()])

    def handle_event(self, event: Event):
        """Clicking on the dialogue box goes to the next script. Calls on_event if there are no more scripts."""
        if self.is_mouse_over_element(event) and event.get_type() == EventType.MOUSE_DOWN and self.active and self.clickable:
            if not self.next_script():
                self.on_event()

    def update(self, dt: float):
        """Updating itself."""
        if not self.active:
            return
        self.dt_runner.dt_update(dt, self.add_letter)

    def draw_portrait(self):
        """Displays the current portrait."""
        pos = self.get_position()
        self.d_data.get_portrait().blit((pos[0] + self.theme["p_padding"][0], pos[1] + self.theme["p_padding"][1]))

    def draw_words(self):
        """Displays the words with automatic wrapping."""
        pos = self.get_position()
        for i, line in enumerate(self.lines):
            line_s = Label(" ".join(line), self.theme["font"], (0, 0, 0))
            line_s.blit((pos[0] + self.theme["padding"][0], pos[1] + self.theme["padding"][1] + line_s.get_height()*i))

    def draw(self):
        """Displays itself."""
        if not self.active:
            return
        self.images[0].blit(self.get_position())
        self.draw_border()
        self.draw_portrait()
        self.draw_words()
