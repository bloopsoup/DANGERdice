from random import randint
from entities.enemies.enemy import Enemy


baggins_stats = [
    {"level": randint(3, 4), "health_factor": 13, "money_factor": 30, "preference": ["basic2"]},
    {"level": randint(5, 6), "health_factor": 14, "money_factor": 35, "preference": ["basic3"]},
    {"level": randint(6, 7), "health_factor": 14, "money_factor": 55, "preference": ["basic4"]},
    {"level": randint(8, 9), "health_factor": 15, "money_factor": 65, "preference": ["basic5"]},
    {"level": randint(10, 11), "health_factor": 16, "money_factor": 80, "preference": ["basic5", "heal3"]},
    {"level": randint(11, 14), "health_factor": 16, "money_factor": 100, "preference": ["basic5", "heal3", "heal3"]}
]


class Baggins(Enemy):
    """Bag with a heart of gold."""

    enemy_stats = baggins_stats

    def __init__(self):
        super().__init__()
        self.change_name("Baggins")
