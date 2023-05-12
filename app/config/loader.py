import random
from . import dice_config, enemy_config, idle_animation_config, dialogue_config
from ..entities.enemies import Enemy, Player
from ..entities.dice import Die, DiceSet
from ..entities.level import LevelManager
from ..entities.shop import ShopInventory
from src.core import get_all_sprites
from src.gui.utils import IndexCycler, DialogueData


def load_idle_animation(animation: str) -> IndexCycler:
    """Loads an idle animation."""
    assert animation in idle_animation_config, f"{animation} is not a valid animation"
    indices, frames = idle_animation_config[animation]
    return IndexCycler(indices, frames)


def load_dialogue(dialogue: str, tier: int) -> DialogueData:
    """Loads dialogue."""
    assert dialogue in dialogue_config, f"no dialogue has that name {dialogue}"
    texts, portrait_seq = dialogue_config[dialogue][tier]
    portraits = [get_all_sprites("player_icons"), get_all_sprites(f"{dialogue}_icons")]
    return DialogueData(texts, portraits, portrait_seq)


def create_die(die_type: str) -> Die:
    """Creates a die."""
    assert die_type in dice_config, f"{die_type} is not a valid die type"
    side, multiple, additional_cost, damage_type, safe = dice_config[die_type]
    return Die(side, multiple, int(130 * 1.5 * (multiple + 0.5)) + additional_cost, damage_type, safe)


def create_random_die() -> Die:
    """Creates a random die."""
    return create_die(random.choice(list(dice_config.keys())))


def create_dice_set(preference: list[str]) -> DiceSet:
    """Creates a dice set from a preference."""
    return DiceSet([create_die(die_name) for die_name in preference])


def create_shop_inventory() -> ShopInventory:
    """Creates the inventory for the shop."""
    return ShopInventory([["basic2", "poison1", "heal1"], ["basic2", "poison2", "heal1"],
                          ["basic3", "poison2", "heal2"], ["basic3", "poison3", "heal2"],
                          ["basic4", "divider1", "heal2"], ["basic5", "divider1", "multiplier1"]], 4)


def create_level_manager() -> LevelManager:
    """Creates a level manager."""
    enemy_list = list(enemy_config.keys())
    enemy_list.remove("shopkeeper")
    return LevelManager([4, 4, 4, 4, 4, 1], enemy_list, ["loot", "player_menu"], "ending")


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy."""
    assert enemy in enemy_config, f"{enemy} is not a valid enemy"
    stats = enemy_config[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    player = Player()
    for _ in range(2):
        player.append_to_preference("basic1")
    return player
