from controller.states.state import *
from controller.utils.path import load_screen
from gui.themes import BUTTON_DEFAULT
from gui.canvas import Canvas
from gui.elements.moving_background import MovingBackgroundElement
from gui.elements.static_background import StaticBG
from gui.elements.button import Button as Butt


class MainMenu(State):
    """Main menu."""

    def __init__(self, bank: AssetBank):
        super().__init__(bank)

    def startup(self):
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement(load_screen("back1.png"), (0, 2), (800, 600)), 0)
        self.canvas.add_element(StaticBG(load_screen("logo.png"), (0, 0)), 0)
        self.canvas.add_element(Butt(self.bank.get_images("button2", 0, 0, 3), (0, 270), BUTTON_DEFAULT, self.intro), 0)
        self.canvas.add_element(Butt(self.bank.get_images("button2", 2, 0, 3), (0, 340), BUTTON_DEFAULT, self.load), 0)
        self.canvas.add_element(Butt(self.bank.get_images("button2", 4, 0, 3), (0, 410), BUTTON_DEFAULT,
                                     self.quit_game), 0)
        self.canvas.add_element(Butt(self.bank.get_images("button", 1, 0, 3), (730, 530), BUTTON_DEFAULT, self.test), 0)

        # Setup Player
        # self.player.change_name("")
        # self.player.direct_move(-100, -100)
        # self.player.display_mode("")

    def test(self):
        print(self.canvas)

    def intro(self):
        """Onto giving your character a name!"""
        self.to("intro")

    def load(self):
        """Go to the loading screen."""
        self.to("load")
