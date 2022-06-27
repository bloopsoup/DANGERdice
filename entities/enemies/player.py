from .enemy import Enemy


class Player(Enemy):
    """The main character of the game."""

    required_exp = [0, 8, 10, 12, 14, 17, 19, 22, 25, 30, 500]

    def __init__(self, starting_stage: str):
        super().__init__("", 1, 100, 0, [])
        self.starting_stage = starting_stage
        self.current_stage = self.starting_stage

        self.inventory = []
        self.exp = 0

    def get_stage(self) -> str:
        """Gets the player's current stage."""
        return self.current_stage

    def set_stage(self, stage: str):
        """Sets the player's current stage."""
        self.current_stage = stage

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

    def reset_player(self):
        """Resets the player to basic stats."""
        self.reset_to_base_stats()
        self.current_stage = self.starting_stage
        self.inventory = []
        self.exp = 0

    def package_data(self) -> dict:
        """Returns a dictionary aggregating player data."""
        return {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "max_health": self.max_health,
            "money": self.money,
            "preference": self.preference,
            "inventory": self.inventory,
            "current_stage": self.current_stage,
            "exp": self.exp
        }
