from .game_state import GameState
from ..config import load_idle_animation, BUTTON_DEFAULT
from src.core import get_image, get_sprites, get_all_sprites, SOUND_PLAYER
from src.gui.elements import StaticBG, MovingBackgroundElement, Button, Idle


class GameOver(GameState):
    """You died. Quit or load past save."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(get_all_sprites("player"), (350, 472), None, load_idle_animation("player"))

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([get_image("tall_squares")], (0, 2), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("bricks")], (0, 0)), "")
        self.canvas.add_element(StaticBG([get_image("game_over")], (0, 0)), "")
        self.canvas.add_element(Button(get_sprites("quit"), (150, 200), BUTTON_DEFAULT, self.return_menu), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")
        self.canvas.add_element(self.player_display, "")

    def setup_music(self):
        SOUND_PLAYER.change_music("menu")

    def return_menu(self):
        """Goes back to the main menu and resets the stats."""
        self.persistent_data.reset_data()
        self.to("main_menu")
