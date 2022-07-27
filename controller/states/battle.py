import pygame
from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound, load_idle_animation, \
    create_dice_set, create_enemy
from ..themes import BUTTON_DEFAULT
from entities.dice import DiceSet
from entities.enemies import DamageHandler
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button, Tooltip
from gui.commands import TimerCommand, AnimationHandler


class Battle(State):
    """Battle enemies, get hurt, and earn loot."""

    def __init__(self, enemy_name: str, tier: int, destination: str):
        super().__init__()
        self.destination = destination
        self.active, self.your_turn = False, True

        self.enemy = create_enemy(enemy_name, tier)
        self.player_set = None
        self.enemy_set = create_dice_set(self.enemy.get_preference())
        self.damage_handler = DamageHandler([self.player, self.enemy])

        self.player_display = Idle(load_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.player_s_display = PTexts(load_all_sprites("player"), (0, 0), load_font("SS"), [(0, -50), (0, -25)], True)
        self.enemy_display = Idle(load_all_sprites(enemy_name), (0, 0), None, load_idle_animation(enemy_name))
        self.enemy_s_display = PTexts(load_all_sprites(enemy_name), (0, 0), load_font("SS"), [(0, -50), (0, -25)], True)
        self.animation_handler = AnimationHandler(self.player_display, (60, 257), self.enemy_display, (740 - self.enemy_display.get_width(), 357 - self.enemy_display.get_height()), self.command_queue)

        self.stat_display = PTexts([pygame.Surface((1, 1))], (38, 460), load_font("SS"), [(0, 0), (0, 20), (0, 40), (0, 60)], False)
        self.damage_display = PTexts([load_static("black")], (0, 0), load_font("SS"), [(50, 435), (370, 435)], False)
        self.reward_display = PTexts([load_static("black")], (0, 0), load_font("L"), [(0, 100)], True)

    def setup_state(self):
        self.player_set = create_dice_set(self.player.get_preference())

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
        self.animation_handler.to_start(self.enable_hud)

    def reset_state(self):
        self.active, self.your_turn = False, True
        self.damage_handler.reset()
        self.enemy.revive()
        self.enemy.restore_health()

    def update_components(self):
        self.update_set_on_canvas()
        self.update_text_on_canvas()

    def enable_hud(self):
        """Enables the HUD for interaction."""
        self.active = True

    def disable_hud(self):
        """Disables the HUD."""
        self.active = False

    def add_player_set_to_canvas(self):
        """Adds a player's or enemy's dice to the canvas."""
        self.canvas.delete_group(2)
        preference = self.player.get_preference() if self.your_turn else self.enemy.get_preference()
        x_start = 375 if self.your_turn else 40
        for i, die_name in enumerate(preference):
            die_display = Idle(load_some_sprites(die_name), (x_start + (i * 100), 460),
                               lambda x=i: self.roll(x) if self.your_turn else None, load_idle_animation("square"))
            self.canvas.add_element(die_display, 2)

    def add_status_icons_to_canvas(self):
        """Adds a player's or enemy's status icons to the canvas."""
        self.canvas.delete_group(4)
        x_start, status = 40, self.damage_handler.get_status(0 if self.your_turn else 1)
        if status.get_poison() > 0:
            poison_icon = StaticBG([load_static("poison")], (x_start, 360))
            poison_text = "{0} damage ending turn".format(status.get_poison())
            self.canvas.add_element(Tooltip((x_start + 65, 360), {}, load_font("SS"), poison_text, poison_icon), 4)
            x_start += 50
        if status.get_weaken() > 1:
            weaken_icon = StaticBG([load_static("weakened")], (x_start, 360))
            weaken_text = "Damage reduced by {0}X".format(status.get_weaken())
            self.canvas.add_element(Tooltip((x_start + 65, 360), {}, load_font("SS"), weaken_text, weaken_icon), 4)

    def switch_hud(self):
        """Switches the HUD for the turn player."""
        self.canvas.delete_group(1)
        hud = "player_hud" if self.your_turn else "enemy_hud"
        self.canvas.insert_element(StaticBG([load_static(hud)], (0, 0)), 1, 2)
        if self.your_turn:
            self.canvas.add_element(Button(load_some_sprites("attack"), (580, 370), BUTTON_DEFAULT, self.attack), 1)

        self.add_player_set_to_canvas()
        self.add_status_icons_to_canvas()

        pos = (38, 460) if self.your_turn else (450, 460)
        self.stat_display.set_position(pygame.Vector2(pos))
        new_texts = ["", str(self.damage_handler)] if self.your_turn else [str(self.damage_handler), ""]
        self.damage_display.set_texts(new_texts)

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

    def run_ai(self):
        """Enemy decides whether to roll or attack."""
        decision = self.enemy_set.basic_decide()
        self.roll(decision) if decision != -1 or not self.damage_handler.has_damage() else self.attack()

    def queue_ai_action(self):
        """If it's the enemy's turn, queue up an AI action."""
        if not self.your_turn:
            self.command_queue.add([TimerCommand(0.3, self.run_ai)])

    def popup_notice(self, notice: str, func):
        """Pops up a notice for a short time and runs func after."""
        self.disable_hud()
        self.canvas.add_element(StaticBG([load_static(notice)], (0, 210)), 3)
        self.command_queue.add([TimerCommand(0.5, func)])

    def attack(self):
        """Disables the HUD and starts the attacking animation. Can't attack with no damage."""
        if not self.active or not self.damage_handler.has_damage():
            return
        self.disable_hud()
        hooks = [lambda: music_handler.play_sfx(load_sound("charge", True)),
                 lambda: music_handler.play_sfx(load_sound("shatter", True)), self.apply_damage]
        self.animation_handler.rush(self.your_turn, hooks)

    def apply_damage(self):
        """Applies damage to the other player and then apply status damage."""
        self.damage_handler.apply_benefits(0 if self.your_turn else 1)
        self.damage_handler.apply_s_effects(0 if self.your_turn else 1)
        self.damage_handler.apply_damage(1 if self.your_turn else 0)
        self.damage_handler.reset()
        self.apply_status_damage()

    def apply_status_damage(self):
        """Applies damage to the turn player before ending the turn."""
        self.canvas.delete_group(3)
        status_idx = 0 if self.your_turn else 1
        if self.damage_handler.has_status_damage(status_idx):
            self.damage_handler.apply_s_damage(status_idx)
            music_handler.play_sfx(load_sound("poison", True))
            self.command_queue.add([TimerCommand(1, self.end_turn)])
        else:
            self.end_turn()

    def end_battle(self):
        """Ends the battle when the player wins."""
        msg = "You won!" if self.enemy.is_dead() else "Ouch."
        destination = self.destination if self.enemy.is_dead() else "game_over"
        self.reward_display.set_text(0, msg)
        music_handler.play_sfx(load_sound("good", True))
        self.player.advance_stage()
        self.command_queue.add([TimerCommand(2, lambda: self.to(destination))])

    def switch_turn(self):
        """Switches to the other player's turn."""
        self.your_turn = not self.your_turn
        self.player_set.reset_dice()
        self.enemy_set.reset_dice()
        self.damage_handler.reset()
        self.switch_hud()
        self.enable_hud()
        self.queue_ai_action()

    def direct_turn_flow(self, result: int, dice_set: DiceSet):
        """Determines what to do after rolling a die. Either you end your turn prematurely,
           reset the dice (which queues another AI action), or continue your turn normally."""
        if result != -1:
            music_handler.play_sfx(load_sound("roll", True))
        if result == 0:
            music_handler.play_sfx(load_sound("one", True))
            self.popup_notice("rolled_one", self.apply_status_damage)
        elif dice_set.needs_reset():
            music_handler.play_sfx(load_sound("good", True))
            self.popup_notice("refresh", lambda: self.reset_rolls(dice_set))
            self.queue_ai_action()
        else:
            self.queue_ai_action()

    def end_turn(self):
        """Ends the turn where the next step depends on if the other player is defeated."""
        src, target = self.player if self.your_turn else self.enemy, self.enemy if self.your_turn else self.player
        if target.is_dead():
            src.try_revive()
            self.animation_handler.scavenge(self.your_turn, self.end_battle)
        elif src.is_dead():
            self.animation_handler.scavenge(not self.your_turn, self.end_battle)
        else:
            self.switch_turn()
