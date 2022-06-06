import pygame
from entities.dice.die import Die


class Multiplier(Die):
    """When rolled successfully, the die will multiply your current DMG by the rolled value."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], sides: list, multiple: int, ID: str,
                 level: int):
        super().__init__(images, pos, sides, multiple, ID)
        self.price += (3000 * (level + 1))
        self.name = "Multiplier Die{0}".format("+" * level)
        self.damage_type = "multiply"
