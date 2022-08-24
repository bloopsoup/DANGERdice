import sys
import pygame
from control import Control
from core.state import State, StateManager

"""
The initialization for pygame starts when constants.py is imported (which is done via 
indirectly importing Control). This sets up the window that will be drawn on. This function 
makes the Control object and starts managing the game states.
"""


def run():
    """Starts running the game."""
    controller = Control(StateManager("attributions", {"attributions": State()}))
    controller.main_loop()
    pygame.quit()
    sys.exit()


run()
