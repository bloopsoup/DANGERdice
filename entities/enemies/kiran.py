from random import randint
from entities.enemies.enemy import Enemy


kiran_stats = [
    {"level": randint(3, 5), "health_factor": 10, "money_factor": 20, "preference": ["basic1", "heal1"]},
    {"level": randint(5, 6), "health_factor": 11, "money_factor": 25, "preference": ["basic2", "basic2", "heal1"]},
    {"level": randint(6, 8), "health_factor": 12, "money_factor": 45, "preference": ["basic3", "basic3", "heal2"]},
    {"level": randint(9, 10), "health_factor": 12, "money_factor": 55, "preference": ["basic4", "basic4", "heal2"]},
    {"level": randint(11, 13), "health_factor": 15, "money_factor": 75, "preference": ["basic5", "basic5", "heal3"]},
    {"level": randint(15, 17), "health_factor": 15, "money_factor": 85, "preference": ["basic5", "basic5", "divider3", "multiplier3"]}
]


class Kiran(Enemy):
    """A rich star. Also a random final boss."""

    enemy_stats = kiran_stats

    def __init__(self):
        super().__init__()
        self.change_name("Kiran")
