import pyglet
from .constants import translate_keys, translate_mouse
from ..components import tl_to_bl
from ..enums import EventType
from ..path import ICON_PATH
from ..control import Event, StateManager


class App(pyglet.window.Window):
    """Manages the game loop for pyglet."""

    def __init__(self, state_manager: StateManager):
        super().__init__(800, 600, "DANGERdice")
        self.set_icon(pyglet.image.load(ICON_PATH))
        self.state_manager = state_manager
        pyglet.clock.schedule_interval(self.on_update, 1 / 240.0)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol in translate_keys:
            self.state_manager.pass_event(Event(EventType.KEY_DOWN, key=translate_keys[symbol]))

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in translate_keys:
            self.state_manager.pass_event(Event(EventType.KEY_UP, key=translate_keys[symbol]))

    def on_text(self, text: str):
        self.state_manager.pass_event(Event(EventType.TEXT_INPUT, text=text))

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button in translate_mouse:
            pos = tl_to_bl((x, y), 600)
            self.state_manager.pass_event(Event(EventType.MOUSE_DOWN, mouse_button=translate_mouse[button], pos=pos))

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button in translate_mouse:
            pos = tl_to_bl((x, y), 600)
            self.state_manager.pass_event(Event(EventType.MOUSE_UP, mouse_button=translate_mouse[button], pos=pos))

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pos = tl_to_bl((x, y), 600)
        self.state_manager.pass_event(Event(EventType.MOUSE_MOVE, pos=pos))

    def on_update(self, dt: float):
        self.state_manager.update(dt)
        if self.state_manager.is_done():
            pyglet.app.exit()

    def on_draw(self):
        self.clear()
        self.state_manager.draw()
