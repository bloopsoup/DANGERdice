import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


arca_stats = [
    {"level": randint(2, 3), "health_factor": 8, "money_factor": 15, "preference": ["basic1", "basic1"]},
    {"level": randint(5, 6), "health_factor": 10, "money_factor": 25, "preference": ["basic1", "basic1"]},
    {"level": randint(7, 9), "health_factor": 12, "money_factor": 30, "preference": ["basic1", "basic1"]},
    {"level": randint(10, 12), "health_factor": 12, "money_factor": 50, "preference": ["basic1", "basic1"]},
    {"level": randint(12, 15), "health_factor": 14, "money_factor": 70, "preference": ["basic1", "basic1"]},
    {"level": randint(15, 20), "health_factor": 18, "money_factor": 80, "preference": ["basic1", "basic1"]}
]


class Arca(Enemy):
    """Sucks at fighting games. Will you let him beat you?"""

    enemy_stats = arca_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 1, 2, 3, 3, 3, 2, 1, 0, 0, 0],
                                         [0, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 0],
                                         [0, 0, 0, 5, 6, 7, 7, 7, 6, 5, 0, 0, 8, 9, 10, 10, 10, 9, 8, 0, 0, 0],
                                         [0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 0]], 0.09)
        self.change_name("Arca")
