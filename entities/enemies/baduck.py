from random import randint
from entities.enemies.enemy import Enemy


baduck_stats = [
    {"level": randint(2, 4), "health_factor": 7, "money_factor": 25, "preference": ["poison1", "poison1"]},
    {"level": randint(5, 7), "health_factor": 8, "money_factor": 30, "preference": ["poison2", "poison2", "poison2"]},
    {"level": randint(7, 10), "health_factor": 8, "money_factor": 30, "preference": ["poison2", "poison2", "divider3"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 50, "preference": ["poison3", "poison2", "divider3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 70, "preference": ["poison3", "poison3", "divider3"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 80, "preference": ["poison3", "poison3", "poison3", "divider3"]}
]


class Baduck(Enemy):
    """Not bulky but annoying."""

    enemy_stats = baduck_stats

    def __init__(self):
        super().__init__()
        self.change_name("Baduck")
