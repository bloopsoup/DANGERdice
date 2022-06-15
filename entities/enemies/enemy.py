class Enemy:
    """Base class for enemy characters of the game. In this case, they have a name, level, health, and dice_set."""

    enemy_stats = None

    def __init__(self):
        self.name = ""
        self.level = 0
        self.max_health = 0
        self.health = 0
        self.money = 0
        self.preference = None

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

    def set_stats(self, tier: int):
        """To be called after the enemy is created. Tier determines what stats and dice the enemy will get."""
        self.level = self.enemy_stats[tier]["level"]
        self.max_health = self.level * self.enemy_stats[tier]["health_factor"]
        self.health = self.max_health
        self.money = self.level * self.enemy_stats[tier]["money_factor"]
        self.preference = self.enemy_stats[tier]["preference"]
