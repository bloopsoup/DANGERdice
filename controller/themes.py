from .utils import music_handler, path_sfx


# THEME HELPERS

def blank():
    """Does nothing."""
    pass


# BUTTONS


BUTTON_DEFAULT = {
    "play_sfx": lambda: music_handler.play_sfx(path_sfx("click.mp3")),
    "border_size": 4
}

BUTTON_GHOST = {
    "play_sfx": blank,
    "border_size": 0
}

# INPUT TEXT

INPUT_DEFAULT = {
    "play_sfx": blank,
    "border_size": 4,
    "padding": 35,
}

# DIALOGUE BOX

DIALOGUE_DEFAULT = {
    "play_sfx": blank,
    "border_size": 4,
    "padding": 35,
    "LPL": 40,
    "line_spacing": 35,
    "lines": 3
}
