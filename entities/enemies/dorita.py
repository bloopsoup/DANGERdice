import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


dorita_stats = [
    {"level": randint(3, 4), "health_factor": 6, "money_factor": 20, "preference": ["basic1", "basic1"]},
    {"level": randint(4, 6), "health_factor": 10, "money_factor": 40, "preference": ["basic2", "basic2", "divider2"]},
    {"level": randint(7, 9), "health_factor": 11, "money_factor": 60, "preference": ["basic2", "basic3", "divider3"]},
    {"level": randint(10, 12), "health_factor": 12, "money_factor": 80, "preference": ["basic4", "basic3", "basic3", "divider3"]},
    {"level": randint(12, 15), "health_factor": 12, "money_factor": 90, "preference": ["basic5", "divider3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 100, "preference": ["basic5", "basic5", "divider3"]}
]


class Dorita(Enemy):
    """A floating nacho chip surrounded by balls. Likes to roll crap dice."""

    enemy_stats = dorita_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                          15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                                          37, 38, 39]], 0.015)
        self.change_name("Dorita")
