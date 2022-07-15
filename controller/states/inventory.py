from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_font, load_sound, load_idle_animation, create_die
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button


class Inventory(State):
    """Where the player can change up their dice set and view their inventory of dice."""

    dice_per_page = 12
    dice_per_set = 4

    def __init__(self):
        super().__init__()
        self.page_start = 0
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
        self.info_display.set_text(0, "")
        self.canvas.add_element(self.stash_display, 0)

        self.add_set_to_canvas()
        self.add_inventory_to_canvas()

    def setup_music(self):
        music_handler.change(load_sound("note", False))

    def reset_state(self):
        self.page_start = 0
        self.selected_index, self.in_set = -1, False

    def update_components(self):
        self.info_display.set_text(1, "Page {0}".format((self.page_start // self.dice_per_page) + 1))
        self.stash_display.set_texts(["{0} Dice".format(len(self.player.get_inventory())),
                                      "{0} G".format(self.player.get_money())])

    def add_set_to_canvas(self):
        """Adds dice from your set to the canvas."""
        for i, die_name in enumerate(self.player.get_preference()):
            die_display = Idle(load_some_sprites(die_name), (208 + (i * 100), 75), lambda x=i: self.select(x, True),
                               load_idle_animation("square"))
            die_display.set_idle(False)
            self.canvas.add_element(die_display, 1)

    def add_set_buttons_to_canvas(self):
        """Make the unequip button appear."""
        if self.selected_index != 0:
            self.canvas.add_element(Button(load_some_sprites("unequip"), (105, 200), BUTTON_DEFAULT, self.unequip), 3)
        self.canvas.add_element(Button(load_some_sprites("cancel"), (105, 280), BUTTON_DEFAULT, self.deselect), 3)

    def add_inventory_to_canvas(self):
        """Adds inventory dice to the canvas."""
        i, inventory = self.page_start, self.player.get_inventory()
        for row in range(3):
            for col in range(4):
                if i >= len(inventory):
                    return
                die_display = Idle(load_some_sprites(inventory[i]), (205 + (100 * col), 270 + (100 * row)),
                                   lambda x=i: self.select(x, False), load_idle_animation("square"))
                die_display.set_idle(False)
                self.canvas.add_element(die_display, 2)
                i += 1

    def add_inventory_buttons_to_canvas(self):
        """Make the inventory die buttons appear."""
        if len(self.player.get_preference()) < self.dice_per_set:
            self.canvas.add_element(Button(load_some_sprites("equip"), (105, 280), BUTTON_DEFAULT, self.equip), 3)
        self.canvas.add_element(Button(load_some_sprites("sell"), (105, 200), BUTTON_DEFAULT, self.sell), 3)
        self.canvas.add_element(Button(load_some_sprites("cancel"), (105, 360), BUTTON_DEFAULT, self.deselect), 3)

    def refresh_display(self):
        """Refreshes the inventory display to reflect inventory changes."""
        self.deselect()
        self.canvas.delete_group(1)
        self.add_set_to_canvas()
        self.canvas.delete_group(2)
        self.add_inventory_to_canvas()

    def show_die_info(self):
        """Shows the currently selected die's info."""
        dice_names = self.player.get_preference() if self.in_set else self.player.get_inventory()
        die = create_die(dice_names[self.selected_index])
        self.info_display.set_text(0, "{0} worth {1}".format(die.get_name(), die.get_sell_price()))

    def show_die_animated(self, selected: bool):
        """Toggles the selected die's animation."""
        if self.selected_index == -1:
            return
        dice_display = self.canvas.get_group(1) if self.in_set else self.canvas.get_group(2)
        dice_display[self.selected_index % self.dice_per_page].set_idle(selected)

    def select(self, index: int, in_set: bool):
        """Selects a die and shows die-related buttons."""
        self.deselect()
        self.selected_index, self.in_set = index, in_set
        self.add_set_buttons_to_canvas() if in_set else self.add_inventory_buttons_to_canvas()
        self.show_die_info()
        self.show_die_animated(True)

    def deselect(self):
        """Deselects a die and deletes die-related buttons."""
        self.canvas.delete_group(3)
        self.info_display.set_text(0, "")
        self.show_die_animated(False)
        self.selected_index, self.in_set = -1, False

    def equip(self):
        """Equips the selected die from the inventory."""
        self.player.append_to_preference(self.player.remove_inventory(self.selected_index))
        self.refresh_display()
        self.pg_reset()

    def unequip(self):
        """Unequips the selected die."""
        self.player.append_to_inventory(self.player.remove_preference(self.selected_index))
        self.refresh_display()

    def sell(self):
        """Sells the selected die."""
        dice = self.player.get_preference() if self.in_set else self.player.get_inventory()
        die = create_die(dice[self.selected_index])
        self.player.remove_inventory(self.selected_index)
        self.player.add_money(die.get_sell_price())
        self.refresh_display()
        self.pg_reset()

    def pg_left(self):
        """Go back a page."""
        if self.page_start > 0:
            self.page_start -= self.dice_per_page
            self.refresh_display()

    def pg_right(self):
        """Go to the next page."""
        if len(self.player.get_inventory()) > self.page_start + self.dice_per_page:
            self.page_start += self.dice_per_page
            self.refresh_display()

    def pg_reset(self):
        """Scrolls left if the page is empty."""
        if len(self.player.get_inventory()) <= self.page_start:
            self.pg_left()
