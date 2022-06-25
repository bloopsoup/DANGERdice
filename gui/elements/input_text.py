import pygame
from gui.elements.interactive import Interactive


class InputText(Interactive):
    """A place to input text."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], theme: dict, on_event,
                 font: pygame.font):
        # Uses two images: [active, inactive]
        super().__init__(images, pos, theme, on_event)
        self.font = font

        self.active = False
        self.text = ""
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))

    def current_picture_index(self) -> int:
        """Determines image index to use to reflect the state of the widget."""
        return 0 if self.active else 1

    def will_overflow(self, char: str) -> bool:
        """Determines whether adding char will make the text go past its boundaries."""
        char_s = self.font.render(char, True, (0, 0, 0))
        return self.text_surface.get_width() + char_s.get_width() + self.theme["padding"] >= self.reference.width

    def submit_text(self):
        """Calls on_event with self.text as an argument then clears itself."""
        self.on_event(self.text)
        self.text = ""

    def handle_event(self, event):
        """Clicking toggles the box which allows inputting text. ENTER to submit the text."""
        # Clicking on the input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.reference.collidepoint(pygame.mouse.get_pos()):
                self.active = not self.active
            else:
                self.active = False

        # Typing into the input box / submitting with ENTER
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.theme["play_sfx"]()
                self.submit_text()
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif not self.will_overflow(event.unicode):
                self.text += event.unicode

    def draw(self, surface: pygame.Surface):
        """Displays itself onto surface."""
        # Draw the input box
        selected_image = self.current_picture_index()
        surface.blit(self.images[selected_image], (self.pos.x, self.pos.y))
        self.draw_border(surface)

        # Draw the text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        offset = self.find_center_offset(self.text_surface)
        surface.blit(self.text_surface, (self.reference.x + offset.x, self.reference.y + offset.y))
