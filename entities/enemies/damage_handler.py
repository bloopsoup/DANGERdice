from .enemy import Enemy
from .status import Status


class DamageHandler:
    """Handles dishing out damage."""

    def __init__(self, entities: list[Enemy]):
        assert len(entities) > 0, "must track at least one entity"
        self.tracked = [(entity, Status()) for entity in entities]
        self.damage = 0
        self.heal = 0
        self.poison = 0
        self.weaken = 1

    def __str__(self):
        return "DMG: {0} PSN: {1} HEAL: {2} WKN: {3}X".format(self.damage, self.poison, self.heal, self.weaken)

    def get_status(self, i: int) -> Status:
        """Returns the status of the ith tracked entity."""
        return self.tracked[i][1]

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
        self.weaken = 1

    def add_damage(self, amount: int, damage_type: str):
        """Adds damage to the appropriate type."""
        if damage_type == "basic":
            self.damage += amount
        elif damage_type == "heal":
            self.heal += amount
        elif damage_type == "poison":
            self.poison += amount
        elif damage_type == "multiplier":
            self.damage *= amount
        elif damage_type == "divide":
            self.weaken *= amount

    def has_damage(self) -> bool:
        """Is there damage present?"""
        return self.damage > 0 or self.heal > 0 or self.poison > 0 or self.weaken > 1

    def has_status_damage(self, i: int) -> bool:
        """Is there status damage present in the ith tracked entity?"""
        status = self.tracked[i][1]
        return status.get_poison() > 0 or status.get_weaken() > 1

    def apply_benefits(self, i: int):
        """Applies benefits to the ith tracked entity."""
        target, status = self.tracked[i]
        target.add_health(self.heal)

    def apply_s_effects(self, i: int):
        """Applies status effects to the ith tracked entity."""
        status = self.tracked[i][1]
        self.damage //= status.get_weaken()
        status.set_weaken(1)

    def apply_damage(self, i: int):
        """Applies the damage to the ith tracked entity."""
        target, status = self.tracked[i]
        target.subtract_health(self.damage)
        status.add_poison(self.poison)
        status.set_weaken(self.weaken)
        target.try_die()

    def apply_s_damage(self, i: int):
        """Applies status damage to the ith tracked entity."""
        target, status = self.tracked[i]
        if status.get_poison() > 0:
            target.subtract_health(status.get_poison())
            status.subtract_poison(1)
        status.set_weaken(1)
        target.try_die()
