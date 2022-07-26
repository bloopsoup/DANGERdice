import pygame
from .interactive import Interactive
from ..utils import DialogueData


class DialogueBox(Interactive):
    """Displays text in a box like it's typed."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event,
                 font: pygame.font.Font, d_data: DialogueData):
        super().__init__(images, pos, theme, on_event)
        self.dt_runner.set_frames(0.03)
        self.font = font
        self.d_data = d_data
        self.active = False
        self.display = ""
        self.letter_idx = 0

    def toggle_visibility(self):
        """Toggles visibility of the dialogue box."""
        self.active = not self.active

    def reset_scripts(self):
        """Reset the texts and portraits to the beginning."""
        self.d_data.reset()

    def next_script(self) -> bool:
        """Moves to the next text and portrait and calls the current hook. Returns FALSE if there's no more content."""
        self.display = ""
        self.letter_idx = 0
        self.d_data.call_hook()
        if not self.d_data.advance():
            self.toggle_visibility()
            return False
        return True

    def add_letter(self):
        """Adds another letter from the script to the display text."""
        char = self.d_data.get_text()[self.letter_idx]
        if char != "`":
            self.theme["play_sfx"]()
            self.display += char
        self.letter_idx += 1

    def handle_event(self, event):
        """Clicking on the dialogue box goes to the next script. Calls on_event if there are no more scripts."""
        if self.is_mouse_over_element() and event.type == pygame.MOUSEBUTTONDOWN and self.active and self.clickable:
            if not self.next_script():
                self.on_event()

    def update(self, dt: float):
        """Updating itself."""
        if not self.active:
            return
        if self.letter_idx < len(self.d_data.get_text()):
            self.dt_runner.dt_update(dt, self.add_letter)

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        if not self.active:
            return

        surface.blit(self.images[0], (self.pos.x, self.pos.y))
        self.draw_border(surface)
        surface.blit(self.d_data.get_portrait(), (self.pos.x + self.theme["p_padding"][0],
                                                  self.pos.y + self.theme["p_padding"][1]))

        for i in range(self.theme["lines"]):
            text_surface = self.font.render(self.display[i*self.theme["LPL"]:(i+1)*self.theme["LPL"]], True, (0, 0, 0))
            surface.blit(text_surface, (self.reference.x + self.theme["padding"][0],
                                        self.reference.y + (self.theme["padding"][1] * (i+1))))
