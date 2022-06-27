import pygame
from .utils import rp, path_c, path_b
from .config import dice_config, enemy_config, fonts_config, spritesheet_config
from entities.enemies import Enemy, Player
from entities.dice import Die
from gui.utils import Spritesheet


# UTILS
def get_base_price(multiple: int) -> int:
    """Returns the base price for a standard die which is subject to balance changes."""
    return int(130 * 1.5 * (multiple + 0.5))


def load_sheet(sheet: str, character: bool) -> Spritesheet:
    """Loads in either a character or a button spritesheet."""
    assert sheet in spritesheet_config, "not a valid spritesheet"
    path, height, width, rows, cols = spritesheet_config[sheet]
    path = path_c(path) if character else path_b(path)
    return Spritesheet(path, height, width, rows, cols)


def load_font(size: str) -> pygame.font.Font:
    """Loads a font."""
    assert size in fonts_config, "not a valid size"
    return pygame.font.Font(rp("assets/VT323-Regular.ttf"), fonts_config[size])


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



