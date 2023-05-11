from .game_state import GameState
from ..config import load_idle_animation, BUTTON_DEFAULT, DIALOGUE_SMALL, TEXT_LARGE
from core import get_image, get_sprites, get_all_sprites, SOUND_PLAYER
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Button, Idle, DialogueBox
from gui.commands import MoveCommand
from gui.utils import DialogueData


class Tutorial(GameState):
    """Teaching the player the basic mechanics."""

    def __init__(self):
        super().__init__()
        self.damage = 0
        self.aaron_display = Idle(get_all_sprites("aaron"), (0, 0), None, load_idle_animation("aaron"))
        self.damage_display = PTexts([get_image("black")], (0, 350), TEXT_LARGE, [(0, 0)], True)
        self.dice_display = [Idle(get_sprites("basic1"), (220, 260), None, load_idle_animation("square")),
                             Idle(get_sprites("basic2"), (320, 260), None, load_idle_animation("square")),
                             Idle(get_sprites("basic3"), (420, 260), None, load_idle_animation("square")),
                             Idle(get_sprites("basic4"), (520, 260), None, load_idle_animation("square"))]
        self.dialogue_box = DialogueBox([get_image("text_box_small")], (150, 450), DIALOGUE_SMALL,
                                        lambda: self.to("player_menu"), self.load_tutorial_dialogue())

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([get_image("tall_squares")], (0, 2), (800, 600)), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")
        self.canvas.add_element(self.dialogue_box, "")
        self.dialogue_box.reset_scripts()
        self.canvas.add_element(self.aaron_display, "")
        self.aaron_display.set_position((-200, 450))
        self.canvas.add_element(self.damage_display, "")
        self.damage_display.set_text(0, "")

    def setup_commands(self):
        self.command_queue.add([MoveCommand(self.aaron_display, (5, 0), (-200, 450), (30, 450),
                                            self.dialogue_box.toggle_visibility)])

    def reset_state(self):
        self.damage = 0

    def setup_music(self):
        SOUND_PLAYER.change_music("trittle")

    def load_tutorial_dialogue(self) -> DialogueData:
        """Loads the dialogue for the tutorial"""
        texts = ["Hello.", "Welcome to the tutorial!", "Let's teach you stuff!", "See this thingy?",
                 "You interact with this to fight!", "These are your dice.", "These are your stats.",
                 "So how do you play?", "By clicking on dice!", "You roll dice by clicking on it.",
                 "Rolling dice adds damage.", "And best of all...", "when you roll all your dice...",
                 "you get to roll again for more pain!", "When you're done building damage", "click this nifty button",
                 "to end your turn and hurt your foes!", "Your enemy's health gets decreased",
                 "by the damage you have accumulated", "during your turn.", "Beware...", "if you roll a one",
                 "all your damage becomes zero", "and your turn immediately ends!", "That's all there is to it!",
                 "Good luck!"]
        portrait_seq = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                        (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                        (0, 0), (0, 0)]
        portraits = [get_all_sprites("aaron_icons")]
        hooks = [None, None, lambda: self.show_hud_element(True), None, lambda: self.show_icon((365, 175), "arrow_down"),
                 lambda: self.show_icon((35, 190), "arrow_down"), self.hide_hud_element, self.show_dice,
                 lambda: self.click_dice(0, 1), lambda: self.click_dice(1, 3), lambda: self.click_dice(2, 4),
                 lambda: self.click_dice(3, 5), self.reset_dice, self.hide_hud_element, lambda: self.show_hud_element(False),
                 None, None, None, self.hide_hud_element, self.show_dice, lambda: self.click_dice(0, 0), None,
                 self.hide_hud_element, None, None, None]
        return DialogueData(texts, portraits, portrait_seq, hooks)

    def update_damage(self, amount: int):
        """Increments damage and updates the display."""
        self.damage += amount
        self.damage_display.set_text(0, f"DMG: {self.damage}")

    def zero_damage(self):
        """Zeroes the damage and updates the display."""
        self.damage = 0
        self.damage_display.set_text(0, f"DMG: {self.damage}")

    def show_icon(self, pos: tuple[int, int], icon: str):
        """Shows a small icon in group 2."""
        self.canvas.delete_group("icon")
        self.canvas.add_element(StaticBG([get_image(icon)], pos), "icon")

    def show_hud_element(self, example: bool):
        """Shows a hud element in group 1."""
        SOUND_PLAYER.play_sfx("good")
        element = StaticBG([get_image("example_hud")], (0, 0)) if example else \
            Button(get_sprites("attack"), (305, 290), BUTTON_DEFAULT, lambda: "o")
        self.canvas.add_element(element, "hud")

    def hide_hud_element(self):
        """Hides the hud element and the icon."""
        SOUND_PLAYER.play_sfx("one")
        self.canvas.delete_group("hud")
        self.canvas.delete_group("icon")

    def show_dice(self):
        """Shows the die displays."""
        SOUND_PLAYER.play_sfx("roll")
        self.damage_display.set_text(0, "DMG: {0}".format(self.damage))
        for die_display in self.dice_display:
            self.canvas.add_element(die_display, "hud")

    def click_dice(self, i: int, side: int):
        """Simulates clicking the ith dice and rolls it on side."""
        if side != 0:
            SOUND_PLAYER.play_sfx("roll")
            self.update_damage(side + 1)
        else:
            SOUND_PLAYER.play_sfx("one")
            self.zero_damage()
        self.dice_display[i].set_idle(False)
        self.dice_display[i].set_image(side)
        pos = self.dice_display[i].get_position()
        self.show_icon((pos[0] + 60, pos[1] + 60), "mouse")

    def reset_dice(self):
        """Resets the dice displays to be rolling."""
        self.canvas.delete_group("icon")
        SOUND_PLAYER.play_sfx("good")
        for die_display in self.dice_display:
            die_display.set_idle(True)
