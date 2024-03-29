import sys
import pygame
import asyncio
from .app import App
from ..control import State, StateManager

"""
The initialization for pygame starts when constants.py is imported (which is done via 
indirectly importing Control). This sets up the window that will be drawn on. This function 
makes the App object and starts managing the game states.
"""


def run(start: str, states: dict[str, State]):
    """Starts running the game."""
    app = App(StateManager(start, states))
    asyncio.run(app.main_loop())
    pygame.quit()
    sys.exit()
