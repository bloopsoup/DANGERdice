from .game_state import GameState
from ..config import TEXT_WHITE_LARGE
from src.core import get_image, SOUND_PLAYER
from src.gui.elements import StaticBG, PTexts
from src.gui.commands import TimerCommand


class Attributions(GameState):
    """First thing you see when you open the game. Gives credit to some folks."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([get_image("black")], (0, 220), TEXT_WHITE_LARGE, [(0, 0)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("black")], (0, 0)), "")
        self.canvas.add_element(self.text_display, "")
        self.text_display.set_text(0, "A BMB GAME")
        self.canvas.add_element(StaticBG([get_image("badmc")], (350, 280)), "logo")

    def setup_commands(self):
        self.command_queue.add([TimerCommand(1.2, self.remove_face)])
        self.command_queue.add([TimerCommand(1.2, lambda: self.to("main_menu"))])

    def setup_music(self):
        SOUND_PLAYER.play_sfx("one")

    def remove_face(self):
        """Removes the face, changes the text, and then plays a sound."""
        self.text_display.set_text(0, "Inspired by TinyDiceDungeons")
        self.canvas.delete_group("logo")
        SOUND_PLAYER.play_sfx("one")
