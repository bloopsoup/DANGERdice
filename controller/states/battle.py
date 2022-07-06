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
        self.add_player_set_to_canvas(True)

        self.canvas.add_element(Button(load_some_sprites("music"), (730, 0), BUTTON_DEFAULT, music_handler.toggle), 0)
        self.canvas.add_element(Button(load_some_sprites("attack"), (580, 370), BUTTON_DEFAULT, self.end_turn), 2)

    def setup_commands(self):
        enemy_destination = (740 - self.enemy_display.get_width(), 357 - self.enemy_display.get_height())
        self.command_queue.append_commands([MoveCommand(self.player_display, (10, 0), (60, 257), None),
                                            MoveCommand(self.enemy_display, (10, 0), enemy_destination, None)])

    def update_components(self):
        dice_set = self.player_set if self.your_turn else self.enemy_set
        for die_display, die in zip(self.canvas.get_group(3), dice_set.get_dice()):
            die_display.set_idle(die.is_rolled())

    def add_player_set_to_canvas(self, player: bool):
        """Adds a player's or enemy's dice to the canvas."""
        preference = self.player.get_preference() if player else self.enemy.get_preference()
        x_start = 369 if player else 33
        for i, die_name in enumerate(preference):
            die_display = Idle(load_some_sprites(die_name), (x_start + (i * 100), 455), None,
                               load_idle_animation("square"))
            die_display.set_idle(True)
            self.canvas.add_element(die_display, 3)

    def roll(self, index):
        """Roll the player's ith die."""

        current = self.turn_player.roll_die(index)
        if current == 0:
            # If there is another popup, remove it and flash the ONE
            if self.flash != 0:
                self.canvas.delete_group(self.flash)
            self.popup_one()

            self.damage = 0
            self.poison_damage = 0
            self.heal_value = 0
            self.weaken_attack = 1

            self.rolled_one()
        elif current is not None:
            # Play the successful roll sound
            handle_sound("roll.mp3")

            # Since battling and Die types are separate, special dice effects are checked here
            if isinstance(self.turn_player.dice_set[index], Poison):
                self.poison_damage += current
            elif isinstance(self.turn_player.dice_set[index], Heal):
                handle_sound("heal.mp3")
                self.heal_value += current
            elif isinstance(self.turn_player.dice_set[index], Divider):
                self.weaken_attack = current
            elif isinstance(self.turn_player.dice_set[index], Multiplier):
                self.damage *= current
            else:
                self.damage += current

    def end_turn(self):
        """Function that's called when the player wants to end their turn."""
        if not self.can_end_turn or not self.active_dice:
            return

        if self.damage or self.poison_damage or self.weaken_attack > 1:
            self.trigger_anim("rush", 3)
        elif self.heal_value:
            self.rolled_one()

    def rolled_one(self):
        """Facilitates the turn switching by applying damage and then
           updating HUB and AI with process_status()."""
        self.active_dice = False

        # Apply divider
        self.damage //= self.turn_player.divided
        self.turn_player.divided = 1

        # Get rid of blessed status
        self.turn_player.blessed = 0

        # Deduct health from the other side
        if self.turn_player == self.player:
            self.enemy.current -= self.damage
            self.enemy.poison += self.poison_damage
            self.enemy.divided = self.weaken_attack
        else:
            self.player.current -= self.damage
            self.player.poison += self.poison_damage
            self.player.divided = self.weaken_attack

        # Healing
        self.turn_player.current = min(self.turn_player.health, self.turn_player.current + self.heal_value)
        self.turn_player.poison = max(0, self.turn_player.poison - self.heal_value)

    def next_turn(self):
        """Switches the player's turn."""
        if self.turn_player == self.player:
            self.turn_player = self.enemy
        else:
            self.turn_player = self.player

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

            # A little rigging
            self.turn_player.blessed = random.randint(1, 4)
        else:
            self.canvas.delete_group(1)
            self.canvas.add_element(StaticBG([load_img(load_s("ehub0.png"))], (0, 0)), 2)
            self.player.display_mode("")
            self.enemy.display_mode("enemy")
            self.canvas.delete_group(-1)

            self.timer.activate(1, True)

    def handle_dying(self):
        """Handles who dies during turns. If one kills the opposing player and will subsequently die
           from statuses themself, they will live with 1 HP with no status."""
        if self.turn_player == self.player:
            if self.enemy.current <= 0:
                self.enemy.die()
                if self.turn_player.current <= 0:
                    self.turn_player.cleanse()
                    self.turn_player.current = 1
            elif self.turn_player.current <= 0:
                self.turn_player.die()
        else:
            if self.player.current <= 0:
                self.player.die()
                if self.turn_player.current <= 0:
                    self.turn_player.cleanse()
                    self.turn_player.current = 1
            elif self.turn_player.current <= 0:
                self.turn_player.die()

    def reset_turn(self):
        """Resets damage, the leaving player's dice, and switch the turn player and hub and enable
           active dice if needed."""
        # Check for deaths
        self.handle_dying()
        self.trigger_death()

        self.damage = 0
        self.poison_damage = 0
        self.heal_value = 0
        self.weaken_attack = 1

        self.turn_player.reset_dice()
        self.next_turn()
        self.switch()
        self.active_dice = True

    def remove_popups(self):
        """Remove the current popups."""
        self.canvas.delete_group(3)
        self.canvas.delete_group(4)

    def popup_one(self):
        """Pop up the one display."""
        handle_sound("one.mp3")
        self.remove_popups()
        self.canvas.add_element(StaticBG([load_img(load_s("one.png"))], (0, 210)), 4)
        self.flash_timer.activate(0.5)
        self.flash = 4

        # For flashing the character as hurt
        self.turn_player.status(False)
        self.turn_player.image = self.turn_player.images[13]

    def popup_refresh(self):
        """Pop up the refresh display."""
        self.remove_popups()
        self.canvas.add_element(StaticBG([load_img(load_s("refresh.png"))], (0, 210)), 3)
        self.flash_timer.activate(0.5)
        self.flash = 3
