from entities.enemies import Enemy


class Status:
    """Stores persistent status info throughout the battle."""

    def __init__(self):
        self.poison = 0
        self.blessed = 0
        self.weaken = 0

    def add_poison(self, amount: int):
        """Increases poison."""
        self.poison += amount

    def subtract_poison(self, amount: int):
        """Decreases poison."""
        self.poison -= amount

    def add_blessed(self, amount: int):
        """Increases blessed."""
        self.blessed += amount

    def subtract_blessed(self, amount: int):
        """Decreases blessed."""
        self.blessed -= amount

    def add_weaken(self, amount: int):
        """Increases weaken."""
        self.weaken += amount

    def subtract_weaken(self, amount: int):
        """Decreases weaken."""
        self.weaken -= amount


class DamageHandler:
    """Handles dishing out damage."""

    def __init__(self, num_entities: int):
        assert num_entities > 0, "must track at least one entity"
        self.statuses = [Status() for _ in range(num_entities)]
        self.damage = 0
        self.heal = 0
        self.poison = 0
        self.weaken = 0

    def __str__(self):
        return "DMG: {0} PSN: {1} HEAL: {2} WKN: {3}X".format(self.damage, self.poison, self.heal, self.weaken)

    def get_damage(self) -> int:
        """Returns the damage."""
        return self.damage

    def get_poison(self) -> int:
        """Returns the poison damage."""
        return self.poison

    def get_heal(self) -> int:
        """Returns the heal damage."""
        return self.heal

    def get_weaken(self) -> int:
        """Returns the weaken damage."""
        return self.weaken

    def reset(self):
        """Resets everything."""
        self.damage = 0
        self.heal = 0
        self.poison = 0
        self.weaken = 0

    def add_damage(self, amount: int, damage_type: str):
        """Adds damage to the appropriate type."""
        if damage_type == "basic":
            self.damage += amount
        elif damage_type == "heal":
            self.heal += amount
        elif damage_type == "poison":
            self.poison += amount
        elif damage_type == 'weaken':
            self.weaken += amount

    def apply_damage(self, target: Enemy, i: int):
        """Applies the damage to target and ith Status."""
        status = self.statuses[i]
        target.subtract_health(self.damage)
        target.add_health(self.heal)
        status.add_poison(self.poison)
        status.add_weaken(self.weaken)
        self.reset()
