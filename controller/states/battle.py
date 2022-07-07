import pygame
from .state import State
from ..utils import music_handler, DamageHandler
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound, load_idle_animation, \
    create_dice_set, create_enemy
from ..themes import BUTTON_DEFAULT
from entities.dice import DiceSet
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button
from gui.commands import TimerCommand, MoveCommand


class Battle(State):
    """Battle enemies, get hurt, and earn loot."""

    def __init__(self, enemy_name: str, tier: int):
        super().__init__()
        self.active, self.your_turn = False, True
        self.damage_handler = DamageHandler(2)

        self.enemy = create_enemy(enemy_name, tier)
        self.player_set = create_dice_set(self.player.get_preference())
        self.enemy_set = create_dice_set(self.enemy.get_preference())

        self.player_display = Idle(load_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.player_s_display = PTexts(load_all_sprites("player"), (0, 0), load_font("SS"), 2, [(0, -50), (0, -25)], True)
        self.enemy_display = Idle(load_all_sprites(enemy_name), (0, 0), None, load_idle_animation(enemy_name))
        self.enemy_s_display = PTexts(load_all_sprites(enemy_name), (0, 0), load_font("SS"), 2, [(0, -50), (0, -25)], True)
        self.stat_display = PTexts([pygame.Surface((1, 1))], (38, 460), load_font("SS"), 4, [(0, 0), (0, 20), (0, 40), (0, 60)], False)
        self.damage_display = PTexts([load_static("black")], (0, 0), load_font("SS"), 2, [(50, 435), (370, 435)], False)
        self.reward_display = PTexts([load_static("black")], (0, 0), load_font("M"), 1, [(0, 100)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("hills")], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_static("thick_clouds")], (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("player_hud")], (0, 0)), 1)

        self.canvas.add_element(self.player_display, 0)
        self.player_display.set_position(pygame.Vector2(-300, 257))
        self.canvas.add_element(self.player_s_display, 0)
        self.player_s_display.set_text(0, self.player.get_name())
        self.canvas.add_element(self.enemy_display, 0)
        self.enemy_display.set_position(pygame.Vector2(1000, 357 - self.enemy_display.get_height()))
        self.canvas.add_element(self.enemy_s_display, 0)
        self.enemy_s_display.set_text(0, self.enemy.get_name())
        self.canvas.add_element(self.stat_display, 0)
        self.canvas.add_element(self.damage_display, 0)
        self.damage_display.set_texts(["", str(self.damage_handler)])
        self.canvas.add_element(self.reward_display, 0)
        self.reward_display.set_text(0, "")

        self.canvas.add_element(Button(load_some_sprites("music"), (730, 0), BUTTON_DEFAULT, music_handler.toggle), 0)
        self.canvas.add_element(Button(load_some_sprites("attack"), (580, 370), BUTTON_DEFAULT, self.attack), 1)
        self.add_player_set_to_canvas()

    def setup_commands(self):
        enemy_pos = (740 - self.enemy_display.get_width(), 357 - self.enemy_display.get_height())
        self.command_queue.append_commands([MoveCommand(self.player_display, (10, 0), (60, 257), None),
                                            MoveCommand(self.enemy_display, (10, 0), enemy_pos, self.enable_hud)])

    def startup(self):
        self.setup_canvas()
        self.setup_commands()
        music_handler.change(load_sound("huh", False))

    def update_components(self):
        self.update_set_on_canvas()
        self.update_text_on_canvas()

    def add_player_set_to_canvas(self):
        """Adds a player's or enemy's dice to the canvas."""
        preference = self.player.get_preference() if self.your_turn else self.enemy.get_preference()
        x_start = 375 if self.your_turn else 40
        for i, die_name in enumerate(preference):
            die_display = Idle(load_some_sprites(die_name), (x_start + (i * 100), 460),
                               lambda x=i: self.roll(x) if self.your_turn else None, load_idle_animation("square"))
            self.canvas.add_element(die_display, 2)

    def update_set_on_canvas(self):
        """Updates the dice to stop animating when rolled."""
        dice_set = self.player_set if self.your_turn else self.enemy_set
        for die_display, die in zip(self.canvas.get_group(2), dice_set.get_dice()):
            die_display.set_idle(not die.is_rolled())
            if die.is_rolled():
                die_display.set_image(die.get_rolled())

    def update_text_on_canvas(self):
        """Updates the text to reflect the latest state."""
        self.player_s_display.set_position(self.player_display.get_position())
        self.player_s_display.set_text(1, "{0} HP".format(self.player.get_health()))
        self.enemy_s_display.set_position(self.enemy_display.get_position())
        self.enemy_s_display.set_text(1, "{0} HP".format(self.enemy.get_health()))
        entity = self.player if self.your_turn else self.enemy
        self.stat_display.set_texts([entity.get_name(), "LVL: {0}".format(entity.get_level()),
                                     "HP: {0} / {1}".format(entity.get_health(), entity.get_max_health()),
                                     "Gold: {0}".format(entity.get_money())])
        self.damage_display.set_text(1 if self.your_turn else 0, str(self.damage_handler))

    def enable_hud(self):
        """Enables the HUD for interaction."""
        self.active = True

    def disable_hud(self):
        """Disables the HUD."""
        self.active = False

    def switch_hud(self):
        """Switches the HUD for the turn player."""
        self.canvas.delete_group(1)
        hud = "player_hud" if self.your_turn else "enemy_hud"
        self.canvas.insert_element(StaticBG([load_static(hud)], (0, 0)), 1, 2)
        if self.your_turn:
            self.canvas.add_element(Button(load_some_sprites("attack"), (580, 370), BUTTON_DEFAULT, self.attack), 1)

        self.canvas.delete_group(2)
        self.add_player_set_to_canvas()

        pos = (38, 460) if self.your_turn else (450, 460)
        self.stat_display.set_position(pygame.Vector2(pos))
        new_texts = ["", str(self.damage_handler)] if self.your_turn else [str(self.damage_handler), ""]
        self.damage_display.set_texts(new_texts)

    def popup_notice(self, notice: str, func):
        """Pops up a notice for a short time and runs func after."""
        self.disable_hud()
        self.canvas.add_element(StaticBG([load_static(notice)], (0, 210)), 3)
        self.command_queue.append_commands([TimerCommand(0.5, func)])

    def roll(self, i: int):
        """Roll the player's ith die and update the damage handler."""
        if not self.active:
            return
        dice_set = self.player_set if self.your_turn else self.enemy_set
        amount, damage_type = dice_set.roll_die(i, False)
        self.damage_handler.add_damage(amount, damage_type)
        self.direct_turn_flow(amount, dice_set)

    def reset_rolls(self, dice_set: DiceSet):
        """Reset the rolls and removes the REFRESH display."""
        self.canvas.delete_group(3)
        dice_set.reset_dice()
        self.enable_hud()

    def direct_turn_flow(self, result: int, dice_set: DiceSet):
        """Determines what to do after rolling a die. Either you end your turn prematurely,
           reset the dice (which queues another AI action), or continue your turn normally."""
        if result != -1:
            music_handler.play_sfx(load_sound("roll", True))
        if result == 0:
            music_handler.play_sfx(load_sound("one", True))
            self.popup_notice("rolled_one", self.end_turn)
        elif dice_set.needs_reset():
            music_handler.play_sfx(load_sound("good", True))
            self.popup_notice("refresh", lambda: self.reset_rolls(dice_set))
            self.queue_ai_action()
        else:
            self.queue_ai_action()

    def run_ai(self):
        """Enemy decides whether to roll or attack."""
        decision = self.enemy_set.basic_decide()
        self.roll(decision) if decision != -1 else self.attack()

    def queue_ai_action(self):
        """If it's the enemy's turn, queue up an AI action."""
        if not self.your_turn:
            self.command_queue.append_commands([TimerCommand(0.3, self.run_ai)])

    def attack(self):
        """Applies damage to the other player."""
        self.disable_hud()
        self.damage_handler.apply_damage(self.enemy if self.your_turn else self.player, 1 if self.your_turn else 0)
        self.end_turn()

    def end_turn(self):
        """Switches to the other player's turn."""
        self.disable_hud()
        self.your_turn = not self.your_turn
        self.player_set.reset_dice()
        self.enemy_set.reset_dice()
        self.damage_handler.reset()
        self.canvas.delete_group(3)
        self.switch_hud()
        self.enable_hud()
        self.queue_ai_action()
