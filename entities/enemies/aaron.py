import pygame
from random import randint
from utils.index_cycler import IndexCycler
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

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                                         [5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 7, 6, 5, 0, 0, 0, 0],
                                         [10, 11, 12, 12, 12, 12, 12, 12, 12, 11, 10, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)
        self.change_name("Aaron")
