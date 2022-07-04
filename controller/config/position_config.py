import pygame
from gui.elements import PTexts

# [self.name, "LVL: {0}", "HP: {0} / {1}", "Gold: {0}"]
height = 0  # self.text_name.get_height()
offsets = [(0, 0), (0, height), (0, height * 2), (0, height * 3)]
INFO_MENU = PTexts([pygame.Surface((1, 1))], (145, 72), None, 4, offsets, False)
INFO_PLAYER = PTexts([pygame.Surface((1, 1))], (38, 460), None, 4, offsets, False)
INFO_ENEMY = PTexts([pygame.Surface((1, 1))], (450, 460), None, 4, offsets, False)
ENTITY_DISPLAY = PTexts([pygame.Surface((100, 100))], (0, 0), None, 4, offsets, True)

# Dice preset
# (100 x 100)
# (369. 72) (369, 455) (33, 455)
