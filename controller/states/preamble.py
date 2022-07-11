import pygame
from .state import State
from ..loader import load_static, load_all_sprites, load_font, load_idle_animation, load_dialogue
from ..themes import DIALOGUE_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, Idle, DialogueBox
from gui.commands import AnimationHandler


class Preamble(State):
    """Sometimes you have a chit-chat before battle."""

    def __init__(self, enemy_name: str):
        super().__init__()
        self.player_display = Idle(load_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.enemy_display = Idle(load_all_sprites(enemy_name), (0, 0), None, load_idle_animation(enemy_name))
        self.animation_handler = AnimationHandler(self.player_display, (60, 257), self.enemy_display, (
            740 - self.enemy_display.get_width(), 357 - self.enemy_display.get_height()), self.command_queue)
        self.dialogue_box = DialogueBox([load_static("text_box")], (100, 350), DIALOGUE_DEFAULT,
                                        lambda: self.to("player_menu"), load_font("M"), load_dialogue(enemy_name))

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("hills")], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_static("thick_clouds")], (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("ground")], (0, 0)), 0)
        self.canvas.add_element(self.player_display, 0)
        self.player_display.set_position(pygame.Vector2(-300, 257))
        self.canvas.add_element(self.enemy_display, 0)
        self.enemy_display.set_position(pygame.Vector2(1000, 357 - self.enemy_display.get_height()))
        self.canvas.add_element(self.dialogue_box, 0)

    def setup_commands(self):
        self.animation_handler.to_start(lambda: self.dialogue_box.toggle_visibility())
