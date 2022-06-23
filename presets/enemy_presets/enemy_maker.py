from entities.enemies.enemy import Enemy
from entities.enemies.player import Player
from presets.enemy_presets.presets import presets


def create_enemy(enemy: str, tier: int) -> Enemy:
    """Creates an enemy using a preset."""
    assert enemy in presets, "not a valid enemy"
    stats = presets[enemy][tier]
    return Enemy(enemy,
                 stats["level"],
                 stats["level"] * stats["health_factor"],
                 stats["level"] * stats["money_factor"],
                 stats["preference"])


def create_player() -> Player:
    """Creates a player."""
    return Player("p0-0")
