import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


ria_stats = [
    {"level": randint(5, 6), "health_factor": 9, "money_factor": 40, "preference": ["basic1", "basic1", "heal1"]},
    {"level": randint(6, 8), "health_factor": 8, "money_factor": 50, "preference": ["basic2", "basic2", "heal2"]},
    {"level": randint(8, 11), "health_factor": 10, "money_factor": 70, "preference": ["basic3", "basic2", "basic1", "heal2"]},
    {"level": randint(11, 13), "health_factor": 11, "money_factor": 90, "preference": ["basic3", "basic3", "heal2"]},
    {"level": randint(13, 15), "health_factor": 13, "money_factor": 110, "preference": ["basic4", "basic4", "heal3"]},
    {"level": randint(15, 17), "health_factor": 10, "money_factor": 120, "preference": ["basic5", "basic5", "heal2", "heal3"]}
]


class Ria(Enemy):
    """A kind spirit. But also a sadist."""

    enemy_stats = ria_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                                         [0, 0, 2, 3, 4, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 0, 0],
                                         [0, 0, 0, 5, 6, 6, 6, 5, 0, 0, 0, 0, 0, 7, 8, 9, 8, 7, 0, 0, 0],
                                         [0, 0, 0, 10, 11, 10, 11, 10, 0, 0, 0]], 0.1)
        self.change_name("Ria")
