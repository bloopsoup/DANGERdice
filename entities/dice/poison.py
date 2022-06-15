from entities.dice.die import Die


class Poison(Die):
    """When rolled, deals the displayed damage and then poisons the opponent
       with a counter to keep track. Opponent takes poison damage = counter at
       the end of their turn (so after they attack or fail one). Counter is
       then floor divided by 2 every turn until it is 0. Rolling subsequent poison
       dice can add to the counter."""

    def __init__(self, sides: list, multiple: int):
        super().__init__(sides, multiple)
        self.price += 400
        self.name = "Poison {0}X Die".format(self.multiple)
        self.damage_type = "poison"
