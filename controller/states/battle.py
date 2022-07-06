import pygame
from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound, load_idle_animation, \
    create_dice_set, create_enemy
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button
from gui.commands import TimerCommand, MoveCommand


class Battle(State):
    """Battle enemies, get hurt, and earn loot."""

    def __init__(self, enemy_name: str, tier: int):
        super().__init__()
        self.your_turn = True

        self.enemy = create_enemy(enemy_name, tier)

        self.player_set = create_dice_set(self.player.get_preference())
        self.enemy_set = create_dice_set(self.enemy.get_preference())

        self.player_display = Idle(load_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.enemy_display = Idle(load_all_sprites(enemy_name), (0, 0), None, load_idle_animation(enemy_name))
        self.damage_display = PTexts([load_static("black")], (0, 0), load_font("SS"), 2, [(50, 435), (370, 435)], False)
        self.reward_display = PTexts([load_static("black")], (0, 0), load_font("M"), 1, [(0, 100)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("hills")], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_static("thick_clouds")], (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("player_hud")], (0, 0)), 1)

        self.canvas.add_element(self.player_display, 0)
        self.player_display.set_position(pygame.Vector2(-300, 257))
        self.canvas.add_element(self.enemy_display, 0)
        self.enemy_display.set_position(pygame.Vector2(1000, 357 - self.enemy_display.get_height()))
        self.canvas.add_element(self.damage_display, 0)
        self.damage_display.set_texts(["", "DMG: 0 PSN: 0 HEAL: 0 WKN: 1X"])
        self.canvas.add_element(self.reward_display, 0)
        self.reward_display.set_text(0, "")
        self.add_player_set_to_canvas()

        self.canvas.add_element(Button(load_some_sprites("music"), (730, 0), BUTTON_DEFAULT, music_handler.toggle), 0)
        self.canvas.add_element(Button(load_some_sprites("attack"), (580, 370), BUTTON_DEFAULT, print), 2)

    def setup_commands(self):
        enemy_destination = (740 - self.enemy_display.get_width(), 357 - self.enemy_display.get_height())
        self.command_queue.append_commands([MoveCommand(self.player_display, (10, 0), (60, 257), None),
                                            MoveCommand(self.enemy_display, (10, 0), enemy_destination, None)])

    def update_components(self):
        dice_set = self.player_set if self.your_turn else self.enemy_set
        for die_display, die in zip(self.canvas.get_group(3), dice_set.get_dice()):
            die_display.set_idle(not die.is_rolled())
            die_display.set_image(die.get_rolled())

    def add_player_set_to_canvas(self):
        """Adds a player's or enemy's dice to the canvas."""
        preference = self.player.get_preference() if self.your_turn else self.enemy.get_preference()
        x_start = 369 if self.your_turn else 33
        for i, die_name in enumerate(preference):
            die_display = Idle(load_some_sprites(die_name), (x_start + (i * 100), 455),
                               lambda: self.roll(i) if self.your_turn else None, load_idle_animation("square"))
            die_display.set_idle(True)
            self.canvas.add_element(die_display, 3)

    def roll(self, i: int):
        """Roll the player's ith die."""
        current = self.turn_player.roll_die(index)
        if current == 0:
            self.rolled_one()
        elif current is not None:
            handle_sound("roll.mp3")

    def switch(self):
        """Handles the hub and displays and also enables and disables the AI."""
        if self.turn_player == self.player:
            self.canvas.delete_group(2)
            self.canvas.add_element(StaticBG([load_img(load_s("phub0.png"))], (0, 0)), 1)
            self.player.display_mode("player")
            self.enemy.display_mode("")
            self.canvas.add_element(Butt(Control.sheets["button4"].load_some_images(0, 0, 3), (580, 370),
                                         BUTTON_DEFAULT, self.end_turn), -1)
            self.timer.deactivate()
        else:
            self.canvas.delete_group(1)
            self.canvas.add_element(StaticBG([load_img(load_s("ehub0.png"))], (0, 0)), 2)
            self.player.display_mode("")
            self.enemy.display_mode("enemy")
            self.canvas.delete_group(-1)

            self.timer.activate(1, True)
