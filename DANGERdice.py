from core import run
from game.states import Attributions, MainMenu

states = {
    "attributions": Attributions(),
    "main_menu": MainMenu()
}

run("attributions", states)
