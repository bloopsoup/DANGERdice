import pygame
from random import randint
from utils.index_cycler import IndexCycler
from entities.enemies.enemy import Enemy


wally_stats = [
    {"level": randint(3, 4), "health_factor": 15, "money_factor": 70, "preference": ["basic2"]},
    {"level": randint(5, 8), "health_factor": 10, "money_factor": 80, "preference": ["basic2", "heal1"]},
    {"level": randint(8, 11), "health_factor": 10, "money_factor": 100, "preference": ["basic2", "basic2", "heal1", "heal1"]},
    {"level": randint(11, 13), "health_factor": 11, "money_factor": 120, "preference": ["basic3", "basic3"]},
    {"level": randint(13, 16), "health_factor": 12, "money_factor": 140, "preference": ["basic5", "basic5"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 150, "preference": ["basic5", "basic5", "heal2"]},
]


class Wally(Enemy):
    """Sometimes whales like to play craps. Hits hard with one die."""

    enemy_stats = wally_stats

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)
        self.idle_handler = IndexCycler([[0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 7, 8, 7, 4, 3, 2, 1, 0, 0, 0],
                                         [0, 0, 9, 9, 0, 0, 10, 11, 12, 12, 16, 16, 16, 12, 12, 12, 16, 12, 11, 10, 0, 0],
                                         [0, 0, 9, 9, 15, 9, 15, 9, 0, 0],
                                         [0, 0, 17, 18, 19, 20, 21, 22, 23, 24, 17, 18, 19, 20, 21, 22, 23, 24, 0, 0],
                                         [0, 0, 0, 0, 0]], 0.07)
        self.change_name("Wally")
