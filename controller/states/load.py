from .state import State
from ..utils import music_handler, load_json
from ..loader import load_static, load_some_sprites, load_font
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, PTexts, Button


class Load(State):
    """A load confirmation screen before loading data that overrides the current session."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([load_static("black")], (0, 0), load_font("M"), [(0, 220)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("yellow")], (0, 0)), "")
        self.canvas.add_element(Button(load_some_sprites("confirm"), (320, 280), BUTTON_DEFAULT, self.load_data), "")
        self.canvas.add_element(Button(load_some_sprites("cancel"), (410, 280), BUTTON_DEFAULT, self.back), "")
        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), "")
        self.canvas.add_element(self.text_display, "")
        self.text_display.set_text(0, "Load saved data?")

    def load_data(self):
        """Loads player save data. If there is no data, does nothing."""
        data = load_json("game_data.json")
        if data:
            self.player.import_data(data["player"])
            self.shop_inventory.import_data(data["shop"])
            self.to("player_menu")
        else:
            self.text_display.set_text(0, "No save data detected")
