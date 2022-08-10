from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_song
from ..themes import BUTTON_DEFAULT
from gui.elements import MovingBackgroundElement, StaticBG, Button


class MainMenu(State):
    """Main menu."""

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([load_static("tall_squares")], (0, 2), (800, 600)), "")
        self.canvas.add_element(StaticBG([load_static("logo")], (0, 0)), "")
        self.canvas.add_element(Button(load_some_sprites("campaign"), (150, 270), BUTTON_DEFAULT, self.intro), "")
        self.canvas.add_element(Button(load_some_sprites("load"), (150, 355), BUTTON_DEFAULT, self.load), "")
        self.canvas.add_element(Button(load_some_sprites("quit"), (150, 440), BUTTON_DEFAULT, self.quit_game), "")
        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), "")

    def setup_music(self):
        music_handler.change(load_song("trooper"))

    def intro(self):
        """Go to the intro sequence."""
        self.to("intro")

    def load(self):
        """Go to the loading screen."""
        self.to("load")
