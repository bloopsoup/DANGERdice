import random


class IndexCycler:
    """Cycles through random lists of indices every call to update."""

    def __init__(self, indices: list[list[int]], frames: float):
        self.indices = indices
        self.run = random.choice(self.indices)
        self.frames = frames
        self.count = 0
        self.index = 0

    def will_end_list(self, dt: float) -> bool:
        """Returns whether the cycler will be done with the list with the next dt update."""
        return self.index == len(self.run) - 1 and self.count + dt >= self.frames

    def update(self, dt: float) -> int:
        """Returns a new index if enough time has passed. Otherwise return -1."""
        self.count += dt
        if self.count >= self.frames:
            self.count = 0
            self.index += 1
            if self.index > len(self.run) - 1:
                self.index = 0
                self.run = random.choice(self.indices)
            return self.run[self.index]
        else:
            return -1
