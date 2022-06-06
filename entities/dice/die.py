import random
import pygame
from utils.index_cycler import IndexCycler
from entities.base_entity import BaseEntity


class Die(BaseEntity):
    """The DIE object is what players roll to deal damage to one another. Has sides and a
       multiplier if provided. Enemy classes contain dice within their dice_set. For dice,
       files must consist of 6 pictures indexed from 0. Note: For no-1 dice, we can roll the
       index to obtain the picture and then add to it so that it meets the minimum.
       In addition, each die has a price and a name (generated upon construction)."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], sides: list, multiple: int, ID: str):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 1, 2, 3, 4, 5],
                                         [3, 4, 1, 2, 0, 5],
                                         [5, 2, 1, 3, 4, 0],
                                         [1, 2, 5, 3, 0, 4]], 0.05)

        self.sides = sides
        self.multiple = multiple
        self.price = int(130 * 1.5 * (multiple + 0.5))
        self.name = "Basic {0}X Die".format(self.multiple)
        self.ID = ID

        self.safe = False
        self.rolled = False
        self.damage_type = "basic"

    def damage_type(self) -> str:
        """Returns the damage type of this die."""
        return self.damage_type

    def roll(self, failsafe: bool, number: int = -1) -> int:
        """Rolls this die. If it is 1, we return 0 since rolling a one immediately ends your turn.
           If NUMBER is provided, die will always output that side. If failsafe is TRUE, a rolled one
           gets changed to the value of the die's fifth side."""
        self.rolled = True
        side = number if number != -1 else random.randint(0, 5)
        self.image = self.images[side]
        value = self.sides[side] if self.sides[side] != 1 or self.safe else 0

        if value == 0 and failsafe:
            self.image = self.images[4]
            return self.sides[4] * self.multiple
        else:
            return value * self.multiple
