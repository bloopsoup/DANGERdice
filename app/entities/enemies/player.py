from .enemy import Enemy


class Player(Enemy):
    """The main character of the game."""

    required_exp = [0, 8, 10, 12, 14, 17, 19, 22, 25, 30, 500]

    def __init__(self):
        super().__init__("", 1, 100, 0, [])
        self.inventory = []
        self.exp = 0

    def get_inventory(self) -> list[str]:
        """Gets a copy of the player's inventory as a list."""
        return self.inventory[:]

    def append_to_inventory(self, element: str):
        """Adds an element to the player's inventory."""
        self.inventory.append(element)

    def remove_inventory(self, i: int):
        """Removes and returns the ith element of the player's inventory."""
        assert i < len(self.inventory), "inventory index out of bounds"
        return self.inventory.pop(i)

    def gain_exp(self, exp: int):
        """Gives the player experience."""
        self.exp += exp

    def try_level_up(self) -> bool:
        """If the player's amount of experience meets the requirement, it levels up the player and returns True."""
        if self.exp < self.required_exp[self.level]:
            return False

        self.level += 1
        self.exp = self.exp - self.required_exp[self.level]
        self.max_health += self.max_health // 10
        self.restore_health()
        return True

    def reset_data(self):
        """Resets player data."""
        self.name = ""
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.money = 0
        self.preference = ["basic1", "basic1"]
        self.inventory = []
        self.exp = 0
        self.dead = False

    def import_data(self, data: dict):
        """Reads in a dictionary of player data and sets the player's attributes."""
        self.name = data["name"]
        self.level = data["level"]
        self.health = data["health"]
        self.max_health = data["max_health"]
        self.money = data["money"]
        self.preference = data["preference"]
        self.inventory = data["inventory"]
        self.exp = data["exp"]
        self.dead = False

    def export_data(self) -> dict:
        """Returns a dictionary aggregating player data."""
        return {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "max_health": self.max_health,
            "money": self.money,
            "preference": self.preference,
            "inventory": self.inventory,
            "exp": self.exp
        }
