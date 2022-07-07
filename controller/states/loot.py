import pygame
from .state import State
from ..utils import music_handler
from ..loader import load_static, load_all_sprites, load_font, load_sound, load_idle_animation, random_die_name
from gui.elements import StaticBG, PTexts, Idle
from gui.commands import TimerCommand, MoveCommand


class Loot(State):
    """A screen that can show up if the player has won a die from the previous battle."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(load_all_sprites("player"), (-300, 257), None, load_idle_animation("player"))
        self.loot_display = PTexts([load_static("black")], (0, 0), load_font("M"), 1, [(0, 100)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("crate")], (0, 0)), 0)
        self.canvas.add_element(StaticBG([load_static("ground")], (0, 0)), 0)
        self.canvas.add_element(self.player_display, 0)
        self.player_display.set_position(pygame.Vector2(-300, 257))
        self.canvas.add_element(self.loot_display, 0)
        self.loot_display.set_text(0, "")

    def setup_commands(self):
        self.command_queue.add([MoveCommand(self.player_display, (10, 0), (-300, 257), (300, 257), None),
                                TimerCommand(1.5, self.give_loot)])
        self.command_queue.add([TimerCommand(2, lambda: self.to("player_menu"))])

    def give_loot(self):
        """Gives the player loot."""
        die_name = random_die_name()
        self.player.append_to_inventory(die_name)
        self.loot_display.set_text(0, "You got {0}!".format(die_name))
        music_handler.play_sfx(load_sound("good", True))
