import os
import sys
import json


def path_relative(path: str) -> str:
    """To be used when referring to any file in the assets folder for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath("")
    return os.path.join(base_path, path)


def path_asset(path: str) -> str:
    """Returns an asset path."""
    return path_relative("assets/" + path)


def path_sheet(path: str) -> str:
    """Returns a spritesheet picture path."""
    return path_relative("assets/sheets/" + path)


def path_static(path: str) -> str:
    """Returns a static picture path."""
    return path_relative("assets/static/" + path)


def path_song(path: str) -> str:
    """Returns a song path."""
    return path_relative("assets/songs/" + path)


def path_sfx(path: str) -> str:
    """Returns a SFX path."""
    return path_relative("assets/sfx/" + path)


def save_json(data: dict, file_name: str):
    """Saves data as a JSON file to FILE_NAME."""
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def load_json(file_name: str) -> dict:
    """Loads data from JSON file FILE_NAME. If it doesn't exist, return an empty dictionary."""
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
