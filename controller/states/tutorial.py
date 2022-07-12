from .battle import Battle
from ..loader import load_static, load_all_sprites, load_font
from ..themes import DIALOGUE_SMALL
from gui.elements import StaticBG, DialogueBox
from gui.utils import DialogueData

order = [5, 3, 2, 1, 3, 3, 3, 0, 2, 3, 5]


class Tutorial(Battle):
    """A more restricted version of Battle with the aim of teaching the player the basic mechanics."""

    def __init__(self):
        super().__init__("aaron", 0)
        self.allowed_index, self.die_outcome = -1, -1
        self.dialogue_box = DialogueBox([load_static("text_box_small")], (100, 0), DIALOGUE_SMALL, None, load_font("L"),
                                        self.load_tutorial_dialogue())

    def setup_canvas(self):
        super().setup_canvas()
        self.canvas.add_element(self.dialogue_box, 0)

    def setup_commands(self):
        self.animation_handler.to_start(self.start_tutorial)

    def enable_hud(self):
        self.active = True
        self.allowed_index, self.die_outcome = 0, order.pop(0)

    def roll(self, i: int):
        if not self.active or i != self.allowed_index:
            return
        dice_set = self.player_set if self.your_turn else self.enemy_set
        amount, damage_type = dice_set.roll_die_forced(i, self.die_outcome)
        self.damage_handler.add_damage(amount, damage_type)
        self.direct_turn_flow(amount, dice_set)

    def run_ai(self):
        decision = 0
        self.roll(decision) if decision != -1 or not self.damage_handler.has_damage() else self.attack()

    def load_tutorial_dialogue(self) -> DialogueData:
        """Loads the dialogue for the tutorial"""
        texts = ["Here's you.", "Here's the enemy.", "Right now it's your turn.", "Click on the first die to roll it.",
                 "Rolling dice builds up damage.", "Roll the other die.", "Let's attack to unleash that damage!",
                 "Now it's the enemy's turn.", "You can roll as much dice as you want",
                 "in order to keep building damage.", "but rolling a ONE forfeits your turn.",
                 "So don't get too greedy.", "Time to finish him. Keep rolling!", "Destroy him."]
        portrait_seq = [(0, 1), (0, 3), (0, 0), (0, 2), (0, 0), (0, 0), (0, 2), (0, 3), (0, 0), (0, 7), (0, 5), (0, 1),
                        (0, 2), (0, 4)]
        portraits = [load_all_sprites("aaron_icons")]
        hooks = [lambda: self.display_arrow((620, 87)), lambda: self.canvas.delete_group(4), self.hand_off, None,
                 None, None, None,
                 None, None,
                 None, None,
                 None, None, None]
        return DialogueData(texts, portraits, portrait_seq, hooks)

    def display_arrow(self, pos: tuple[float, float]):
        """Displays an arrow at POS."""
        self.canvas.delete_group(4)
        self.canvas.add_element(StaticBG([load_static("arrow_down")], pos), 4)

    def start_tutorial(self):
        self.display_arrow((60, 107))
        self.dialogue_box.toggle_visibility()

    def hand_off(self):
        self.display_arrow((370, 330))
        self.dialogue_box.toggle_visibility()
        self.enable_hud()

    def tutorial_sequence(self):
        if self.step == 4:
            self.canvas.delete_group(10)
            self.menu.do_dialogue_id(2, 2)
            self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                 self.next_dialogue, 3, Button, (630, 0))

            self.active_dice = False
        elif self.step == 5:
            self.canvas.add_element(StaticBG([load_img(load_s("arrowdown.png"))], (470, 330)), 10)
            self.menu.delete_widget(3)

            self.active_dice = True
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 6:
            self.canvas.delete_group(10)
            self.menu.do_dialogue_id(2, 2)

            self.allowed = -1
            self.can_end_turn = True
        elif self.step == 7:
            self.menu.do_dialogue_id(2, 2)
            self.can_end_turn = False
        elif self.step == 8:
            self.can_refresh = True
            self.active_dice = True
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 9:
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 10:
            self.menu.do_dialogue_id(2, 2)
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 11:
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 12:
            self.menu.do_dialogue_id(2, 2)
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 13:
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 14:
            self.menu.do_dialogue_id(2, 2)
            self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                 self.next_dialogue, 3, Button, (630, 0))
        elif self.step == 16:
            self.menu.delete_widget(3)
            self.active_dice = True
            self.allowed = None
            self.fixed = self.order.pop(0)
        elif self.step == 17:
            self.fixed = self.order.pop(0)
        elif self.step == 18:
            self.fixed = self.order.pop(0)
        elif self.step == 19:
            self.menu.do_dialogue_id(2, 2)
            self.can_end_turn = True
