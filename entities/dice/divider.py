import pygame
from entities.dice.die import Die


class Divider(Die):
    """When rolled successfully, the die will divide your opponent's next damage roll by the rolled value.
       The effect WILL happen even if your opponent forfeits their turn or does not have any damage.
       Level is used to affect the die's price and name without affecting the roll result."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], sides: list, multiple: int, ID: str,
                 level: int):
        super().__init__(images, pos, sides, multiple, ID)
        self.price += (1000 * (level + 1))
        self.name = "Divider Die{0}".format("+" * level)
        self.damage_type = "divide"
