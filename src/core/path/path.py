import os
import sys


def path_relative(path: str) -> str:
    """To be used when referring to any file in the assets folder for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath("")
    return os.path.join(base_path, path)


def path_asset(path: str) -> str:
    """Returns an asset path."""
    return path_relative("app/assets/" + path)


def path_sheet(path: str) -> str:
    """Returns a spritesheet picture path."""
    return path_relative("app/assets/sheets/" + path)


def path_static(path: str) -> str:
    """Returns a static picture path."""
    return path_relative("app/assets/static/" + path)


def path_song(path: str) -> str:
    """Returns a song path."""
    return path_relative("app/assets/songs/" + path)


def path_song_ogg(path: str) -> str:
    """Returns a song path."""
    return path_relative("app/assets/songs_ogg/" + path)


def path_sfx(path: str) -> str:
    """Returns a SFX path."""
    return path_relative("app/assets/sfx/" + path)


def path_sfx_ogg(path: str) -> str:
    """Returns a SFX path."""
    return path_relative("app/assets/sfx_ogg/" + path)
