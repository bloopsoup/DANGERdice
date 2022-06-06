import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


baggins_stats = [
    {"level": randint(3, 4), "health_factor": 13, "money_factor": 30, "preference": ["basic2"]},
    {"level": randint(5, 6), "health_factor": 14, "money_factor": 35, "preference": ["basic3"]},
    {"level": randint(6, 7), "health_factor": 14, "money_factor": 55, "preference": ["basic4"]},
    {"level": randint(8, 9), "health_factor": 15, "money_factor": 65, "preference": ["basic5"]},
    {"level": randint(10, 11), "health_factor": 16, "money_factor": 80, "preference": ["basic5", "heal3"]},
    {"level": randint(11, 14), "health_factor": 16, "money_factor": 100, "preference": ["basic5", "heal3", "heal3"]}
]


class Baggins(Enemy):
    """Bag with a heart of gold."""

    enemy_stats = baggins_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 5, 5, 6, 5, 5, 4, 4, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                                         [7, 8, 7, 8, 7, 8, 8, 8, 9, 9, 9, 8, 9],
                                         [10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)
        self.change_name("Baggins")
