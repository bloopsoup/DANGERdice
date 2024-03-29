class Status:
    """Stores persistent status info throughout the battle."""

    def __init__(self):
        self.poison = 0
        self.blessed = 0
        self.weaken = 1

    def get_poison(self) -> int:
        """Gets the poison."""
        return self.poison

    def add_poison(self, amount: int):
        """Increases poison."""
        self.poison += amount

    def subtract_poison(self, amount: int):
        """Decreases poison."""
        self.poison -= amount

    def get_blessed(self) -> int:
        """Gets blessed."""
        return self.blessed

    def set_blessed(self, amount: int):
        """Sets blessed."""
        self.blessed = amount

    def get_weaken(self) -> int:
        """Gets weaken."""
        return self.weaken

    def set_weaken(self, amount: int):
        """Sets weaken."""
        self.weaken = amount
