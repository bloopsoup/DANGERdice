import pygame


class DialogueData:
    """Dialogue related data."""

    def __init__(self, texts: list[str], portraits: list[list[pygame.Surface]], portrait_seq: list[tuple[int, int]]):
        self.texts = texts
        self.portraits = portraits
        self.portrait_seq = portrait_seq
        self.seq_idx = 0
        assert len(self.texts) == len(self.portrait_seq), "texts and portrait_seq should be the same length"

    def advance(self) -> bool:
        """Advances to the next text and portrait to display. Returns FALSE if there's no more content."""
        self.seq_idx += 1
        return self.seq_idx < len(self.texts)

    def get_text(self) -> str:
        """Returns the current text."""
        return self.texts[self.seq_idx]

    def get_portrait(self) -> pygame.Surface:
        """Returns the current portrait."""
        portraits, portrait_index = self.portrait_seq[self.seq_idx]
        return self.portraits[portraits][portrait_index]
