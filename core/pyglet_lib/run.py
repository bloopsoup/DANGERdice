import pyglet
from control import Control
from core.state import State, StateManager

"""
Initialization for pyglet begins when constants.py is imported which sets up the fonts. Then the Control object 
is instantiated which sets up the caption, icons, and clock.
"""


def run():
    """Starts running the game."""
    controller = Control(StateManager("attributions", {"attributions": State()}))
    pyglet.app.run()
    return controller


run()
