import pygame
from entities.enemies import Enemy, Player
from entities.dice import Die
from gui.utils import Spritesheet, IndexCycler

from .utils import rp, path_sheet, path_static, path_sfx, path_song
from .config import dice_config, enemy_config, fonts_config, idle_animation_config, static_config, spritesheet_config, \
    chunk_config, sound_config


# UTILS
def load_idle_animation(animation: str) -> IndexCycler:
    """Loads an idle animation."""
    assert animation in idle_animation_config, "not a valid animation"
    indices, frames = idle_animation_config[animation]
    return IndexCycler(indices, frames)


def load_font(size: str) -> pygame.font.Font:
    """Loads a font."""
    assert size in fonts_config, "not a valid size"
    return pygame.font.Font(rp("assets/VT323-Regular.ttf"), fonts_config[size])


def load_sound(name: str, sfx: bool):
    """Returns a path to a sound file (sfx or music)."""
    assert name in sound_config, "not a valid sound"
    path = sound_config[name]
    path = path_sfx(path) if sfx else path_song(path)
    return path


def load_static(name: str) -> pygame.Surface:
    """Loads a screen."""
    assert name in static_config, "not a valid screen"
    return pygame.Surface.convert_alpha(pygame.image.load(path_static(static_config[name])))


def load_spritesheet(name: str) -> Spritesheet:
    """Loads in images from a character or a button spritesheet."""
    assert name in spritesheet_config, "not a valid spritesheet"
    path, height, width, rows, cols = spritesheet_config[name]
    return Spritesheet(path_sheet(path), height, width, rows, cols)


def load_some_sprites(name: str) -> list[pygame.Surface]:
    """Loads some sprites using a NAME preset."""
    assert name in chunk_config, "not a valid chunk name"
    sheet, row, col, amount = chunk_config[name]
    return load_spritesheet(sheet).load_some_images(row, col, amount)


def load_all_sprites(name: str) -> list[pygame.Surface]:
    """Loads all sprites from a spritesheet."""
    return load_spritesheet(name).load_all_images()


# FACTORY FUNCTIONS
def create_die(die_type: str, multiple: int) -> Die:
    """Creates a die."""
    assert die_type in dice_config, "not a valid die type"
    side, additional_cost, safe = dice_config[die_type]
    return Die(side, multiple, int(130 * 1.5 * (multiple + 0.5)) + additional_cost, die_type, safe)


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy."""
    assert enemy in enemy_config, "not a valid enemy"
    stats = enemy_config[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    player = Player("p0-0")
    player.append_to_preference("basic1")
    player.append_to_preference("basic1")
    return player
