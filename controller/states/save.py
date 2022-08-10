from .state import State
from ..utils import music_handler, save_json
from ..loader import load_static, load_some_sprites, load_font
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, PTexts, Button


class Save(State):
    """A save confirmation screen before overwriting the current save."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([load_static("black")], (0, 0), load_font("M"), [(0, 220)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("yellow")], (0, 0)), "")
        self.canvas.add_element(Button(load_some_sprites("confirm"), (320, 280), BUTTON_DEFAULT, self.save_data), "")
        self.canvas.add_element(Button(load_some_sprites("cancel"), (410, 280), BUTTON_DEFAULT, self.back), "")
        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), "")
        self.canvas.add_element(self.text_display, "")
        self.text_display.set_text(0, "Save current data?")

    def save_data(self):
        """Saves current player data."""
        save_json({"player": self.player.export_data(), "shop": self.shop_inventory.export_data()}, "game_data.json")
        self.to("player_menu")
