class Enemy:
    """Base class for enemy characters of the game."""

    def __init__(self, name: str, level: int, max_health: int, money: int, preference: list[str]):
        self.name = name
        self.level = level
        self.money = money
        self.preference = preference
        self.max_health = max_health
        self.health = self.max_health
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

    def subtract_money(self, money: int):
        """Decreases the enemy's money."""
        self.money -= money

    def get_preference(self) -> list[str]:
        """Gets a copy of the enemy's preference as a list."""
        return self.preference[:]

    def append_to_preference(self, element: str):
        """Adds element to the enemy's preference."""
        self.preference.append(element)

    def remove_preference(self, i: int) -> str:
        """Removes and returns the ith element of the enemy's preference."""
        assert i < len(self.preference), "preference index out of bounds"
        return self.preference.pop(i)

    def get_health(self) -> int:
        """Gets an enemy's health."""
        return self.health

    def add_health(self, amount: int):
        """Increases an enemy's health."""
        self.health += amount

    def subtract_health(self, amount: int):
        """Decreases an enemy's health."""
        self.health -= amount

    def get_max_health(self) -> int:
        """Gets an enemy's max health."""
        return self.max_health

    def restore_health(self):
        """Restores an enemy's health."""
        self.health = self.max_health

    def is_dead(self) -> bool:
        """Is the enemy dead?"""
        return self.dead

    def try_die(self):
        """Tries to kill the enemy if it's health is 0 or below."""
        if self.health <= 0:
            self.dead = True

    def try_revive(self):
        """Tries to revive the enemy to one health if they died."""
        if self.dead:
            self.dead = False
            self.health = 1

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
