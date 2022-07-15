import pygame


class DialogueData:
    """Dialogue related data."""

    def __init__(self, texts: list[str], portraits: list[list[pygame.Surface]], portrait_seq: list[tuple[int, int]],
                 hooks: list = None):
        self.texts = texts
        self.portraits = portraits
        self.portrait_seq = portrait_seq
        self.hooks = hooks
        self.seq_idx = 0
        assert len(self.texts) == len(self.portrait_seq), "texts and portrait_seq should be the same length"
        assert hooks is None or len(self.texts) == len(self.hooks), "texts and hooks should be the same length"

    def reset(self):
        """Resets to the beginning of the text sequence."""
        self.seq_idx = 0

    def advance(self) -> bool:
        """Advances to the next text and portrait to display. Returns FALSE if there's no more content."""
        self.seq_idx += 1
        return self.seq_idx < len(self.texts)

    def call_hook(self):
        """Calls the current hook if it's not None."""
        if self.hooks is not None and self.hooks[self.seq_idx] is not None:
            self.hooks[self.seq_idx]()

    def get_text(self) -> str:
        """Returns the current text."""
        return self.texts[self.seq_idx]

    def get_portrait(self) -> pygame.Surface:
        """Returns the current portrait."""
        portraits, portrait_index = self.portrait_seq[self.seq_idx]
        return self.portraits[portraits][portrait_index]
