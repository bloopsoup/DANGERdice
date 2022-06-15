from random import randint
from entities.enemies.enemy import Enemy


connor_stats = [
    {"level": randint(3, 4), "health_factor": 9, "money_factor": 15, "preference": ["basic1", "basic1", "basic1", "basic1"]},
    {"level": randint(5, 7), "health_factor": 9, "money_factor": 20, "preference": ["basic2", "basic2", "basic1", "basic1"]},
    {"level": randint(6, 8), "health_factor": 11, "money_factor": 40, "preference": ["basic3", "basic2", "basic1"]},
    {"level": randint(9, 11), "health_factor": 11, "money_factor": 50, "preference": ["basic4", "basic2"]},
    {"level": randint(11, 12), "health_factor": 13, "money_factor": 70, "preference": ["basic5", "basic5", "basic2"]},
    {"level": randint(13, 15), "health_factor": 15, "money_factor": 85, "preference": ["basic4", "multiplier3", "multiplier3"]}
]


class Connor(Enemy):
    """A six-sided enthusiast."""

    enemy_stats = connor_stats

    def __init__(self):
        super().__init__()
        self.change_name("Connor")
