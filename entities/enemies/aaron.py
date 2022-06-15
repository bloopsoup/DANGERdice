from random import randint
from entities.enemies.enemy import Enemy


aaron_stats = [
    {"level": 1, "health_factor": 20, "money_factor": 0, "preference": ["basic1", "basic1"]},
    {"level": randint(6, 8), "health_factor": 11, "money_factor": 40, "preference": ["basic2", "basic2"]},
    {"level": randint(8, 11), "health_factor": 9, "money_factor": 60, "preference": ["basic3", "basic3", "basic2"]},
    {"level": randint(10, 13), "health_factor": 11, "money_factor": 75, "preference": ["basic4", "basic3", "basic3"]},
    {"level": randint(13, 16), "health_factor": 10, "money_factor": 70, "preference": ["basic4", "basic5"]},
    {"level": randint(16, 17), "health_factor": 12, "money_factor": 80, "preference": ["basic5", "basic5"]}
]


class Aaron(Enemy):
    """Placeholder enemy for testing battling."""

    enemy_stats = aaron_stats

    def __init__(self):
        super().__init__()
        self.change_name("Aaron")
