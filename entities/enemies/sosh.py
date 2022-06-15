from random import randint
from entities.enemies.enemy import Enemy


sosh_stats = [
    {"level": randint(3, 4), "health_factor": 7, "money_factor": 15, "preference": ["basic1", "basic1"]},
    {"level": randint(5, 6), "health_factor": 9, "money_factor": 20, "preference": ["basic2", "multiplier2"]},
    {"level": randint(7, 9), "health_factor": 9, "money_factor": 40, "preference": ["basic2", "basic2", "multiplier3"]},
    {"level": randint(10, 12), "health_factor": 10, "money_factor": 60, "preference": ["basic3", "multiplier3"]},
    {"level": randint(12, 15), "health_factor": 12, "money_factor": 80, "preference": ["basic4", "basic4", "multiplier3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 90, "preference": ["basic5"]}
]


class Sosh(Enemy):
    """He's more likely to help you out than try to kill you. But sometimes that doesn't line up."""

    enemy_stats = sosh_stats

    def __init__(self):
        super().__init__()
        self.change_name("Sosh")
