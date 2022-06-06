import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


baduck_stats = [
    {"level": randint(2, 4), "health_factor": 7, "money_factor": 25, "preference": ["poison1", "poison1"]},
    {"level": randint(5, 7), "health_factor": 8, "money_factor": 30, "preference": ["poison2", "poison2", "poison2"]},
    {"level": randint(7, 10), "health_factor": 8, "money_factor": 30, "preference": ["poison2", "poison2", "divider3"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 50, "preference": ["poison3", "poison2", "divider3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 70, "preference": ["poison3", "poison3", "divider3"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 80, "preference": ["poison3", "poison3", "poison3", "divider3"]}
]


class Baduck(Enemy):
    """Not bulky but annoying."""

    enemy_stats = baduck_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 5, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0],
                                         [0, 0, 8, 9, 10, 11, 11, 11, 10, 9, 8, 0, 0, 5, 6, 7, 6, 5, 0],
                                         [0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 0],
                                         [0, 0, 0, 0, 0]], 0.06)
        self.change_name("Baduck")
