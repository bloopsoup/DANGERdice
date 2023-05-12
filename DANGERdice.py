from src.core import run
from app.states import Attributions, Battle, Ending, GameOver, Intro, Inventory, Load, Loot, MainMenu, PlayerMenu, \
    Preamble, Save, Shop, Story, Tutorial

states = {
    "attributions": Attributions(),
    "battle": Battle(),
    "ending": Ending(),
    "game_over": GameOver(),
    "intro": Intro(),
    "inventory": Inventory(),
    "load": Load(),
    "loot": Loot(),
    "main_menu": MainMenu(),
    "player_menu": PlayerMenu(),
    "preamble": Preamble(),
    "save": Save(),
    "shop": Shop(),
    "story": Story(),
    "tutorial": Tutorial()
}

run("attributions", states)
