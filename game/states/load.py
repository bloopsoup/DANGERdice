from .game_state import GameState
from ..config import BUTTON_DEFAULT, TEXT_MEDIUM
from core import get_image, get_sprites, load_json, SOUND_PLAYER
from gui.elements import StaticBG, PTexts, Button


class Load(GameState):
    """A load confirmation screen before loading data that overrides the current session."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([get_image("black")], (0, 0), TEXT_MEDIUM, [(0, 220)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("yellow")], (0, 0)), "")
        self.canvas.add_element(Button(get_sprites("confirm"), (320, 280), BUTTON_DEFAULT, self.load_data), "")
        self.canvas.add_element(Button(get_sprites("cancel"), (410, 280), BUTTON_DEFAULT, self.back), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")
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
