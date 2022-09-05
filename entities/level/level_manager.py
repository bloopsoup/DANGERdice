import random


class LevelManager:
    """Creates and manages levels. Generates levels upon initialization."""

    def __init__(self, structure: list[int], enemy_list: list[str], exits: list[str], ending: str):
        self.structure, self.enemy_list, self.exits, self.ending = structure, enemy_list, exits, ending
        self.levels, self.current_level = self.make_levels(), [0, 0]

    def get_level(self) -> dict:
        """Gets information about the current level."""
        return self.levels[self.current_level[0]][self.current_level[1]]

    def next_level(self):
        """Move to the next level."""
        self.current_level[1] += 1
        if self.current_level[1] >= len(self.levels[self.current_level[0]]):
            self.current_level[0] += 1
            self.current_level[1] = 0

    def make_levels(self) -> list[list[dict]]:
        """Returns a list of levels."""
        levels = []
        for i, num_levels in enumerate(self.structure):
            stage, enemy_list = [], self.enemy_list[:]
            for j in range(num_levels):
                stage.append({"name": f"Level {i}-{j}",
                              "tier": i,
                              "enemy": enemy_list.pop(random.randint(0, len(enemy_list) - 1)),
                              "dest": random.choice(self.exits) if (i, j) == (len(self.structure)-1, num_levels-1)
                              else self.ending})
            levels.append(stage)
        return levels

    def reset_data(self):
        """Resets player data."""
        self.levels, self.current_level = self.make_levels(), [0, 0]

    def import_data(self, data: dict):
        """Reads in a dictionary to configure the level manager."""
        self.levels, self.current_level = data["levels"], data["current_level"]

    def export_data(self) -> dict:
        """Returns a dictionary of the level manager's data."""
        return {"levels": self.levels, "current_level": self.current_level}
