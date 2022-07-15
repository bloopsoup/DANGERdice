import random
from .state import State
from .preamble import Preamble
from .battle import Battle
from ..loader import all_enemy_names


def add_battle_state(states: dict[str, State], stage: int, level: int, enemy_name: str):
    """Adds a preamble (by chance) and a battle to the states dictionary."""
    preamble = Preamble(enemy_name, random.randint(0, 5), "battle_stage{0}_level{1}".format(stage, level))
    states["pre_battle_stage{0}_level{1}".format(stage, level)] = preamble
    battle = Battle(enemy_name, stage, random.choice(["loot", "player_menu"]))
    states["battle_stage{0}_level{1}".format(stage, level)] = battle


def add_battle_states(states: dict[str, State], stage_structure: list[int]):
    """Adds preambles and battle states to the provided states dictionary following a structure."""
    for i, num_stages in enumerate(stage_structure):
        enemy_names = all_enemy_names()
        for j in range(num_stages):
            if i == 0 and j == 0:
                enemy_names.remove("aaron")
            add_battle_state(states, i, j, enemy_names.pop(random.randint(0, len(enemy_names) - 1)))
