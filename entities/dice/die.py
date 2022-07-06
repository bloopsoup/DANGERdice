import random


class Die:
    """The DIE object is what players roll to deal damage to one another. Has sides and a
       multiplier if provided. Each die has a price and a name (generated upon construction)."""

    def __init__(self, sides: list[int], multiple: int, price: int, damage_type: str, safe: bool):
        self.sides = sides
        self.multiple = multiple
        self.price = price
        self.damage_type = damage_type
        self.safe = safe
        self.name = "{0}{1}".format(self.damage_type, self.multiple)
        self.rolled = -1

    def get_price(self) -> int:
        """Returns the die price."""
        return self.price

    def get_sell_price(self) -> int:
        """Returns the die sell price."""
        return self.price // 3

    def get_name(self) -> str:
        """Returns the die name."""
        return self.name

    def get_damage_type(self) -> str:
        """Returns the damage type of this die."""
        return self.damage_type

    def is_rolled(self) -> bool:
        """Returns whether this die was rolled."""
        return self.rolled != -1

    def get_rolled(self) -> int:
        """Returns the side the die is on."""
        return self.rolled

    def roll(self, failsafe: bool, number: int = -1) -> int:
        """Rolls this die. If it is 1, we return 0 since rolling a one immediately ends your turn.
           If NUMBER is provided, die will always output that side. If failsafe is TRUE, a rolled one
           gets changed to the value of the die's fifth side."""
        side = number if number != -1 else random.randint(0, 5)
        if self.sides[side] == 1 and failsafe:
            side = 4
        self.rolled = side
        value = self.sides[side] if self.sides[side] != 1 or self.safe else 0
        return value * self.multiple

    def unroll(self):
        """Unrolls the die."""
        self.rolled = -1
