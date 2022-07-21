import pygame
from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound, load_idle_animation
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button


class PlayerMenu(State):
    """The player_menu. Return here after every battle to stock up or save."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(load_all_sprites("player"), (38, 72), None, load_idle_animation("player"))
        self.stat_display = PTexts([pygame.Surface((1, 1))], (145, 72), load_font("SS"),
                                   [(0, 0), (0, 20), (0, 40), (0, 60)], False)
        self.level_display = PTexts([load_static("black")], (0, 210), load_font("M"), [(0, 0)], True)

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([load_static("tall_rectangles_light")], (0, -1), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("menu_hud")], (0, 0)), 0)

        self.canvas.add_element(self.player_display, 0)
        self.player_display.set_position(pygame.Vector2(38, 72))
        self.canvas.add_element(self.stat_display, 0)
        self.stat_display.set_texts([self.player.get_name(), "LVL: {0}".format(self.player.get_level()),
                                     "HP: {0} / {1}".format(self.player.get_health(), self.player.get_max_health()),
                                     "Gold: {0}".format(self.player.get_money())])
        self.canvas.add_element(self.level_display, 0)
        self.level_display.set_text(0, "Next Level: {0}".format(self.player.get_stage()))
        self.add_dice_to_canvas()

        self.canvas.add_element(Button(load_some_sprites("play"), (150, 250), BUTTON_DEFAULT, self.play), 0)
        self.canvas.add_element(Button(load_some_sprites("inventory"), (150, 335), BUTTON_DEFAULT, self.inventory), 0)
        self.canvas.add_element(Button(load_some_sprites("shop"), (150, 420), BUTTON_DEFAULT, self.shop), 0)
        self.canvas.add_element(Button(load_some_sprites("save_icon"), (0, 530), BUTTON_DEFAULT, self.save), 0)
        self.canvas.add_element(Button(load_some_sprites("load_icon"), (70, 530), BUTTON_DEFAULT, self.load), 0)
        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), 0)

    def setup_music(self):
        music_handler.change(load_sound("note", False))

    def add_dice_to_canvas(self):
        """Adds dice to the canvas."""
        for i, die_name in enumerate(self.player.get_preference()):
            die_display = Idle(load_some_sprites(die_name), (376 + (i * 100), 79), None, load_idle_animation("square"))
            die_display.set_idle(False)
            self.canvas.add_element(die_display, 0)

    def play(self):
        """Onto battle!"""
        self.to(self.player.get_stage())

    def shop(self):
        """Let's go shopping!"""
        self.to("shop")

    def inventory(self):
        """Let's see your inventory."""
        self.to("inventory")

    def save(self):
        """Saves the game."""
        self.to("save")

    def load(self):
        """Loads the game."""
        self.to("load")
