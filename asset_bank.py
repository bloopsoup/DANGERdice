from utils.spritesheet import *
from entities.dice.
from utils.path import *


class AssetBank:
    """A container serving assets."""

    def __init__(self):
        self.sheets = load_sheets()
        self.enemies = load_enemies(self.sheets)
        self.dice = load_dice(self.sheets)
        self.fonts = load_fonts()

    def get_images(self, key: str, row: int, col: int, amount: int):
        """Wrapper around a spritesheet's load_some_images method."""
        assert key in self.sheets
        return self.sheets[key].load_some_images(row, col, amount)

    def get_enemy(self, key: str, tier: int):
        """Creates a new enemy object from the enemy catalog."""
        assert key in self.enemies
        enemy = self.enemies[key]()
        enemy.set_stats(tier)
        return enemy

    def get_dice(self, key: str):
        """Creates a new die object from the dice catalog."""
        assert key in self.dice
        return self.dice[key]()

    def get_font(self, key: str):
        """Gets a font."""
        assert key in self.fonts
        return self.fonts[key]


def load_sheets() -> dict:
    """Loads and returns all the sprite sheets used for the game."""
    return {"mc": Spritesheet(path_c("mc100x3x5.png"), 100, 100, 3, 5),
            "aaron": Spritesheet(path_c("ah120x3x5.png"), 120, 120, 3, 5),
            "dorita": Spritesheet(path_c("dorita130x5x8.png"), 130, 130, 5, 8),
            "wally": Spritesheet(path_c("whale200x250x5x5.png"), 200, 250, 5, 5),
            "duck": Spritesheet(path_c("duck180x150x5x5.png"), 180, 150, 5, 5),
            "migahexx.xml": Spritesheet(path_c("mik3x5x220x220.png"), 220, 220, 3, 5),
            "shop": Spritesheet(path_c("shop45x3x5.png"), 45, 45, 3, 5),
            "dice1": Spritesheet(path_c("1dice85x6x6.png"), 85, 85, 6, 6),
            "dice2": Spritesheet(path_c("2dice85x6x6.png"), 85, 85, 6, 6),
            "dice3": Spritesheet(path_c("3dice85x6x6.png"), 85, 85, 6, 6),
            "ria": Spritesheet(path_c("ria140x3x5.png"), 140, 140, 3, 5),
            "bursa": Spritesheet(path_c("bursa85x120x3x5.png"), 85, 120, 3, 5),
            "wandre": Spritesheet(path_c("wandre100x160x3x5.png"), 100, 160, 3, 5),
            "cena": Spritesheet(path_c("cena190x100x3x5.png"), 190, 100, 3, 5),
            "sosh": Spritesheet(path_c("sosh70x140x3x5.png"), 70, 140, 3, 5),
            "arca": Spritesheet(path_c("arca160x110x3x5.png"), 160, 110, 3, 5),
            "ellie": Spritesheet(path_c("ellie100x3x5.png"), 100, 100, 3, 5),
            "kiran": Spritesheet(path_c("kiran150x3x5.png"), 150, 150, 3, 5),
            "connor": Spritesheet(path_c("connor85x100x3x5.png"), 85, 100, 3, 5),
            "baggins": Spritesheet(path_c("baggins110x3x5.png"), 110, 110, 3, 5),
            "portrait1": Spritesheet(path_c("chat100x3x6.png"), 100, 100, 2, 6),
            "button": Spritesheet(path_b("1button70x3x6.png"), 70, 70, 3, 6),
            "button2": Spritesheet(path_b("2button75x500x6x3.png"), 75, 500, 6, 3),
            "button3": Spritesheet(path_b("3button70x3x6.png"), 70, 70, 3, 6),
            "button4": Spritesheet(path_b("4button50x200x2x3.png"), 50, 200, 2, 3)
            }


def load_enemies(sheets: dict) -> dict:
    """Loads and returns all the enemies used for the game where images are from SHEETS."""
    return {"player": lambda: Player(sheets["mc"].load_all_images(), -100, -100),
            "aaron": lambda: Aaron(sheets["aaron"].load_all_images(), -150, -150),
            "dorita": lambda: Dorita(sheets["dorita"].load_all_images(), -150, -150),
            "shopkeeper": lambda: Shopkeeper(sheets["shop"].load_all_images(), -150, -150),
            "wally": lambda: Wally(sheets["wally"].load_all_images(), -300, -300),
            "square": lambda: GSquare(sheets["dice1"].load_some_images(0, 0, 15), -100, -100),
            "duck": lambda: BadDuck(sheets["duck"].load_all_images(), -300, -300),
            "michael": lambda: Michael(sheets["migahexx.xml"].load_all_images(), -300, -300),
            "ria": lambda: Ria(sheets["ria"].load_all_images(), -300, -300),
            "wandre": lambda: Wandre(sheets["wandre"].load_all_images(), -300, -300),
            "cena": lambda: Cena(sheets["cena"].load_all_images(), -300, -300),
            "bursa": lambda: Bursa(sheets["bursa"].load_all_images(), -300, -300),
            "sosh": lambda: Sosh(sheets["sosh"].load_all_images(), -300, -300),
            "arca": lambda: Arca(sheets["arca"].load_all_images(), -300, -300),
            "ellie": lambda: Ellie(sheets["ellie"].load_all_images(), -300, -300),
            "kiran": lambda: Kiran(sheets["kiran"].load_all_images(), -300, -300),
            "connor": lambda: Connor(sheets["connor"].load_all_images(), -300, -300),
            "baggins": lambda: Baggins(sheets["baggins"].load_all_images(), -300, -300)
            }


def load_dice(sheets: dict) -> dict:
    """Loads and returns all the dice used for the game where images are from SHEETS."""
    return {"basic1": lambda: Die(sheets["dice1"].load_some_images(0, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 1, "basic1"),
            "basic2": lambda: Die(sheets["dice1"].load_some_images(1, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 2, "basic2"),
            "basic3": lambda: Die(sheets["dice1"].load_some_images(2, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 3, "basic3"),
            "basic4": lambda: Die(sheets["dice1"].load_some_images(3, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 4, "basic4"),
            "basic5": lambda: Die(sheets["dice1"].load_some_images(4, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 5, "basic5"),
            "poison1": lambda: Poison(sheets["dice1"].load_some_images(5, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 1,
                                      "poison1"),
            "poison2": lambda: Poison(sheets["dice2"].load_some_images(0, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 2,
                                      "poison2"),
            "poison3": lambda: Poison(sheets["dice2"].load_some_images(1, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 3,
                                      "poison3"),
            "heal1": lambda: Heal(sheets["dice2"].load_some_images(2, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 1, "heal1"),
            "heal2": lambda: Heal(sheets["dice2"].load_some_images(3, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 2, "heal2"),
            "heal3": lambda: Heal(sheets["dice2"].load_some_images(4, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 3, "heal3"),
            "divider1": lambda: Divider(sheets["dice3"].load_some_images(0, 0, 6), 0, 0, [1, 1, 1, 1, 2, 2],
                                        1, "divider1", ""),
            "divider2": lambda: Divider(sheets["dice3"].load_some_images(1, 0, 6), 0, 0, [1, 1, 1, 2, 2, 2],
                                        1, "divider2", "+"),
            "divider3": lambda: Divider(sheets["dice3"].load_some_images(2, 0, 6), 0, 0, [1, 1, 2, 2, 2, 3],
                                        1, "divider3", "++"),
            "multiplier1": lambda: Multiplier(sheets["dice3"].load_some_images(3, 0, 6), 0, 0, [1, 1, 1, 1, 2, 2],
                                              1, "multiplier1", ""),
            "multiplier2": lambda: Multiplier(sheets["dice3"].load_some_images(4, 0, 6), 0, 0, [1, 1, 1, 2, 2, 2],
                                              1, "multiplier2", "+"),
            "multiplier3": lambda: Multiplier(sheets["dice3"].load_some_images(5, 0, 6), 0, 0, [1, 1, 2, 2, 2, 3], 1,
                                              "multiplier3", "++")
            }


def load_fonts() -> dict:
    """Loads and returns all the fonts used for the game."""
    return {"SS": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 25),
            "S": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 30),
            "M": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 40),
            "L": pygame.font.Font(rp("assets/VT323-Regular.ttf"), 50)}
