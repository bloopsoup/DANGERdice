import random
import pygame
from .utils import rp, path_sheet, path_static, path_sfx, path_song
from .config import dice_config, enemy_config, fonts_config, idle_animation_config, static_config, spritesheet_config, \
    chunk_config, sound_config, dialogue_config
from gui.utils import Spritesheet, IndexCycler, DialogueData
from entities.enemies import Enemy, Player
from entities.dice import Die, DiceSet


loaded_spritesheets = {}
loaded_static = {}


def load_font(size: str) -> pygame.font.Font:
    """Loads a font."""
    assert size in fonts_config, "{0} is not a valid size".format(size)
    return pygame.font.Font(rp("assets/VT323-Regular.ttf"), fonts_config[size])


def load_sound(name: str, sfx: bool):
    """Returns a path to a sound file (sfx or music)."""
    assert name in sound_config, "{0} is not a valid sound".format(name)
    path = sound_config[name]
    path = path_sfx(path) if sfx else path_song(path)
    return path


def load_static(name: str) -> pygame.Surface:
    """Loads a static image."""
    assert name in static_config, "{0} is not a valid screen".format(name)
    if name in loaded_static:
        return loaded_static[name]
    static = pygame.Surface.convert_alpha(pygame.image.load(path_static(static_config[name])))
    loaded_static[name] = static
    return static


def load_spritesheet(name: str) -> Spritesheet:
    """Loads in images from a character or a button spritesheet."""
    assert name in spritesheet_config, "{0} is not a valid spritesheet".format(name)
    if name in loaded_spritesheets:
        return loaded_spritesheets[name]
    path, height, width, rows, cols = spritesheet_config[name]
    sheet = Spritesheet(path_sheet(path), height, width, rows, cols)
    loaded_spritesheets[name] = sheet
    return sheet


def load_some_sprites(name: str) -> list[pygame.Surface]:
    """Loads some sprites using a NAME preset."""
    assert name in chunk_config, "{0} is not a valid chunk name".format(name)
    sheet, row, col, amount = chunk_config[name]
    return load_spritesheet(sheet).load_some_images(row, col, amount)


def load_all_sprites(name: str) -> list[pygame.Surface]:
    """Loads all sprites from a spritesheet."""
    return load_spritesheet(name).load_all_images()


def load_idle_animation(animation: str) -> IndexCycler:
    """Loads an idle animation."""
    assert animation in idle_animation_config, "{0} is not a valid animation".format(animation)
    indices, frames = idle_animation_config[animation]
    return IndexCycler(indices, frames)


def load_dialogue(dialogue: str, tier: int) -> DialogueData:
    """Loads dialogue."""
    assert dialogue in dialogue_config, "no dialogue has that name {0}".format(dialogue)
    texts, portrait_seq = dialogue_config[dialogue][tier]
    portraits = [load_all_sprites("player_icons"), load_all_sprites("{0}_icons".format(dialogue))]
    return DialogueData(texts, portraits, portrait_seq)


def random_die_name() -> str:
    """Gets a random die name."""
    return random.choice(list(dice_config.keys()))


def all_enemy_names() -> list[str]:
    """Gets a list of enemy names."""
    enemy_names = list(enemy_config.keys())
    return enemy_names


def create_die(die_type: str) -> Die:
    """Creates a die."""
    assert die_type in dice_config, "{0} is not a valid die type".format(die_type)
    side, multiple, additional_cost, damage_type, safe = dice_config[die_type]
    return Die(side, multiple, int(130 * 1.5 * (multiple + 0.5)) + additional_cost, damage_type, safe)


def create_dice_set(preference: list[str]) -> DiceSet:
    """Creates a dice set from a preference."""
    return DiceSet([create_die(die_name) for die_name in preference])


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy."""
    assert enemy in enemy_config, "{0} is not a valid enemy".format(enemy)
    stats = enemy_config[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    player = Player()
    for _ in range(4):
        player.append_to_preference("basic1")
    for _ in range(13):
        player.append_to_inventory("basic1")
    return player
