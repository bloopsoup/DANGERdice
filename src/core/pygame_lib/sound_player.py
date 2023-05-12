import pygame
from .constants import loaded_sounds
from ..components import AbstractSoundPlayer


class SoundPlayer(AbstractSoundPlayer):
    def __init__(self):
        super().__init__()
        self.playlist = ["calm", "doma", "huh", "jong", "menu", "ones", "somedrums", "Something", "stomp", "stomp2",
                         "trittle", "zins"]

    def reset_player(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.set_volume(0.4)

    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def play_sfx(self, sound: str):
        if not self.mute:
            assert sound in loaded_sounds, f"{sound} is not a valid sound"
            pygame.mixer.Sound(loaded_sounds[sound]).play()

    def change_music(self, sound: str):
        if sound == self.current_song:
            return
        assert sound in loaded_sounds, f"{sound} is not a valid sound"
        self.current_song = sound
        self.reset_player()
        pygame.mixer.music.load(loaded_sounds[sound])
        pygame.mixer.music.play(-1)
        if self.mute:
            pygame.mixer.music.pause()

    def stop_music(self):
        self.current_song = None
        self.reset_player()
