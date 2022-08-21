import pyglet
from control import Control
from core.state import State, StateManager


def load_fonts():
    """Loads the fonts for pyglet."""
    pyglet.font.add_file('../../assets/VT323-Regular.ttf')


def run():
    """Starts running the game."""
    load_fonts()
    controller = Control(StateManager("attributions", {"attributions": State()}))
    pyglet.app.run()
    return controller


run()
