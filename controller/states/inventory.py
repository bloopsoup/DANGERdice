from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_font, load_sound, load_idle_animation
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PositionedTexts, Idle, Button


class Inventory(State):
    """Where the player can change up their dice set and view their inventory of dice."""

    def __init__(self):
        super().__init__()
        self.reference_index = 0
        self.info_display = PositionedTexts([load_static("black")], (0, 0), load_font("M"), 2,
                                            [(0, 10), (0, 560)], True)
        self.stash_display = PositionedTexts([load_static("black")], (0, 0), load_font("S"), 2,
                                             [(100, 100), (610, 100)], False)

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

    def add_dice_to_canvas(self):
        """Adds dice from your set to the canvas."""
        for i, die in enumerate(self.player.get_preference()):
            die_display = Idle(load_some_sprites(die), (208 + (i * 100), 75), None, load_idle_animation("square"))
            die_display.set_idle(False)
            self.canvas.add_element(die_display, 1)

    def add_inventory_to_canvas(self):
        """Adds inventory dice to the canvas."""
        indices, i = range(self.reference_index, len(self.player.get_inventory_all())), 0
        for row in range(3):
            for col in range(4):
                die_display = Idle(load_some_sprites(self.player.get_inventory(indices[i])),
                                   (205 + (100 * col), 270 + (100 * row)), None, load_idle_animation("square"))
                die_display.set_idle(False)
                self.canvas.add_element(die_display, 2)
                i += 1

    def add_inventory_buttons_to_canvas(self):
        """Make the inventory die buttons appear."""
        self.canvas.add_element(Button(load_some_sprites("delete"), (105, 200), BUTTON_DEFAULT, print), 3)
        self.canvas.add_element(Button(load_some_sprites("equip"), (105, 280), BUTTON_DEFAULT, print), 3)
        self.canvas.add_element(Button(load_some_sprites("cancel"), (105, 360), BUTTON_DEFAULT, print), 3)

    def add_set_buttons_to_canvas(self):
        """Make the unequip button appear."""
        self.canvas.add_element(Button(load_some_sprites("unequip"), (105, 200), BUTTON_DEFAULT, print), 3)
        self.canvas.add_element(Button(load_some_sprites("cancel"), (105, 280), BUTTON_DEFAULT, print), 3)

    def empty_page(self):
        """Scrolls left if the current page is empty."""
        if len(self.player.get_inventory_all()) <= self.reference_index:
            self.pg_left()

    def pg_left(self):
        """Scroll to the left to go back a page."""
        if self.reference_index > 0:
            self.reference_index -= 12

    def pg_right(self):
        """Scroll to the right to reveal more dice from your inventory."""
        if len(self.player.inventory) > self.reference_index + 12:
            self.reference_index += 12
