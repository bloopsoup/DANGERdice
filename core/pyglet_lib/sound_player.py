import pyglet
from .constants import loaded_sounds
from ..components import AbstractSoundPlayer


class SoundPlayer(AbstractSoundPlayer):
    def __init__(self):
        super().__init__()
        self.sfx_player = pyglet.media.Player()
        self.music_player = pyglet.media.Player()
        self.music_player.volume = 0.4
        self.music_player.loop = True
        self.playlist = ["calm", "doma", "huh", "jong", "menu", "ones", "somedrums", "Something", "stomp", "stomp2",
                         "trittle", "zins"]

    def reset_player(self):
        self.music_player.pause()
        self.music_player = pyglet.media.Player()
        self.music_player.volume = 0.4
        self.music_player.loop = True

    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            self.music_player.pause()
        else:
            self.music_player.play()

    def play_sfx(self, sound: str):
        if not self.mute:
            assert sound in loaded_sounds, f"{sound} is not a valid sound"
            self.sfx_player = pyglet.media.Player()
            self.sfx_player.queue(loaded_sounds[sound])
            self.sfx_player.play()

    def change_music(self, sound: str):
        if sound == self.current_song:
            return
        assert sound in loaded_sounds, f"{sound} is not a valid sound"
        self.current_song = sound
        self.reset_player()
        self.music_player.queue(loaded_sounds[sound])
        self.music_player.play()
        if self.mute:
            self.music_player.pause()

    def stop_music(self):
        self.current_song = None
        self.reset_player()
