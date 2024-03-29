from .game_state import GameState
from ..config import load_idle_animation, DIALOGUE_DEFAULT, TEXT_WHITE_LARGE
from src.core import get_image, get_all_sprites, SOUND_PLAYER
from src.gui.elements import StaticBG, MovingBackgroundElement, PTexts, Idle, DialogueBox
from src.gui.commands import TimerCommand, MoveCommand
from src.gui.utils import DialogueData


class Story(GameState):
    """Today is not your lucky day."""

    def __init__(self):
        super().__init__()
        self.text_display = PTexts([get_image("black")], (0, 220), TEXT_WHITE_LARGE, [(0, 0)], True)
        self.player_display = Idle(get_all_sprites("player"), (0, 0), None, load_idle_animation("player"))
        self.aaron_display = Idle(get_all_sprites("aaron"), (0, 0), None, load_idle_animation("aaron"))
        self.dorita_display = Idle(get_all_sprites("dorita"), (0, 0), None, load_idle_animation("dorita"))
        self.dialogue_box = DialogueBox([get_image("text_box")], (100, 350), DIALOGUE_DEFAULT,
                                        lambda: self.to("tutorial"), self.load_story_dialogue())

    def setup_canvas(self):
        self.canvas.add_element(StaticBG([get_image("casino")], (0, 0)), "")
        self.canvas.add_element(MovingBackgroundElement([get_image("thin_clear_clouds")], (-1, 0), (800, 600)), "")
        self.canvas.add_element(StaticBG([get_image("ground")], (0, 0)), "")
        self.canvas.add_element(self.text_display, "")
        self.text_display.set_text(0, "")
        self.canvas.add_element(self.player_display, "")
        self.player_display.set_position((-100, 257))
        self.canvas.add_element(self.aaron_display, "")
        self.aaron_display.set_position((900, 237))
        self.canvas.add_element(self.dorita_display, "")
        self.dorita_display.set_position((900, 227))
        self.canvas.add_element(self.dialogue_box, "")
        self.dialogue_box.reset_scripts()

    def setup_commands(self):
        self.command_queue.add([MoveCommand(self.player_display, (2, 0), (-100, 257), (100, 257),
                                            lambda: self.dialogue_box.toggle_visibility())])

    def setup_music(self):
        SOUND_PLAYER.stop_music()

    def load_story_dialogue(self) -> DialogueData:
        """Loads the dialogue for the story."""
        texts = ["Ah Monday.", "Another day running my shady casino.", "Good morning.", "Wow, you're already here.",
                 "Don't you think it's a bit early for gambling everything away?", "It's never too early.",
                 "And besides, ````````I'm feeling lucky.", "And so do other people.",
                 "There goes the last of my money.", "Why do people keep getting jackpots?", "Told you so.",
                 "Got my jackpot as well, ````so where's my money?", "Well... ``````", "Do you take I.O.U's?", "No.",
                 "Then I have another solution.", "What is it?", "What the...", "MY MONEY!"]
        portrait_seq = [(0, 0), (0, 1), (1, 0), (0, 1), (0, 6), (1, 1), (1, 2), (1, 0), (0, 5), (0, 6), (1, 1), (1, 6),
                        (0, 7), (0, 0), (1, 3), (0, 2), (1, 3), (1, 6), (1, 4)]
        portraits = [get_all_sprites("player_icons"), get_all_sprites("dorita_icons")]
        hooks = [None, self.enter_dorita, None, None, None, None, None, self.enter_transition, None, self.enter_dorita,
                 None, None, None, None, None, None, self.exit_player, None, None]
        return DialogueData(texts, portraits, portrait_seq, hooks)

    def enter_player(self):
        """Player enters the picture."""
        self.command_queue.add([MoveCommand(self.player_display, (5, 0), (-100, 257), (100, 257),
                                            self.dialogue_box.toggle_visibility)])

    def exit_player(self):
        """Player runs away."""
        self.dialogue_box.toggle_visibility()
        self.command_queue.add([MoveCommand(self.player_display, (10, 0), (100, 257), (1000, 257),
                                            self.dialogue_box.toggle_visibility)])

    def enter_dorita(self):
        """Dorita comes in to talk."""
        self.dialogue_box.toggle_visibility()
        self.command_queue.add([MoveCommand(self.dorita_display, (3, 0), (900, 227), (580, 227),
                                            self.dialogue_box.toggle_visibility)])

    def enter_transition(self):
        """Show a time transition."""
        self.dialogue_box.toggle_visibility()
        self.canvas.insert_element(StaticBG([get_image("black")], (0, 0)), "black_screen", 3)
        self.text_display.set_text(0, "2 HOURS LATER")
        self.player_display.set_position((-100, 257))
        self.dorita_display.set_position((900, 227))
        SOUND_PLAYER.play_sfx("one")
        self.command_queue.add([TimerCommand(1.5, self.exit_transition)])

    def exit_transition(self):
        """Exit the time transition."""
        self.canvas.delete_group("black_screen")
        self.text_display.set_text(0, "")
        self.aaron_display.set_position((300, 237))
        self.command_queue.add([MoveCommand(self.aaron_display, (5, 0), (300, 237), (1000, 237), self.enter_player)])
