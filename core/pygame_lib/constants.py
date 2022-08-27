import pygame
from core.enums import Key, MouseButton

###############
#    SETUP    #
###############

pygame.init()
pygame.display.set_icon(pygame.image.load("../../assets/icon.png"))
pygame.display.set_caption("DANGERdice")
pygame.key.set_repeat(500, 100)

###############
#  CONSTANTS  #
###############

surface = pygame.display.set_mode((800, 600))

loaded_fonts = {
    "SS": pygame.font.Font("../../assets/VT323-Regular.ttf", 25),
    "S": pygame.font.Font("../../assets/VT323-Regular.ttf", 30),
    "M": pygame.font.Font("../../assets/VT323-Regular.ttf", 40),
    "L": pygame.font.Font("../../assets/VT323-Regular.ttf", 50)
}

loaded_sounds = {

}

translate_keys = {
    pygame.K_a: Key.A, pygame.K_b: Key.B, pygame.K_c: Key.C, pygame.K_d: Key.D, pygame.K_e: Key.E, pygame.K_f: Key.F,
    pygame.K_g: Key.G, pygame.K_h: Key.H, pygame.K_i: Key.I, pygame.K_j: Key.J, pygame.K_k: Key.K, pygame.K_l: Key.L,
    pygame.K_m: Key.M, pygame.K_n: Key.N, pygame.K_o: Key.O, pygame.K_p: Key.P, pygame.K_q: Key.Q, pygame.K_r: Key.R,
    pygame.K_s: Key.S, pygame.K_t: Key.T, pygame.K_u: Key.U, pygame.K_v: Key.V, pygame.K_w: Key.W, pygame.K_x: Key.X,
    pygame.K_y: Key.Y, pygame.K_z: Key.Z,
    pygame.K_0: Key._0, pygame.K_1: Key._1, pygame.K_2: Key._2, pygame.K_3: Key._3, pygame.K_4: Key._4,
    pygame.K_5: Key._5, pygame.K_6: Key._6, pygame.K_7: Key._7, pygame.K_8: Key._8, pygame.K_9: Key._9,
    pygame.K_ESCAPE: Key.ESCAPE, pygame.K_MINUS: Key.MINUS, pygame.K_EQUALS: Key.EQUALS,
    pygame.K_BACKSPACE: Key.BACKSPACE, pygame.K_LEFTBRACKET: Key.LEFT_BRACKET, pygame.K_RIGHTBRACKET: Key.RIGHT_BRACKET,
    pygame.K_BACKSLASH: Key.BACKSLASH, pygame.K_SEMICOLON: Key.SEMICOLON, pygame.K_QUOTE: Key.APOSTROPHE,
    pygame.K_RETURN: Key.ENTER, pygame.K_LSHIFT: Key.SHIFT, pygame.K_RSHIFT: Key.SHIFT, pygame.K_COMMA: Key.COMMA,
    pygame.K_PERIOD: Key.PERIOD, pygame.K_SLASH: Key.SLASH, pygame.K_LEFT: Key.LEFT, pygame.K_RIGHT: Key.RIGHT,
    pygame.K_UP: Key.UP, pygame.K_DOWN: Key.DOWN,
}

translate_mouse = {
    0: MouseButton.LEFT,
    1: MouseButton.MIDDLE,
    2: MouseButton.RIGHT
}