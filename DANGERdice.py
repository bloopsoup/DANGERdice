from utils.path import *
from asset_bank import AssetBank
from states.main_menu import MainMenu
from control import Control

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

# Set up assets
BANK = AssetBank()

# Set up states
STATES = {
    "main_menu": MainMenu(BANK)
}

###############
#     RUN     #
###############

GAME = Control("main_menu", STATES, SURFACE)
GAME.main_loop()
pygame.quit()
sys.exit()
