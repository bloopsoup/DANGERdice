import math
from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_font, load_sound, load_idle_animation, create_die
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button


class Inventory(State):
    """Where the player can change up their dice set and view their inventory of dice."""

    def __init__(self):
        super().__init__()
        self.reference_index = 0
        self.selected_index, self.in_set = -1, False
        self.info_display = PTexts([load_static("black")], (0, 0), load_font("M"), 2, [(0, 10), (0, 560)], True)
        self.stash_display = PTexts([load_static("black")], (0, 0), load_font("S"), 2, [(100, 100), (610, 100)], False)

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([load_static("tall_rectangles")], (0, -1), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_static("inventory_layout")], (0, 0)), 0)

        self.canvas.add_element(Button(load_some_sprites("back"), (0, 0), BUTTON_DEFAULT, self.back), 0)
        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), 0)
        self.canvas.add_element(Button(load_some_sprites("right_arrow"), (625, 530), BUTTON_DEFAULT, self.pg_right), 0)
        self.canvas.add_element(Button(load_some_sprites("left_arrow"), (105, 530), BUTTON_DEFAULT, self.pg_left), 0)
        self.canvas.add_element(self.info_display, 0)
        self.canvas.add_element(self.stash_display, 0)

        self.add_dice_to_canvas()
        self.add_inventory_to_canvas()

    def startup(self):
        self.setup_canvas()
        music_handler.change(load_sound("note", False))

    def update_components(self):
        self.info_display.set_text(1, "Page {0}".format(max(1, math.ceil(self.reference_index // 12))))
        self.stash_display.set_texts(["{0} Dice".format(len(self.player.get_inventory())),
                                      "{0} Gold".format(self.player.get_money())])

    def add_dice_to_canvas(self):
        """Adds dice from your set to the canvas."""
        for i, die in enumerate(self.player.get_preference()):
            die_display = Idle(load_some_sprites(die), (208 + (i * 100), 75),
                               lambda x=i: self.select(x, True), load_idle_animation("square"))
            die_display.set_idle(False)
            self.canvas.add_element(die_display, 1)

    def add_inventory_to_canvas(self):
        """Adds inventory dice to the canvas."""
        inventory = self.player.get_inventory()
        if not len(inventory):
            return

        i, indices = 0, range(self.reference_index, len(inventory))
        for row in range(3):
            for col in range(4):
                die_display = Idle(load_some_sprites(inventory[indices[i]]), (205 + (100 * col), 270 + (100 * row)),
                                   lambda x=i: self.select(x, False), load_idle_animation("square"))
                die_display.set_idle(False)
                self.canvas.add_element(die_display, 2)
                i += 1

    def add_inventory_buttons_to_canvas(self):
        """Make the inventory die buttons appear."""
        self.canvas.add_element(Button(load_some_sprites("sell"), (105, 200), BUTTON_DEFAULT, print), 3)
        self.canvas.add_element(Button(load_some_sprites("equip"), (105, 280), BUTTON_DEFAULT, print), 3)
        self.canvas.add_element(Button(load_some_sprites("cancel"), (105, 360), BUTTON_DEFAULT, self.deselect), 3)

    def add_set_buttons_to_canvas(self):
        """Make the unequip button appear."""
        self.canvas.add_element(Button(load_some_sprites("unequip"), (105, 200), BUTTON_DEFAULT, print), 3)
        self.canvas.add_element(Button(load_some_sprites("cancel"), (105, 280), BUTTON_DEFAULT, self.deselect), 3)

    def show_die_info(self):
        """Shows the currently selected die's info."""
        lst = self.player.get_preference() if self.in_set else self.player.get_inventory()
        die = create_die(lst[self.selected_index])
        self.info_display.set_text(0, "{0} worth {1}".format(die.get_name(), die.get_price()))

    def select(self, index: int, in_set: bool):
        """Selects a die and shows die-related buttons."""
        self.deselect()
        self.selected_index, self.in_set = index, in_set
        self.add_set_buttons_to_canvas() if in_set else self.add_inventory_buttons_to_canvas()
        self.show_die_info()

    def deselect(self):
        """Deselects a die and deletes die-related buttons."""
        self.selected_index, self.in_set = -1, False
        self.canvas.delete_group(3)
        self.info_display.set_text(0, "")

    def pg_left(self):
        """Scroll to the left to go back a page."""
        if self.reference_index > 0:
            self.reference_index -= 12

    def pg_right(self):
        """Scroll to the right to reveal more dice from your inventory."""
        if len(self.player.get_inventory()) > self.reference_index + 12:
            self.reference_index += 12

    def empty_page(self):
        """Scrolls left if the current page is empty."""
        if len(self.player.get_inventory()) <= self.reference_index:
            self.pg_left()
