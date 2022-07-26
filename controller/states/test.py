from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_font
from ..themes import BUTTON_DEFAULT
from gui.elements import StaticBG, Button, Tooltip


class Test(State):
    """A minimal state to test experimental widgets and game mechanics."""

    def __init__(self):
        super().__init__()

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("yellow")], (0, 0)), 0)
        mute_button = Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle)
        self.canvas.add_element(Tooltip((730, 500), {}, load_font("SS"), "I AM A TOOLTIP", mute_button), 0)
