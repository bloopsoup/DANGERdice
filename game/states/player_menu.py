from .game_state import GameState
from ..persistent_data import PERSISTENT_DATA
from ..config import load_idle_animation, BUTTON_DEFAULT, TEXT_DEFAULT, TEXT_MEDIUM
from core import get_image, get_sprites, get_all_sprites, AbstractImage, SOUND_PLAYER
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button


class PlayerMenu(GameState):
    """The player_menu. Return here after every battle to stock up or save."""

    def __init__(self):
        super().__init__()
        self.player = PERSISTENT_DATA.get_player()
        self.player_display = Idle(get_all_sprites("player"), (38, 72), None, load_idle_animation("player"))
        self.stat_display = PTexts([AbstractImage(None)], (145, 72), TEXT_DEFAULT, [(0, 0), (0, 20), (0, 40), (0, 60)], False)
        self.level_display = PTexts([get_image("black")], (0, 210), TEXT_MEDIUM, [(0, 0)], True)

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([get_image("tall_rectangles_light")], (0, -1), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("menu_hud")], (0, 0)), "")

        self.canvas.add_element(self.player_display, "")
        self.player_display.set_position((38, 72))
        self.canvas.add_element(self.stat_display, "")
        self.stat_display.set_texts([self.player.get_name(), f"LVL: {self.player.get_level()}",
                                     f"HP: {self.player.get_health()} / {self.player.get_max_health()}",
                                     f"Gold: {self.player.get_money()}"])
        self.canvas.add_element(self.level_display, "")
        self.level_display.set_text(0, f"Next Level: {self.player.get_stage()}")
        self.add_dice_to_canvas()

        self.canvas.add_element(Button(get_sprites("play"), (150, 250), BUTTON_DEFAULT, lambda: self.to(self.player.get_stage())), "")
        self.canvas.add_element(Button(get_sprites("inventory"), (150, 335), BUTTON_DEFAULT, lambda: self.to("inventory")), "")
        self.canvas.add_element(Button(get_sprites("shop"), (150, 420), BUTTON_DEFAULT, lambda: self.to("shop")), "")
        self.canvas.add_element(Button(get_sprites("save_icon"), (0, 530), BUTTON_DEFAULT, lambda: self.to("save")), "")
        self.canvas.add_element(Button(get_sprites("load_icon"), (70, 530), BUTTON_DEFAULT, lambda: self.to("load")), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")

    def setup_music(self):
        SOUND_PLAYER.change_music("note")

    def add_dice_to_canvas(self):
        """Adds dice to the canvas."""
        for i, die_name in enumerate(self.player.get_preference()):
            die_display = Idle(get_sprites(die_name), (376 + (i * 100), 79), None, load_idle_animation("square"))
            die_display.set_idle(False)
            self.canvas.add_element(die_display, "")
