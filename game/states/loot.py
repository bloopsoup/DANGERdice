from .game_state import GameState
from ..config import load_idle_animation, create_random_die, TEXT_MEDIUM
from core import get_image, get_all_sprites, SOUND_PLAYER
from gui.elements import StaticBG, PTexts, Idle
from gui.commands import TimerCommand, MoveCommand


class Loot(GameState):
    """A screen that can show up if the player has won a die from the previous battle."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(get_all_sprites("player"), (-300, 257), None, load_idle_animation("player"))
        self.loot_display = PTexts([get_image("black")], (0, 0), TEXT_MEDIUM, [(0, 100)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("crate")], (0, 0)), "")
        self.canvas.add_element(StaticBG([get_image("ground")], (0, 0)), "")
        self.canvas.add_element(self.player_display, "")
        self.player_display.set_position((-300, 257))
        self.canvas.add_element(self.loot_display, "")
        self.loot_display.set_text(0, "")

    def setup_commands(self):
        self.command_queue.add([MoveCommand(self.player_display, (10, 0), (-300, 257), (300, 257), None),
                                TimerCommand(1.5, self.give_loot)])
        self.command_queue.add([TimerCommand(2, lambda: self.to("player_menu"))])

    def setup_music(self):
        SOUND_PLAYER.stop_music()

    def give_loot(self):
        """Gives the player loot."""
        die = create_random_die()
        self.player.append_to_inventory(die.get_name())
        self.loot_display.set_text(0, f"You got {die.get_name()}!")
        SOUND_PLAYER.play_sfx("good")
