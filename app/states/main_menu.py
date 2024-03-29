from .game_state import GameState
from ..config import BUTTON_DEFAULT
from src.core import get_image, get_sprites, SOUND_PLAYER
from src.gui.elements import MovingBackgroundElement, StaticBG, Button


class MainMenu(GameState):
    """Main menu."""

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([get_image("tall_squares")], (0, 2), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("logo")], (0, 0)), "")
        self.canvas.add_element(Button(get_sprites("campaign"), (150, 270), BUTTON_DEFAULT, lambda: self.to("intro")), "")
        self.canvas.add_element(Button(get_sprites("load"), (150, 355), BUTTON_DEFAULT, lambda: self.to("load")), "")
        self.canvas.add_element(Button(get_sprites("quit"), (150, 440), BUTTON_DEFAULT, self.quit_game), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")

    def setup_music(self):
        SOUND_PLAYER.change_music("trooper")
