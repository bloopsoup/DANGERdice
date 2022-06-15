from random import randint
from entities.enemies.enemy import Enemy


bursa_stats = [
    {"level": randint(4, 5), "health_factor": 6, "money_factor": 25, "preference": ["basic1"]},
    {"level": randint(6, 7), "health_factor": 8, "money_factor": 30, "preference": ["basic2", "basic2", "heal1"]},
    {"level": randint(7, 10), "health_factor": 9, "money_factor": 45, "preference": ["basic3", "basic2", "heal2"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 65, "preference": ["basic3", "basic3", "heal3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 75, "preference": ["basic4", "basic4", "heal3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 85, "preference": ["basic5", "basic5", "heal3"]}
]


class Bursa(Enemy):
    """Bursa has not seen his vegan brother. Must've gone to a different game."""

    enemy_stats = bursa_stats

    def __init__(self):
        super().__init__()
        self.change_name("Bursa")
