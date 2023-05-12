from .game_state import GameState
from ..config import BUTTON_DEFAULT, TEXT_MEDIUM
from src.core import get_image, get_sprites, save_json, SOUND_PLAYER
from src.gui.elements import StaticBG, PTexts, Button


class Save(GameState):
    """A save confirmation screen before overwriting the current save."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([get_image("black")], (0, 0), TEXT_MEDIUM, [(0, 220)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("yellow")], (0, 0)), "")
        self.canvas.add_element(Button(get_sprites("confirm"), (320, 280), BUTTON_DEFAULT, self.save_data), "")
        self.canvas.add_element(Button(get_sprites("cancel"), (410, 280), BUTTON_DEFAULT, self.back), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")
        self.canvas.add_element(self.text_display, "")
        self.text_display.set_text(0, "Save current data?")

    def save_data(self):
        """Saves current player data."""
        save_json(self.persistent_data.export_data(), "game_data.json")
        self.to("player_menu")
