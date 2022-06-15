from random import randint
from entities.enemies.enemy import Enemy


dorita_stats = [
    {"level": randint(3, 4), "health_factor": 6, "money_factor": 20, "preference": ["basic1", "basic1"]},
    {"level": randint(4, 6), "health_factor": 10, "money_factor": 40, "preference": ["basic2", "basic2", "divider2"]},
    {"level": randint(7, 9), "health_factor": 11, "money_factor": 60, "preference": ["basic2", "basic3", "divider3"]},
    {"level": randint(10, 12), "health_factor": 12, "money_factor": 80, "preference": ["basic4", "basic3", "basic3", "divider3"]},
    {"level": randint(12, 15), "health_factor": 12, "money_factor": 90, "preference": ["basic5", "divider3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 100, "preference": ["basic5", "basic5", "divider3"]}
]


class Dorita(Enemy):
    """A floating nacho chip surrounded by balls. Likes to roll crap dice."""

    enemy_stats = dorita_stats

    def __init__(self):
        super().__init__()
        self.change_name("Dorita")
