import random
from .die import Die


class DiceSet:
    """Handles dice rolling by acting as a container for Die objects."""

    def __init__(self, dice_set: list[Die]):
        self.dice_set = dice_set

    def get_dice(self) -> list[Die]:
        """Returns a copy of the list of dice."""
        return self.dice_set[:]

    def roll_die(self, i: int, blessed: bool) -> tuple[int, str]:
        """Roll the ith die in your dice set."""
        if len(self.dice_set) > i and not self.dice_set[i].is_rolled():
            value = self.dice_set[i].roll(failsafe=blessed)
            return value, self.dice_set[i].get_damage_type()
        return -1, "n/a"

    def roll_die_forced(self, i: int, number: int) -> tuple[int, str]:
        """Roll the ith die in your inventory where outcome is the specified side."""
        if len(self.dice_set) > i and not self.dice_set[i].is_rolled():
            value = self.dice_set[i].roll(failsafe=False, number=number)
            return value, self.dice_set[i].get_damage_type()
        return -1, "n/a"

    def needs_reset(self) -> bool:
        """Checks if all the dice has been rolled."""
        return all([die.is_rolled() for die in self.dice_set])

    def reset_dice(self):
        """Reset all dice to be unrolled."""
        for die in self.dice_set:
            die.unroll()

    def basic_decide(self) -> int:
        """Returns a random index of the dice to roll. -1 signals ending a turn."""
        if random.randint(0, 3) == 0:
            return -1
        if not self.needs_reset():
            return random.choice([i for i in range(len(self.dice_set)) if not self.dice_set[i].is_rolled()])
        return 0
