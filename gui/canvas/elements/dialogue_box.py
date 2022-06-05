import pygame

from gui.canvas.elements.interactive import Interactive


class DialogueData:
    """Dialogue related data."""

    def __init__(self, texts: list[str], portraits: list[pygame.Surface], portrait_seq: list[int]):
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
        return self.portraits[int(self.portrait_seq[self.seq_idx])]


class DialogueBox(Interactive):
    """Displays text in a box like it's typed."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event,
                 font, d_data: DialogueData):
        super().__init__(images, pos, theme, on_event)
        self.font = font
        self.frames = 0.03

        self.d_data = d_data

        self.active = False
        self.display = ""
        self.letter_idx = 0

        self.text_surface = self.font.render("", True, (0, 0, 0))

    def toggle_visibility(self):
        """Toggles visibility of the dialogue box."""
        self.active = not self.active

    def next_script(self) -> bool:
        """Moves to the next text and portrait. Returns FALSE if there's no more content."""
        self.count = 0
        self.display = ""
        self.letter_idx = 0

        if not self.d_data.advance():
            self.toggle_visibility()
            return False
        return True

    def handle_event(self, event):
        """Trigger an event by clicking on the dialogue box. Defaults to moving to the next script."""
        if self.reference.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            if self.on_event is not None:
                self.on_event()
            else:
                self.next_script()

    def update(self, surface: pygame.Surface, dt: float):
        """Displays itself onto surface."""
        if not self.active:
            return

        # Draw text box + portrait
        surface.blit(self.images[0], (self.pos.x, self.pos.y))
        self.draw_border(surface)
        surface.blit(self.d_data.get_portrait(), (self.pos.x, self.pos.y - 100))

        # Adding one letter at a time
        if self.letter_idx < len(self.d_data.get_text()):
            self.count += dt
            if self.count >= self.frames:
                self.count = 0

                char = self.d_data.get_text()[self.letter_idx]
                # (`) is a pause character
                if char != "`":
                    self.theme["play_sfx"]()
                    self.display += char
                self.letter_idx += 1

        # Display the text
        for i in range(self.theme["lines"]):
            self.text_surface = self.font.render(
                self.display[i * self.theme["LPL"]:(i+1) * self.theme["LPL"]], True, (0, 0, 0))
            surface.blit(self.text_surface, (self.reference.x + self.theme["padding"],
                                             self.reference.y + (self.theme["line_spacing"] * (i+1))))
