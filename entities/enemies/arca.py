from random import randint
from entities.enemies.enemy import Enemy


arca_stats = [
    {"level": randint(2, 3), "health_factor": 8, "money_factor": 15, "preference": ["basic1", "basic1"]},
    {"level": randint(5, 6), "health_factor": 10, "money_factor": 25, "preference": ["basic1", "basic1"]},
    {"level": randint(7, 9), "health_factor": 12, "money_factor": 30, "preference": ["basic1", "basic1"]},
    {"level": randint(10, 12), "health_factor": 12, "money_factor": 50, "preference": ["basic1", "basic1"]},
    {"level": randint(12, 15), "health_factor": 14, "money_factor": 70, "preference": ["basic1", "basic1"]},
    {"level": randint(15, 20), "health_factor": 18, "money_factor": 80, "preference": ["basic1", "basic1"]}
]


class Arca(Enemy):
    """Sucks at fighting games. Will you let him beat you?"""

    enemy_stats = arca_stats

    def __init__(self):
        super().__init__()
        self.change_name("Arca")
