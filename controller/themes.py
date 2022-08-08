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
    "padding": (140, 35),
    "p_padding": (20, 45)
}

DIALOGUE_SMALL = {
    "play_sfx": lambda: music_handler.play_sfx(path_sfx("text.mp3")),
    "border_size": 4,
    "padding": (10, 20),
    "p_padding": (-110, -10)
}
