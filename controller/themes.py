from .utils import music_handler, path_sfx

# BUTTONS
BUTTON_DEFAULT = {
    "play_sfx": lambda: music_handler.play_sfx(path_sfx("click.mp3")),
    "border_size": 4
}

# INPUT TEXT
INPUT_DEFAULT = {
    "play_sfx": lambda: music_handler.play_sfx(path_sfx("click.mp3")),
    "border_size": 4,
    "padding": 35,
}

# DIALOGUE BOX
DIALOGUE_DEFAULT = {
    "play_sfx": lambda: music_handler.play_sfx(path_sfx("text.mp3")),
    "border_size": 4,
    "padding": 140,
    "LPL": 27,
    "line_spacing": 35,
    "lines": 3
}

DIALOGUE_SMALL = {
    "play_sfx": lambda: music_handler.play_sfx(path_sfx("text.mp3")),
    "border_size": 4,
    "padding": 10,
    "LPL": 40,
    "line_spacing": 0,
    "lines": 1
}
