import random
from . import dice_config, enemy_config, idle_animation_config, dialogue_config
from core import get_all_sprites
from gui.utils import IndexCycler, DialogueData
from entities.enemies import Enemy, Player
from entities.dice import Die, DiceSet
from entities.shop import ShopInventory


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


def random_battle_song() -> str:
    """Returns a random battle song path."""
    battle_songs = ["calm", "doma", "huh", "jong", "menu", "ones", "somedrums", "Something", "stomp", "stomp2",
                    "trittle", "zins"]
    return random.choice(battle_songs)


def random_die_name() -> str:
    """Gets a random die name."""
    return random.choice(list(dice_config.keys()))


def all_enemy_names() -> list[str]:
    """Gets a list of enemy names."""
    enemy_names = list(enemy_config.keys())
    return enemy_names


def create_die(die_type: str) -> Die:
    """Creates a die."""
    assert die_type in dice_config, f"{die_type} is not a valid die type"
    side, multiple, additional_cost, damage_type, safe = dice_config[die_type]
    return Die(side, multiple, int(130 * 1.5 * (multiple + 0.5)) + additional_cost, damage_type, safe)


def create_dice_set(preference: list[str]) -> DiceSet:
    """Creates a dice set from a preference."""
    return DiceSet([create_die(die_name) for die_name in preference])


def create_shop_inventory() -> ShopInventory:
    """Creates the inventory for the shop."""
    return ShopInventory([["basic2", "poison1", "heal1"], ["basic2", "poison2", "heal1"],
                          ["basic3", "poison2", "heal2"], ["basic3", "poison3", "heal2"],
                          ["basic4", "divider1", "heal2"], ["basic5", "divider1", "multiplier1"]], 4)


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy."""
    assert enemy in enemy_config, f"{enemy} is not a valid enemy"
    stats = enemy_config[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    player = Player()
    for _ in range(4):
        player.append_to_preference("basic5")
    for _ in range(13):
        player.append_to_inventory("basic1")
    return player
