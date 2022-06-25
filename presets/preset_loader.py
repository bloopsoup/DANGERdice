from entities.dice.die import Die
from entities.enemies.enemy import Enemy
from entities.enemies.player import Player
from presets.dice_presets import dice_presets
from presets.enemy_presets import enemy_presets


# UTILS
def get_base_price(multiple: int) -> int:
    """Returns the base price for a standard die which is subject to balance changes."""
    return int(130 * 1.5 * (multiple + 0.5))


# FACTORY FUNCTIONS
def create_die(die_type: str, multiple: int) -> Die:
    """Creates a die using a preset."""
    assert die_type in dice_presets, "not a valid die type"
    side, additional_cost, safe = dice_presets[die_type]
    return Die(side, multiple, get_base_price(multiple) + additional_cost, die_type, safe)


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy using a preset."""
    assert enemy in enemy_presets, "not a valid enemy"
    stats = enemy_presets[enemy][tier]
    return Enemy(enemy, stats["level"], stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"], stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    return Player("p0-0")