from .game_state import GameState
from ..config import create_die, load_idle_animation, BUTTON_DEFAULT, TEXT_MEDIUM
from core import get_image, get_sprites, get_all_sprites, SOUND_PLAYER
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button
from gui.commands import TimerCommand


class Shop(GameState):
    """Where the player can purchase dice."""

    def __init__(self):
        super().__init__()
        self.selected_index, self.active = -1, True
        self.keeper_display = Idle(get_all_sprites("shopkeeper"), (650, 420), None, load_idle_animation("shopkeeper"))
        self.gold_display = PTexts([get_image("black")], (0, 0), TEXT_MEDIUM, [(100, 170)], False)
        self.info_display = PTexts([get_image("black")], (0, 0), TEXT_MEDIUM, [(0, 476), (0, 544)], True)

    def setup_canvas(self):
        self.canvas.add_element(MovingBackgroundElement([get_image("tall_rectangles")], (0, -1), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("shop")], (0, 0)), "")
        self.canvas.add_element(self.gold_display, "")
        self.gold_display.set_text(0, "Gold: {0}".format(self.player.get_money()))
        self.canvas.add_element(self.info_display, "")
        self.info_display.set_texts(["", "Click on a Die you wish to purchase."])
        self.canvas.add_element(self.keeper_display, "")
        self.add_dice_to_canvas()
        self.canvas.add_element(Button(get_sprites("back"), (0, 0), BUTTON_DEFAULT, self.back), "")
        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")

    def setup_music(self):
        SOUND_PLAYER.change_music("note")

    def reset_state(self):
        self.selected_index, self.active = -1, True

    def add_dice_to_canvas(self):
        """Adds dice from the shop's inventory to the canvas. If the die was sold, replace it with a gray die."""
        for i, die_name in enumerate(self.shop_inventory.get_inventory()):
            if not len(die_name):
                die_name = "placeholder_die"
            die_display = Idle(get_sprites(die_name), (104 + (i * 253), 290), lambda x=i: self.select(x),
                               load_idle_animation("square"))
            die_display.set_idle(False)
            self.canvas.add_element(die_display, "dice")

    def add_shop_buttons_to_canvas(self):
        """Make the buttons for buying/canceling appear."""
        self.canvas.add_element(Button(get_sprites("confirm"), (320, 525), BUTTON_DEFAULT, self.buy), "buttons")
        self.canvas.add_element(Button(get_sprites("cancel"), (410, 525), BUTTON_DEFAULT, self.deselect), "buttons")

    def show_die_info(self):
        """Shows the currently selected die's info."""
        die = create_die(self.shop_inventory.get_item(self.selected_index))
        self.info_display.set_texts(["{0} costing {1} gold.".format(die.get_name(), die.get_price()), ""])

    def show_die_animated(self, selected: bool):
        """Toggles the selected die's animation."""
        if self.selected_index != -1:
            self.canvas.get_group("dice")[self.selected_index].set_idle(selected)

    def select(self, i: int):
        """Select a die. Can't select if HUD is disabled or the die is grayed out."""
        if not self.active or not len(self.shop_inventory.get_item(i)):
            return
        self.deselect()
        self.selected_index = i
        self.add_shop_buttons_to_canvas()
        self.show_die_info()
        self.show_die_animated(True)

    def deselect(self):
        """Deselects the current die."""
        self.canvas.delete_group("buttons")
        self.info_display.set_texts(["", "Click on a Die you wish to purchase."])
        self.show_die_animated(False)
        self.selected_index = -1

    def deactivate(self):
        """Deactivates the shop HUD."""
        self.active = False
        self.deselect()
        self.info_display.set_text(1, "")
        self.canvas.delete_group("dice")
        self.add_dice_to_canvas()

    def activate(self):
        """Reactivates the shop HUD."""
        self.active = True
        self.info_display.set_text(1, "Click on a Die you wish to purchase.")
        self.canvas.delete_group("notice")

    def popup_notice(self, sold: bool):
        """Pops up a notice for a short time and handles timing issues."""
        self.deactivate()
        self.canvas.add_element(StaticBG([get_image("bought" if sold else "broke")], (0, 130) if sold else (0, 0)), "notice")
        self.command_queue.add([TimerCommand(0.5, self.activate)])

    def buy(self):
        """Purchases the selected die."""
        die_name = self.shop_inventory.get_item(self.selected_index)
        die = create_die(die_name)
        if die.get_price() <= self.player.get_money():
            self.shop_inventory.consume_item(self.selected_index)
            self.player.subtract_money(die.get_price())
            self.player.append_to_inventory(die_name)
            self.gold_display.set_text(0, "Gold: {0}".format(self.player.get_money()))
            SOUND_PLAYER.play_sfx("roll")
            self.popup_notice(True)
        else:
            SOUND_PLAYER.play_sfx("one")
            self.popup_notice(False)
