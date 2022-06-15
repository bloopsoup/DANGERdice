from random import randint
from entities.enemies.enemy import Enemy


square_stats = [
    {"level": randint(3, 4), "health_factor": 7, "money_factor": 10, "preference": ["basic1", "poison1", "heal1"]},
    {"level": randint(6, 7), "health_factor": 9, "money_factor": 30, "preference": ["basic2", "poison2", "heal2", "divider2"]},
    {"level": randint(7, 9), "health_factor": 9, "money_factor": 40, "preference": ["basic2", "poison2", "heal2", "basic3"]},
    {"level": randint(10, 12), "health_factor": 9, "money_factor": 60, "preference": ["basic3", "poison3", "divider3", "basic3"]},
    {"level": randint(12, 15), "health_factor": 10, "money_factor": 80, "preference": ["basic4", "basic5", "divider3", "heal3"]},
    {"level": randint(15, 17), "health_factor": 12, "money_factor": 90, "preference": ["basic5", "poison3", "divider3", "heal3"]}
]


class Square(Enemy):
    """A sentient die that doesn't want to roll anymore. Though it also uses dice."""

    enemy_stats = square_stats

    def __init__(self):
        super().__init__()
        self.change_name("Gamble Square")
