from .game_state import GameState
from ..config import BUTTON_DEFAULT
from core import get_image, get_sprites, SOUND_PLAYER
from gui.elements import MovingBackgroundElement, StaticBG, Button


class MainMenu(GameState):
    """Main menu."""

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([get_image("tall_squares")], (0, 2), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("logo")], (0, 0)), "")
        self.canvas.add_element(Button(get_sprites("campaign"), (150, 270), BUTTON_DEFAULT, self.intro), "")
        self.canvas.add_element(Button(get_sprites("load"), (150, 355), BUTTON_DEFAULT, self.load), "")
        self.canvas.add_element(Button(get_sprites("quit"), (150, 440), BUTTON_DEFAULT, self.quit_game), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")

    def setup_music(self):
        SOUND_PLAYER.change_music("trooper")

    def intro(self):
        """Go to the intro sequence."""
        self.to("intro")

    def load(self):
        """Go to the loading screen."""
        self.to("load")
