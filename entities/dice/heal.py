from entities.dice.die import Die


class Heal(Die):
    """When rolled, it will restore your health by the rolled value. In addition,
       it decreases your poison counter by the value as well. Cannot forfeit your turn with this die."""

    def __init__(self, sides: list, multiple: int):
        super().__init__(sides, multiple)
        self.price += 600
        self.name = "Heal {0}X Die".format(self.multiple)
        self.safe = True
        self.damage_type = "heal"
