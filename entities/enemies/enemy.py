class Enemy:
    """Base class for enemy characters of the game."""

    def __init__(self, name: str, level: int, max_health: int, money: int, preference: list[str]):
        self.name = name
        self.level = level
        self.money = money
        self.preference = preference
        self.max_health = max_health
        self.health = self.max_health

        # STATUS
        self.poison = 0
        self.divided = 1
        self.blessed = 0
        self.dead = False

    def get_name(self) -> str:
        """Returns the enemy's name."""
        return self.name

    def change_name(self, name: str):
        """Changes the enemy's name."""
        self.name = name

    def get_level(self) -> int:
        """Gets the enemy's level."""
        return self.level

    def get_money(self) -> int:
        """Gets the enemy's money."""
        return self.money

    def add_money(self, money: int):
        """Adds to the enemy's money."""
        self.money += money

    def get_preference(self) -> list[str]:
        """Gets a copy of the enemy's preference as a list."""
        return self.preference[:]

    def append_to_preference(self, element: str):
        """Adds element to the enemy's preference."""
        self.preference.append(element)

    def remove_preference(self, i: int):
        """Removes and returns the ith element of the enemy's preference."""
        assert i < len(self.preference), "preference index out of bounds"
        return self.preference.pop(i)

    def get_health(self) -> int:
        """Gets an enemy's health."""
        return self.health

    def get_max_health(self) -> int:
        """Gets an enemy's max health."""
        return self.max_health

    def restore_health(self):
        """Restores an enemy's health."""
        self.health = self.max_health

    def cleanse(self):
        """Removes all status elements."""
        self.poison = 0
        self.divided = 1
        self.blessed = 0

    def die(self):
        """Kills the enemy. All status elements are removed first."""
        self.cleanse()
        self.dead = True

    def revive(self):
        """Revives the enemy."""
        self.dead = False

    def reset_to_base_stats(self):
        """Resets the enemy to base stats."""
        self.level = 0
        self.max_health = 100
        self.restore_health()
        self.money = 0
        self.preference = []
        self.revive()
