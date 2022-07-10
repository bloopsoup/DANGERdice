import pygame
from .state import State
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound, load_idle_animation
from gui.elements import StaticBG, MovingBackgroundElement, Idle
from gui.commands import AnimationHandler


class Preamble(State):
    """Sometimes you have a chit-chat before battle."""

    def __init__(self, enemy_name: str):
        super().__init__()
        self.player_display = Idle(load_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.enemy_display = Idle(load_all_sprites(enemy_name), (0, 0), None, load_idle_animation(enemy_name))
        self.animation_handler = AnimationHandler(self.player_display, (60, 257), self.enemy_display, (
            740 - self.enemy_display.get_width(), 357 - self.enemy_display.get_height()), self.command_queue)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("hills")], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_static("thick_clouds")], (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("ground")], (0, 0)), 0)

        self.canvas.add_element(self.player_display, 0)
        self.player_display.set_position(pygame.Vector2(-300, 257))
        self.canvas.add_element(self.enemy_display, 0)
        self.enemy_display.set_position(pygame.Vector2(1000, 357 - self.enemy_display.get_height()))

    def setup_commands(self):
        self.animation_handler.to_start(print)
