from .components import AbstractImage, AbstractSpritesheet, Rectangle
from .control import Event, State
from .enums import EventType, Key, MouseButton
from .path import chunk_config

###############
#    SETUP    #
###############

ACTIVE_LIBRARY = "pygame"
if ACTIVE_LIBRARY == "pygame":
    from .pygame_lib import loaded_static, loaded_sheets, Image, Label, run, SoundPlayer, Spritesheet
else:
    raise ImportError

###############
#  CONSTANTS  #
###############

SOUND_PLAYER = SoundPlayer()

###############
#   LOADERS   #
###############


def get_image(name: str) -> AbstractImage:
    """Loads a static image."""
    assert name in loaded_static, f"{name} is not a valid image"
    return Image(loaded_static[name])


def get_spritesheet(name: str) -> AbstractSpritesheet:
    """Loads in images from a character or a button spritesheet."""
    assert name in loaded_sheets, f"{name} is not a valid spritesheet"
    sheet, height, width, rows, cols = loaded_sheets[name]
    return Spritesheet(sheet, height, width, rows, cols)


def get_sprites(name: str) -> list[AbstractImage]:
    """Loads some sprites using a NAME preset."""
    assert name in chunk_config, f"{name} is not a valid chunk name"
    sheet, row, col, amount = chunk_config[name]
    return get_spritesheet(sheet).load_some_images(row, col, amount)


def get_all_sprites(name: str) -> list[AbstractImage]:
    """Loads all sprites from a spritesheet."""
    return get_spritesheet(name).load_all_images()
