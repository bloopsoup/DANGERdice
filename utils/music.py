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
