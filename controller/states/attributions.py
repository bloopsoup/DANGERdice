from .state import State
from ..utils import music_handler
from ..loader import load_static, load_font, load_sound
from gui.elements import StaticBG, PTexts
from gui.commands import TimerCommand


class Attributions(State):
    """First thing you see when you open the game. Gives credit to some folks."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([load_static("black")], (0, 220), load_font("L"), 1, [(0, 0)], True)
        self.text_display.set_color((255, 255, 255))

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("black")], (0, 0)), 0)
        self.canvas.add_element(self.text_display, 0)
        self.text_display.set_text(0, "A BMB GAME")
        self.canvas.add_element(StaticBG([load_static("badmc")], (350, 280)), 1)

    def setup_commands(self):
        self.command_queue.add([TimerCommand(1.2, self.remove_face)])
        self.command_queue.add([TimerCommand(1.2, lambda: self.to("main_menu"))])

    def startup(self):
        self.setup_canvas()
        self.setup_commands()
        music_handler.play_sfx(load_sound("one", True))

    def remove_face(self):
        """Removes the face, changes the text, and then plays a sound."""
        self.text_display.set_text(0, "Inspired by TinyDiceDungeons")
        self.canvas.delete_group(1)
        music_handler.play_sfx(load_sound("one", True))
