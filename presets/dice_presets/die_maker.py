from entities.dice.die import Die
from presets.dice_presets.presets import presets


def get_base_price(multiple: int) -> int:
    """Returns the base price for a standard die which is subject to balance changes."""
    return int(130 * 1.5 * (multiple + 0.5))


def create_die(die_type: str, multiple: int) -> Die:
    """Creates a die using a preset."""
    assert die_type in presets, "not a valid die type"
    side, additional_cost, safe = presets[die_type]
    return Die(side, multiple, get_base_price(multiple) + additional_cost, die_type, safe)
