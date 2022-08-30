from core import run
from game.states import Attributions, Intro, MainMenu, Story, Tutorial

states = {
    "attributions": Attributions(),
    "intro": Intro(),
    "main_menu": MainMenu(),
    "story": Story(),
    "tutorial": Tutorial()
}

run("attributions", states)
