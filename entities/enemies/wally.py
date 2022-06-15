from random import randint
from entities.enemies.enemy import Enemy


wally_stats = [
    {"level": randint(3, 4), "health_factor": 15, "money_factor": 70, "preference": ["basic2"]},
    {"level": randint(5, 8), "health_factor": 10, "money_factor": 80, "preference": ["basic2", "heal1"]},
    {"level": randint(8, 11), "health_factor": 10, "money_factor": 100, "preference": ["basic2", "basic2", "heal1", "heal1"]},
    {"level": randint(11, 13), "health_factor": 11, "money_factor": 120, "preference": ["basic3", "basic3"]},
    {"level": randint(13, 16), "health_factor": 12, "money_factor": 140, "preference": ["basic5", "basic5"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 150, "preference": ["basic5", "basic5", "heal2"]},
]


class Wally(Enemy):
    """Sometimes whales like to play craps. Hits hard with one die."""

    enemy_stats = wally_stats

    def __init__(self):
        super().__init__()
        self.change_name("Wally")
