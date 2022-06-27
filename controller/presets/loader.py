import pygame
from controller.utils.path import rp
from entities.dice import Die
from entities.enemies import Enemy
from entities.enemies import Player

from .dice_config import dice_config
from .enemy_config import enemy_config
from .fonts_config import fonts_config


# UTILS
def get_base_price(multiple: int) -> int:
    """Returns the base price for a standard die which is subject to balance changes."""
    return int(130 * 1.5 * (multiple + 0.5))


# FACTORY FUNCTIONS
def create_die(die_type: str, multiple: int) -> Die:
    """Creates a die using a preset."""
    assert die_type in dice_config, "not a valid die type"
    side, additional_cost, safe = dice_config[die_type]
    return Die(side, multiple, get_base_price(multiple) + additional_cost, die_type, safe)


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy using a preset."""
    assert enemy in enemy_config, "not a valid enemy"
    stats = enemy_config[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    return Player("p0-0")


def load_font(size: str) -> pygame.font.Font:
    assert size in fonts_config, "not a valid size"


def load_fonts() -> dict:
    """Loads and returns all the fonts used for the game."""
    return {"SS": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 25),
            "S": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 30),
            "M": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 40),
            "L": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 50)}
