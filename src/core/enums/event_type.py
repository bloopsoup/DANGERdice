from enum import Enum


class EventType(Enum):
    MOUSE_DOWN = 0
    MOUSE_UP = 1
    MOUSE_MOVE = 2
    KEY_DOWN = 3
    KEY_UP = 4
    TEXT_INPUT = 5
