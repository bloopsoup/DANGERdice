import sys
import os


def rp(path: str) -> str:
    """To be used when referring to any file in the assets folder for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath("")
    return os.path.join(base_path, path)


def path_sheet(path: str) -> str:
    """Returns a spritesheet picture path."""
    return rp("assets/sheets/" + path)


def path_static(path: str) -> str:
    """Returns a static picture path."""
    return rp("assets/static/" + path)


def path_song(path: str) -> str:
    """Returns a song path."""
    return rp("assets/songs/" + path)


def path_sfx(path: str) -> str:
    """Returns a SFX path."""
    return rp("assets/sfx/" + path)


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
