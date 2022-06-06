import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


cena_stats = [
    {"level": randint(3, 4), "health_factor": 5, "money_factor": 15, "preference": ["basic1", "poison1"]},
    {"level": randint(6, 8), "health_factor": 7, "money_factor": 30, "preference": ["basic2", "poison2", "poison2"]},
    {"level": randint(8, 11), "health_factor": 8, "money_factor": 40, "preference": ["basic2", "poison2", "poison3", "heal2"]},
    {"level": randint(11, 13), "health_factor": 9, "money_factor": 60, "preference": ["poison3", "poison3", "heal2"]},
    {"level": randint(13, 15), "health_factor": 10, "money_factor": 75, "preference": ["poison3", "poison3", "heal3"]},
    {"level": randint(15, 17), "health_factor": 12, "money_factor": 80, "preference": ["poison3", "poison3", "poison3", "heal3"]}
]


class Cena(Enemy):
    """Not associated with John Cena."""

    enemy_stats = cena_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0],
                                         [0, 0, 0, 5, 6, 7, 8, 7, 6, 7, 6, 5, 0, 0, 0],
                                         [0, 0, 0, 9, 10, 11, 11, 11, 10, 9, 9, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)
        self.change_name("Cena")
