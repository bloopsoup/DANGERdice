import pygame
from gui.elements.positioned_texts import PositionedTexts

# [self.name, "LVL: {0}", "HP: {0} / {1}", "Gold: {0}"]
height = 0  # self.text_name.get_height()
offsets = [(0, 0), (0, height), (0, height * 2), (0, height * 3)]
INFO_MENU = PositionedTexts([pygame.Surface((1, 1))], (145, 72), None, 4, offsets)
INFO_PLAYER = PositionedTexts([pygame.Surface((1, 1))], (38, 460), None, 4, offsets)
INFO_ENEMY = PositionedTexts([pygame.Surface((1, 1))], (450, 460), None, 4, offsets)
