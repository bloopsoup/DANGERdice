from .game_state import GameState
from ..persistent_data import PERSISTENT_DATA
from ..config import load_idle_animation, BUTTON_DEFAULT, INPUT_DEFAULT, TEXT_DEFAULT, TEXT_MEDIUM
from core import get_image, get_sprites, get_all_sprites, SOUND_PLAYER
from gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, Button, InputText
from gui.commands import MoveCommand


class Intro(GameState):
    """Screen to give your character a name."""

    def __init__(self):
        super().__init__()
        self.destination = "story"
        self.player = PERSISTENT_DATA.get_player()
        self.player_display = Idle(get_all_sprites("player"), (350, 472), None, load_idle_animation("player"))
        self.name_display = PTexts(get_all_sprites("player"), (350, 472), TEXT_DEFAULT, [(0, -25)], True)
        self.skip_display = PTexts([get_image("black")], (0, 220), TEXT_MEDIUM, [(0, 0)], True)

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("name")], (0, 0)), "")
        self.canvas.add_element(MovingBackgroundElement([get_image("thick_clouds")], (-1, 0), (800, 600)), "")

        self.canvas.add_element(self.player_display, "")
        self.player_display.set_position((350, 472))
        self.canvas.add_element(self.name_display, "")
        self.canvas.add_element(self.skip_display, "")
        self.skip_display.set_text(0, "")

        self.canvas.add_element(Button(get_sprites("music"), (730, 530), BUTTON_DEFAULT, SOUND_PLAYER.toggle_mute), "")
        self.canvas.add_element(Button(get_sprites("back"), (0, 0), BUTTON_DEFAULT, self.back), "inputs")
        i_box = InputText(get_all_sprites("input"), (100, 130), INPUT_DEFAULT, self.enter_name)
        self.canvas.add_element(i_box, "inputs")
        self.canvas.add_element(Button(get_sprites("confirm"), (700, 130), BUTTON_DEFAULT, i_box.submit_text), "inputs")
        self.canvas.add_element(Button(get_sprites("skip_tutorial"), (300, 220), BUTTON_DEFAULT, self.skip), "skip")

    def setup_music(self):
        SOUND_PLAYER.change_music("trooper")

    def cleanup(self):
        self.canvas.delete_all()
        self.destination = "story"

    def update_components(self):
        self.name_display.set_text(0, self.player.get_name())
        self.name_display.set_position(self.player_display.get_position())

    def enter_name(self, text: str):
        """Once you entered a name, gives the player that name and moves him off-screen."""
        self.canvas.delete_group("inputs")
        self.canvas.delete_group("skip")
        self.player.change_name(text)
        self.command_queue.add([MoveCommand(self.player_display, (5, 0), (350, 472), (900, 472), lambda: self.to(self.destination))])

    def skip(self):
        """Skips the story cutscene and tutorial level."""
        self.canvas.delete_group("skip")
        self.skip_display.set_text(0, "Tutorial will be skipped.")
        self.destination = "player_menu"
