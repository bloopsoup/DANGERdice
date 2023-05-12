from src.core import AbstractImage


class DialogueData:
    """Dialogue related data."""

    def __init__(self, texts: list[str], portraits: list[list[AbstractImage]], portrait_seq: list[tuple[int, int]],
                 hooks: list = None):
        assert len(texts) == len(portrait_seq), "texts and portrait_seq should be the same length"
        assert hooks is None or len(texts) == len(hooks), "texts and hooks should be the same length"
        self.texts = texts
        self.portraits = portraits
        self.portrait_seq = portrait_seq
        self.hooks = hooks
        self.seq_idx, self.letter_idx = 0, 0

    def reset(self):
        """Resets to the beginning of the text sequence."""
        self.seq_idx, self.letter_idx = 0, 0

    def advance(self) -> bool:
        """Advances to the next text and portrait to display. Returns FALSE if there's no more content."""
        self.seq_idx, self.letter_idx = self.seq_idx + 1, 0
        return self.seq_idx < len(self.texts)

    def call_hook(self):
        """Calls the current hook if it's not None."""
        if self.hooks is not None and self.hooks[self.seq_idx] is not None:
            self.hooks[self.seq_idx]()

    def get_next_letter(self) -> str:
        """Gets the next character of the current text. Returns '~' if there are no more characters."""
        current_text, char = self.texts[self.seq_idx], "~"
        if self.letter_idx < len(current_text):
            char = current_text[self.letter_idx]
            self.letter_idx += 1
        return char

    def get_portrait(self) -> AbstractImage:
        """Returns the current portrait."""
        portraits, portrait_index = self.portrait_seq[self.seq_idx]
        return self.portraits[portraits][portrait_index]
