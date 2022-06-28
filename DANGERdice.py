import os
import pygame
import sys
from controller import Control
from controller.states import Attributions, MainMenu


###############
#    HELPER   #
###############

def rp(path: str) -> str:
    """To be used when referring to any file in the assets folder for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath("")
    return os.path.join(base_path, path)


###############
#    SETUP    #
###############

pygame.init()

# Set resolution
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set icon
pygame.display.set_icon(pygame.image.load(rp("assets/icon.png")))
pygame.display.set_caption("DANGERdice")

# Set keys
pygame.key.set_repeat(500, 100)

# Set up states
STATES = {
    "attributions": Attributions(),
    "main_menu": MainMenu()
}

###############
#     RUN     #
###############

GAME = Control("attributions", STATES, SURFACE)
GAME.main_loop()
pygame.quit()
sys.exit()
