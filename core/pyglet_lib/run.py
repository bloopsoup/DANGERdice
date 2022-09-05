import pyglet
from .app import App
from ..control import State, StateManager

"""
Initialization for pyglet begins when constants.py is imported which sets up the fonts. Then the App object 
is instantiated which sets up the caption, icons, and clock.
"""


def run(start: str, states: dict[str, State]):
    """Starts running the game."""
    app = App(StateManager(start, states))
    pyglet.app.run()
    return app
