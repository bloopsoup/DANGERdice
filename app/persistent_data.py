from .config import create_player, create_shop_inventory, create_level_manager
from .entities.enemies import Player
from .entities.shop import ShopInventory
from .entities.level import LevelManager


class PersistentData:
    """Container for persistent data accessed globally by game states."""

    def __init__(self):
        self.player = create_player()
        self.shop_inventory = create_shop_inventory()
        self.level_manager = create_level_manager()

    def get_player(self) -> Player:
        """Gets the player."""
        return self.player

    def get_shop_inventory(self) -> ShopInventory:
        """Gets the shop inventory."""
        return self.shop_inventory

    def get_level_manager(self) -> LevelManager:
        """Gets the level manager."""
        return self.level_manager

    def reset_data(self):
        """Resets save data."""
        self.player.reset_data()
        self.shop_inventory.reset_data()
        self.level_manager.reset_data()

    def import_data(self, data: dict):
        """Imports save data."""
        self.player.import_data(data["player"])
        self.shop_inventory.import_data(data["shop"])
        self.level_manager.import_data(data["levels"])

    def export_data(self) -> dict:
        """Exports save data."""
        return {"player": self.player.export_data(),
                "shop": self.shop_inventory.export_data(),
                "levels": self.level_manager.export_data()}


PERSISTENT_DATA = PersistentData()
