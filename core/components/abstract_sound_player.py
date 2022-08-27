class AbstractSoundPlayer:
    """Handles the game's music and sounds."""

    def __init__(self):
        self.mute = False
        self.current_song = None

    def reset_player(self):
        """Resets the player's state."""
        raise NotImplementedError

    def toggle_mute(self):
        """Toggles muting music and sounds."""
        raise NotImplementedError

    def play_sfx(self, sound: str):
        """Play a sound effect."""
        raise NotImplementedError

    def change_music(self, sound: str):
        """Change the currently playing music."""
        raise NotImplementedError

    def stop_music(self):
        """Stops the current song that's playing."""
        raise NotImplementedError
