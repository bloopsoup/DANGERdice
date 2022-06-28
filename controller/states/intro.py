from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound, load_idle_animation
from ..themes import BUTTON_DEFAULT, INPUT_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PositionedTexts, Idle, Button, InputText
from gui.commands import MoveCommand


class Intro(State):
    """Screen to give your character a name."""

    def __init__(self):
        super().__init__()
        self.name_display = PositionedTexts(load_all_sprites("player"), (350, 472), load_font("L"), 1, [(0, 0)], True)
        self.player_display = Idle(load_all_sprites("player"), (350, 472), load_idle_animation("player"))
        self.tutorial_display = PositionedTexts([load_static("black")], (0, 220), load_font("L"), 1, [(0, 0)], True)
        self.setup_canvas()

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("name")], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_static("thick_clouds")], (-1, 0), (800, 600)), 0)

        self.canvas.add_element(self.tutorial_display, 0)
        self.canvas.add_element(self.name_display, 0)
        self.canvas.add_element(self.player_display, 0)

        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), 0)
        i_box = InputText(load_all_sprites("input"), (0, 200), INPUT_DEFAULT, self.enter_name, load_font("L"))
        self.canvas.add_element(i_box, 1)
        self.canvas.add_element(Button(load_some_sprites("skip_tutorial"), (0, 300), BUTTON_DEFAULT, self.skip), 2)
        self.canvas.add_element(Button(load_some_sprites("back"), (0, 0), BUTTON_DEFAULT, self.back), 1)
        self.canvas.add_element(Button(load_some_sprites("confirm"), (700, 130), BUTTON_DEFAULT, i_box.submit_text), 1)

    def startup(self):
        music_handler.change(load_sound("trooper", False))

    def reset_canvas(self):
        pass

    def back(self):
        """Goes back to the previous state. Restores player settings to enable story."""
        pass

    def enter_name(self, text):
        """Once you entered a name, gives the player that name and moves him off-screen."""
        self.canvas.delete_group(1)
        self.canvas.delete_group(2)

        self.player.change_name(text)
        self.name_display.set_text(0, text)

        self.command_queue.append_commands(
            [MoveCommand(self.player_display, (5, 0), (900, 472), lambda: self.to("main_menu"))])

    def skip(self):
        """Skips the story cutscene and tutorial level."""
        self.canvas.delete_group(2)
        self.tutorial_display.set_text(0, "Tutorial will be skipped.")
