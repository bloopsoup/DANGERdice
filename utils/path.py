import sys
import os
import pygame


def rp(path: str) -> str:
    """To be used when referring to any file in the assets folder for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)


def path_c(path: str) -> str:
    """Returns a character picture path."""
    return rp("assets/characters/" + path)


def path_b(path: str) -> str:
    """Returns a button picture path."""
    return rp("assets/buttons/" + path)


def path_s(path: str) -> str:
    """Returns a screen picture path."""
    return rp("assets/screens/" + path)


def path_song(path: str) -> str:
    """Returns a SFX path."""
    return rp("assets/song/" + path)


def path_sfx(path: str) -> str:
    """Returns a SFX path."""
    return rp("assets/sfx/" + path)


def load_img(path: str) -> pygame.Surface:
    """Load an image from PATH."""
    return pygame.Surface.convert_alpha(pygame.image.load(path))


def load_screen(path: str):
    """Load a screen image from PATH."""
    return [load_img(path_s(path))]


def save_data(data, file_name):
    """Saves data in FILE."""
    file = open(file_name, "w")
    file.write(str(data))
    file.close()


def load_data(file_name):
    """Loads data from FILE. If it doesn't exist, return NONE."""
    if os.path.exists(file_name):
        file = open(file_name, "r")
        return eval(file.read())
    return None
