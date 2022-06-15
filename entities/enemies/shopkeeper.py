from random import randint
from entities.enemies.enemy import Enemy


shopkeeper_stats = [
    {"level": randint(8, 10), "health_factor": 13, "money_factor": 300, "preference": ["basic2", "basic2", "multiplier1", "multiplier1"]},
    {"level": randint(10, 13), "health_factor": 15, "money_factor": 500, "preference": ["basic3", "multiplier1", "poison2", "poison2"]},
    {"level": randint(13, 15), "health_factor": 17, "money_factor": 800, "preference": ["basic3", "multiplier2", "heal2", "poison2"]},
    {"level": randint(15, 17), "health_factor": 19, "money_factor": 1000, "preference": ["basic4", "multiplier3", "heal3", "poison3"]},
    {"level": randint(17, 19), "health_factor": 21, "money_factor": 1200, "preference": ["basic5", "multiplier3", "multiplier3", "heal3"]},
    {"level": randint(20, 21), "health_factor": 23, "money_factor": 1500, "preference": ["basic5", "basic5", "multiplier3", "multiplier3"]}
]


class Shopkeeper(Enemy):
    """A small cube maintaining a store full of deadly cubes."""

    enemy_stats = shopkeeper_stats

    def __init__(self):
        super().__init__()
        self.change_name("Shopkeeper")
