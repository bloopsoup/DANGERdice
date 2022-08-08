class ShopInventory:
    """Inventory manager for shops."""

    def __init__(self, inventory_list: list[list[str]], ticks: int):
        assert len(inventory_list) > 0, "inventory list cannot be empty"
        assert ticks > 0, "ticks before restock must be at least 1"
        self.inventory_list, self.tier = inventory_list, 0
        self.ticks, self.current_ticks = ticks, 0
        self.current_inventory = inventory_list[self.tier][:]

    def get_inventory(self) -> list[str]:
        """Returns a copy of the current inventory."""
        return self.current_inventory[:]

    def attempt_restock(self):
        """Increments the inventory's ticks. If enough ticks have passed, the inventory is restocked."""
        self.current_ticks += 1
        if self.current_ticks == self.ticks:
            self.current_ticks = 0
            self.tier += 1
            self.current_inventory = self.inventory_list[self.tier][:]

    def get_item(self, i: int) -> str:
        """Returns the ith item from the current inventory."""
        return self.current_inventory[i]

    def consume_item(self, i: int):
        """Sets the ith item in the inventory to an empty string."""
        self.current_inventory[i] = ""

    def import_data(self, data: dict):
        """Reads in a dictionary of shop inventory data and sets attributes."""
        self.tier = data["tier"]
        self.current_ticks = data["current_ticks"]
        self.current_inventory = data["current_inventory"]

    def export_data(self) -> dict:
        """Returns a dictionary aggregating shop inventory data."""
        return {
            "tier": self.tier,
            "current_ticks": self.current_ticks,
            "current_inventory": self.current_inventory
        }
