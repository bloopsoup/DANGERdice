import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


migahexx_stats = [
    {"level": randint(5, 7), "health_factor": 6, "money_factor": 55, "preference": ["basic1", "multiplier1"]},
    {"level": randint(6, 8), "health_factor": 7, "money_factor": 70, "preference": ["basic2", "multiplier2"]},
    {"level": randint(8, 11), "health_factor": 8, "money_factor": 80, "preference": ["basic2", "basic2", "multiplier2"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 90, "preference": ["basic3", "multiplier3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 110, "preference": ["basic4", "basic4", "multiplier3"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 120, "preference": ["basic5", "basic5", "multiplier3"]}
]


class Migahexx(Enemy):
    """Do not fight."""

    enemy_stats = migahexx_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 5, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0],
                                         [0, 0, 8, 9, 10, 11, 11, 11, 10, 9, 8, 0, 0, 5, 6, 7, 6, 5, 0],
                                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], 0.001)
        self.change_name("migahexx.xml")
