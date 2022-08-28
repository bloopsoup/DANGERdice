import pyglet
from .app import App
from ..control import State, StateManager

"""
Initialization for pyglet begins when constants.py is imported which sets up the fonts. Then the App object 
is instantiated which sets up the caption, icons, and clock.
"""


def run():
    """Starts running the game."""
    app = App(StateManager("attributions", {"attributions": State()}))
    pyglet.app.run()
    return app
