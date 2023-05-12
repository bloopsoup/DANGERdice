import pyglet
from pyglet.window import key, mouse
from ..enums import Key, MouseButton
from ..path import FONT_PATH, sound_config, static_config, spritesheet_config

###############
#    SETUP    #
###############

pyglet.font.add_file(FONT_PATH)

###############
#  CONSTANTS  #
###############

loaded_fonts = {
    "SS": ("VT323", 18),
    "S": ("VT323", 20),
    "M": ("VT323", 28),
    "L": ("VT323", 38)
}
loaded_static = {key: pyglet.image.load(static_config[key]) for key in static_config}
loaded_sheets = {key: [pyglet.image.load(spritesheet_config[key][0])] + spritesheet_config[key][1:]
                 for key in spritesheet_config}
loaded_sounds = {key: pyglet.media.load(sound_config[key], streaming=False) for key in sound_config}

translate_keys = {
    key.A: Key.A, key.B: Key.B, key.C: Key.C, key.D: Key.D, key.E: Key.E, key.F: Key.F, key.G: Key.G, key.H: Key.H,
    key.I: Key.I, key.J: Key.J, key.K: Key.K, key.L: Key.L, key.M: Key.M, key.N: Key.N, key.O: Key.O, key.P: Key.P,
    key.Q: Key.Q, key.R: Key.R, key.S: Key.S, key.T: Key.T, key.U: Key.U, key.V: Key.V, key.W: Key.W, key.X: Key.X,
    key.Y: Key.Y, key.Z: Key.Z,
    key._0: Key._0, key._1: Key._1, key._2: Key._2, key._3: Key._3, key._4: Key._4, key._5: Key._5, key._6: Key._6,
    key._7: Key._7, key._8: Key._8,key._9: Key._9,
    key.ESCAPE: Key.ESCAPE, key.MINUS: Key.MINUS, key.EQUAL: Key.EQUALS, key.BACKSPACE: Key.BACKSPACE,
    key.BRACKETLEFT: Key.LEFT_BRACKET, key.BRACKETRIGHT: Key.RIGHT_BRACKET, key.BACKSLASH: Key.BACKSLASH,
    key.SEMICOLON: Key.SEMICOLON, key.APOSTROPHE: Key.APOSTROPHE, key.ENTER: Key.ENTER, key.LSHIFT: Key.SHIFT,
    key.RSHIFT: Key.SHIFT, key.COMMA: Key.COMMA, key.PERIOD: Key.PERIOD, key.SLASH: Key.SLASH, key.LEFT: Key.LEFT,
    key.RIGHT: Key.RIGHT, key.UP: Key.UP, key.DOWN: Key.DOWN,
}

translate_mouse = {
    mouse.LEFT: MouseButton.LEFT,
    mouse.MIDDLE: MouseButton.MIDDLE,
    mouse.RIGHT: MouseButton.RIGHT
}
