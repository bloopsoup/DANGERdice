import sys
import os
import pygame


# LOADING AND SAVING FILES
def rp(relative_path):
    """To be used when referring to file in the assets folder. Makes it usable with PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


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


def load_files(files, number):
    """Easier way to load images. LEGACY."""
    return [rp(files + str(i) + ".png") for i in range(number)]


def load_c(file):
    """Loads a character picture file."""
    return rp("assets/characters/" + file)


def load_b(file):
    """Loads a button picture file."""
    return rp("assets/buttons/" + file)


def load_s(file):
    """Loads a screen picture file."""
    return rp("assets/screens/" + file)


# SOUND HANDLING
pause = False
current_song = None


def handle_music(current=None):
    """Handles music between states. Run with no arguments if you just want to pause it.
        Otherwise, switches the music to current. Will not do anything if current matches the current song.
        current -- Song name -- The song to switch to."""
    global pause
    global current_song

    if current:
        if current == current_song:
            return
        current_song = current
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(rp("assets/songs/" + current))
        pygame.mixer.music.play(-1)
        if pause:
            pygame.mixer.music.pause()
    else:
        if pause:
            pygame.mixer.music.unpause()
            pause = not pause
        else:
            pygame.mixer.music.pause()
            pause = not pause


def handle_sound(file):
    """Handles sound effects. Uses pause to decide whether to play or not."""
    global pause

    if not pause:
        pygame.mixer.Sound(rp("assets/sfx/" + file)).play()
