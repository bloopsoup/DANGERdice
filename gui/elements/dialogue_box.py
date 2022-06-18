import pygame
from gui.elements.interactive import Interactive
from gui.utils.dialogue_data import DialogueData


class DialogueBox(Interactive):
    """Displays text in a box like it's typed."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event,
                 font, d_data: DialogueData):
        super().__init__(images, pos, theme, on_event)
        self.dt_runner.set_frames(0.03)

        self.font = font
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
        self.display = ""
        self.letter_idx = 0

        if not self.d_data.advance():
            self.toggle_visibility()
            return False
        return True

    def add_letter(self):
        """Adds another letter from the script to the display text."""
        char = self.d_data.get_text()[self.letter_idx]
        # (`) is a pause character
        if char != "`":
            self.theme["play_sfx"]()
            self.display += char
        self.letter_idx += 1

    def handle_event(self, event):
        """Trigger an event by clicking on the dialogue box. Defaults to moving to the next script."""
        if self.reference.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            if self.on_event is not None:
                self.on_event()
            else:
                self.next_script()

    def update(self, dt: float):
        """Updating itself."""
        if not self.active:
            return

        # Adding one letter at a time
        if self.letter_idx < len(self.d_data.get_text()):
            self.dt_runner.dt_update(dt, self.add_letter)

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        if not self.active:
            return

        # Draw text box + portrait
        surface.blit(self.images[0], (self.pos.x, self.pos.y))
        self.draw_border(surface)
        surface.blit(self.d_data.get_portrait(), (self.pos.x, self.pos.y - 100))

        # Display the text
        for i in range(self.theme["lines"]):
            self.text_surface = self.font.render(
                self.display[i * self.theme["LPL"]:(i+1) * self.theme["LPL"]], True, (0, 0, 0))
            surface.blit(self.text_surface, (self.reference.x + self.theme["padding"],
                                             self.reference.y + (self.theme["line_spacing"] * (i+1))))
