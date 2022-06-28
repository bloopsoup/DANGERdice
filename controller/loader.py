import pygame
from entities.enemies import Enemy, Player
from entities.dice import Die
from gui.utils import Spritesheet, IndexCycler

from .utils import rp, path_b, path_c, path_s, path_sfx, path_song
from .config import dice_config, enemy_config, fonts_config, idle_animation_config, screen_config, spritesheet_config, \
    button_config, sound_config


# UTILS
def get_base_price(multiple: int) -> int:
    """Returns the base price for a standard die which is subject to balance changes."""
    return int(130 * 1.5 * (multiple + 0.5))


def load_font(size: str) -> pygame.font.Font:
    """Loads a font."""
    assert size in fonts_config, "not a valid size"
    return pygame.font.Font(rp("assets/VT323-Regular.ttf"), fonts_config[size])


def load_sound(sound: str, sfx: bool):
    """Returns a path to a sound file (sfx or music)."""
    assert sound in sound_config, "not a valid sound"
    path = sound_config[sound]
    path = path_sfx(path) if sfx else path_song(path)
    return path


def load_idle_animation(animation: str) -> IndexCycler:
    """Loads an idle animation."""
    assert animation in idle_animation_config, "not a valid animation"
    indices, frames = idle_animation_config[animation]
    return IndexCycler(indices, frames)


def load_screen(screen: str) -> pygame.Surface:
    """Loads a screen."""
    assert screen in screen_config, "not a valid screen"
    return pygame.Surface.convert_alpha(pygame.image.load(path_s(screen_config[screen])))


def load_spritesheet(sheet: str, character: bool) -> Spritesheet:
    """Loads in images from a character or a button spritesheet."""
    assert sheet in spritesheet_config, "not a valid spritesheet"
    path, height, width, rows, cols = spritesheet_config[sheet]
    path = path_c(path) if character else path_b(path)
    return Spritesheet(path, height, width, rows, cols)


def load_button_sprites(button: str) -> list[pygame.Surface]:
    """Loads images for a button."""
    assert button in button_config, "not a valid button"
    sheet, row, col, amount = button_config[button]
    return load_spritesheet(sheet, False).load_some_images(row, col, amount)


# FACTORY FUNCTIONS
def create_die(die_type: str, multiple: int) -> Die:
    """Creates a die."""
    assert die_type in dice_config, "not a valid die type"
    side, additional_cost, safe = dice_config[die_type]
    return Die(side, multiple, get_base_price(multiple) + additional_cost, die_type, safe)


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy."""
    assert enemy in enemy_config, "not a valid enemy"
    stats = enemy_config[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    return Player("p0-0")
