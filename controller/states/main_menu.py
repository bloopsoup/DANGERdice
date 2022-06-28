from .state import State
from ..utils import music_handler
from ..loader import load_screen, load_button_sprites, load_sound
from ..themes import BUTTON_DEFAULT
from gui.elements import MovingBackgroundElement, StaticBG, Button


class MainMenu(State):
    """Main menu."""

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([load_screen("tall_squares")], (0, 2), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_screen("logo")], (0, 0)), 0)
        self.canvas.add_element(Button(load_button_sprites("campaign"), (150, 270), BUTTON_DEFAULT, self.intro), 0)
        self.canvas.add_element(Button(load_button_sprites("load"), (150, 355), BUTTON_DEFAULT, self.load), 0)
        self.canvas.add_element(Button(load_button_sprites("quit"), (150, 440), BUTTON_DEFAULT, self.quit_game), 0)
        self.canvas.add_element(Button(load_button_sprites("music"), (730, 530), BUTTON_DEFAULT,
                                       music_handler.toggle_music), 0)

    def startup(self):
        self.setup_canvas()
        music_handler.change_music(load_sound("trooper", False))

    def intro(self):
        """Go to the intro sequence."""
        self.to("intro")

    def load(self):
        """Go to the loading screen."""
        self.to("load")