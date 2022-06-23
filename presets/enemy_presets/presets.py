from random import randint

AARON_STATS = [
    {"level": 1, "health_factor": 20, "money_factor": 0, "preference": ["basic1", "basic1"]},
    {"level": randint(6, 8), "health_factor": 11, "money_factor": 40, "preference": ["basic2", "basic2"]},
    {"level": randint(8, 11), "health_factor": 9, "money_factor": 60, "preference": ["basic3", "basic3", "basic2"]},
    {"level": randint(10, 13), "health_factor": 11, "money_factor": 75, "preference": ["basic4", "basic3", "basic3"]},
    {"level": randint(13, 16), "health_factor": 10, "money_factor": 70, "preference": ["basic4", "basic5"]},
    {"level": randint(16, 17), "health_factor": 12, "money_factor": 80, "preference": ["basic5", "basic5"]}
]

ARCA_STATS = [
    {"level": randint(2, 3), "health_factor": 8, "money_factor": 15, "preference": ["basic1", "basic1"]},
    {"level": randint(5, 6), "health_factor": 10, "money_factor": 25, "preference": ["basic1", "basic1"]},
    {"level": randint(7, 9), "health_factor": 12, "money_factor": 30, "preference": ["basic1", "basic1"]},
    {"level": randint(10, 12), "health_factor": 12, "money_factor": 50, "preference": ["basic1", "basic1"]},
    {"level": randint(12, 15), "health_factor": 14, "money_factor": 70, "preference": ["basic1", "basic1"]},
    {"level": randint(15, 20), "health_factor": 18, "money_factor": 80, "preference": ["basic1", "basic1"]}
]

BADUCK_STATS = [
    {"level": randint(2, 4), "health_factor": 7, "money_factor": 25, "preference": ["poison1", "poison1"]},
    {"level": randint(5, 7), "health_factor": 8, "money_factor": 30, "preference": ["poison2", "poison2", "poison2"]},
    {"level": randint(7, 10), "health_factor": 8, "money_factor": 30, "preference": ["poison2", "poison2", "divider3"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 50, "preference": ["poison3", "poison2", "divider3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 70, "preference": ["poison3", "poison3", "divider3"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 80, "preference": ["poison3", "poison3", "poison3", "divider3"]}
]

BAGGINS_STATS = [
    {"level": randint(3, 4), "health_factor": 13, "money_factor": 30, "preference": ["basic2"]},
    {"level": randint(5, 6), "health_factor": 14, "money_factor": 35, "preference": ["basic3"]},
    {"level": randint(6, 7), "health_factor": 14, "money_factor": 55, "preference": ["basic4"]},
    {"level": randint(8, 9), "health_factor": 15, "money_factor": 65, "preference": ["basic5"]},
    {"level": randint(10, 11), "health_factor": 16, "money_factor": 80, "preference": ["basic5", "heal3"]},
    {"level": randint(11, 14), "health_factor": 16, "money_factor": 100, "preference": ["basic5", "heal3", "heal3"]}
]

BURSA_STATS = [
    {"level": randint(4, 5), "health_factor": 6, "money_factor": 25, "preference": ["basic1"]},
    {"level": randint(6, 7), "health_factor": 8, "money_factor": 30, "preference": ["basic2", "basic2", "heal1"]},
    {"level": randint(7, 10), "health_factor": 9, "money_factor": 45, "preference": ["basic3", "basic2", "heal2"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 65, "preference": ["basic3", "basic3", "heal3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 75, "preference": ["basic4", "basic4", "heal3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 85, "preference": ["basic5", "basic5", "heal3"]}
]

CENA_STATS = [
    {"level": randint(3, 4), "health_factor": 5, "money_factor": 15, "preference": ["basic1", "poison1"]},
    {"level": randint(6, 8), "health_factor": 7, "money_factor": 30, "preference": ["basic2", "poison2", "poison2"]},
    {"level": randint(8, 11), "health_factor": 8, "money_factor": 40, "preference": ["basic2", "poison2", "poison3", "heal2"]},
    {"level": randint(11, 13), "health_factor": 9, "money_factor": 60, "preference": ["poison3", "poison3", "heal2"]},
    {"level": randint(13, 15), "health_factor": 10, "money_factor": 75, "preference": ["poison3", "poison3", "heal3"]},
    {"level": randint(15, 17), "health_factor": 12, "money_factor": 80, "preference": ["poison3", "poison3", "poison3", "heal3"]}
]

CONNOR_STATS = [
    {"level": randint(3, 4), "health_factor": 9, "money_factor": 15, "preference": ["basic1", "basic1", "basic1", "basic1"]},
    {"level": randint(5, 7), "health_factor": 9, "money_factor": 20, "preference": ["basic2", "basic2", "basic1", "basic1"]},
    {"level": randint(6, 8), "health_factor": 11, "money_factor": 40, "preference": ["basic3", "basic2", "basic1"]},
    {"level": randint(9, 11), "health_factor": 11, "money_factor": 50, "preference": ["basic4", "basic2"]},
    {"level": randint(11, 12), "health_factor": 13, "money_factor": 70, "preference": ["basic5", "basic5", "basic2"]},
    {"level": randint(13, 15), "health_factor": 15, "money_factor": 85, "preference": ["basic4", "multiplier3", "multiplier3"]}
]

DORITA_STATS = [
    {"level": randint(3, 4), "health_factor": 6, "money_factor": 20, "preference": ["basic1", "basic1"]},
    {"level": randint(4, 6), "health_factor": 10, "money_factor": 40, "preference": ["basic2", "basic2", "divider2"]},
    {"level": randint(7, 9), "health_factor": 11, "money_factor": 60, "preference": ["basic2", "basic3", "divider3"]},
    {"level": randint(10, 12), "health_factor": 12, "money_factor": 80, "preference": ["basic4", "basic3", "basic3", "divider3"]},
    {"level": randint(12, 15), "health_factor": 12, "money_factor": 90, "preference": ["basic5", "divider3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 100, "preference": ["basic5", "basic5", "divider3"]}
]

ELLIE_STATS = [
    {"level": randint(2, 3), "health_factor": 9, "money_factor": 16, "preference": ["basic1"]},
    {"level": randint(4, 5), "health_factor": 9, "money_factor": 25, "preference": ["basic1", "basic2"]},
    {"level": randint(6, 8), "health_factor": 10, "money_factor": 40, "preference": ["basic1", "basic2", "basic2", "heal1"]},
    {"level": randint(9, 11), "health_factor": 12, "money_factor": 55, "preference": ["basic1", "basic3", "poison2", "heal2"]},
    {"level": randint(11, 15), "health_factor": 14, "money_factor": 65, "preference": ["basic1", "basic4", "basic4", "heal3"]},
    {"level": randint(15, 17), "health_factor": 15, "money_factor": 75, "preference": ["basic1", "basic5", "heal3"]}
]

KIRAN_STATS = [
    {"level": randint(3, 5), "health_factor": 10, "money_factor": 20, "preference": ["basic1", "heal1"]},
    {"level": randint(5, 6), "health_factor": 11, "money_factor": 25, "preference": ["basic2", "basic2", "heal1"]},
    {"level": randint(6, 8), "health_factor": 12, "money_factor": 45, "preference": ["basic3", "basic3", "heal2"]},
    {"level": randint(9, 10), "health_factor": 12, "money_factor": 55, "preference": ["basic4", "basic4", "heal2"]},
    {"level": randint(11, 13), "health_factor": 15, "money_factor": 75, "preference": ["basic5", "basic5", "heal3"]},
    {"level": randint(15, 17), "health_factor": 15, "money_factor": 85, "preference": ["basic5", "basic5", "divider3", "multiplier3"]}
]

MIGAHEXX_STATS = [
    {"level": randint(5, 7), "health_factor": 6, "money_factor": 55, "preference": ["basic1", "multiplier1"]},
    {"level": randint(6, 8), "health_factor": 7, "money_factor": 70, "preference": ["basic2", "multiplier2"]},
    {"level": randint(8, 11), "health_factor": 8, "money_factor": 80, "preference": ["basic2", "basic2", "multiplier2"]},
    {"level": randint(11, 13), "health_factor": 10, "money_factor": 90, "preference": ["basic3", "multiplier3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 110, "preference": ["basic4", "basic4", "multiplier3"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 120, "preference": ["basic5", "basic5", "multiplier3"]}
]

PLAYER_STATS = [{"level": 1, "health_factor": 100, "money_factor": 100, "preference": ["basic1", "basic1"]}]

RIA_STATS = [
    {"level": randint(5, 6), "health_factor": 9, "money_factor": 40, "preference": ["basic1", "basic1", "heal1"]},
    {"level": randint(6, 8), "health_factor": 8, "money_factor": 50, "preference": ["basic2", "basic2", "heal2"]},
    {"level": randint(8, 11), "health_factor": 10, "money_factor": 70, "preference": ["basic3", "basic2", "basic1", "heal2"]},
    {"level": randint(11, 13), "health_factor": 11, "money_factor": 90, "preference": ["basic3", "basic3", "heal2"]},
    {"level": randint(13, 15), "health_factor": 13, "money_factor": 110, "preference": ["basic4", "basic4", "heal3"]},
    {"level": randint(15, 17), "health_factor": 10, "money_factor": 120, "preference": ["basic5", "basic5", "heal2", "heal3"]}
]

SHOPKEEPER_STATS = [
    {"level": randint(8, 10), "health_factor": 13, "money_factor": 300, "preference": ["basic2", "basic2", "multiplier1", "multiplier1"]},
    {"level": randint(10, 13), "health_factor": 15, "money_factor": 500, "preference": ["basic3", "multiplier1", "poison2", "poison2"]},
    {"level": randint(13, 15), "health_factor": 17, "money_factor": 800, "preference": ["basic3", "multiplier2", "heal2", "poison2"]},
    {"level": randint(15, 17), "health_factor": 19, "money_factor": 1000, "preference": ["basic4", "multiplier3", "heal3", "poison3"]},
    {"level": randint(17, 19), "health_factor": 21, "money_factor": 1200, "preference": ["basic5", "multiplier3", "multiplier3", "heal3"]},
    {"level": randint(20, 21), "health_factor": 23, "money_factor": 1500, "preference": ["basic5", "basic5", "multiplier3", "multiplier3"]}
]

SOSH_STATS = [
    {"level": randint(3, 4), "health_factor": 7, "money_factor": 15, "preference": ["basic1", "basic1"]},
    {"level": randint(5, 6), "health_factor": 9, "money_factor": 20, "preference": ["basic2", "multiplier2"]},
    {"level": randint(7, 9), "health_factor": 9, "money_factor": 40, "preference": ["basic2", "basic2", "multiplier3"]},
    {"level": randint(10, 12), "health_factor": 10, "money_factor": 60, "preference": ["basic3", "multiplier3"]},
    {"level": randint(12, 15), "health_factor": 12, "money_factor": 80, "preference": ["basic4", "basic4", "multiplier3"]},
    {"level": randint(15, 17), "health_factor": 14, "money_factor": 90, "preference": ["basic5"]}
]

SQUARE_STATS = [
    {"level": randint(3, 4), "health_factor": 7, "money_factor": 10, "preference": ["basic1", "poison1", "heal1"]},
    {"level": randint(6, 7), "health_factor": 9, "money_factor": 30, "preference": ["basic2", "poison2", "heal2", "divider2"]},
    {"level": randint(7, 9), "health_factor": 9, "money_factor": 40, "preference": ["basic2", "poison2", "heal2", "basic3"]},
    {"level": randint(10, 12), "health_factor": 9, "money_factor": 60, "preference": ["basic3", "poison3", "divider3", "basic3"]},
    {"level": randint(12, 15), "health_factor": 10, "money_factor": 80, "preference": ["basic4", "basic5", "divider3", "heal3"]},
    {"level": randint(15, 17), "health_factor": 12, "money_factor": 90, "preference": ["basic5", "poison3", "divider3", "heal3"]}
]

WALLY_STATS = [
    {"level": randint(3, 4), "health_factor": 15, "money_factor": 70, "preference": ["basic2"]},
    {"level": randint(5, 8), "health_factor": 10, "money_factor": 80, "preference": ["basic2", "heal1"]},
    {"level": randint(8, 11), "health_factor": 10, "money_factor": 100, "preference": ["basic2", "basic2", "heal1", "heal1"]},
    {"level": randint(11, 13), "health_factor": 11, "money_factor": 120, "preference": ["basic3", "basic3"]},
    {"level": randint(13, 16), "health_factor": 12, "money_factor": 140, "preference": ["basic5", "basic5"]},
    {"level": randint(15, 17), "health_factor": 13, "money_factor": 150, "preference": ["basic5", "basic5", "heal2"]},
]

WANDRE_STATS = [
    {"level": randint(3, 5), "health_factor": 8, "money_factor": 30, "preference": ["basic1", "basic1", "divider3"]},
    {"level": randint(6, 7), "health_factor": 9, "money_factor": 40, "preference": ["basic2", "basic2", "divider2"]},
    {"level": randint(7, 10), "health_factor": 9, "money_factor": 60, "preference": ["basic3", "basic2", "divider3"]},
    {"level": randint(10, 12), "health_factor": 10, "money_factor": 80, "preference": ["basic4", "basic3", "divider3"]},
    {"level": randint(13, 15), "health_factor": 12, "money_factor": 100, "preference": ["basic5", "basic4", "divider3", "heal2"]},
    {"level": randint(15, 17), "health_factor": 15, "money_factor": 110, "preference": ["basic5", "basic5", "divider3", "heal3"]}
]

presets = {
    "aaron": AARON_STATS,
    "arca": ARCA_STATS,
    "baduck": BADUCK_STATS,
    "baggins": BAGGINS_STATS,
    "cena": CENA_STATS,
    "connor": CONNOR_STATS,
    "dorita": DORITA_STATS,
    "ellie": ELLIE_STATS,
    "kiran": KIRAN_STATS,
    "migahexx.xml": MIGAHEXX_STATS,
    "player": PLAYER_STATS,
    "ria": RIA_STATS,
    "shopkeeper": SHOPKEEPER_STATS,
    "sosh": SOSH_STATS,
    "square": SQUARE_STATS,
    "wally": WALLY_STATS,
    "wandre": WANDRE_STATS
}
