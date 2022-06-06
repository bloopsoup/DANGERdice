import pygame
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


player_stats = [
    {"level": 1, "health_factor": 100, "money_factor": 100, "preference": ["basic1", "basic1"]}
]


class Player(Enemy):
    """The main character of the game. Has an inventory."""

    enemy_stats = player_stats
    required_exp = [0, 8, 10, 12, 14, 17, 19, 22, 25, 30, 500]

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                                        [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                                        [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

        self.inventory = []
        self.current_stage = "p0-0"
        self.exp = 0

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
        self.inventory = []
        self.current_stage = "p0-0"
        self.exp = 0
        self.dead = False
        self.set_stats(0)

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
