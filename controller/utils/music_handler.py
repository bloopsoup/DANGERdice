import pygame


class MusicHandler:
    """Handles the game's music and sounds."""

    def __init__(self):
        self.pause = False
        self.current_path = None

    def play_sfx(self, path: str):
        """Play a sound effect at path."""
        if not self.pause:
            pygame.mixer.Sound(path).play()

    def change(self, path: str):
        """Change the music to the song found at path. Won't do anything if it matches the current song."""
        if path == self.current_path:
            return
        self.current_path = path
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        if self.pause:
            pygame.mixer.music.pause()

    def toggle(self):
        """Toggles sounds."""
        if self.pause:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.pause = not self.pause


# Access this instance
music_handler = MusicHandler()
