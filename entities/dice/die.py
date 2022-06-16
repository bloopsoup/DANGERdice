import random


class Die:
    """The DIE object is what players roll to deal damage to one another. Has sides and a
       multiplier if provided. Each die has a price and a name (generated upon construction)."""

    def __init__(self, sides: list, multiple: int):
        self.sides = sides
        self.multiple = multiple
        self.price = int(130 * 1.5 * (multiple + 0.5))
        self.name = "Basic {0}X Die".format(self.multiple)

        self.safe = False
        self.rolled = False
        self.damage_type = "basic"

    def get_name(self) -> str:
        """Returns the die name."""
        return self.name

    def damage_type(self) -> str:
        """Returns the damage type of this die."""
        return self.damage_type

    def is_rolled(self) -> bool:
        """Returns whether this die was rolled."""
        return self.rolled

    def roll(self, failsafe: bool, number: int = -1) -> tuple:
        """Rolls this die. If it is 1, we return 0 since rolling a one immediately ends your turn.
           If NUMBER is provided, die will always output that side. If failsafe is TRUE, a rolled one
           gets changed to the value of the die's fifth side."""
        self.rolled = True
        side = number if number != -1 else random.randint(0, 5)
        value = self.sides[side] if self.sides[side] != 1 or self.safe else 0

        if value == 0 and failsafe:
            return side, self.sides[4] * self.multiple
        return side, value * self.multiple

    def unroll(self):
        """Unrolls the die."""
        self.rolled = False
