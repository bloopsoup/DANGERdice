import sys
import pygame
import asyncio
from ..enums import EventType
from ..control import Event, StateManager
from .constants import translate_keys


class App:
    """Manages the game loop for pygame."""

    def __init__(self, state_manager: StateManager):
        self.state_manager = state_manager
        self.fps, self.clock = 60, pygame.time.Clock()

    def event_loop(self):
        """Processes events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key in translate_keys:
                self.state_manager.pass_event(Event(EventType.KEY_DOWN, key=translate_keys[event.key]))
            elif event.type == pygame.KEYUP and event.key in translate_keys:
                self.state_manager.pass_event(Event(EventType.KEY_UP, key=translate_keys[event.key]))
            elif event.type == pygame.TEXTINPUT:
                self.state_manager.pass_event(Event(EventType.TEXT_INPUT, text=event.text))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.state_manager.pass_event(Event(EventType.MOUSE_DOWN, pos=pygame.mouse.get_pos()))
            elif event.type == pygame.MOUSEBUTTONUP:
                self.state_manager.pass_event(Event(EventType.MOUSE_UP, pos=pygame.mouse.get_pos()))
            elif event.type == pygame.MOUSEMOTION:
                self.state_manager.pass_event(Event(EventType.MOUSE_MOVE, pos=pygame.mouse.get_pos()))

    async def main_loop(self):
        """Where the game takes place."""
        while not self.state_manager.is_done():
            dt = self.clock.tick(self.fps) / 1000
            if dt >= 0.05:
                continue
            self.event_loop()
            self.state_manager.update(dt)
            self.state_manager.draw()
            pygame.display.update()
            await asyncio.sleep(0)
