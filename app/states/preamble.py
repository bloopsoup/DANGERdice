from .game_state import GameState
from ..config import load_idle_animation, load_dialogue, DIALOGUE_DEFAULT
from src.core import get_image, get_all_sprites, SOUND_PLAYER
from src.gui.elements import StaticBG, MovingBackgroundElement, Idle, DialogueBox
from src.gui.commands import AnimationHandler


class Preamble(GameState):
    """Sometimes you have a chit-chat before battle."""

    def __init__(self):
        super().__init__()
        self.player_display = Idle(get_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.enemy_display, self.animation_handler, self.dialogue_box = None, None, None

    def setup_state(self):
        l_data = self.level_manager.get_level()
        self.enemy_display = Idle(get_all_sprites(l_data["enemy"]), (0, 0), None, load_idle_animation(l_data["enemy"]))
        self.animation_handler = AnimationHandler(self.player_display, (60, 257), self.enemy_display,
                                                  (740 - self.enemy_display.get_width(),
                                                   357 - self.enemy_display.get_height()), self.command_queue)
        self.dialogue_box = DialogueBox([get_image("text_box")], (100, 350), DIALOGUE_DEFAULT,
                                        lambda: self.to("battle"), load_dialogue(l_data["enemy"], l_data["tier"]))

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("hills")], (0, 0)), "")
        self.canvas.add_element(MovingBackgroundElement([get_image("thick_clouds")], (-1, 0), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("ground")], (0, 0)), "")
        self.canvas.add_element(self.player_display, "")
        self.player_display.set_position((-300, 257))
        self.canvas.add_element(self.enemy_display, "")
        self.enemy_display.set_position((1000, 357 - self.enemy_display.get_height()))
        self.canvas.add_element(self.dialogue_box, "")
        self.dialogue_box.reset_scripts()

    def setup_commands(self):
        self.animation_handler.to_start(lambda: self.dialogue_box.toggle_visibility())

    def setup_music(self):
        SOUND_PLAYER.stop_music()
