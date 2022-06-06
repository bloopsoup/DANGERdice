import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


ellie_stats = [
    {"level": randint(2, 3), "health_factor": 9, "money_factor": 16, "preference": ["basic1"]},
    {"level": randint(4, 5), "health_factor": 9, "money_factor": 25, "preference": ["basic1", "basic2"]},
    {"level": randint(6, 8), "health_factor": 10, "money_factor": 40, "preference": ["basic1", "basic2", "basic2", "heal1"]},
    {"level": randint(9, 11), "health_factor": 12, "money_factor": 55, "preference": ["basic1", "basic3", "poison2", "heal2"]},
    {"level": randint(11, 15), "health_factor": 14, "money_factor": 65, "preference": ["basic1", "basic4", "basic4", "heal3"]},
    {"level": randint(15, 17), "health_factor": 15, "money_factor": 75, "preference": ["basic1", "basic5", "heal3"]}
]


class Ellie(Enemy):
    """You have a sister. Apparently."""

    enemy_stats = ellie_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                                         [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                                         [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)
        self.change_name("Ellie")
