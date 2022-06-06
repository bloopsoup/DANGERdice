import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


wandre_stats = [
    {"level": randint(3, 5), "health_factor": 8, "money_factor": 30, "preference": ["basic1", "basic1", "divider3"]},
    {"level": randint(6, 7), "health_factor": 9, "money_factor": 40, "preference": ["basic2", "basic2", "divider2"]},
    {"level": randint(7, 10), "health_factor": 9, "money_factor": 60, "preference": ["basic3", "basic2", "divider3"]},
    {"level": randint(10, 12), "health_factor": 10, "money_factor": 80, "preference": ["basic4", "basic3", "divider3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 100, "preference": ["basic5", "basic4", "divider3", "heal2"]},
    {"level": randint(15, 17), "health_factor": 15, "money_factor": 110, "preference": ["basic5", "basic5", "divider3", "heal3"]}
]


class Wandre(Enemy):
    """A cloud with an attitude. Very upfront about her motives."""

    enemy_stats = wandre_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 0, 0],
                                         [0, 0, 0, 5, 6, 7, 8, 8, 8, 9, 9, 8, 8, 7, 6, 5, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 10, 0, 0, 10, 0, 0, 0, 10, 10, 0, 0, 0],
                                         [0, 0, 0, 11, 0, 11, 0, 11, 0, 0, 0],
                                         [4, 4, 4, 4, 4, 4]], 0.09)
        self.change_name("Wandre")
