import sys
import pygame
from control import Control
from core.state import State, StateManager


def run():
    """Starts running the game."""
    controller = Control(StateManager("attributions", {"attributions": State()}))
    controller.main_loop()
    pygame.quit()
    sys.exit()


run()
