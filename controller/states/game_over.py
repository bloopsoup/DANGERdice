from .state import State
from ..utils import music_handler
from ..loader import load_static, load_sound, load_some_sprites, load_all_sprites, load_idle_animation, create_player, \
    create_shop_inventory
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, Button, Idle


class GameOver(State):
    """You died. Quit or load past save."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(load_all_sprites("player"), (350, 472), None, load_idle_animation("player"))

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([load_static("tall_squares")], (0, 2), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("bricks")], (0, 0)), 0)
        self.canvas.add_element(StaticBG([load_static("game_over")], (0, 0)), 0)
        self.canvas.add_element(Button(load_some_sprites("quit"), (150, 200), BUTTON_DEFAULT, self.return_menu), 0)
        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), 0)
        self.canvas.add_element(self.player_display, 0)

    def setup_music(self):
        music_handler.change(load_sound("menu", False))

    def return_menu(self):
        """Goes back to the main menu and resets the stats."""
        State.player = create_player()
        State.shop_inventory = create_shop_inventory()
        self.to("main_menu")
