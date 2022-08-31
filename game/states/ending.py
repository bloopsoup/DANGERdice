from .game_state import GameState
from ..config import load_idle_animation, create_player, create_shop_inventory, TEXT_WHITE_LARGE
from core import get_image, get_all_sprites, SOUND_PLAYER
from gui.elements import StaticBG, PTexts, Idle
from gui.commands import TimerCommand, MoveCommand


class Ending(GameState):
    """The ending sequence."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(get_all_sprites("player"), (-100, 472), None, load_idle_animation("player"))
        self.text_display = PTexts([get_image("black")], (0, 220), TEXT_WHITE_LARGE, [(0, 0)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("black")], (0, 0)), "")
        self.canvas.add_element(self.text_display, "")
        self.text_display.set_text(0, "AND AFTER THAT FIGHT")
        self.canvas.add_element(self.player_display, "")
        self.player_display.set_position((-100, 472))

    def setup_commands(self):
        self.command_queue.add([TimerCommand(2, lambda: self.change_text("YOU FOUND A LOT OF MONEY")),
                                MoveCommand(self.player_display, (10, 0), (-100, 472), (1000, 472), None)])
        self.command_queue.add([TimerCommand(1.5, lambda: self.change_text("IN THE MOUNTAINS"))])
        self.command_queue.add([TimerCommand(2, lambda: self.change_text("DEBTS HAVE BEEN REPAID"))])
        self.command_queue.add([TimerCommand(1.5, lambda: self.change_text("HAPPY END"))])
        self.command_queue.add([TimerCommand(1.5, self.return_to_menu)])

    def setup_music(self):
        SOUND_PLAYER.play_sfx("one")

    def change_text(self, text: str):
        """Changes the display text while playing a sound."""
        self.text_display.set_text(0, text)
        SOUND_PLAYER.play_sfx("one")

    def return_to_menu(self):
        """Goes back to the main menu and resets the stats."""
        GameState.player = create_player()
        GameState.shop_inventory = create_shop_inventory()
        self.to("main_menu")