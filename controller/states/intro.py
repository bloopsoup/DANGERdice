from .state import State
from ..utils import music_handler
from ..loader import load_static, load_some_sprites, load_all_sprites, load_font, load_sound
from ..themes import BUTTON_DEFAULT, INPUT_DEFAULT
from gui.elements import StaticBG, MovingBackgroundElement, PositionedTexts, Button, InputText
from gui.commands import TimerCommand


class Intro(State):
    """Screen to give your character a name."""

    def __init__(self):
        super().__init__()
        # self.name_display = PositionedTexts([load_static("black")], (0, 220), load_font("L"), 1, [(0, 0)], True)
        self.tutorial_display = PositionedTexts([load_static("black")], (0, 220), load_font("L"), 1, [(0, 0)], True)
        self.setup_canvas()

        self.destination = "player_menu"

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([load_static("name")], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_static("thick_clouds")], (-1, 0), (800, 600)), 0)

        self.canvas.add_element(self.tutorial_display)

        self.canvas.add_element(Button(load_some_sprites("music"), (730, 530), BUTTON_DEFAULT, music_handler.toggle), 0)
        i_box = InputText(load_all_sprites("input"), (0, 200), INPUT_DEFAULT, self.enter_name, load_font("L"))
        self.canvas.add_element(i_box, 1)
        self.canvas.add_element(Button(load_some_sprites("skip_tutorial"), (0, 300), BUTTON_DEFAULT, self.skip), 2)
        self.canvas.add_element(Button(load_some_sprites("back"), (0, 0), BUTTON_DEFAULT, self.back), 3)
        self.canvas.add_element(Button(load_some_sprites("confirm"), (700, 130), BUTTON_DEFAULT, i_box.submit_text), 4)

    def startup(self):
        self.player.name_display(True)
        self.player.health_display(False)
        self.player.display_mode("")
        self.player.direct_move(350, 472)

    def cleanup(self):
        self.text = self.font.render("", True, (0, 0, 0))

    def handle_event(self, event):
        """Needed a timer this time to finish the animation."""
        self.canvas.handle_event(event)

        if event.type == self.timer.event:
            self.to(self.destination)

    def update(self, surface, dt):
        """Needed for updating timer."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))

    def back(self):
        """Goes back to the previous state. Restores player settings to enable story."""
        self.player.current_level = "l0-1"
        self.destination = "player_menu"
        self.to(self.previous)

    # Functions

    def enter_name(self, text):
        """Once you entered a name, gives the player that name and moves him off screen. We then
           wait 2 seconds (to finish animation) and move onto the story state."""
        self.canvas.delete_group(1)
        self.canvas.delete_group(2)
        self.canvas.delete_group(3)
        self.canvas.delete_group(4)
        self.player.change_name(text)
        self.player.command_move(5, 0, 1000, 472)
        self.timer.activate(2)

    def skip(self):
        """Skips the story and tutorial level."""
        self.player.current_level = "l0-1"
        self.destination = "player_menu"
        self.player.exp = 1
        self.canvas.delete_group(2)
        self.text = self.font.render("Tutorial will be skipped.", True, (0, 0, 0))
